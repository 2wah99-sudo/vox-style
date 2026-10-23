# v2_porsche — agent C — frames f3973–f5898 (132.43–196.60 s, end of video)

Status: COMPLETE pass over seq_074 … seq_109 (every sheet), overview_06–09 read.
Source 640x360 @ 30 fps. Conversion used everywhere: **px@1080 = px@360 × 3**, % of frame height = px@360 / 3.6.
Cadence words: "on 2s/3s" = new pose every 2 or 3 frames alternating (2,3,2,3 = 12 fps in a 30 fps timeline).

---

## 1. Overview

The last 64 s of "the history of Porsche" cover the modern era: a 1998–2005 sales bar chart (with a hand-drawn red circle), a 3D photo-print carousel over a dark "handwriting" background, the SUV pivot (a glowing yellow "SUV" label, Cayenne photos with neon-yellow borders and a "2002" year), four identical **model cards** (Cayenne / Panamera / Macan / Taycan: a side-view car cut-out on warm paper with a lemon highlighter title and "The price at launch is $…"), each followed by full-colour press footage with italic lower-third captions, a green-Taycan photo where "2023" and "$43 000 000 000" live in world space between the background and the cut-out cars, a CRT-TV "slot-machine word reel" that lands on **Legacy** under a dry-brush yellow highlighter, a camera that drifts across a desk of taped Polaroid-style prints (356 → 911 → Boxster → Cayenne → Macan), and an end quote card ("We build cars that people desire, not just those they need." — Ferdinand Anton Ernst Porsche) with a B&W cut-out of the man and a yellow offset silhouette, then a linear 1.6 s fade to black.

