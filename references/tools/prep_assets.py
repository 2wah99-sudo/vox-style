"""Asset prep for the vox style: archival B&W, newspaper halftone, round-join outlines.

usage:
  python3 prep_assets.py bw       in.png out.png [--contrast 1.35]
  python3 prep_assets.py halftone in.png out.png [--period 11] [--angle 45]
  python3 prep_assets.py outline  in.png out.png [--width 28] [--color #FFFFFF]
Inputs with transparency (cut-outs) keep their alpha. Sizes are in output pixels:
at 4K use period 11 / width 28 (= 5.5 px and 14 px at 1080p).
"""
import argparse
import math

import numpy as np
from PIL import Image, ImageDraw, ImageOps


def archival_bw(img, contrast=1.35):
    alpha = img.getchannel("A") if img.mode == "RGBA" else None
    g = np.asarray(ImageOps.grayscale(img), np.float32) / 255.0
    g = np.clip((g - 0.5) * contrast + 0.5, 0, 1)          # +35 % contrast
    g = np.clip((g - 0.06) / 0.92, 0, 1)                    # crush blacks, blow highlights
    out = Image.fromarray((g * 255).astype(np.uint8)).convert("RGB")
    if alpha is not None:
        out.putalpha(alpha)
    return out


def halftone(img, period=11, angle=45):
    """Black dots on white, 45° screen; dot area proportional to darkness."""
    alpha = img.getchannel("A") if img.mode == "RGBA" else None
    g = ImageOps.grayscale(img)
    w, h = g.size
    diag = int(math.hypot(w, h)) + 2 * period
    rot = g.rotate(angle, expand=True, fillcolor=255, resample=Image.BICUBIC)
    rot = ImageOps.pad(rot, (diag, diag), color=255)
    small = rot.resize((diag // period, diag // period), Image.BOX)
    dots = Image.new("L", (diag * 2, diag * 2), 255)        # 2× supersampling for clean dots
    d = ImageDraw.Draw(dots)
    s = np.asarray(small, np.float32) / 255.0
    cell = period * 2
    for j in range(s.shape[0]):
        for i in range(s.shape[1]):
            dark = 1.0 - s[j, i]
            if dark < 0.02:
                continue
            r = cell * 0.5 * math.sqrt(dark) * 1.12          # area ∝ darkness, full cells touch
            cx, cy = (i + 0.5) * cell, (j + 0.5) * cell
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=0)
    dots = dots.resize((diag, diag), Image.LANCZOS).rotate(-angle, resample=Image.BICUBIC, fillcolor=255)
    left, top = (diag - w) // 2, (diag - h) // 2
    out = dots.crop((left, top, left + w, top + h)).convert("RGB")
    if alpha is not None:
        out.putalpha(alpha)
    return out


def outline(img, width=28, color="#FFFFFF"):
    """Outside-only stroke with round joins (true disc dilation), no gap, no shadow."""
    img = img.convert("RGBA")
    a = np.asarray(img.getchannel("A")) > 127
    pad = width + 2
    a = np.pad(a, pad)
    grown = np.zeros_like(a)
    for dy in range(-width, width + 1):
        for dx in range(-width, width + 1):
            if dx * dx + dy * dy <= width * width:
                grown |= np.roll(np.roll(a, dy, 0), dx, 1)
    rgb = tuple(int(color.lstrip("#")[k:k + 2], 16) for k in (0, 2, 4))
    stroke = Image.new("RGBA", grown.shape[::-1], rgb + (0,))
    stroke.putalpha(Image.fromarray((grown * 255).astype(np.uint8)))
    base = Image.new("RGBA", stroke.size, (0, 0, 0, 0))
    base.alpha_composite(stroke)
    base.alpha_composite(img, (pad, pad))
    return base


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["bw", "halftone", "outline"])
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--contrast", type=float, default=1.35)
    ap.add_argument("--period", type=int, default=11)
    ap.add_argument("--angle", type=float, default=45)
    ap.add_argument("--width", type=int, default=28)
    ap.add_argument("--color", default="#FFFFFF")
    o = ap.parse_args()
    im = Image.open(o.src)
    im = im.convert("RGBA") if "A" in im.getbands() else im.convert("RGB")
    if o.mode == "bw":
        res = archival_bw(im, o.contrast)
    elif o.mode == "halftone":
        res = halftone(im, o.period, o.angle)
    else:
        res = outline(im, o.width, o.color)
    res.save(o.dst)
    print(f"{o.mode}: {o.src} -> {o.dst} {res.size}")
