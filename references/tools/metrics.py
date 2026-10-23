"""Per-frame metrics for every frame of a video.

usage: python3 metrics.py VIDEO OUTDIR
writes OUTDIR/metrics.csv, scenes.json, palette.json, palette.png, summary.txt
"""
import json, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

video, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)

probe = json.loads(subprocess.check_output([
    "ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
    "stream=width,height,r_frame_rate,nb_frames", "-of", "json", video]))["streams"][0]
num, den = map(int, probe["r_frame_rate"].split("/"))
fps = num / den
W, H = 192, 108

raw = subprocess.check_output([
    "ffmpeg", "-v", "error", "-i", video, "-vf", f"scale={W}:{H}:flags=area",
    "-f", "rawvideo", "-pix_fmt", "rgb24", "-vsync", "0", "-"])
frames = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
n = len(frames)
f32 = frames.astype(np.float32)

def hist(fr):
    q = (fr // 32).reshape(-1, 3).astype(np.int32)
    idx = q[:, 0] * 64 + q[:, 1] * 8 + q[:, 2]
    h = np.bincount(idx, minlength=512).astype(np.float32)
    return h / h.sum()

hists = np.stack([hist(fr) for fr in frames])
mx = f32.max(axis=3); mn = f32.min(axis=3)
sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1), 0).mean(axis=(1, 2))
luma = (0.2126 * f32[..., 0] + 0.7152 * f32[..., 1] + 0.0722 * f32[..., 2])
luma_mean = luma.mean(axis=(1, 2)); luma_std = luma.std(axis=(1, 2))

diff = np.zeros(n); changed = np.zeros(n); hdist = np.zeros(n)
for i in range(1, n):
    d = np.abs(f32[i] - f32[i - 1])
    diff[i] = d.mean()
    changed[i] = (d.max(axis=2) > 12).mean()
    hdist[i] = 0.5 * np.abs(hists[i] - hists[i - 1]).sum()

# hard cuts: large, isolated spike in both pixel and histogram change
cuts = []
for i in range(1, n):
    lo, hi = max(1, i - 6), min(n, i + 7)
    neigh = np.median(np.r_[diff[lo:i], diff[i + 1:hi]]) if hi - lo > 1 else 0
    if changed[i] > 0.45 and diff[i] > 18 and diff[i] > 3 * neigh + 6:
        if not cuts or i - cuts[-1] > 3:
            cuts.append(i)

state = np.where(changed < 0.002, "hold", np.where(changed < 0.15, "local", "global"))
state[0] = "hold"
for c in cuts:
    state[c] = "cut"

with open(os.path.join(out, "metrics.csv"), "w") as fh:
    fh.write("frame,t,diff,changed,hdist,luma,luma_std,sat,state\n")
    for i in range(n):
        fh.write(f"{i},{i / fps:.3f},{diff[i]:.2f},{changed[i]:.4f},{hdist[i]:.4f},"
                 f"{luma_mean[i]:.1f},{luma_std[i]:.1f},{sat[i]:.3f},{state[i]}\n")

def kmeans(px, k, iters=30, seed=0):
    rng = np.random.default_rng(seed)
    c = px[rng.integers(len(px))][None]
    for _ in range(1, k):
        d = ((px[:, None] - c[None]) ** 2).sum(-1).min(1)
        c = np.vstack([c, px[rng.choice(len(px), p=d / d.sum()) if d.sum() > 0 else rng.integers(len(px))]])
    for _ in range(iters):
        lab = ((px[:, None] - c[None]) ** 2).sum(-1).argmin(1)
        c = np.stack([px[lab == j].mean(0) if (lab == j).any() else c[j] for j in range(k)])
    lab = ((px[:, None] - c[None]) ** 2).sum(-1).argmin(1)
    w = np.bincount(lab, minlength=k) / len(lab)
    o = np.argsort(-w)
    return c[o], w[o]

