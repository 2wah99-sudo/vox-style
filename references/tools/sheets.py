"""Contact sheets covering every distinct frame of a video.

usage: python3 sheets.py WORKDIR
Reads WORKDIR/metrics.csv and WORKDIR/frames/*.jpg, writes:
  WORKDIR/sheets/seq_NNN.jpg      every non-hold frame in order; runs of identical
                                  frames that follow are folded into the tile ("+hold Ns").
                                  Label colour = how the frame differs from the one before:
                                  red = hard cut, orange = global motion, blue = local
                                  motion, grey = first frame.
  WORKDIR/sheets/overview_NN.jpg  one frame per second, 5x4 per sheet
  WORKDIR/sheets/index.txt        which frames each sheet covers
"""
import csv, json, os, sys
from PIL import Image, ImageDraw, ImageFont

wd = sys.argv[1]
rows = list(csv.DictReader(open(os.path.join(wd, "metrics.csv"))))
meta = json.load(open(os.path.join(wd, "palette.json")))
fps = meta["fps"]
out = os.path.join(wd, "sheets")
os.makedirs(out, exist_ok=True)
for f in os.listdir(out):
    os.remove(os.path.join(out, f))

TW = 320
TH = round(TW * meta["height"] / meta["width"])
LABEL = 22
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 15)
COLORS = {"cut": (220, 30, 30), "global": (230, 130, 0), "local": (30, 90, 220), "hold": (110, 110, 110)}

def frame(i):
    return Image.open(os.path.join(wd, "frames", f"{i:05d}.jpg")).convert("RGB").resize((TW, TH), Image.LANCZOS)

# build tile list: one tile per distinct frame; identical (hold) frames extend the tile
tiles = []
for i, r in enumerate(rows):
    if r["state"] == "hold" and tiles:
        tiles[-1]["end"] = i
    else:
        tiles.append({"kind": r["state"], "start": i, "end": i, "show": i})

def label(t):
    s, e = t["start"], t["end"]
    txt = f"f{s} {s / fps:.2f}s {t['kind'][0].upper()}"
    return txt + (f" +hold {(e - s) / fps:.2f}s" if e > s else "")

def sheet(tiles_, path, cols):
    rws = (len(tiles_) + cols - 1) // cols
    img = Image.new("RGB", (cols * TW + (cols + 1) * 4, rws * (TH + LABEL) + (rws + 1) * 4), (20, 20, 20))
    dr = ImageDraw.Draw(img)
    for k, t in enumerate(tiles_):
        x = 4 + (k % cols) * (TW + 4)
        y = 4 + (k // cols) * (TH + LABEL + 4)
        dr.rectangle([x, y, x + TW - 1, y + LABEL - 1], fill=COLORS[t["kind"]])
        dr.text((x + 4, y + 2), label(t), fill="white", font=font)
        img.paste(frame(t["show"]), (x, y + LABEL))
    img.save(path, quality=88)

PER = 30
index = []
for k in range(0, len(tiles), PER):
    chunk = tiles[k:k + PER]
    name = f"seq_{k // PER:03d}.jpg"
    sheet(chunk, os.path.join(out, name), 6)
    index.append(f"{name}: f{chunk[0]['start']}-f{chunk[-1]['end']} "
                 f"t={chunk[0]['start'] / fps:.2f}-{chunk[-1]['end'] / fps:.2f}s")

ov = [{"kind": rows[i]["state"], "start": i, "end": i, "show": i} for i in range(0, len(rows), max(1, round(fps)))]
for k in range(0, len(ov), 20):
    chunk = ov[k:k + 20]
    name = f"overview_{k // 20:02d}.jpg"
    sheet(chunk, os.path.join(out, name), 5)
    index.append(f"{name}: 1 fps, t={chunk[0]['start'] / fps:.1f}-{chunk[-1]['start'] / fps:.1f}s")

open(os.path.join(out, "index.txt"), "w").write("\n".join(index) + "\n")
print(f"{wd}: {len(tiles)} tiles -> {sum(1 for x in index if x.startswith('seq'))} seq sheets, "
      f"{sum(1 for x in index if x.startswith('overview'))} overview sheets")
