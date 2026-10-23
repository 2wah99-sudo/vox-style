"""Measure how something moves across a frame range, to recover timing and easing.

usage: python3 motion.py WORKDIR START END [x0 y0 x1 y1]
  START/END are frame numbers (inclusive). The optional box (in full-frame pixels)
  restricts analysis to a region, e.g. one sliding label or one map pin.

Prints, per frame:
  shift_x/shift_y  whole-region translation vs START (phase correlation): pans, slides
  scale            zoom factor vs START (search 0.5x-2.5x, centred): push-ins
  energy           mean abs change vs previous frame
  bbox             bounding box of pixels that changed vs previous frame
  progress         0..1 cumulative motion (from shift if it moves, else energy)
Then fits progress against common easing curves and reports the best match,
the duration in frames/seconds, and the travel distance in px and % of frame.
"""
import json, os, sys
import numpy as np
from PIL import Image

wd, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
box = tuple(int(v) for v in sys.argv[4:8]) if len(sys.argv) >= 8 else None
meta = json.load(open(os.path.join(wd, "palette.json")))
fps, FW, FH = meta["fps"], meta["width"], meta["height"]

def load(i):
    im = Image.open(os.path.join(wd, "frames", f"{i:05d}.jpg")).convert("L")
    if box:
        im = im.crop(box)
    return np.asarray(im, np.float32)

def phase_shift(f0, f1):
    w = np.hanning(f0.shape[0])[:, None] * np.hanning(f0.shape[1])[None]
    F0, F1 = np.fft.fft2(f0 * w), np.fft.fft2(f1 * w)
    R = F0 * np.conj(F1)
    r = np.fft.ifft2(R / (np.abs(R) + 1e-6)).real
    y, x = np.unravel_index(np.argmax(r), r.shape)
    if y > r.shape[0] // 2: y -= r.shape[0]
    if x > r.shape[1] // 2: x -= r.shape[1]
    return -x, -y

def scale_err(f0, f1, s):
    h, w = f0.shape
    arr = np.asarray(Image.fromarray(f0.astype(np.uint8)).resize(
        (max(2, int(w * s)), max(2, int(h * s))), Image.BILINEAR), np.float32)
    H2, W2 = arr.shape
    if s >= 1:
        y0, x0 = (H2 - h) // 2, (W2 - w) // 2
        return np.abs(arr[y0:y0 + h, x0:x0 + w] - f1).mean()
    y0, x0 = (h - H2) // 2, (w - W2) // 2
    return np.abs(arr - f1[y0:y0 + H2, x0:x0 + W2]).mean()

def best_scale(f0, f1):
    # coarse log-spaced search 0.5x-2.5x, then refine around the best
    coarse = np.exp(np.linspace(np.log(0.5), np.log(2.5), 41))
    s0 = min(coarse, key=lambda s: scale_err(f0, f1, s))
    fine = s0 * np.exp(np.linspace(-0.04, 0.04, 9))
    return float(min(fine, key=lambda s: scale_err(f0, f1, s)))

frames = [load(i) for i in range(a, b + 1)]
base = frames[0]
rec = []
for k, f in enumerate(frames):
    sx, sy = phase_shift(base, f) if k else (0, 0)
    sc = best_scale(base, f) if k else 1.0
    e = float(np.abs(f - frames[k - 1]).mean()) if k else 0.0
    m = np.abs(f - frames[k - 1]) > 12 if k else np.zeros_like(f, bool)
    ys, xs = np.nonzero(m)
    bb = (int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())) if len(xs) else None
    rec.append((a + k, sx, sy, sc, e, bb))

dist = np.array([np.hypot(r[1], r[2]) for r in rec])
scl = np.array([abs(np.log(r[3])) for r in rec])
energy = np.cumsum([r[4] for r in rec])
if dist.max() >= 3 and np.all(np.diff(dist) >= -2):
    prog, src = dist / dist.max(), "translation"
elif scl.max() > 0.02:
    prog, src = scl / scl.max(), "scale"
else:
    prog, src = (energy / energy[-1] if energy[-1] > 0 else energy), "energy"

print(f"frames {a}-{b} ({b - a + 1} frames, {(b - a) / fps:.3f}s at {fps:g}fps) region={box or 'full frame'}")
print("frame  t(s)   shift_x shift_y scale  energy  progress  changed_bbox")
for r, p in zip(rec, prog):
    print(f"{r[0]:5d} {r[0] / fps:6.2f} {r[1]:7d} {r[2]:7d} {r[3]:5.3f} {r[4]:7.2f}  {p:6.3f}   {r[5]}")

t = np.linspace(0, 1, len(prog))
E = {
    "linear": t,
    "easeInQuad": t ** 2, "easeOutQuad": 1 - (1 - t) ** 2,
    "easeInOutQuad": np.where(t < .5, 2 * t * t, 1 - (-2 * t + 2) ** 2 / 2),
    "easeInCubic": t ** 3, "easeOutCubic": 1 - (1 - t) ** 3,
    "easeInOutCubic": np.where(t < .5, 4 * t ** 3, 1 - (-2 * t + 2) ** 3 / 2),
    "easeOutQuart": 1 - (1 - t) ** 4,
    "easeInOutQuart": np.where(t < .5, 8 * t ** 4, 1 - (-2 * t + 2) ** 4 / 2),
    "easeOutQuint": 1 - (1 - t) ** 5,
    "easeOutExpo": np.where(t == 1, 1, 1 - 2 ** (-10 * t)),
    "easeInOutExpo": np.where(t == 0, 0, np.where(t == 1, 1, np.where(t < .5, 2 ** (20 * t - 10) / 2, (2 - 2 ** (-20 * t + 10)) / 2))),
    "easeInOutSine": -(np.cos(np.pi * t) - 1) / 2,
    "easeOutBack": 1 + 2.70158 * (t - 1) ** 3 + 1.70158 * (t - 1) ** 2,
}
fit = sorted((float(np.sqrt(((prog - c) ** 2).mean())), k) for k, c in E.items())
print(f"\nprogress source: {src}")
if src == "translation":
    r = rec[-1]
    print(f"travel: dx={r[1]}px dy={r[2]}px ({abs(r[1]) / (box[2] - box[0] if box else FW) * 100:.1f}% / "
          f"{abs(r[2]) / (box[3] - box[1] if box else FH) * 100:.1f}% of region)")
if src == "scale":
    print(f"zoom: {rec[-1][3]:.3f}x over the range")
print("easing fit (rms error, lower is better): " + ", ".join(f"{k} {e:.3f}" for e, k in fit[:5]))
over = prog.max() > 1.02 or (len(dist) > 2 and src == "translation" and dist.argmax() < len(dist) - 2)
print("overshoot detected" if over else "no overshoot")
