# 10 · QA checklist

Run this on every render before review. Check by **stepping through frames** in the player, not
by watching at speed. Most failures only show frame by frame.

## Frame-step checks (2-second sample from every scene)

- [ ] **Cadence.** Graphic elements change only on drawing frames (30 fps: frames where
      `frame % 5` is 0 or 3). No graphic changes on in-between frames. Footage and map cameras may
      change every frame.
- [ ] **No motion blur** on stepped graphics.
- [ ] **Nothing dead still.** A held graphic layer still changes every 5 frames (Archive weave),
      every 3–4 frames (Ink & Paper boil) or every 15 frames (Scrapbook prop boil).
- [ ] **The paper does not jitter** in Archive (only the graphic layers do).
- [ ] **Every box starts as a cursor.** The first visible frame of a highlight is an 8–24 px bar.
- [ ] **Box reveals mask their text** (letters cut mid-glyph at the edge) when the text wasn't
      already visible.
- [ ] **Shots start mid-move** (settle, punch-out, slide or zoom-out), never on a static frame.
- [ ] **Shots end with a 3–8 f ease-in exit** into the cut, or the cut is part of a zoom-through.
- [ ] **No bounce** on type, paper or photos. Overshoot is allowed only on Scrapbook object pops
      (6–23 %) or one Archive photo pop (≤ 15 %).

## Colour

- [ ] **One accent colour** in the whole film (sample it; ΔE < 3 between uses).
- [ ] The accent never fills a background.
- [ ] Text on paper is a warm near-black, not `#000000`.
- [ ] Archival photos are B&W or faded; only the hero object is in saturated colour.
- [ ] No gradients except the vignette, glows on dark backgrounds, and photos.

## Type

- [ ] One serif family for running text (Archive). Emphasis by italic, box or ink-bleed, never by
      switching fonts.
- [ ] Sizes match `02-typography.md` within ±5 % (title 95–100 px on a 138 px box; caption 52 px
      at a 90 % H baseline).
- [ ] At most one emphasised word per line.
- [ ] Captions fit on one line (≤ 77 % W).
- [ ] No outlines, drop shadows or bevels on type.
- [ ] Fonts are self-hosted and actually loaded (look for fallback serifs in stills).

## Layout

- [ ] 30–60 % of the frame is calm paper; type sits only there (or in a box).
- [ ] Recurring templates are pixel-identical (overlay two instances at 50 % opacity).
- [ ] Text stays inside the title-safe area (9 % W, 8 % H) except deliberate bleeds.
- [ ] Hero words, display words and collage scraps bleed off the edge where the dialect calls for it.

## Materials

- [ ] Cut-outs have hard edges (no feathering). Their edge treatment matches the dialect: accent
      offset shadow (Archive), none (Ink & Paper / Scrapbook) or sticker outline (Postcard).
- [ ] No soft drop shadows except dithered paper-prop shadows (Scrapbook) or desk-print shadows.
- [ ] Raster assets are ≥ 2× their on-screen size at 1080p (check a 4K still at 100 %).
- [ ] No lens flares, light leaks, bokeh or stock "film" overlays on graphics.

## Transitions

- [ ] More than 70 % of transitions are hard cuts into motion.
- [ ] No dissolves outside dark montages; at most 1–2 paper transitions per minute.
- [ ] Fade to black only at the very end (49 f + 23 f of black).

## Timing

- [ ] Builds take 0.7–1.3 s; holds after the last element lands are ≥ 0.5 s (quotes ≥ 1 s).
- [ ] Keywords and captions lead the voice-over or cut by 3–6 f.
- [ ] The average shot is 2–3 s; one rhythm break (montage) per 1–2 minutes.

## Render

- [ ] 1080p: H.264 CRF ≤ 16. 4K: `--scale=2` from the same design.
- [ ] Check banding on the paper vignette at 4K. If you see banding, add a 1 % noise layer to the
      paper (not to the graphics).
- [ ] Audio-picture sync: each type-on finishes before the narrated word ends.