Visual identity in this section: warm off-white paper (#FAF0E7 centre, vignetted to ~#C0BCB3 corners), charcoal/brown-grey transitional serif type, **one accent only: lemon/acid yellow (#F2F709)** used for highlighter bars, tape, caption icons, glows and offset rims; real photos and video kept in full colour here (unlike the B&W archival first half), with a 1-frame-step "weave" on holds. Editing is fast and on the beat (hard cuts every 1.0 s in montages), and most graphic animation is stepped at 12 fps while camera moves on footage are on ones.

---

## 2. Colour

All values sampled with median of small patches (not by eye). Screen share is approximate for my range.

| Role | Hex | Notes / share |
|---|---|---|
| Paper card bg, centre | **#FAF0E7** (250,240,231) | model cards, chart, slideshow, end card. ~35% of my range's screen time |
| Paper card bg, mid | #E8DED5 / #ECE3DA | radial falloff |
| Paper card corners (vignette) | #CECAC1 (TL) … #BFBBB3 (BR) | ≈ -20 % luma at corners, slightly cooler/greyer than centre |
| End-card paper | #F4EBE2 centre, #CECAC1 corners | with grid lines (see §5) |
| Desk (mood-board) paper | #E4DBD3 | pinkish cream, dotted specks |
| Chart gridlines | #EBE070 core (blurred yellow) | horizontal only; baseline more saturated ≈ #AAC01F |
| Chart bars | **#333230** | charcoal, rounded top corners |
| Hand-drawn circle | #7E1029 median, core #61000A | crimson marker |
| Highlighter / label yellow | **#F2F709** (cards), #E9F70B (price), #EFF70E (SUV box) | lemon yellow with a slight green bias; never orange |
| Tape strips on desk | #F3F80B | same yellow |
| Caption ▶ triangle | #D7DE16 | |
| Footage caption text (on dark footage) | #E2EE48 | yellow italic |
| Footage caption text (on light footage) | #3B2A1C | dark brown italic (Panamera) |
| Neon year "2002" core | #E7FF21 | + yellow outer glow |
| Neon photo border (dark scene) | #9CA050 at 2 px | thin yellow-green glowing stroke |
| Title ink (on yellow) | charcoal ≈ #2A2A2A (JPEG reads #322C00) | |
| Subtitle ink | **#554949** | warm grey |
| Quote ink (end card) | #564A4B (darkest) | warm grey-brown |
| "2023" (world-space year) | #514948 | |
| Price figure on yellow | dark brown ≈ #3A3008 | |
| Crop / registration marks | ≈ #87787F at 2 px (~40 % opacity dark grey) | end card |
| Dark scenes bg (carousel, SUV, triptych) | #020202–#0A0A0A | with faint texture at luma 10–25 |
| CRT bezel | #1A1712; outer casing #939B82; screen #D4CBBD centre → #BFB7A9 edges | |
| Fade-to-black end | #000000 | |

Colour rules observed:
- Yellow is the **only** accent. It marks: (a) the thing to read (highlighter bars behind titles/prices/keywords), (b) attachment (tape), (c) narrative pointers (▶ icon, glows), (d) offset "shadow" rims on photos and cut-outs. Red appears only once (chart circle).
- In this section photos/video are **full colour** (Cayenne, Panamera, Taycan footage, desk prints). The only B&W image is the end-card portrait of Porsche (archival).
- Text is never pure black: charcoal on yellow, warm grey (#554949) on paper.
- Footage gets a mild film grade: lifted blacks are NOT used (p1 luma 0–3), but highlights are rolled (p99 ≈ 210–240), saturation moderate (mean S 0.18–0.26) and a dark vignette is added on some shots (Taycan green still: corners #333 … #696, centre #D3D0CA).

---

## 3. Typography

All sizes measured from ink bounding boxes at 360p.

### 3.1 Model-card title (template, 4 uses)
- Text: "Porsche Cayenne" / "Porsche Panamera" / "Porsche Macan" / "Porsche Taycan".
- Typeface: high-contrast transitional serif, Regular weight, Title Case (looks like a Caslon/Baskerville-style news serif). Closest free: **Libre Caslon Text Regular** or **Libre Baskerville Regular** (alt: Source Serif 4 Display).
- Cap height ("P"): 23 px@360 (rows 72–94) = **6.4 % H → 69 px@1080** ⇒ font-size ≈ 95–100 px@1080.
- Colour: charcoal (#2A2A2A-ish) on yellow #F2F709.
- Highlighter box: height **46 px@360 (12.8 % H → 138 px@1080)**, top y=60 (16.7 % H from top), left x=191–192, width 254 px (Cayenne/Macan/Taycan) / 285 px (Panamera). Padding: ~12 px@360 left (36 px@1080), ~9–11 px right, ~11 px above cap height, ~7 px below baseline (descender-free). Hard rectangular edges, no rotation, no texture, no shadow.
- Box is horizontally centred on the frame (centre x≈318–320).
- Animation: see §6.4 (box grows L→R from an 8 px cursor; glyphs revealed by a hard mask at the box's right edge).

### 3.2 Model-card subtitle
- "The price at launch is $56,300 / $89,800 / $79,000 / $103,800".
- Same serif, Regular, sentence case; cap ≈ 11 px@360 (3.1 % H → 33 px@1080; font-size ≈ 46 px@1080). Ink rows 123–138; the price figure is a touch darker/heavier.
- Colour #554949. Centred, width 200 px@360 (x 220–420). Baseline ≈ 34 px@360 below the title baseline (102 px@1080).
- Animation: soft-edged L→R wipe starting 5 frames after the title box starts and finishing ≈10 frames before it.

### 3.3 Chart typography (only the tail of the chart is in my range)
- Title "Porsche Global Sales Numbers" in serif semibold, small source line under it ("stuttcars.com"), year labels 1998–2005 in grey serif under bars, value labels tiny dark-red serif above bars.

### 3.4 "SUV" label on dark
- Serif caps "SUV", cap height 29 px@360 (8 % H → 87 px@1080), dark olive ink on a glowing yellow box 122×51 px@360 (366×153 px@1080), centred.

### 3.5 Neon year "2002"
- Bold/semibold serif numerals, height 13 px@360 (≈39 px@1080), core #E7FF21, outer glow radius ≈ 10 px@360 (30 px@1080), centred above the middle panel of the triptych.

### 3.6 World-space year "2023" and price "$43 000 000 000"
- "2023": serif Regular/Medium lining figures, figure height 32 px@360 (8.9 % H → 96 px@1080), colour #514948, no box. Centred (x 272–399).
- "$43 000 000 000": **bold** serif (closest: Libre Baskerville Bold), figure height 30 px@360 (8.3 % H → 90 px@1080), dark brown on yellow box 343×55 px@360 (1029×165 px@1080), thin-space-style digit grouping with spaces. Text visible BEFORE the highlighter arrives.

### 3.7 Footage lower-third captions
- Italic serif sentence, sentence case, ending with a period sometimes: "Porsche first introduced the Panamera back in 2009", "The production version of the Macan was unveiled at the 2013", "Accelerates from 0 to 100 km/h in as little as 2.8 seconds.", "Range of up to 590 km on a single charge."
- Closest free: **Libre Baskerville Italic** / Georgia Italic, semibold feel. x-height ≈ 8 px@360, ink rows 312–328 (16 px incl. ascenders/descenders → cap ≈ 11 px@360 = 33 px@1080).
- Position: left-aligned, text starts x≈103 (16 % W), baseline ≈ y 325 (90 % H). A yellow ▶ triangle 18×21 px@360 (54×63 px@1080) sits at x 70–88, i.e. 15 px@360 left of the text.
- Colour: yellow #E2EE48 on dark footage; dark brown #3B2A1C on bright footage (Panamera, where the triangle is yellow and text dark).

### 3.8 CRT word reel
- Words (one per line, centred): Performance / Excellence / Precision / Engineering / Mastery / Velocity / Legacy / Prestige.
- Serif semibold (Libre Baskerville Bold-ish), cap ≈ 13 px@360 initially (≈ 39 px@1080), line pitch ≈ 37 px@360 (111 px@1080).
- Inside the focus window: dark ink #595400-ish on the highlight (pure dark grey on paper). Outside: ghost at ≈10–15 % opacity (luma 205 vs paper 212).
- Focus window: thin dark outline rectangle, stroke ≈ 1.5 px@360 (≈4–5 px@1080), final 212×42 px@360 before push-in.

### 3.9 End quote card
- Quote: italic serif (Libre Baskerville Italic / Georgia Italic), sentence case with straight double quotes, 3 lines left-aligned: "We build cars that people / desire, not just those they / need."
- Cap height ≈ 12 px@360 (3.3 % H → 36 px@1080; font-size ≈ 52 px@1080), x-height 9 px@360, leading 23 px@360 (69 px@1080 ≈ 1.33× size). Left edge x=121 (19 % W), top y=111 (31 % H). Colour #564A4B.
- Attribution "-Ferdinand Anton Ernst Porsche": bold upright serif, cap ≈ 6 px@360 (18 px@1080), right-aligned to x≈351 (right edge of quote block), 15 px@360 below the last quote line.
- Typed on character-by-character (see §6.10).

### 3.10 Desk labels
- Stamp-edged cards with "356", "944", "911", "Boxster", "Cayenne", "Macan": serif (numerals Regular, dark brown), cap ≈ 18 px@360 for numerals (54 px@1080), ≈ 9 px@360 for words.

---

## 4. Layout & composition

- **Model card grid** (identical for all 4 cards): title box top at 16.7 % H, subtitle baseline at ~38 % H, car cut-out occupying 55–90 % H (y 200–330 @360), car width 337–378 px@360 (53–59 % W), horizontally centred (car centre x≈318). Everything centred on the vertical axis; generous negative space left/right (~22 % W each side). Layers: paper bg (vignette baked) → car cut-out (with soft contact shadow) → highlighter box → title text → subtitle.
- **Chart**: plot area x 157–510 (25–80 % W), baseline y=262 (73 % H), 8 bars at 42–43 px pitch, bar width ≈ 22 px@360.
- **Slideshow photos** on paper: centred, width 486 px@360 (76 % W) at rest, top/bottom margins ≈ 18 px (5 % H). Video frame: 581 px wide (91 % W), 300 px tall.
- **Lower-third captions**: left margin 11 % W (icon) / 16 % W (text), baseline 90 % H — title-safe but low.
- **Dark-scene photo frames**: single photo 241×301 px@360 portrait centred; triptych = 3 × 197 px panels with 6 px gaps, spanning x 18–621 (94 % W); middle panel offset 42 px down to make room for "2002".
- **World-space text sandwich** (green Taycan): background plate → text ("2023", "$43 000 000 000") → car cut-out layer (cars occlude the text) → highlighter is behind the price text.
- **CRT**: TV screen fills ~92 % W × 90 % H, rounded-rect bezel with 18 px@360 dark band; all content centred.
- **End card**: quote block in the left-centre (x 19–55 % W, y 31–54 % H); cut-out portrait anchored bottom-right (x 60–84 % W, bleeds off bottom edge); crop marks frame the composition: top-right L (horizontal at y≈33 from x 467→610, vertical at x≈578 from y 30→195) and bottom-left L (vertical x≈62, y 215→360; horizontal y≈340, x 30→172). Lines ≈ 2 px@360.
- **Desk**: top-down view, 5–7 objects visible at once, each prints ~140–200 px@360 wide (22–31 % W), rotated −12°…+10°, labels next to their photo group; camera wanders.

---

## 5. Textures & materials

- **Paper**: warm off-white with baked radial vignette (centre #FAF0E7 → corners #C0BCB3, ≈ -20 % luma; vignette radius starts ~55 % of half-diagonal). Very faint grid paper on chart/model cards (lines ~6–8 luma below paper); clear grid on end card: pitch **11.5 px@360 (34.5 px@1080, 3.2 % H)**, line ≈ 1 px@360, 5–8 luma darker, warm-grey. High-pass grain std only 0.5–0.9 luma at 360p (i.e. almost no visible grain at this resolution; at 1080p use a very subtle paper fibre texture, ≤2 % contrast).
- **Highlighter, flat type** (model cards, price, SUV): perfectly hard-edged rectangle, flat colour, no texture.
- **Highlighter, dry-brush type** (CRT "Legacy"): ragged brush stroke with streaky edges and tapered/blobby left end; height ≈ 100 px@360 at final zoom (≈ 72 px@360 before push-in = 1.7× the word cap height ×… i.e. ~1.7 × window height), extends ~40 px@360 beyond the window on both sides, slightly tilted (+2–3°, higher on the right).
- **Yellow offset rim / shadow on photos** (slideshow f4356–4473): a solid yellow copy of the photo rectangle offset **(+3, +4) px@360 → (+9, +12) px@1080** down-right, softened ≈1 px@360 blur; visible as a 3–5 px yellow line on the right and bottom edges only. Photos have ~4 px@360 rounded corners, no white border.
- **Neon photo border** (dark scenes f4199–4255): 2 px@360 yellow-green stroke (#9CA050 peak) with ~3 px soft glow, rounded corners ~3 px.
- **Glow** (SUV box, 2002): outer glow falloff measured from box edge (G channel): 165 @1 px, 83 @7, 57 @13, 41 @19, 24 @25, 14 @31, ~3 @49 px@360 ⇒ Gaussian-ish, σ ≈ 12–15 px@360 (≈ 40 px@1080), opacity ≈ 35 % at 7 px.
- **Cut-out portrait** (end card): B&W photo cut-out, hard matte edge, plus a solid yellow silhouette duplicate offset right that settles to a 3–5 px@360 yellow-green rim (blurred ~2 px) on the right side of head/shoulder/chair.
- **Car cut-outs on model cards**: clean colour press images, hard mattes, **no visible drop or contact shadow** (paper under the wheels stays at luma 222–231; under the body only −4 luma).
- **Prints in carousel**: cream border **#FAF0E6**, top ≈10 px@360, sides ≈8–12 px, bottom ≈24 px (Polaroid-like, ~2.4× thicker bottom), 3D-rotated, foreground prints defocused (DOF blur ≈ 4–6 px@360).
- **Desk prints**: white/cream border ≈ 6 px@360 (18 px@1080), drop shadow down-right ≈ 2–3 px@360 offset, ~3 px blur, 30–40 % opacity, edge slightly brownish; yellow tape strip 20×8 px@360 (60×24 px@1080) centred on top edge, slightly rotated; stamp-perforated label cards (scalloped left/right edges).
- **Dark backgrounds**: near-black #020202 with very faint content at luma 10–25: (a) cursive handwriting lines (carousel), (b) blueprint/photo views of a Cayenne (SUV scene). These read as "texture", ~5–8 % visibility.
- **Film weave / boil**: on every paper/static shot the whole frame (or each layer) receives a random sub-pixel offset **every 5 frames (6 Hz)**: measured ±0.05–0.9 px@360 (≈ ±0.2–2.7 px@1080), text layer shifting slightly more than background (independent jitter per layer of ~1.5×). No luminance flicker (±0.2 luma).
- **No measurable chromatic aberration** globally (R/G/B phase correlation = 0.00 px); colour fringes seen on desk prints are from the source photos/JPEG.
- **Fade to black**: linear, see §7.

---

## 6. Motion

### 6.1 Cadence
- Graphic elements (bars, highlighter boxes, type-on, desk pan, reel, portrait slide, crop marks) update on **2s/3s alternating (12 fps)**: e.g. title box changes at f4266, 4269, 4271, 4274, 4276, 4279, 4281, 4284, 4286 …; desk pan steps at 5560, 5562, 5565, 5567, 5570, 5572, 5575 ….
- Holds use a **6 fps sub-pixel weave** (changes every 5 frames).
- Slow push-ins on graphic scenes are stepped every 5 frames (6 fps) (CRT f5473–5536).
- Live footage and digital zooms on footage are on ones (30 fps).
- metrics.csv gaps between changing frames (diff ≥ 1.5) in my range: {1: 429, 2: 215, 3: 89, 4: 21, 5: 12}. Per scene: desk pan {2: 29, 3: 28} (pure 12 fps); end card {2: 7, 3: 7}; carousel {1: 15, 2: 31, 3: 4}; Macan footage {1: 51, 2: 10} (ones); green-Taycan still {1: 22, 2: 19, 3: 9, 4: 5, 5: 3}. State mix f3973–5898: hold 861, local 644, global 349, "cut" 72 (≈30 real cuts; the rest are 12-fps desk-pan steps big enough to trip the cut detector).

### 6.2 Bar chart (tail; begins f3927 in agent B's range)
- Bars grow from baseline, staggered **5 frames (0.167 s)** L→R: bar starts f3939, 3946, 3949, 3954, 3959, 3964, 3969, 3974. Each grows in ≈15–18 frames (0.5–0.6 s), easeOutCubic-like, heights stepped on 2s.
- Hand-drawn circle f4003–4014 (11 frames, 0.37 s): stroke starts at ~6 o'clock and draws clockwise (6→9→12→3) and overshoots its start slightly (open loop), on 2s. Hold 0.5 s.
- Exit f4028–4035: whole chart slides left with ease-in (dx -1, -8, -32 px@360 cumulative) → hard cut at f4036.

### 6.3 Photo carousel (f4036–f4148)
- f4036–4043: first print rotates from ≈15° Y-rotation to flat (≈8 frames) while drifting.
- f4038–4089: camera trucks right; content travels **≈1270 px@360 (≈2 frame widths) left + 50 px up in 51 frames (1.7 s)**, easeInOutSine/Cubic: per-step px -19,-4,-1,-28,-63,-86,-99,-136,-136,-128,-94,-84,-75,-66,-56,-47,-50,-39,-29,-20,-10,-2 (peak ≈ 136 px per 12-fps step ≈ 1630 px/s@360 ≈ 4.2 frame widths/s). Prints sit at different depths (parallax and DOF).
- f4099–4124: pull back: Porsche-HQ print 427→222 px wide (0.52×) while the layout resolves into a 2-over-3 mosaic; hold to f4148.

### 6.4 Highlighter box reveal (model-card template)
- Starts **7–10 frames after the cut** as an 8 px@360 vertical yellow "cursor".
- Width keyframes (px@360) — identical across cards:
  - Cayenne f4266→4296: 8, 16, 27, 42, 65, 133, 200, 220, 232, 243, 249, 254.
  - Macan f4699→4726: 8, 17, 28, 43, 64, 133, 200, 220, 233, 242, 250, 255.
  - Taycan f5009→5036: 8, 16, 17, 28, 43, 65, 134, 201, 221, 232, 242, 243, 250, 254.
  - Panamera f4571→4599 (wider): 10, 19, 31, 48, 76, 181, 231, 251, 264, 274, 281, 284.
- ≈ 28–30 frames (0.95 s) total, on 2s/3s. Shape: slow first 10 frames (cursor + 1st letters, ~25 % of width), big jump in the middle (65→133→200), long ease-out tail ⇒ approx **easeInOutCubic** sampled at 12 fps.
- Title glyphs are revealed by a hard mask locked to the box's right edge (letters cut mid-glyph).
- Subtitle: soft-edge (≈15 px feather) L→R wipe beginning 5 frames after the box, done ≈10 frames before the box finishes.

### 6.5 Model-card car cut-out
- At the cut the car is already ~90 % in place and settles **leftward** 25–41 px@360 (4–6 % W) in 7–8 frames, easeOutCubic, on 2s: Cayenne x 190→161→152→150; Panamera 171→152→147; Macan 182→153→144→141.
- Taycan variant: scale-in 0.79→1.0 (width 298→351→372→378) over 7 frames.
- Exit: in the last 3–5 frames the car shrinks to ≈0.88–0.95× (Macan 355→341→313 px, f4739–4743) with ease-in, then hard cut. Macan exit adds a **1-frame white flash** (f4743, luma 204→225, paper goes to #F6F3EE).

### 6.6 SUV label + Cayenne photo pop (f4164–4255)
- "SUV" yellow box: left-anchored at x=255@360, height constant 51 px, width 5→16→29→79→101→111→118→122 px (f4164–4181, 17 frames = 0.57 s, ease-out, on 2s), letters revealed with it. Hold to f4193.
- Morph: box stretches horizontally 122→150 px (f4194–4198) and becomes the photo frame.
- Photo pop f4199–4211: height 212→282→301→284→262 px (0.81 → 1.08 → 1.15 → 1.08 → 1.00): **overshoot ≈15 % then settle, 12 frames (0.4 s)** — easeOutBack(s≈2.5) sampled on 2s/3s.
- Triptych split f4213–4221: two copies slide out L and R from behind the centre panel (332 → 516 → 587 px total span), 8 frames, ease-out; panels 197 px wide, 6 px gaps.
- f4229–4236: middle panel drops 42 px (ease-out, 7 frames) and "2002" (neon yellow) fades/scales in above it.

### 6.7 Paper slideshow (f4356–4473), one photo per 30 frames (1.0 s), hard cuts on the beat
Each photo "breathes": eases to rest scale in the first 8 frames, holds ~14, eases away in the last 6–7 frames; direction alternates so motion continues through the cut:
- P1 Cayenne (f4356–4385): width 445→471→482→486 (0.916→1.0, easeOut 8 f), hold, 486→482→471→449 (easeIn 6 f).
- P2 desert (f4386–4415): 409 (1.16×) → 352 (f4394) shrinking easeOut; hold; grows 365→388→426 (1.21×) easeIn.
- P3 canyon road (f4416–4445): 308 (0.87×) → 355 (f4424); hold; shrinks 347→338.
- P4 factory (f4446–4473): 627 (1.12×) → 558 (f4454); hold; grows to 581 before cut.
- P5 = framed video (f4474–4563): 0.845× → 1.0 on ONES: 491, 515, 536, 552, 562, 570, 573, 577, 580, 581 (easeOutCubic, 9 frames); footage inside cuts twice (f4507, f4531) while the frame stays; exit: slide left ease-in (centre x 321→318.5→316→311.5→305→295, f4556–4561) + hard cut.

### 6.8 Footage moves and captions
- Panamera highway (f4625–4660): digital zoom-out 1.0→0.51× in 35 frames, constant rate (linear fit rms 0.08, ≈ -1.9 %/frame), on ones.
- Other footage (Macan bridge, factory, Taycan) uses native camera motion; no added moves detected.
- Caption fade-in (measured by caption yellowness): Macan f4768→4776 (8 f), Taycan#1 f5105→5114 (9 f), Taycan#2 f5175→5184 (9 f) — ≈linear opacity 0→1 over **8–9 frames (0.3 s)**, starting 2–7 frames after the shot's cut. Fade-out f5162→5168 (6 f) ending at the cut. A caption carries across a cut when the next shot continues the same sentence (f5202).
- Panamera caption: ▶ triangle rises from below the frame edge and **spins CCW 270°** (pointing up → left → down → right) over ≈10 frames (f4640–4650), lands pointing right; text then fades in 6 frames (f4650–4656), no slide.

### 6.9 Green Taycan "2023 → $43 000 000 000" (f5221–5398), 2.5D camera on a still
- Push-in 1.0→1.16× over f5221–5228 (8 frames, ease-out), hold.
- Tilt-up / pull-back f5244–5266: cars move down y154→228 and shrink to 0.84×; "2023" emerges from behind the car roofs (it's on a layer behind the cars). Steps every 2–3 frames.
- Hold 1.4 s (f5266–5304) with 6 Hz weave.
- Tilt-down + push-in f5306–5334: cars y 230→92, scale ×1.45; "2023" scrolls out the top, "$43 000 000 000" scrolls in from the bottom. Ease-in-out envelope.
- Price highlighter f5326–5346: 1-frame thin cursor bar at left (f5326), then widths 23, 57, 123, 218, 284, 319, 336, 343 px@360 at f5329, 31, 34, 36, 39, 41, 44, 46 (≈20 frames, **easeOutCubic**: 70 % width in 10 frames).
- Exit f5393–5398: push-in accelerates (green bbox 421→481 px, ≈ +14 % in 5 frames, ease-in) → hard cut (zoom-through).

### 6.10 CRT word reel "Legacy" (f5399–5544)
- f5399–5415: hold 17 frames (0.57 s) — a 1 px vertical cursor in the centre over ghosted words.
- Focus window grows from the cursor: width ≈ 8, 16, 27, 42, 63, 93, 125, 154, 175, 189, 198, 205, 212 px@360 (f5416→~5446, 30 frames, easeInOutCubic on 2s/3s — same curve family as the title boxes); height ≈ 42 px@360.
- Reel scrolls DOWN through the window (new words enter from the top): accelerates from f5411 (steps 3, 5, 7, 10, 15, 22 px per 12-fps step), then decelerates and lands on "Legacy" at ≈ f5446 — slot-machine ease-in-out, ≈ 6 word pitches (≈ 220 px@360) in ≈ 35 frames.
- Dry-brush highlighter paints L→R behind the window starting while the reel still moves: bbox width 49 (f5428), 54, 66, 92, 142, 199, 232, 251, 260, 263, 264 (f5455) px@360 — **≈ 27 frames, easeInOut**, height grows 53→72 px as the bristle body fills in.
- Punch-in f5456→5468: scale 1.0 → 1.21 (f5458) → 1.29 (f5461) → 1.33 → 1.35 (fast ease-out, 12 frames).
- Creep f5468–5536: 1.35 → 1.46 (≈ +0.16 %/frame, stepped every 5 frames = 6 fps).
- Exit f5537–5544: accelerating zoom 1.46 → 1.49 → 1.54 → 1.64 (ease-in, 8 frames, on ones) → hard cut to desk.

### 6.11 Desk pan (f5545–5720), 12 fps steps
- f5545–5557: continues the zoom-through: zooms IN ≈ +7.5 % per step (×1.07–1.08 at f5547, 5550, 5552, 5555) — momentum carried across the cut.
- f5557–5625: pan, content moves (+29, +10) px@360 per step at peak (camera travels up-left), ramping 8→21→24→26→28→30 and back to 20 → then 31→44.
- f5627–5662: content moves (+8, +20) per step (camera up); smooth curved turn f5627–5635.
- f5665–5704: content moves (+24, −17) per step (camera down-left).
- Speeds ≈ 30–44 px@360 per step ≈ 12–17 px/frame ≈ 360–520 px/s@360 (≈ 1.1–1.6 k px/s@1080).
- f5704–5719: pull-back ≈ ×0.955 per step (6 steps ⇒ ≈0.76×), easeInOutSine, then hard cut to the end card.
- Total ≈ 5.8 s for 5 model groups ⇒ each label/photo group is on screen ~1.2 s.

### 6.12 End card (f5721–5898)
- Cut in on an empty grid-paper card; 3 frames later elements start.
- Crop/registration marks draw on (lines grow from their corner) f5724→5742 (≈18 frames, on 2s/3s).
- Portrait cut-out slides in from the right: left-edge x = 638, 628, 615, 598, 573, 540, 503, 469, 443, 424, 410, 400, 393, 387, 384, 383, 382 (f5724→5764): **40 frames (1.33 s), easeOutCubic/Quart**, peak 37 px per step.
- Yellow silhouette duplicate lags behind: offset of its right edge vs the portrait's: +39 (f5747), +27, +19, +13, +9, +7, ≈+3 (f5762) px@360 — i.e. a follow-through layer that settles ~15 frames after the portrait and remains as a 3–5 px rim.
- Quote typing: starts f5727 (6 f after cut), ends f5777 (≈57 characters in 50 frames ≈ 34 char/s ≈ 1.1 char/frame, updated on 2s/3s, newest character fades in over ~2 frames). Attribution typed f5777→5797 (≈30 chars in 20 frames, ≈45 char/s).
- Hold f5797–5827 (1.0 s) with 6 Hz weave (offsets up to 0.9 px@360).
- **Fade to black f5827→5876: 49 frames (1.63 s), linear** (luma drops 4.35 per frame, 205→0), then pure black f5876–5898 (23 frames, 0.77 s) to the end of file.

---

## 7. Transitions (frame-exact, my range)

| # | Frames | Type | Detail |
|---|---|---|---|
| 1 | f4028–4036 | ease-in slide-left + hard cut | chart slides 32 px@360 left in 3 frames (easeInCubic) then cut to carousel |
| 2 | f4149 | hard cut | mosaic → dark SUV bg |
| 3 | f4194–4199 | shape morph | SUV highlighter box stretches into the photo frame which then pops with overshoot |
| 4 | f4213–4221 | split / duplicate | single photo → triptych (copies slide out from behind) |
| 5 | f4256 | hard cut | dark → paper model card (big luma jump 55→201) |
| 6 | f4356, 4386, 4416, 4446, 4474 | hard cuts on the beat (every 30 f) with **zoom-through** (outgoing photo accelerates in scale, incoming decelerates) | slideshow |
| 7 | f4556–4564 | slide-left ease-in + cut | video frame exits left 26 px in 5 frames |
| 8 | f4625, 4689, 4744, 4999, 5061 | hard cut card ⇄ footage | card car shrinks 0.88–0.95× in last 3–5 frames before cut (pull-away) |
| 9 | f4743 | 1-frame white flash before cut | luma 204→225 then footage |
| 10 | f4816, 4858, 4914, 4959, 5105, 5168, 5202, 5221 | plain hard cuts between footage | 1.3–2.1 s shots |
| 11 | f5393–5399 | zoom-through cut | accelerating push-in then cut to CRT |
| 12 | f5537–5557 | zoom-through cut with carried momentum | CRT accelerating zoom (ease-in) → cut → desk continues zooming in, decelerating into a pan |
| 13 | f5704–5721 | pull-back + hard cut | desk zooms out 0.76× then cut to static end card |
| 14 | f5827–5876 | linear fade to black (1.63 s) + 0.77 s black | outro |

Frequency in my range: hard cuts dominate (≈30 real cuts; metrics flags 72 because the 12-fps desk pan steps register as "cut"); zoom-through cuts 5–7×; morph/split 2×; slide-off + cut 2×; flash 1×; fade-to-black 1× (only at the very end). No dissolves, no wipes, no paper-tear transitions in this section.

---

## 8. Recurring devices

1. **Flat highlighter box** (lemon #F2F709, hard edges): grows L→R from an 8 px cursor with easeInOutCubic (title cards, ~29 f) or easeOutCubic (price, ~20 f, SUV, 17 f). As a reveal mask (cards, SUV) or behind already-visible text (price).
2. **Dry-brush highlighter** (CRT "Legacy"): ragged stroke painted L→R in ~27 f behind a keyword.
3. **Typewriter cursor → box**: every highlight/box begins as a thin vertical bar (1–8 px) that stays 1–17 frames before growing (cards, price, CRT window, SUV).
4. **Hand-drawn circle** (red marker) on charts, drawn clockwise in ~11 f.
5. **Model card template** (car cut-out + title + price): used 4× identically, always followed by footage.
6. **Lower-third caption**: yellow ▶ + italic serif sentence; fades in 8–9 f; ▶ can spin in.
7. **Yellow offset rim/shadow**: photos (+3,+4 px@360 down-right), portrait cut-out (yellow silhouette lagging then settling to a rim), neon borders on dark scenes.
8. **Glow** (dark scenes): SUV box, 2002 year, photo borders — Gaussian σ≈13 px@360.
9. **World-space text between photo layers** (2.5D: plate → text → cut-out cars), revealed by camera tilt.
10. **Slot-machine word reel** with focus window and ghosted neighbours.
11. **Desk mood-board** with Polaroid prints, yellow tape, stamp-edge labels, pencils, highlighter pens, newspaper clippings ("Years Ahead in Engineering"), paper clips.
12. **Quote card** with grid paper, crop/registration marks, typed quote + bold attribution, cut-out portrait.
13. **3D print carousel** with DOF on dark textured background.

---

## 9. Scene log

| frames | time (s) | on screen | devices | motion / transition notes |
|---|---|---|---|---|
| (f3927)–f4035 | 130.90–134.50 | Bar chart "Porsche Global Sales Numbers" 1998–2005 on paper | yellow blurred gridlines, charcoal bars, red value labels, red hand-drawn circle around 1998–2001 | bars staggered 5 f; circle f4003–4014; ease-in slide-left + cut |
| f4036–f4148 | 134.53–138.27 | Cream-bordered photo prints (factory aerials, workers, Porsche HQ with handwriting overlay) on near-black handwriting bg | 3D prints, DOF | print un-rotates; truck right 1270 px in 1.7 s; pull-back to 2-over-3 mosaic |
| f4149–f4198 | 138.30–139.97 | Near-black bg with ghosted Cayenne blueprint views; glowing "SUV" label | flat highlighter + glow | box wipe 17 f; stretch-morph |
| f4199–f4255 | 139.97–141.85 | Cayenne factory photo with neon yellow border → triptych → "2002" | neon border, glow year | pop overshoot 15 %, split, middle drops |
| f4256–f4355 | 141.87–145.17 | Paper card: Cayenne + "Porsche Cayenne / The price at launch is $56,300" | title highlighter | car settle 8 f; title box 30 f; 6 Hz weave hold; cut |
| f4356–f4473 | 145.20–149.13 | Paper bg + centred colour photos (Cayenne in quarry, desert hill-climb, canyon road, factory), 1 per second | yellow offset rim (down-right) | breathing scale, zoom-through cuts on the beat |
| f4474–f4563 | 149.17–152.10 | Framed colour video (Cayenne production line) 91 % W on paper | yellow rim | scale-in on ones 9 f; inner cuts f4507, f4531; slide-left exit |
| f4564–f4624 | 152.13–154.13 | Paper card: blue Panamera, "$89,800" | title highlighter (wider) | same template |
| f4625–f4688 | 154.17–156.27 | Footage: two Panameras on highway | ▶ spins in, dark italic caption "Porsche first introduced the Panamera back in 2009" | digital zoom-out 0.51× linear |
| f4689–f4743 | 156.30–158.10 | Paper card: white Macan, "$79,000" | title highlighter | 1-frame white flash at end |
| f4744–f4815 | 158.13–160.50 | Footage: red Macan on cable-stayed bridge | yellow italic caption "The production version of the Macan was unveiled at the 2013" | caption fade 8 f |
| f4816–f4857 | 160.53–161.90 | Footage: Macan body-in-white on assembly line | — | cut |
| f4858–f4913 | 161.93–163.77 | Footage: worker in orange Porsche shirt | — | handheld |
| f4914–f4958 | 163.80–165.27 | Footage: Taycan wheel/brake assembly with yellow tooling | — | handheld push |
| f4959–f4998 | 165.30–166.60 | Footage: worker with wheel tool | — | cut |
| f4999–f5060 | 166.63–168.67 | Paper card: silver Taycan, "$103,800" | title highlighter | car scales 0.79→1.0 in 7 f |
| f5061–f5104 | 168.70–170.13 | Footage: silver Taycan parked (dark, desaturated) | — | cut |
| f5105–f5167 | 170.17–172.23 | Footage: Taycan tracking shot | caption "Accelerates from 0 to 100 km/h in as little as 2.8 seconds." | fade in 9 f, out 6 f |
| f5168–f5201 | 172.27–173.37 | Footage: Taycan front close-up | caption "Range of up to 590 km on a single charge." | fade in 9 f |
| f5202–f5220 | 173.40–174.00 | Footage: white Taycan by highway wall | same caption carried across cut | — |
| f5221–f5398 | 174.03–179.93 | Still: two green Taycans on concrete, dark vignette; "2023" then "$43 000 000 000" | world-space text sandwich, price highlighter | push-in, tilt-up reveal, hold, tilt-down/push, highlight sweep, zoom-through |
| f5399–f5544 | 179.97–184.80 | CRT TV screen: word reel lands on "Legacy" | focus window, ghost words, dry-brush highlighter | cursor hold, window grow, reel spin, brush, punch-in, creep, accelerate |
| f5545–f5720 | 184.83–190.67 | Desk mood-board pan: 356 → 911 → Boxster → Cayenne → Macan prints | tape, stamp labels, pens, clippings | zoom-in carried from CRT, 12 fps zig-zag pan, pull-back |
| f5721–f5826 | 190.70–194.20 | End quote card on grid paper, B&W cut-out of Ferdinand (Ferry) Porsche in a chair | crop marks, typed quote, yellow lagging silhouette | marks draw 18 f, portrait slides 40 f, typing 50+20 f |
| f5827–f5898 | 194.23–196.60 | Same, fading to black, then black | — | linear fade 49 f + 23 f black |

---

## 10. Replication recipes

```js
// R1 — Highlighter title box reveal (model cards, CRT window, price variant)
const HL = {
  color: '#F2F709', heightPx1080: 138, padX: 36, padTop: 33,
  cursorW1080: 24,            // starts as 8px@360 bar
  startDelayFrames: 9,        // after the scene cut (7–10 observed)
  durationFrames: 29,         // 30 fps
  ease: 'easeInOutCubic',     // sampled on 12 fps (step every 2/3 frames)
  // measured fraction of final width at 12-fps samples:
  keyframes: [0.03,0.06,0.11,0.17,0.26,0.52,0.79,0.87,0.91,0.96,0.98,1.0],
  textReveal: 'hard mask at box right edge',
  subtitle: { delayFrames: 5, durationFrames: 15, featherPx1080: 45, ease: 'linear' },
};
// price variant: text already visible, ease 'easeOutCubic', 20 frames, cursor visible 1–3 frames first.
```

```js
// R2 — Model card layout (1920x1080)
card = {
  bg: radialVignette('#FAF0E7', '#C0BCB3', {inner: 0.55, outer: 1.0}),
  grid: { pitch: 34.5, color: 'rgba(120,100,90,0.05)', width: 2 },   // barely visible
  title: { font: 'Libre Caslon Text 400', size: 98, color: '#2A2A2A', boxTopY: 180, boxH: 138, centered: true },
  subtitle: { font: 'Libre Caslon Text 400', size: 46, color: '#554949', baselineBelowTitle: 102 },
  car: { widthPct: 0.55, bottomY: 990, centreX: 955,
         enter: { fromDx: +100, frames: 8, ease: 'easeOutCubic', cadence: 12 },
         exit:  { scaleTo: 0.9, frames: 4, ease: 'easeInQuad' } },
  hold: 'weave(6Hz, ±2px)', duration: '≈2.0 s', next: 'hard cut to footage',
};
```

```js
// R3 — 12 fps stepped animation in a 30 fps timeline
const step12 = (frame) => { // returns the frame to sample: pattern 2,3,2,3
  const cycle = Math.floor(frame / 5) * 5;  // 5 frames = 2 poses
  return frame - cycle < 2 ? cycle : cycle + 2;
};
// apply to: highlight widths, type-on, bar growth, desk pan, portrait slide, crop marks.
// camera moves on live footage and the slideshow video frame: on ones.
```

```js
// R4 — Hold "weave" (applies to every static graphic shot)
weave = { intervalFrames: 5, ampPx1080: { x: 1.5, y: 1.5 }, maxPx1080: 2.7,
          perLayer: true, textLayerMultiplier: 1.5, distribution: 'uniform', rotation: 0 };
```

```js
// R5 — Yellow offset rim / lagging silhouette
photoRim = { color: '#E6E43A', offset1080: [9, 12], blur1080: 3, behindPhoto: true, cornerRadius1080: 12 };
cutoutSilhouette = { color: '#F2F709', fill: 'solid silhouette of cut-out', blur1080: 6,
  follow: 'same path as cut-out but with 4–6 frame lag (spring k≈0.25/step)',
  restOffset1080: [9, -3] };  // ends as 9–15 px rim on the right of head/shoulder
```

```js
// R6 — Paper slideshow on the beat
slideshow = { periodFrames: 30, photoWidthPct: 0.76, rim: photoRim,
  scaleIn:  { from: [0.87, 1.16][alt], to: 1.0, frames: 8, ease: 'easeOutCubic' },
  hold: 14,
  scaleOut: { to: [0.92, 1.21][alt], frames: 7, ease: 'easeInCubic' },
  cut: 'hard, on the beat' };
```

```js
// R7 — Footage lower-third caption
caption = { icon: { shape: 'triangle ▶', w: 54, h: 63, color: '#D7DE16', x: 210, baselineY: 975 },
  text: { font: 'Libre Baskerville Italic', size: 44, color: '#E2EE48' /* or #3B2A1C on light */, x: 309, baselineY: 975 },
  in: { opacity: [0,1], frames: 9, ease: 'linear', delayAfterCut: 3 },
  out: { opacity: [1,0], frames: 6, endsAtCut: true },
  iconSpinIn: { fromY: '+60px below frame', rotate: '-270deg', frames: 10 } };
```

```js
// R8 — 2.5D world-space text on a still (green Taycan)
layers = ['plate (bg photo)', 'text "2023" / "$43 000 000 000"', 'cars cut-out (occludes text)'];
// frame numbers relative to the shot start (f5221); px are @1080
camera = [
  { f: [0, 8],    scale: [1.0, 1.16], ease: 'easeOutCubic' },
  { f: [23, 45],  scale: [1.16, 0.97], contentDy: +222 /* cars move down = camera tilts up */, ease: 'easeInOutSine' }, // reveals "2023" from behind the roofs
  { f: [45, 83],  hold: true /* + 6 Hz weave */ },
  { f: [85, 113], scale: [0.97, 1.41], contentDy: -414 /* camera tilts down */, ease: 'easeInOutCubic' },
  { f: [105,125], highlight: 'price box 1029x165, cursor 1-3f then easeOutCubic 20f, behind visible text' },
  { f: [172,177], scale: '+14%', ease: 'easeInQuad', then: 'hard cut' } ];
// all camera keys sampled on 2s/3s (12 fps)
```

```js
// R9 — Slot-machine word reel (CRT)
reel = { words: ['Performance','Excellence','Precision','Engineering','Mastery','Velocity','Legacy','Prestige'],
  pitch1080: 111, font: 'Libre Baskerville 700', size1080: 54, ghostOpacity: 0.12,
  window: { strokePx1080: 4, h1080: 126, wFinal1080: 636, growFrames: 30, ease: 'easeInOutCubic', startsAsCursor: true, cursorHoldFrames: 17 },
  spin: { words: 6, frames: 35, ease: 'easeInOutCubic', direction: 'down' },
  brush: { color: '#E8EC1E', texture: 'dry brush', startFrame: 29, frames: 27, ease: 'easeInOutSine', overhang1080: 120 },
  camera: [ {punchIn: [1.0, 1.35], frames: 12, ease: 'easeOutCubic'},
            {creep: [1.35, 1.46], frames: 68, steppedEvery: 5},
            {exit: [1.46, 1.64], frames: 8, ease: 'easeInCubic', then: 'cut + keep zooming 4 steps ×1.075'} ],
  frame: { bezel: '#1A1712', bezelW1080: 54, screen: '#D4CBBD', screenVignette: '#BFB7A9', cornerRadiusPct: 0.12 } };
```

```js
// R10 — Desk mood-board pan
desk = { bg: '#E4DBD3', prints: { border1080: 18, shadow: {dx: 7, dy: 7, blur: 9, opacity: 0.35}, rotate: [-12, 10] },
  tape: { color: '#F3F80B', w: 60, h: 24, rotate: [-6, 6] }, labels: 'stamp-perforated cards, serif',
  path: [ {dir: [-1, -0.35], frames: 68}, {dir: [-0.4, -1], frames: 37}, {dir: [-1, +0.7], frames: 40} ], // camera direction
  speed1080PerFrame: [36, 52], cadence: '12 fps (2,3,2,3)', cornersRounded: true,
  start: 'zoom-in carried from previous shot, ×1.075 per step, 4 steps', end: 'pull-back to 0.76× over 15 f, easeInOutSine, cut' };
```

```js
// R11 — End card + outro
end = { bg: 'grid paper #F4EBE2, pitch 34.5px, vignette to #CECAC1',
  cropMarks: { color: 'rgba(60,45,50,0.45)', width1080: 5, drawFrames: 18, delay: 3 },
  portrait: { bw: true, enterFromRight: true, frames: 40, ease: 'easeOutQuart', cadence: 12, silhouette: cutoutSilhouette },
  quote: { font: 'Libre Baskerville Italic', size1080: 52, leading1080: 69, color: '#564A4B', x1080: 363, y1080: 333,
           typeOn: { charsPerSec: 34, newCharFadeFrames: 2, delay: 6 } },
  attribution: { font: 'Libre Baskerville 700', size1080: 26, align: 'right of quote block', charsPerSec: 45 },
  hold: 30, fadeToBlack: { frames: 49, ease: 'linear' }, blackTail: 23 };
```

---

## 11. Uncertainties

- **Fonts**: identified by shape only at 360p; the title serif could be Caslon-, Baskerville- or Georgia-like. Treat named Google fonts as stand-ins.
- **Grain/texture**: 360p compression removes fine grain; high-pass std 0.5–0.9 luma on paper means grain amplitude at 1080p cannot be measured — the 6 Hz weave is the only reliable "boil".
- **Chart start and circle** begin in agent B's range (f3927); only the bar tail/circle/exit were measured here.
- **Reel scroll speed**: ghost words have ~5 % contrast, so per-step displacement measurements (3,5,7,10,15,22 px) are approximate and may alias at the word pitch.
- **Desk pan zoom**: the per-step zoom estimates (×1.075 in, ×0.955 out) were fitted with translation; ±2 % error. Scale during the middle of the pan was assumed constant.
- **Carousel 3D**: rotation angles and DOF blur amounts are estimated visually (~15° Y-rotation, 4–6 px blur).
- **Dry-brush highlighter shape**: whether it's a texture wipe-on (mask revealing a static brush image) or a procedurally drawn stroke can't be determined; the bbox grows L→R and the left end is blobby from the start, consistent with a masked brush texture.
- **Yellow silhouette on the end card**: could be either a lagging duplicate (follow-through) or an offset that animates from +40 px to +3 px; both give the measured offsets.
- **White flash f4743**: only one occurrence; may be an editing artefact rather than a deliberate device.
- Colours on yellow boxes (title ink) are contaminated by JPEG chroma subsampling; ink likely neutral charcoal.
