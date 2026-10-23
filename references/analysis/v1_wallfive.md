# v1_wallfive — style notes (agent v1_wallfive)

Source: `$VOX/src/v1_wallfive.mp4` — 1070x720, 30 fps, 2091 frames, 69.7 s, 31 hard cuts / 32 scenes.
**Conversion used everywhere below:** px@1080p = px@720 × 1.5; "% H" = px / 720. Frame numbers are 0-indexed (f0 = `00000.jpg`).
Every sheet seq_000…seq_024 and overview_00…03 was read; key frames opened at full res; measurements by pixel sampling /
template tracking (scripts in `$VOX/tmp/v1_wallfive/`: `tmatch.py` scale+position tracker, `pshift.py` sub-px shift,
`textbox.py` text line boxes, `dom.py` k-means colours, `efit.py` easing fits).

## 1. Overview
A 70-s promo/explainer for a real-estate-investing webinar ("Be the Bank.", "Safe & predictable _investment.",
"Create real passive income.", presenter "Robert Hytha", end card "FIXnotes — Live on the last Wednesday of every month";
the very last frame f2068-2090 is a Fiverr thumbnail "COLLAGE STYLE EXPLAINER VIDEO", fiverr watermark top-right all video).
Visual identity: **paper collage on white** — high-contrast B&W cut-out photos (bank facade, bank-headed man, hands, houses,
magnifier, padlock, handshake, bare tree) where only the *hero object* is in saturated red-orange colour (toy house roof,
bank-head windows/door, balloon, watering can, octopus); flat **pastel geometric shapes** (salmon half/three-quarter discs,
salmon grid-paper circles, pale-green circles/semicircles/wedges) behind the cut-outs; layered **paper stock** (crumpled
white sheets with torn edges, blue-grey grid paper strips, saturated green textured paper) plus **scan/photocopy noise
blocks** and **olive masking-tape strips**; one **bold black neo-grotesk** headline per scene, sentence case with a full stop.
Everything is animated on **12 fps (3:2 pulled into 30 fps)** and the paper texture/props re-randomise ("boil") every
**15 frames (0.5 s)** — it reads as stop-motion even though the moves themselves are smooth eases.

## 2. Colour
Global k-means (palette.json, share of all pixels): #E9E8E9 30.1 %, #FCFCFC 17.1 %, #D5D9D2 15.8 %, #BABBB7 6.3 %,
#F9D8CE 5.3 %, #979694 4.5 %, #797166 3.8 %, #EAB19D 3.7 %, #504841 3.6 %, #E46841 2.1 %, #501B09 1.9 %, #BDAD75 1.7 %,
#1F1D18 1.7 %, #ADD095 1.2 %, #8EB770 1.1 %. Mean luma 203/255, mean saturation 0.105 → ~90 % of the screen is
white/grey paper; colour is spent in small doses.

Sampled roles (median of a patch / k-means of a region):
| role | hex | where / notes | approx share |
|---|---|---|---|
| base background (pure white "table") | #FFFFFF (sd 0) | around/behind paper sheets, f850, f1563, end card | 15-20 % |
| crumpled paper sheet (grey crease texture) | #DCDADC – #F0EFF0 (creases to ~#BABBB7) | main paper sheets in almost every scene | 30-40 % |
| grid paper (cool) | paper #CFCFD7, lines #ABA9B2 (f45); light variant paper #F1F3F8, lines #D6D8DE (f2030) | strips/panels | 5-10 % |
| grid-paper red margin line | thin red/maroon horizontal line on grid (f45 y≈596) | | <1 % |
| salmon flat shape | #E4ADA2 / #E5ADA1 (k-means 86 % of disc) | half-discs, 3/4-discs (f203-262, f438-577, f1593-1719) | 5-10 % when present |
| salmon grid circle (pink paper with red grid) | fill #FAC9BE / #FCD7D0, lines ≈ #E9B3A8–#E87C66 | behind hero objects (house, can, portrait) | 5-12 % |
| very pale pink soft circle | #FDEDF0 / #FEE2E5 | top of opening, portrait halo | 5-10 % |
| pale green circle / wedge | #BFD4B3, #C6D8BF–#D2E7CF (semi-transparent over grid) | edges of frame, behind man/scales | 3-8 % |
| saturated mint semicircle | #AEE192 (flat, sd 3) | f845-877 big semicircle | 30 % of that shot |
| green textured paper | #90C372 / #8FC171 (grainy) | frame borders f203-262, f1563-1719 | 3-10 % |
| dark olive green paper | #878E4D / #8D9452 | left border in Safe scene (green paper under a dark multiply wedge) | 5 % |
| olive masking tape | #B9BA73 / #BBC17B (slight highlight streak) | 2-4 strips per scene | 1-2 % |
| hero accent red-orange | #F25A45 / #E8625F (octopus), #D93624–#EA533A (toy-house roof), #CD4529–#E87C66 (balloon), #B72813–#DE5539 (watering can), #F07457 (padlock echo), #EC5A3C (logo) | ONLY on the hero object of the scene | 2-5 % |
| coral paper border | #F68168 / #EC7258 (grainy) | left edge of padlock scene and end card | 3-5 % |
| maroon duotone (portrait) | shirt #440F02 / #3E170D, skin highlights #F6AC9C, mid #AC9A74 | presenter photo only | 10 % of that shot |
| lime duotone devices | #919538 mid, #292904 shadow, #ECEFBC highlight | laptop & phone f1218-1319 | 3 % |
| brown/black scan block | #48281C / #8A4838 | padlock scene left | 3 % |
| headline black | #121213 (core), anti-aliased to paper | all headlines | 1-3 % |
| label white on black brush | brush #2E2E2E–#303030 (flat), text #FFFFFF | PRINCIPAL/INTEREST, "the last Wednesday" | <1 % |
| red caption text | ≈#E65B40 (anti-aliased median #B56663) | "of every month" | <1 % |

