# Style-analysis brief (shared by all analysis agents)

## Goal
We are reverse-engineering a family of editorial / "Vox-style" documentary motion-graphics
(paper collage, archival cut-out photos, highlighter marks, editorial type, textured paper,
stop-motion "boil"). Your notes will be merged with other agents' notes into a Markdown
instruction system that tells a developer how to **recreate this style in code** (e.g.
Remotion / Motion Canvas / After Effects expressions / canvas+WebGL) as high-resolution
(1920x1080 and 3840x2160) explainer animations.

So everything you write must be **measurable and reproducible**: hex values, sizes, offsets,
durations in frames *and* seconds, easing names, stagger offsets, layer order. Prefer
"stroke ≈ 9px @1080p, #FFFFFF, no blur" over "a white outline".

## Workspace (all under $VOX = <workspace>)
For each video `work/<id>/` holds:
- `frames/NNNNN.jpg` — **every frame** at native resolution, 0-indexed (frame 0 = 00000.jpg).
- `metrics.csv` — every frame: `diff` (mean abs change vs previous frame, 0-255), `changed`
  (fraction of pixels that changed), `hdist` (colour-histogram change), `luma`, `sat`, and
  `state`: `hold` (identical to previous frame), `local` (<15% of pixels changed — an element
  moving), `global` (camera move / full-frame change), `cut` (hard cut).
- `summary.txt` — resolution, fps, cut list, shot-length stats, per-scene state mix and colours.
- `scenes.json` — scenes split at hard cuts with hold runs and 5 dominant colours each.
- `palette.json` / `palette.png` — k-means palette of the whole video with pixel shares.
- `sheets/seq_NNN.jpg` — contact sheets that together show **every distinct frame** in order
  (30 per sheet, 6 columns). Identical following frames are folded into the tile and shown as
  `+hold Ns`. Label colour: red = hard cut, orange = global motion, blue = local motion.
- `sheets/overview_NN.jpg` — 1 frame per second, for orientation.
- `sheets/index.txt` — which frames / times each sheet covers.

Helpers (run with `python3`, numpy + Pillow available, no OpenCV):
- `$VOX/motion.py WORKDIR START END [x0 y0 x1 y1]` — per-frame translation (phase
  correlation), zoom factor, change energy and changed-pixel bbox over a frame range,
  optionally inside a box (full-res pixel coords). Fits the progress curve to common easings
  and reports duration and travel. Use it on **clean, isolated** moves (one element sliding,
  one push-in) — mixed ranges give noisy fits. It is slow-ish: keep ranges < ~60 frames and
  use a box when you can.
- Write your own small Pillow/numpy snippets for anything else: crop + zoom a region to read
  type, sample exact pixel colours (`Image.getpixel` / median of a small patch), measure
  stroke widths and shadow offsets, check whether animation is on 1s/2s/3s (do positions
  change every frame, or every 2nd frame while the frames in between are `hold`?).
  Put scratch scripts/crops in `$VOX/tmp/<your-id>/`, never inside `work/<id>/frames/`.

## Method — "frame by frame"
1. Read `summary.txt`, `index.txt`, and the overview sheets for your range to orient.
2. Go through **every `seq_` sheet in your range in order** — these cover every distinct
   frame. Log every scene, every element entrance/exit, every transition.
3. For anything that matters for replication, open the **full-resolution frames** (Read the
   jpg directly, or crop/upscale a region with Pillow) — especially typography, textures,
   stroke/shadow treatments, and the first/last frames of every move and transition.
4. Measure: colours by pixel sampling (not by eye), sizes in px converted to **% of frame
   height and px @1080p** (multiply by 1080 / video height), durations in frames + seconds,
   easing via `motion.py` and by stepping through frames, stagger offsets between elements.
5. Determine the animation cadence: are moves animated on ones, twos or threes? Is there a
   texture "boil" (paper/outline re-randomised every N frames even when nothing moves)?
   `metrics.csv` local-motion during otherwise-static shots is a strong hint.

## Output
Write **one Markdown file** to `$VOX/work/notes/<your-id>.md` with exactly these sections
(write "none observed" rather than omitting a section):

1. **Overview** — what the piece is, its visual identity in 3-5 sentences, source res/fps.
2. **Colour** — background(s), paper tones, accent(s), text colours, photo treatment colours;
   sampled hex values with roles and approximate screen share; colour rules ("accent used only
   for…").
3. **Typography** — each text style: likely typeface (+ closest free/Google font), weight,
   case, size (% of frame height and px @1080p), tracking, leading, alignment, colour,
   decoration (highlighter bar, underline, box), and how text animates on/off with timing.
4. **Layout & composition** — margins/safe areas (% of frame), grid, focal placement, number
   of layers, depth order, scale relationships, use of negative space.
5. **Textures & materials** — paper, grid paper, halftone, grain, torn/ragged edges, cut-out
   outlines (width, colour), drop shadows (offset, blur, opacity, colour), photo treatments
   (B&W, contrast, duotone, colour cut-outs on mono), vignette, scan/print artefacts, light
   leaks, film grain/flicker. Give parameters.
6. **Motion** — per element type: entrance, idle, exit (duration frames+s, easing,
   overshoot, rotation, scale-from, direction, distance as % of frame), stagger, camera moves
   (push-in %, pan speed, parallax ratios between layers), cadence (ones/twos), boil/jitter
   (amplitude px@1080p, interval frames). Include `motion.py` measurements you made.
7. **Transitions** — every distinct transition type with a frame-exact description
   (e.g. "f1203-f1211: paper wipe L→R, ragged edge, 8 frames, easeInOutCubic") and how often
   each is used.
8. **Recurring devices** — highlighter, drawn circles/arrows, scribbles, maps, pins,
   timelines, labels, stickers, tape, number counters, etc., each with how it is drawn and
   animated.
9. **Scene log** — table: frames | time | what is on screen | devices | motion/transition notes.
   Every scene in your range.
10. **Replication recipes** — the 5-12 most important techniques in your range as concrete,
    code-ready parameter blocks (pseudo-code or JSON-ish is fine).
11. **Uncertainties** — what you could not determine and why.

Be concrete and exhaustive; this file is your only deliverable. When done, reply with
2-3 sentences summarising the style and the path of your notes file.