hexc = lambda c: "#%02X%02X%02X" % tuple(int(round(v)) for v in c)
rng = np.random.default_rng(1)
step = max(1, n // 600)
sample = f32[::step].reshape(-1, 3)
sample = sample[rng.choice(len(sample), min(120000, len(sample)), replace=False)]
centers, weights = kmeans(sample, 16)
palette = [{"hex": hexc(c), "rgb": [int(round(v)) for v in c], "share": round(float(w), 4)}
           for c, w in zip(centers, weights)]

# scenes between cuts
bounds = [0] + cuts + [n]
scenes = []
for s, e in zip(bounds[:-1], bounds[1:]):
    seg = state[s + 1:e] if e - s > 1 else state[s:e]
    mid = (s + e) // 2
    px = f32[mid].reshape(-1, 3)
    sc, sw = kmeans(px[rng.choice(len(px), min(4000, len(px)), replace=False)], 5, iters=15)
    holds = []
    run = None
    for i in range(s + 1, e):
        if state[i] == "hold":
            run = [i, i] if run is None else [run[0], i]
        else:
            if run and run[1] - run[0] + 1 >= max(3, int(fps * 0.25)):
                holds.append(run)
            run = None
    if run and run[1] - run[0] + 1 >= max(3, int(fps * 0.25)):
        holds.append(run)
    scenes.append({
        "scene": len(scenes), "start": s, "end": e - 1, "t_start": round(s / fps, 3),
        "duration_s": round((e - s) / fps, 3),
        "frac_hold": round(float((seg == "hold").mean()), 3) if len(seg) else 1.0,
        "frac_local": round(float((seg == "local").mean()), 3) if len(seg) else 0.0,
        "frac_global": round(float((seg == "global").mean()), 3) if len(seg) else 0.0,
        "mean_diff": round(float(diff[s + 1:e].mean()), 2) if e - s > 1 else 0.0,
        "hold_runs": [[a, b, round((b - a + 1) / fps, 2)] for a, b in holds],
        "colors": [{"hex": hexc(c), "share": round(float(w), 3)} for c, w in zip(sc, sw)],
    })

json.dump({"fps": fps, "frames": n, "width": int(probe["width"]), "height": int(probe["height"]),
           "duration_s": round(n / fps, 3), "cuts": cuts, "palette": palette},
          open(os.path.join(out, "palette.json"), "w"), indent=1)
json.dump(scenes, open(os.path.join(out, "scenes.json"), "w"), indent=1)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 18)
sw_img = Image.new("RGB", (16 * 120, 150), "white")
dr = ImageDraw.Draw(sw_img)
for j, p in enumerate(palette):
    dr.rectangle([j * 120, 0, j * 120 + 119, 100], fill=tuple(p["rgb"]))
    dr.text((j * 120 + 4, 104), p["hex"], fill="black", font=font)
    dr.text((j * 120 + 4, 126), f"{p['share'] * 100:.1f}%", fill="black", font=font)
sw_img.save(os.path.join(out, "palette.png"))

durs = np.array([sc["duration_s"] for sc in scenes])
lines = [
    f"video: {os.path.basename(video)}",
    f"{probe['width']}x{probe['height']} @ {fps:g} fps, {n} frames, {n / fps:.2f}s",
    f"hard cuts: {len(cuts)}  scenes: {len(scenes)}  shot length mean {durs.mean():.2f}s median {np.median(durs):.2f}s min {durs.min():.2f}s max {durs.max():.2f}s",
    f"frame states: hold {(state == 'hold').mean():.1%}  local-motion {(state == 'local').mean():.1%}  global-motion {(state == 'global').mean():.1%}",
    f"luma mean {luma_mean.mean():.1f}  saturation mean {sat.mean():.3f}",
    "global palette (k-means, share of pixels): " + ", ".join(f"{p['hex']} {p['share'] * 100:.1f}%" for p in palette),
    "",
    "scenes:",
]
for sc in scenes:
    lines.append(f"  #{sc['scene']:03d} f{sc['start']}-{sc['end']} t={sc['t_start']:.2f}s dur={sc['duration_s']:.2f}s "
                 f"hold={sc['frac_hold']:.0%} local={sc['frac_local']:.0%} global={sc['frac_global']:.0%} "
                 f"colors={' '.join(c['hex'] for c in sc['colors'])}")
open(os.path.join(out, "summary.txt"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines[:6]))