Colour rules observed:
- Photos are **desaturated B&W, high contrast** (blacks ~#1F1D18, whites clipped); the *one* object the narration is
  about is left in (or tinted to) **saturated red-orange** — toy house, bank-head door/windows, balloon, can, octopus. A
  B&W house turns colour at the moment the hand "picks" it (f155→f158).
- Duotone instead of colour for people/devices: presenter = maroon→orange duotone; laptop/phone = olive-lime duotone.
- Pastel shapes (salmon / pale green / pale pink) are always flat or semi-transparent (multiply-like, grid lines show
  through pale green), never gradients; they sit *behind* the hero cut-out and act as a spotlight.
- Text is always near-black #121213 on paper (white only when it passes over the dark shirt; see §3).
- Green appears as *paper* (#90C372) or *mint shape* (#AEE192), never on objects (except the green cheque/money photos).

## 3. Typography
Typeface: one **bold neo-grotesk** for all headlines — double-storey a, flat-cut t with angled top, tight apertures,
horizontal-ish C terminals, ampersand with open bowl. Matches **Inter Bold/ExtraBold (Inter Display Bold)** best
(also close: SF Pro Display Bold, Helvetica Now Display Bold). Free pick: **Inter 700, letter-spacing −2 %… −3 %**.
| style | example | size @720 | size @1080 | leading | case / align | colour |
|---|---|---|---|---|---|---|
| H1 headline | "Be the / Bank.", "Robert / Hytha", "Safe & / predictable / _investment.", "10+ years of / experience" | cap/ascender height 59-60 px (8.3 % H); font-size ≈ 81 px | cap ≈ 89 px, font-size ≈ 122 px | line pitch 73-76 px (10.4 % H) → line-height ≈ 0.93 | sentence case, ends with "."; left-aligned, 2-3 short lines (1-2 words each) | #121213 |
| H2 headline | "Create real / passive income." | cap ≈ 44 px (6.1 % H) | ≈ 66 px (font ≈ 90 px) | 56 px → ≈ 0.93 | sentence case, left | #121213 |
| H3 caption line | "income, security & growth" | ascender 47 px, x-height 34 px (font ≈ 62 px) | font ≈ 93 px | single line, 764 px wide (71 % W) | lower case, left at (153,75) | #121213 |
| small headline | "Live on" | cap ≈ 31 px | ≈ 46 px | — | sentence case | #121213 |
| brush label | "PRINCIPAL", "INTEREST" | cap 22-23 px (3.1 % H), tracking ≈ +10 % | cap ≈ 34 px | — | ALL CAPS, semi-bold geometric (Inter SemiBold / Montserrat SemiBold) | #FFFFFF on black dry-brush bar 53 px tall (80 px@1080), bar extends 25-40 px past text, ragged ends |
| brush caption | "the last Wednesday" | ascender 24 px | 36 px | — | lower case, Regular/Light weight | white on #2E2E2E brush bar |
| paper-slip caption | "of every month" | ≈ 33 px tall bbox, rotated ≈ −3° | | | lower case Regular | red-orange on torn white paper slip with grainy drop shadow |
| end thumbnail (not part of the animation system) | "COLLAGE STYLE / EXPLAINER VIDEO" | | | | heavy EXTENDED caps (Monument Extended / Archivo Expanded Black), black + #D33C24, white outline ≈ 4 px | |

Text decorations / devices:
- **Full stop** closes every headline — part of the voice.
- **The underscore device**: "_investment." — a real "_" glyph of the headline font placed before the keyword on the
  last line, baseline-aligned, 48×10 px @720 (72×15 px @1080; ≈ 0.8 × cap-height wide, ≈ 0.17 × cap thick). It does
  NOT blink (dark-pixel count constant 585 from f443 to f570) — it is a static "cursor/prompt" accent, not a typing anim.
- No highlighter, no underline, no box on headlines. Labels instead get a **black dry-brush bar** (see §8).
- Text never has outline or shadow.

How text animates (all on the 12-fps grid):
1. **Stepped "drop-in" (hold-keyframe zoom-down)** — used for "Be the Bank.", "Robert Hytha", "Create real passive income.":
   the headline appears already fully set but **oversized and displaced**, then jumps (no in-betweens) to smaller
   poses until it lands. Measured "Be the Bank.": f240 cap-line 112 px at x=401 (1.87×), hold 8 fr → f248 76 px at x=268
   (1.27×), hold 5 fr → f253 60 px at x=217 (1.00×). "Create real passive income.": f1813 ≈1.4× centred over the tree
   (lines y 305-471) → f1818 ≈1.15× at x=530 (overflowing right edge) → f1823 final 1.0× at x=543,y=180. "Robert Hytha":
   f1035 ≈1.8× at right (x 584-1053), small slides on f1038/f1040, f1043-1045 jumps to the LEFT edge cropped by the frame,
   f1048 final 1.0× at (30,223). So: 3 poses, 5-8 frames each (2-3 ticks), total ≈ 13 frames (0.43 s).
2. **Slide with the layer**: "Safe & predictable _investment." is set on the paper sheet and slides in with the whole
   collage from the right: x 450→316→(lens)→218→195→181→171→166→164 on f423…f443 — easeOutExpo, ≈ 27 fr (0.9 s)
   total, first visible frame already ≈ 85 % through (see §6).
3. **Rise**: "Live on" slides up from y 475→419→397→388→384→383 (f1980-1993): easeOutQuint/Quart, ≈ 18-25 fr, 92 px
   travel (12.8 % H). Then "the last Wednesday" is revealed by a L→R brush-bar wipe (§8) and "of every month" pops in on a
   paper slip (f2010).
4. **Colour by background**: "10+ years of experience" enters large & WHITE over the dark maroon shirt (f1083 at left,
   cropped; f1088-1090 centre-bottom) then jumps to its final place right of the face in BLACK at 1.0× (f1095). Rule:
   text over a dark photo is white, over paper black (implemented as a hard switch per pose, not a blend mode —
   white measured #FFECEE, not a difference-blend cyan).
5. Exit: text is simply cut away with the scene, or vanishes on a tick (f1218 "Robert Hytha"/"10+" removed when the
   laptop/phone pop in). No fades anywhere.

## 4. Layout & composition
- Frame is filled edge to edge; **no safe-area margin for collage** (paper sheets, tape and shapes bleed off all edges),
  but **text keeps ≈ 3-15 % margin**: "Be the Bank." left edge x=217 (20 % W), top 150 (21 % H); "Safe…" x=164-168
  (15 % W), y=222 (31 % H); "Robert Hytha" x=30 (2.8 % W!), y=223; "income, security & growth" x=153, y=75 (10 % H);
  "Create real…" x=543 (51 % W), y=180 (25 % H). Text sits in the empty half of an asymmetric composition.
- Typical composition = **hero cut-out on one third, headline on the opposite third**, pastel circle centred behind the
  hero (circle diameter ≈ 55-75 % H, e.g. salmon grid circle ≈ 470 px @720), secondary props near the edges.
- Background stack (back → front), measured on f230 / f460 / f1615:
  0 white table #FFFFFF → 1 coloured paper border (green #90C372 / coral #F68168, 3-10 % W strips at an edge) →
  2 grid-paper strip(s) (vertical or horizontal band 15-35 % W) → 3 crumpled/torn white paper sheet (60-85 % of frame,
  slightly rotated 0-2°, torn/ragged edge) → 4 scan-noise block (dark streaky photocopy rectangle at an edge, ≈ 75×420 px)
  and grain/halftone patches → 5 pastel flat shape(s) (salmon disc, pale-green circle; often 2) → 6 B&W cut-out photo(s)
  → 7 colour hero object → 8 doodles (sparkle ✧, thin arrows, crosshair +) → 9 headline text → 10 tape strips on top
  (often crossing a sheet corner) → 11 global boil (paper crease overlay).
  ≈ 8-12 layers per shot.
- Scale relationships: hero object 35-60 % H tall (bank-head man 100 % H, toy house ≈ 30 % H, watering can ≈ 45 % H,
  handshake 609×171 px = 57 % W). Doodles tiny: sparkle ≈ 25-40 px, arrows 1.5-2 px stroke, 90-190 px long.
- Negative space: 30-45 % of every frame is calm paper; headlines are placed only in that space.

## 5. Textures & materials
- **Crumpled paper sheet**: scanned white paper with soft grey creases (luma 220-240, crease lines down to ~170),
  high-pass noise std ≈ 5 (fine grain). Torn/ragged sheet edges with a thin darker rim; sheets are rectangles 60-85 % of
  frame, rotated 0-2°. In the end card the sheet has scuffs, a dark smudge and a hand-drawn dot.
- **Grid paper**: square grid, pitch 19.5 px @720 (29 px @1080) on the blue-grey stock (#CFCFD7 / lines #ABA9B2,
  1 px) and 16.5-17 px (25 px @1080) on the light stock (#F1F3F8 / lines #D6D8DE). One stock has a red margin line.
  Salmon grid circle: same 20-px grid in red on #FAC9BE paper, cut into a circle, with darker red smudges.
- **Green paper**: #90C372 with visible pulp grain (sd ≈ 6-8), used as frame-edge borders.
- **Scan/photocopy blocks**: rectangles (~75-160 px wide, 300-420 px tall) of dark streaky "photocopier" texture —
  greenish-black (Be the Bank / Safe), brown-black (#48281C, padlock), orange-black (end card) — always at the left edge.
- **Halftone / stipple patches**: black dot halftone gradients (f45 left: coarse dots fading to white, ≈ 120×300 px;
  f698-767 big black dot-gradient block top-centre) and grey stipple squares (≈ 80×80 to 150×100 px) near the bottom
  of many shots. CMYK-halftone colour photos (row of town houses f63-130, f580-697) — visible rosette dots.
- **Cut-out photos**: hard, clean scissor edges, **no white outline, no stroke**; B&W with crushed blacks. Some objects
  (padlock) get a **misregistered colour echo**: an orange (#F07457) copy offset ≈ 15-20 px right behind the B&W photo.
- **Drop shadows** — only on paper props (contract, cheque, paper slip, right edge of the tree sheet, end-card sheet):
  **grainy / dithered soft shadow**, offset mostly downward (≈ +6…+15 px y, 0…+10 px x @720), very large blur
  (falloff ≈ 100-160 px @720 from luma 53 at the edge back to ~180), opacity ≈ 75 % black at the edge, with heavy
  monochrome noise inside the shadow (high-pass std ≈ 18 vs 5 on paper) — i.e. a stipple/dither shadow, not a smooth
  Gaussian. Cut-out photos (people, houses, hands) have NO shadow.
- **Balloon**: airbrushed red with grain (hp std ≈ 9), white "$".
- **Global grain/flicker**: none at 30 fps (hold frames are bit-identical apart from codec noise, mean |Δ| 0.04). No
  vignette, no light leaks, no gate weave.
- **Boil**: see §6 — paper/crease overlay and prop positions re-randomise every 15 frames.

## 6. Motion
### 6.1 Cadence (verified on metrics.csv, all 2091 frames)
- 743 changing frames; gaps between changing frames: 2 (347×), 3 (345×), 5 (24×), 7/8 (18×), longer = holds. Only 3
  gaps of 1: f1022→1023 (cut placed 1 frame off-grid) and f1033→1034→1035 (f1034 = 0.14 codec blip).
- Every changing frame sits on frame % 5 ∈ {0, 3} (372 + 369 of 743): content is rendered at **12 fps** and pulled into
  30 fps with a 2-3-2-3 cadence (0,3,5,8,10,13,…). In code: render at 12 fps and hold; or at 30 fps quantise time:
  `t12 = Math.floor(frame30 * 12 / 30); t = t12 / 12`. Hold frames are identical (max mean |Δ| 1.18 = codec noise) →
  **no per-frame grain/boil at 30 fps; textures also step only on the 12 fps grid** (and boil much slower, below).
- Cuts are also on the grid, with one exception (f1022 changes, f1023 cut) (cut frames 3,60,65,135,140,198,203,208,263,268,420,425,438,578,698,768,845,878,883,935,
  1023,1028,1320,1563,1593,1720,1725,1730,1875,1880,2068 — all ≡ 0 or 3 mod 5).
### 6.2 Boil / "alive" stepping (all on the 12-fps grid)
- **Texture & placement boil every 15 frames (0.5 s = every 6th 12-fps tick)** in static holds: e.g. f30,45 / f93,108,123
  / f453,468,483,498,513,528,543,558 / f1608,1623,…,1698 / f1753,1768,…,1843 (exact 15-fr spacing). Some shots use 7-8
  fr (every 3rd tick, f140-197, f580-767) and the portrait shot 17-18 fr (f1125,1143,1160,1178,1193).
  What changes at a boil tick (pairwise diff + sub-px tracking):
  * crumpled-paper crease/smudge overlay is swapped / re-offset (crease lines jump, 20-60 % of pixels change slightly);
  * selected props are nudged: sparkle ±2-9 px, whole paper-sheet group toggles 0 / −13.5 px vertically (f1638, f1653,
    f1683, f1698 vs f1623, f1668), balance scales up to (−18, +32) px; watering can (−1, +3.5) px;
  * headlines, hero photos and scan blocks stay pixel-locked (shift 0.00 px).
  States do not loop: in 3 test regions of f440-573 and f1753-1873 every boil tick gives a new state (pairwise
  mean |Δ| 8-40); only isolated small props occasionally return to an earlier pose.
- **Mirror-flip twitch**: the bank-head man (f300-419) is horizontally mirrored and un-mirrored ("BANK" reads mirrored on
  f305/f323…, normal on f308/f320) at 8/22-frame intervals with a (+33, −16) px offset — a cheap "alive" wiggle.
- **Continuous swing/bob**: in f1440-1562 the Victorian house (hanging on the red rope) + its salmon grid circle move on
  every 12-fps tick along a slow loop: centre x 683→655→712→664→706, y 276→349→247→251 (@720) = amplitude ≈ ±28 px x,
  ±50 px y (±42/±75 px @1080), period ≈ 1.5-2 s, eased (sine-like), rotation ≤ ±2° (template tracking).
- Octopus tentacles (f3-59) are frame-by-frame animated on 12 fps and recolour maroon→coral.
### 6.3 Entrances (measured, easings fitted with `efit.py` on 12-fps samples)
| element | frames | measured values | fit |
|---|---|---|---|
| paper sheet slide-in from right (f580 scene) | f580-600 | left edge x 683,431,279,209,169,147,137,133 | easeOutQuint, 28 fr (0.93 s), start ≈ f575 under the cut; first visible frame ≈ 60 % done; travel ≥ 550 px (≥ 51 % W) |
| paper sheet slide-in (f203 scene) | f203-210 | x 376,238,181,159 (template corner) | easeOutExpo ≈ 14 fr (0.47 s) |
| balloon + pump slide-in from right | f583-603 | x 953,787,647,575,531,501,481,467,459 | easeOutExpo 36 fr (1.2 s) — slower than the sheet (parallax: decay 0.62/tick vs 0.50/tick) |
| headline slide-in with layer ("Safe…") | f423-443 | x 450,316,218,195,181,171,166,164 | easeOutExpo 27 fr (0.9 s) |
| "Live on" rise | f1980-1993 | y 475,419,397,388,384,383 | easeOutQuint ≈ 25 fr / easeOutQuart 18 fr (rms 1.1 px) |
| opening zoom-out (whole collage) | f0-18 | scale 1.289(f0-2 hold),1.167,1.099,1.056,1.035,1.015,1.015,0.994→1.0 | easeOutExpo/Quint ≈ 27-30 fr, from ≈ 1.3-1.45× |
| logo card grow (end) | f1880-1895 | logo width 163,208,229,241,248,252,254 → 256 (0.64→1.0) | easeOutExpo 30 fr (1.0 s) |
| handshake grow | f1595-1610 | width 443,535,575,598,606,609 (0.73→1.0) | easeOutQuart ≈ 18 fr (0.6 s) |
| **pop with overshoot** – laptop | f1218-1240 | scale 0.30,0.81,1.17,1.23,1.17,1.06,1.00 | easeOutBack, 18 fr (0.6 s), **overshoot 23 %** (stronger than default s=1.70158 → use s≈3) |
| pop with overshoot – Victorian house | f1325-1345 | height scale 0.83,0.98,1.057,1.062,1.04,1.015,1.0 | easeOutBack ≈ 20 fr, overshoot 6 % |
| **pop-big-hold-settle** – toy house | f938-968 | roof width 135,277,328,351,356 (hold 8 fr) 347,319,243,221,214,213 → scale vs final 0.63,1.30,1.54,1.65,1.67, hold, 1.63,1.50,1.14,1.04,1.0 | 2 eases: out (≈8 fr) to 1.67×, hold ≈ 8-10 fr (0.3 s), easeInOut down (≈ 10 fr) |
| padlock scene zoom-out reveal | f878-893 | text template scale 1.205 (f880),1.084,1.055,1.0 (f888); padlock starts ≈ 2.5× at f878 | easeOutExpo ≈ 12-15 fr |
| contract / cheque "spin-in" | f700-708, f770-780 | starts ≈ 0.25× scale, rotated ≈ −10°, → 1.0×, ≈ −3° over 8-10 fr | easeOut (≈ Quart), rotation settles with scale |
| bank-head man rise from bottom | f205-225 | head centre y 614,468,320,169,112,109,121,131,139 (tracking ncc 0.4-0.96, approximate; overshoots up ≈ 30 px then settles) | easeOutBack-like, ≈ 20 fr (0.67 s), travel ≈ 475 px = 66 % H |
| green semicircle grow from bottom edge | f845-850 | radius ≈ 340 → 540 → 560 px (scale 0.6→0.96→1.0) | 2 ticks, easeOut |
| money stacks / props pop up from bottom | f8-15, f850-860 | 3-4 ticks each, staggered 2-3 ticks | easeOut |
| safe slides up from bottom | f78-88 | 4 ticks | easeOut |
| hand enters from frame edge | f90-98 (left), f140-155 (top-right), f973 (top-right with grabber), f1375 (bottom-left) | 3-4 ticks in, holds, 3-4 ticks out the same edge | easeOut in / easeIn out |
- Stagger between elements in an incoming scene: 1-2 ticks (2-5 frames); e.g. f263-273: paper (f263), grid strip
  (f265), white panel (f268), pale-green circle + hand/house from left (f270), money stacks from right (f273).
- Rotation: hero objects held by a hand tilt 5-15° (toy house f158-170), watering can enters rotating ≈ 30°→ −20°
  (f1725-1733), cheque/contract −10°→ −3°. No continuous spin.
### 6.4 Idle
- Holds of 0.5-2 s with only the 15-fr boil. Repeating cycles: the → arrow above the toy house re-draws every ≈ 25 fr
  (draw-on f280-290: right end x 364,405,425,436/440→441 = 4 ticks, easeOut; erased at f300; redrawn f305, f330, f355, f380), and a $ bill
  flies from house to stack every ≈ 25 fr (8-10 ticks per flight, flipping/curling bill) — a GIF-like loop f278-400.
- Balloon inflates in 3 pump pulses (f600-673), then pops in 2 frames of red shards (f675, f678) and is gone (f680).
- Watering can pours dotted arcs (f1740-1775, 2-3 dotted lines growing), dollar-bill "leaves" grow on the tree in bursts
  (f1778-1850, 3-6 bills per tick).
### 6.5 Exits
- Elements rarely exit individually; the scene is pushed/zoomed out (§7). Hands exit the way they came (3-4 ticks).
  The toy house is lifted out top-right by the grabber (f1005-1013). Text disappears on a tick.
### 6.6 Camera
- No continuous camera drift/parallax pans. "Camera" moves exist only as **transition pushes** (§7) and the zoom-out
  reveals at scene starts (opening, padlock, logo). Different layers of an incoming collage arrive at different speeds
  (sheet decay 0.50/tick vs balloon 0.62/tick) — parallax only during the slide-in.

## 7. Transitions
Every scene change is a hard cut on the 12-fps grid, dressed as a **push**: the outgoing collage accelerates out
(ease-in, 2-3 ticks) and the incoming collage is already ~50-85 % arrived on its first frame and decelerates in
(ease-out expo/quint, 15-30 frames). No dissolves, no wipes with soft edges, no flashes.
| frames | type | details |
|---|---|---|
| f0-2→f3 | poster hold → zoom-out | f0-2 = first pose held 3 fr (scale 1.29), zoom-out starts f3 |
| f55-65 | push-in cut ×2 | outgoing small push; f60/f63/f65: new $-bill-engraving scene appears zoomed (bank carried over) and settles while the halftone house row shrinks/slides (f63-80) |
| f130-140 | cut + slide from right | f138 new white scene with houses entering from right, f140 houses row in place (layers staggered 1 tick) |
| f195-203 | **push-in through cut** | outgoing scale 1.008 (f195) → 1.068 (f198) → 1.307 (f200) about (≈ 740, 220) — easeInExpo ≈ 9 fr; cut f203 to sheet sliding in from right (x +217, +79, +22, 0) |
| f258-273 | slide-right + rebuild | outgoing drifts right (+26 px f260), cut f263; the bank-head man stays (moved right) while bg layers swap tick by tick (paper → grid → white → circle → hand/house L → money R) |
| f413-425 | **push-left** | outgoing centre x 749,737,713,631 (f413-420, easeInExpo ≈ 12 fr), cut f423: Safe collage arrives from right (easeOutExpo 27 fr) with the magnifier sweeping L→R over the headline (lens shows a ≈ 1.5-1.7× magnified copy of the text under it) |
| f568-580 | push-left | outgoing x 285,278,260,210 (f570-578, easeInCubic 8 fr), cut f580, incoming sheet/balloon from right (easeOutQuint 28 fr / easeOutExpo 36 fr) |
| f693-708 | cut + spin-in | f698 empty bg (green half-disc, horizon line), f700-708 contract scales 0.25→1 with rotation, pen flies in |
| f765-780 | cut + spin-in | f770 empty paper bg, f773-780 cheque scales 0.25→1, −10°→ −3° |
| f843-850 | cut to graphic | white frame, mint semicircle grows from bottom edge in 2 ticks, money stacks pop |
| f875-893 | cut + zoom-out reveal | f878 padlock + text ≈ 2.5×, zooms out to 1.0 by f888 (easeOutExpo) |
| f933-945 | cut + pop | f938 empty bg, toy house pops (0.63→1.67× hold → 1.0) |
| f1020-1033 | cut + layer build | portrait appears whole (f1023); pink/salmon circles, saxophone and olive strip arrive over 2-3 ticks |
| f1318-1333 | cut + pop | f1323 white bg with tiny house (≈0.1×) → easeOutBack to 1.06 → 1.0 |
| f1560-1575 | cut + slide | torn sheet in place, split-circle grows f1565-1573, scales slide in from top-right f1573-1585 |
| f1590-1600 | cut + grow | handshake 0.73→1.0 easeOutQuart with its salmon disc |
| f1718-1730 | triple cut | f1720 handshake layout re-posed (shift), f1723 tree scene layer 1 (green semicircle + grid strip), f1725 paper sheet + can entering right, f1728/1730 can rotates in — rapid 2-3 fr build |
| f1870-1880 | **push-in through cut** | "Create real passive income." + can scale up ≈ 1.3-1.4× (f1873-1878), cut f1880 to end card: card/logo grow 0.64→1.0 (easeOutExpo 30 fr) |
| f1968-1980 | in-scene re-layout | logo shrinks 0.66× and rises (top y 287→221, easeInOutCubic 11 fr) to make room for "Live on" |
| f2068 | hard cut | Fiverr thumbnail held 23 fr |
Frequency: push-in-through-cut 3×, push-left/right 4×, cut + pop/spin/grow 8×, cut + layer rebuild 4×, zoom-out reveal 3×.
Rule of thumb: **every new shot starts with motion** (something sliding/growing for the first 0.3-1.0 s) and
**every shot ends with an ease-in push** in the last 3-8 frames.

## 8. Recurring devices
- **Pastel spotlight shapes**: salmon grid-paper circle (Ø ≈ 470 px @720 = 65 % H) behind the hero; salmon flat half-disc
  / 3/4-disc (#E4ADA2) rotating/growing open behind the subject (f203-215: half-disc scales 0.3→1 while rotating ≈ 30°);
  pale-green circle/wedge at frame edges; mint semicircle. Enter by scale-from-centre (2-4 ticks) or rotation of a wedge
  (f1383-1393, f160-165).
- **Split circle**: a circle made of a left half in B&W scan texture and a right half in pale green (f1565-1590) — grows
  from 0.3 to 1.0 in 3 ticks.
- **Thin hand-drawn arrows**: 1.5-2 px @720 black line with an open "V" head (≈ 12 px); → above/below objects, ↑ below the
  cheque and house, ↓ above the bank. Drawn on L→R / bottom→top in 3-4 ticks (stroke end x 364,405,425,440,441 → ease-out, no
  overshoot), held ≈ 0.4-0.7 s, removed on one tick, redrawn (loop, period ≈ 25 fr).
- **Sparkle ✧**: 4-point concave star outline, 1.5 px stroke, ≈ 30-40 px; appears on one tick, nudges ±2-9 px on every
  boil tick. Also a thin crosshair "+" (≈ 20 px) and "×" marks with a short dash (f938-1022, f1440-1560).
- **Olive masking tape strips** (#B9BA73, 60-180 × 15-25 px, angled 10-60°): 2-4 per scene; they fly in/out flipping
  over 2-3 ticks during transitions and re-pose at boil ticks.
- **Dry-brush label bar**: black (#2E2E2E) rough brush stroke 53 px tall, ragged/streaky ends, white caps text centred;
  revealed by a **hard-edged L→R wipe** in 3 ticks (≈ 25 %, 70 %, 100 % on f790/793/795; INTEREST f803/805/808 — 2nd
  label starts 13 fr after the 1st). Text is masked together with the bar. The end card uses the same bar for
  "the last Wednesday" (wipe x 456→556→697→827 on f1990/1993/1995, i.e. 3 ticks, ≈ 6 fr).
- **Paper slip caption**: torn white paper slip, rotated ≈ −3°, red text, grainy drop shadow; pops in on one tick (f2010).
- **Colour-on-select**: a B&W object turns colour when picked/featured (house f155→158).
- **Hands** (B&W, cropped at the wrist, entering from a frame edge): holding/giving money, picking a house, pulling a
  rope, holding a grabber tool. Always hard-edged cut-outs.
- **Magnifier lens**: B&W magnifying glass cut-out; inside the lens the underlying text/image is shown ≈ 1.5-1.7× (f428-433, by eye)
  — real magnification, not a static photo.
- **Money**: B&W or green $100 bills/stacks — flying bills curl/flip per tick (6-8 distinct drawings), stacks pop up
  from below, bills sprout on the tree.
- **Dotted water/flow lines**: 2-3 dotted arcs (dot ≈ 3 px, gap ≈ 4 px) grow from the spout tick by tick.
- **Misregistered colour echo** (orange offset copy behind the B&W padlock).
- **Halftone dot-gradient blocks** and **photocopy scan strips** as pure decoration at edges.

## 9. Scene log
| frames | time | on screen | devices | motion / transition notes |
|---|---|---|---|---|
| f0-2 | 0.00-0.07 | Poster pose: B&W bank facade + maroon photo octopus tentacles on grid panel / crumpled paper; pale-green circles L/R; black halftone patch left | — | hold 3 fr at scale 1.29 |
| f3-59 | 0.10-1.97 | Zoom-out (1.29→1.0, easeOutExpo ≈ 1 s); tentacles wiggle frame-by-frame and shift maroon→coral #F25A45; B&W $-stacks pop up behind bank L+R (f8-15); soft pink circle top; thin ↓ arrow draws above bank (f13); white strip with torn black edge slides in at left; tape strips fly/flip | tape, ↓ arrow, halftone, pastel circles | boil f30, f45 |
| f60-64 | 2.00-2.13 | double cut | — | push-in cut |
| f65-134 | 2.17-4.47 | Bank carried over (moved right) on faint B&W $-bill engraving ("IN GOD WE TRUST" + Treasury) over grid; CMYK-halftone colour row of houses shrinks/slides left (f63-80); big black serif "?" pops (f73, ≈ 425 px tall, 59 % H); grey safe with orange-red dial slides up from bottom (f78-88); B&W hand with colour $100 stack enters from left (f90-98), safe door opens, money goes in; thin → arrow draws bottom-left (f98-103); door closes (f118); hand exits left (f123-130) | ?, →, tape | boil f93,108,123 |
| f135-139 | 4.50-4.63 | cut + houses enter from right | | slide |
| f140-197 | 4.67-6.57 | Row of B&W houses on thin black ground line; B&W hand from top-right picks the last house → it turns colour (red roof #D93624, brown walls) and tilts 10-15°; salmon grid circle scales up behind it (f158-165); pale-green wedge rotates in left; grain patch bottom | colour-on-select, grid circle | boil every 7-8 fr |
| f198-202 | 6.60-6.73 | outgoing push-in 1.00→1.07→1.31 | | easeInExpo, cut f203 |
| f203-262 | 6.77-8.73 | Crumpled sheet slides in from right over green paper + grid strip + right stained paper; salmon half-disc rotates/scales open; bank-head man rises from bottom (f205-225, overshoot 30 px); ✧; black pen top-right; green-black scan block left; **"Be the / Bank."** stepped drop-in f240 (1.87×) → f248 (1.27×) → f253 (1.0×) at (217,150) | half-disc, ✧, stepped text | text holds 8 + 5 fr |
| f258-267 | 8.60-8.90 | outgoing drifts right (+26 px), cut f263 — man persists | | rebuild |
| f268-419 | 8.93-13.97 | Loop scene: B&W hand (left) holds colour toy house on salmon grid circle; $ bills fly in an arc to a growing pile of green $ stacks beside the bank-head man (right, on pale-green circle, crosshair +); → arrow above draws on/off (≈ 25-fr loop); man mirror-flips (f305/308/323/345/353/375/383); grain patch | arrow loop, flip twitch | |
| f413-437 | 13.77-14.57 | outgoing push-left (easeInExpo), cut f423 → Safe collage slides in from right; magnifier sweeps L→R magnifying the headline | lens | |
| f438-577 | 14.60-19.23 | **"Safe & / predictable / _investment."** left on paper sheet; salmon half-disc lower-left; olive-green paper + scan strip left; B&W magnifier drifts over B&W stock-chart prints and a colour line-chart paper (top right), magnifying what is under it (incl. "le" of predictable, f513-570); ✧ | magnifier, underscore, ✧ | boil every 15 fr (453…558) |
| f570-579 | 19.00-19.30 | outgoing push-left (easeInCubic 8 fr) | | cut f580 |
| f580-697 | 19.33-23.23 | Crumpled sheet slides in from right (easeOutQuint); CMYK-halftone town-house row on horizon line; red balloon with white "$" + B&W bicycle pump (olive handle, black hose) arrive from right (easeOutExpo, slower); 3 pump strokes inflate the balloon (f600-673); balloon pops (f675-678 red shards) | balloon pop | boil 7-15 fr |
| f698-767 | 23.27-25.57 | Contract spins/scales in (0.25→1, −10°→ −3°) with grainy shadow; red fountain pen flies in and signs; colour 3D pie chart pops on salmon grid circle (f718-725); colour line chart on pale-green half-disc; old letter bottom-left; black halftone gradient block top | shadow, pie, + | |
| f768-844 | 25.60-28.13 | Green cheque (First National Bank of Washington) spins/scales in on paper; salmon grid circle TL; green wedge R; B&W eyes photo strip behind; **PRINCIPAL** (f790-795) and **INTEREST** (f803-808) brush-bar wipes; thin ↑ arrow below | brush labels | |
| f845-877 | 28.17-29.23 | White bg, mint #AEE192 semicircle grows from bottom (2 ticks); B&W $100 stacks pop up, staggered | | |
| f878-934 | 29.27-31.13 | Zoom-out reveal: padlock (B&W + orange echo) + cash pile + **"income, security & growth"** (H3) top; coral paper border + brown scan block left; grid panel right; ✧ | colour echo | easeOutExpo ≈ 12-15 fr |
| f935-1022 | 31.17-34.07 | 3D colour toy house (red roof) on white/crumpled paper, ground line slides in from right; house pops 0.63→1.67×, holds, settles 1.0× (f938-968); B&W hand with grabber enters top-right (f973), lifts the house out (f1005-1013); salmon grid circle grows (f988-998); × mark | pop-hold-settle | |
| f1023-1027 | 34.10-34.23 | cut ×2 to portrait | | |
| f1028-1319 | 34.27-43.97 | Presenter (maroon/orange duotone) on salmon grid circle + pale pink circle; grid panel right; plaid scan strip under bust; saxophone (gold→B&W) bottom-left; tape. **"Robert / Hytha"** stepped drop-in (1.8× right → cropped left → 1.0× at (30,223), f1035-1048); ✧ (f1055); → arrow draws under name (f1055-1060); **"10+ years of / experience"** white over shirt → black right of face (f1083-1095); orange spiky burst flickers behind (f1195-1240); text cut at f1218; lime laptop pops (easeOutBack 23 % overshoot, f1218-1235) and lime phone (f1230-1238) | stepped text, arrow, ✧, pop | boil 17-18 fr |
| f1320-1322 | 44.00-44.07 | cut | | |
| f1323-1562 | 44.10-52.07 | B&W Victorian house pops from tiny (easeOutBack, 6 % overshoot) over pale-green semicircle + crumpled sheet; B&W hand pulls red rope (f1375) lifting/tilting the house; red diagonal slash across house; pale-green wedge rotates in (f1383-1393); thin ↑ arrow draws below (f1418-1438, loops); salmon grid circle appears (f1440-1450); house + circle swing/bob every tick (±28 px x, ±50 px y, period ≈ 1.5-2 s) till f1562; × mark | rope, slash, ↑, wobble | wobble on ones of 12 fps |
| f1563-1592 | 52.10-53.07 | Torn sheet on green paper + grid strip; split circle (B&W scan half + pale-green half) grows (f1565-1573); balance scales slide in top-right (f1573-1585); tape | split circle | |
| f1593-1719 | 53.10-57.30 | B&W handshake grows 0.73→1.0 (easeOutQuart) over salmon 3/4-disc; scales top-right; pale-green circle right; scan block left; ✧ | | boil exactly 15 fr (1608…1713), sheet toggles −13.5 px |
| f1720-1729 | 57.33-57.63 | triple cut | | rapid layer build |
| f1730-1874 | 57.67-62.47 | B&W bare tree on grid strip + crumpled sheet (dithered shadow on its right edge); red watering can rotates in from right (f1725-1733); dotted water arcs (f1740-1775); salmon grid circle behind can (f1750-1755); olive tape; $ bills sprout on the tree (f1778-1850); **"Create real / passive income."** stepped drop-in (f1813 ≈1.4× → f1818 ≈1.15× → f1823 1.0× at (543,180)) | dotted flow, stepped text | boil 15 fr |
| f1870-1879 | 62.33-62.63 | push-in through cut (≈1.35×) | | |
| f1880-2067 | 62.67-68.90 | End card: torn crumpled sheet (scuffs, dithered smudge) centred on white; coral paper border + orange-black scan block left; light grid panel + pale-green circle right; tape TR/BL. FIXnotes logo (orange hexagon-house icon + "FIX" bold orange + "notes" grey) grows 0.64→1.0 (f1880-1895); at f1970 logo shrinks to 0.66× and rises; "Live on" rises (f1980-1990); brush bar "the last Wednesday" wipes L→R (f1990-1995); red "of every month" slip pops (f2010) | brush bar, paper slip | holds 0.5 s, tiny drift |
| f2068-2090 | 68.93-69.70 | Fiverr thumbnail "COLLAGE STYLE EXPLAINER VIDEO" (hand+toy house on salmon grid circle, flying bill, → arrow, bank-head man with money, halftone patch) | | hard cut, hold |

## 10. Replication recipes
```js
// R1 — 12 fps stepped time (everything: moves, textures, cuts)
const FPS_OUT = 30, FPS_ANIM = 12;
const tAnim = (frame) => Math.floor(frame * FPS_ANIM / FPS_OUT) / FPS_ANIM;   // seconds, quantised
// at 1080p/30fps: render each element with t = tAnim(frame); cuts only on frames where tAnim changes.
// 60 fps master? use Math.floor(frame*12/60)/12 (5-frame holds).

// R2 — boil (paper crease overlay + prop nudge), in addition to R1
const BOIL_PERIOD_S = 0.5;            // 15 fr @30; use 0.25 s for busy shots
const boilIdx = Math.floor(tAnim(frame) / BOIL_PERIOD_S);
paperOverlay.src   = creaseTextures[hash(boilIdx) % creaseTextures.length]; // 4-8 scanned crumple maps, multiply, opacity .6-.9
paperOverlay.offset = randVec(hash(boilIdx), 0, 60);                       // px @1080
for (const p of props) {             // sparkles, tape, small cut-outs, sometimes the whole sheet group
  p.dx = rand(hash(boilIdx, p.id), -6, 6) * 1.5;   // ±9 px @1080 (sparkle), up to ±30 px for loose props
  p.dy = rand(hash(boilIdx, p.id, 1), -6, 6) * 1.5;
  p.rot = rand(hash(boilIdx, p.id, 2), -1.5, 1.5); // deg
}
// headlines and hero photos: NO boil (pixel-locked).

// R3 — push transition (outgoing ease-in → hard cut → incoming ease-out with parallax)
outgoing: { prop: 'x', by: -0.5*W .. -1.0*W, dur: 0.27-0.40 s, ease: 'easeInExpo' /* or scale 1→1.3-1.4 easeInExpo for push-in */ }
cut at tAnim boundary;
incoming layers: [
  { layer: 'paperSheet', fromX: +0.9*W, dur: 0.93, ease: 'easeOutQuint', delay: -0.15 /* starts under the cut */ },
  { layer: 'heroObject', fromX: +1.3*W, dur: 1.20, ease: 'easeOutExpo',  delay: -0.15 },
  { layer: 'headline',   travelsWithSheet: true },
  { layer: 'tape/doodles', appear: 'on tick', stagger: 2-5 fr },
]

// R4 — stepped headline drop-in (hold keyframes, no interpolation)
// measured block centres "Be the Bank.": (620,386) 1.87x -> (413,400) 1.27x -> (338,217) 1.0x  @720
// "Create real passive income.": (≈800,388) ≈1.4x -> (800,333) ≈1.15x -> (769,230) 1.0x
poses = [ {scale: 1.4-1.9, centre: frameCentre + (0.08*W, 0.03*H), hold: 8/30},  // big, roughly centred
          {scale: 1.15-1.27, centre: lerp(poseA, final, 0.5..0.7), hold: 5/30},   // may be cropped by frame edge
          {scale: 1.00, centre: final} ];                                          // no in-betweens, no fades
font: Inter 700, size 122 px @1080 (H1) | 90 px (H2), letterSpacing -0.025em, lineHeight 0.93, color #121213, left aligned,
sentence case, end with '.'; optional '_' glyph prefix on the key word of the last line (static, no blink).
// Variant: if a pose overlaps a dark photo, render that pose in #FFFFFF.

// R5 — pop with overshoot (devices, houses)
scale: 0.3 → 1.0, dur 0.6 s, ease easeOutBack(s≈3.0) /* measured peak 1.23 */ ; or s=1.0 for subtle 6 % (house)
// pop-big-hold-settle (emphasis): 0.6 → 1.67 (easeOutCubic 0.27 s) hold 0.3 s → 1.0 (easeInOutCubic 0.33 s)
// spin-in (paper props): scale 0.25→1, rotate -10°→-3°, 0.3 s easeOutQuart + dithered shadow.

// R6 — paper collage stack (per shot)
layers = [white #FFFFFF table, edge paper (green #90C372 | coral #F68168, grain), grid strip (pitch 29 px @1080, lines #ABA9B2 1.5 px on #CFCFD7 | #D6D8DE on #F1F3F8),
          crumpled sheet (60-85 % frame, rot 0-2°, torn edge), scan-noise block at left edge (≈110×630 px @1080),
          halftone/stipple patch, pastel shape (salmon #E4ADA2 disc | salmon grid circle #FAC9BE + red grid | pale green #BFD4B3 @ ~70 % opacity),
          B&W cut-out photo (hard edge, no outline, contrast +40 %, blacks crushed), red-orange hero object (#D93624-#F25A45),
          doodles (✧, thin arrows 2.5 px @1080), headline, olive tape #B9BA73 strips]

// R7 — dithered drop shadow for paper props
shadow = { color: '#000', opacityAtEdge: 0.75, offset: [0..15, 9..22] /*px @1080*/, blur: 150..240 /*px @1080, falloff*/,
           grain: 'monochrome noise, std ≈ 18/255, 1-px', blend: 'multiply' }   // cut-out photos get NO shadow

// R8 — dry-brush label wipe
bar = { tex: 'black dry-brush stroke, ragged ends', h: 80 /*px @1080*/, padX: 40..60, color: '#2E2E2E' };
text = { font: 'Inter 600', caps: true, size: 34 /*cap px @1080*/, tracking: '+0.10em', color: '#FFFFFF' };
reveal = 'hard-edged rectangular mask L→R', steps: [0.25, 0.70, 1.0] on 3 consecutive 12-fps ticks; 2nd label +0.43 s.

// R9 — hand-drawn arrow draw-on (+ loop)
arrow = { stroke: 2.5 /*px @1080*/, color: '#111', head: 'open V 18 px', length: 140..280 px };
drawOn: 3-4 ticks easeOut (stroke end 0, .28, .66, .85, .97, 1.0 of length); loop: visible ~0.5 s, off 1-2 ticks, redraw (period ≈ 0.83 s).

// R10 — continuous swing for "hanging"/alive objects (sampled on 12 fps ticks only)
x = x0 + 42*sin(2π t/1.8), y = y0 + 75*sin(2π t/1.8 + π/2) /*px @1080*/, rot = 1.5*sin(2π t/1.8) deg
```

## 11. Uncertainties
- Exact font cannot be confirmed from 720p; Inter Bold is the closest free match (SF Pro Display Bold / Helvetica Now
  Display Bold equally plausible). Tracking estimated by eye (≈ −2…−3 %).
- Start positions of slide-ins are invisible (the move starts "under the cut"); fitted start values are extrapolations —
  durations/easing classes are reliable (rms 1-10 px), absolute from-offsets are not.
- Whether the 15-fr boil swaps *different* crease textures or re-offsets one texture: diffs show creases moving and
  smudges changing shape → most likely 2+ scans offset randomly; could not separate.
- The mirror-flip of the bank-head man might be an intentional "head turn" substitute; it is a horizontal flip of the
  whole man cut-out with a (+33,−16) px offset.
- Easing of the stepped headline poses is irrelevant (hold keyframes), but the *exact* pose offsets differ per scene;
  given values are measured examples, not a fixed rule.
- Shadow offset/blur values are estimated from luminance profiles (shadow overlaps paper texture, JPEG noise).
- The end card shows slow sub-pixel drift/very small changes between holds (pairwise diff 1-8) that I could not
  attribute (maybe a faint texture boil at 15-25 fr on the scan block).
- f2068-2090 (Fiverr thumbnail) and the "fiverr" watermark are not part of the animation style.
