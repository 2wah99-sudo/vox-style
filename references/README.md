# References & method

The instruction system in `docs/` is based on a frame-by-frame analysis of five reference videos.
The videos and extracted frames are **not** stored in this repository (they are third-party
material); only measurements, notes and our own tools are.

## Reference set

| ID | Content | Source format | Frames | Cuts | Dialect |
|---|---|---|---|---|---|
| v1 `wallfive` | Collage explainer on real-estate investing ("Be the Bank.") | 1070×720, 30 fps, 69.7 s | 2091 | 31 | C · Scrapbook |
| v2 `porsche` | "Vox-style animated documentary: the history of Porsche" | 640×360, 30 fps, 196.6 s | 5899 | ≈ 95 true cuts (168 detector hits; the rest are steps of stepped zooms and pans) | A · Archive |
| v3 `mdriturana` | Rangpur city postcard collage | 736×414, 24 fps, 15.2 s | 364 | 0 | D · Postcard |
| v4 `schaapening` | Scrapbook spots: roadside cafe, jukebox, radio | 714×408, 30 fps, 10.5 s | 316 | 2 | C · Scrapbook |
| v5 `valuable826` | Nike Swoosh 50: a 16:9 paper editorial (0–44 s), then a 9:16 brand film pillarboxed (44–89 s) | 1280×720, 25 fps, 89.4 s | 2234 | ≈ 60, incl. a 25-shot flash montage (30 detector hits; the black pillarbox hides cuts) | B · Ink & Paper / E · Brand film |

**10,904 frames in total, about 5,800 of them visually distinct.**

## Method

1. **Every frame measured** (`tools/metrics.py`): change vs the previous frame, changed-pixel
   fraction, colour-histogram distance, luma and saturation; hard-cut detection; frame states
   (hold / local / global / cut); k-means palettes for the whole video and for each scene.
2. **Every distinct frame viewed** (`tools/sheets.py`): contact sheets in which each tile is a
   distinct frame and identical following frames are folded in as "+hold N s", plus 1 fps
   overview sheets.
3. **Seven analysis agents in parallel** (the Porsche video in 3 parts, v5 in 2 parts, v1, and
   v3+v4), all following `tools/ANALYSIS_BRIEF.md`. Each one stepped through its sheets, opened
   key frames at full resolution and **measured** rather than estimated: pixel-sampled colours,
   sizes converted to px@1080, durations in frames, easing curves fitted with `tools/motion.py`
   (phase-correlation translation, zoom search, easing fit) and with their own trackers.
4. **Cross-checks** across videos: animation cadence from the gaps between changing frames
   (12 fps in v1, v2 graphics and v5; 8–12 fps in v4; ones in v3), and hold-jitter and boil
   intervals.
5. **Synthesis** into `docs/`: values that agree across videos became rules; values specific to
   one video became dialect parameters.

## Analysis notes

| File | Range |
|---|---|
| `analysis/v1_wallfive.md` | whole video |
| `analysis/v2_porsche_A.md` | f0–1996 (0–66.5 s): cold open, Stuttgart, Lohner, timeline, quote, 356, 911 |
| `analysis/v2_porsche_B.md` | f1997–3972 (66.6–132.4 s): callouts, clippings, map, TV, 914–Boxster cards, montage |
| `analysis/v2_porsche_C.md` | f3973–5898 (132.4–196.6 s): chart, SUV, model cards, CRT reel, desk, end card |
| `analysis/v3_v4_short.md` | both short clips |
| `analysis/v5_valuable826_A.md` | f0–1406 (0–56.2 s): paper editorial and the start of the 9:16 section |
| `analysis/v5_valuable826_B.md` | f1407–2233 (56.3–89.3 s): 9:16 brand film and end slate |

Each note has the same 11 sections: overview, colour, typography, layout, textures, motion,
transitions, devices, scene log, recipes and uncertainties. In the notes, `$VOX` refers to the
analysis workspace, which is not included.

## Analysing a new reference

```bash
mkdir -p work/myref/frames
ffmpeg -i myref.mp4 -vsync 0 -start_number 0 -q:v 2 work/myref/frames/%05d.jpg
python3 tools/metrics.py myref.mp4 work/myref      # metrics.csv, summary.txt, scenes.json, palette
python3 tools/sheets.py work/myref                 # sheets/seq_*.jpg (every distinct frame), overview_*.jpg
python3 tools/motion.py work/myref 120 160 400 200 900 500   # timing and easing of one move inside a box
```

Then follow `tools/ANALYSIS_BRIEF.md`, and add the findings to the docs as a new dialect or as
parameter variants.

## Known limits

- The sources are 360p–720p web encodes, so typefaces are visual matches and fine grain cannot be
  measured. Colours of thin strokes are pushed toward lime or grey by chroma subsampling; the docs
  give intended values.
- Slide-in start offsets are extrapolated when moves begin under a cut.
- Easing names are best fits to stepped samples; treat them as curve families.
