# v5_valuable826 — part A (f0–f1406, 0.00–56.24 s) — agent v5_valuable826_A
Status: COMPLETE (all seq sheets 000–022 + overview 00–02 reviewed, key frames measured at full res).
Conventions: source is 1280x720 @ 25 fps. "@720" = measured px; "@1080" = x1.5. %H = px/720.
Frame numbers are 0-indexed (f0 = frames/00000.jpg). 1 frame = 0.04 s.

## 1. Overview
An editorial "Nike Swoosh at 50 / Dept. of Nike Archives" piece. Two sub-pieces live in my range:
**(A) f3–f1108, horizontal 16:9 paper-collage film** — off-white scanned paper (#FDFDFD with grey
specks), gigantic high-contrast serif headlines cropped by the top edge ("NEVER DONE / LEAVING A
MARK", "MOVEMENT"), a single red-orange accent (#E94812-ish) used for crayon/pencil scribbles,
stencil letters and swoosh drawings, small Helvetica "archive caption" blocks that type on with a
`_` cursor, B&W halftone/press photos that arrive by crumpled-paper bursts and torn-paper tunnels,
step-and-repeat (chronophotography) echoes of photos and swooshes, black "quote cards" in cream
serif with an ink-bleed variant, and a 25-shot accelerating flash-cut montage of real-world swooshes.
Everything is animated **at 12 fps (on twos, with one 3-frame step per second)** inside 25 fps,
with the paper texture re-randomised every ~4 frames. **(B) f1109–(beyond f1406) a vertical 9:16
sub-video pillar-boxed on pure black** (panel x=437–842), live video on ones, same type system
(serif headline + Helvetica caption block + "Department of Nike Archives" stamp) over a red studio
and red-paper collages. The metrics' "45 s shot" (f1109–2233) is just this pillarbox — it contains
many internal cuts/collage changes. Ends with the tagline "Never done leaving a mark." and a
"50 + swoosh" logo on blank paper (f1001–f1108).

## 2. Colour
Sampled (median of patches) — hex | role | approx share in my range.
| hex | role |
|---|---|
| #FDFDFD / #F9F9F7 / #FCFCFB | main paper (std 1–2, plus sparse grey fibres/specks) ~35 % of A |
| #000000 | pillarbox bars of part B (f1109+), 68 % of each B frame |
| #010101 – #030303 | black quote card / black handwriting collage bg (+ white dust specks) |
| #262626 – #2C2C2C | lifted "scanned print" black of the Prefontaine collage (f346–353) |
| #E94812 (core #EB4610, range #DE4B1B–#EE4612) | SOLID accent: stencil letters D/Z/A/N, underline bar, outline swoosh (title card) |
| #EB421A | solid orange swooshes (MOVEMENT row) |
| #F1AE9F – #F5BBAC | grainy "echo" swoosh copies (same hue, ~35 % ink density, riso/stipple grain) |
| #E07964 – #E86E52 (core) | crayon/pencil scribble line (semi-transparent, lighter than solid accent) |
| #EE480F / #F0450C | wet paint-dab swoosh (f825–829) |
| #EB370C | paint splat over a face (f571–579) |
| #C0472D / #CB4B2F | burnt-orange flat triangles in Knight torn-tunnel collage |
| #B04C35 (on black, AA'd core ~#B0442A) | quote-card underline |
| #E9E9D0 | cream serif on black quote card |
| #B8B8B8 (peaks #DADADA) | chalk handwriting on black |
| #222931 | MOVEMENT headline ink (blue-black) |
| #1D202A – #2B333E | navy-black swoosh fill in "SWOOSH Design 1971" sketch |
| #29292B | small serif labels (MJ list) |
| #000000–#151515 | headline / caption ink |
| #F3DBB9 | kraft/manila card; masking tape #D0C19A–#D8C9A0 (semi-opaque) |
| #FAFBF7 + grey 1-px grid | graph paper (cell ≈21 px@720 = 31 px@1080) |
| #270707 / #27090C | dark brown suit in torn-tunnel photo (torn fibre bands pure white) |
| Part B: #901517 red studio, #D23821/#BC2F1C/#E7452C red paper, #FFF1EC white serif, #CD0002 red duotone tile, #670026→#9C1349 magenta studio, green duotone ~#265F1D/#4B963D |
Rules:
- ONE accent hue only (red-orange, hue ≈ 10–15°). Everything authored is black / white / cream /
  grey; colour enters only through real product photos (red shoe box, AJ1, Off-White, flash-cut
  footage) and the part-B red studio. Accent is used for: pencil scribbles, sketch annotations,
  stencil letters, underline bars, swoosh drawings, "Oh yeah," type, paint splats. Never for
  headlines or captions.
- Photos are B&W (halftone or press-grain) on paper; colour photos only for product/archival
  colour material.
- Black is used as a "chapter" colour: quote cards and the handwriting collage.

## 3. Typography
### 3.1 Display serif — clean ("NEVER DONE", "MOVEMENT", quote lines 1–2, "NEVER DONE" in part B)
- High-contrast transitional/old-style serif CAPS (Garamond/Sabon-like: wide D/O, long-legged R,
  bracketed serifs). Free: **EB Garamond Medium** or **Cormorant Garamond SemiBold** caps, tracking
  ≈ -2 % (word space almost closed: "NEVERDONE").
- Title card (f18–f123): "NEVER DONE" visible cap 104 px@720 (14.4 %H, 156 px@1080) — top serifs are
  cut by y=0; spans x=180–1102 (72 % W), centred x≈641. Ink ≈ black.
- "MOVEMENT" (f272–f345): true cap 171 px@720 (23.8 %H, 257 px@1080; measured 140 px at 0.818 zoom),
  baseline at y≈100 → **≈41 % of the cap height is above the frame**; bleeds off left and right;
  ink #222931 with rough photocopy edges.
- OVERSIZE RULE: the hero word is set so large that it touches/crosses the top edge and usually
  one or both side edges; it is never fully visible until the camera pulls back.
### 3.2 Display serif — "ink-bleed" variant ("LEAVING A MARK", "LOVE IT.", "BREAKING THE MOLD.", "A VISIONARY")
- Same serif, but every stroke end and joint carries bulbous liquid blobs and short drips (like
  glue/ink piped through a nozzle), slightly swollen strokes. Static (no boil).
- "LEAVING A MARK": rows 116–230 (cap ≈114 px@720 = 15.8 %H, 171 px@1080), x=13–1273 (98.5 % W).
- Used for the SECOND line / punch word of a headline, the clean serif for the first line.
### 3.3 Quote card serif (f427–f484)
- Cream #E9E9D0 on #010101. "WELL, / I DON'T / LOVE IT." — lines 1–2 clean, line 3 ink-bleed.
- Cap 78 px@720 (10.8 %H, 117 px@1080); line pitch 100–102 px@720 (1.3 x cap); block x=419–877,
  y=202–492, left-aligned, block centred on frame (x≈648, y≈347).
### 3.4 Small serif labels
- MJ list "Michael Jordan / Hand Drawn / Swoosh / Air Jordan" (f589–f650): cap ≈25 px@720
  (3.5 %H, 37 px@1080), line pitch ≈34 px@720, left x≈760, #29292B, mixed case Regular.
- "Steve Prefontaine / running in / backwards Swoosh" (f262–f345): same style, very tight leading
  (≈0.85 em), left-aligned, partly cropped by the left edge while typing.
- "1987" (f662–f675), same serif ≈28 px cap@720.
- Tagline (f1001–f1038): "Never done leaving a mark." cap ≈24 px@720 (3.3 %H, 36 px@1080), x=429–834,
  y≈344–368; "Never done" clean, "leaving a mark." in a broken/letterpress-degraded cut (missing
  ink, wobbly glyphs) — same clean→damaged contrast as the headline.
### 3.5 Caption block (Helvetica) — the "archive label"
- Helvetica Neue Regular (free: Inter / Arimo), black on paper, two columns:
  `Year: / 1971` `Story:: / Swoosh` (double colon is in the source) / `Dept. of / Nike Archives`
  `From a simple logo / for the next symbol of inspiration.`
- Cap 16 px@720 (2.2 %H, 24 px@1080); line pitch 21 px@720 (32 px@1080, ≈0.95 em leading);
  pair-to-pair pitch 74 px@720 (111 px@1080); columns at x=29 and x=194 @720 (2.3 % / 15.2 % W);
  last baseline y≈657 → bottom margin ≈8.7 %H.
- Reappears in part B (f1148+): "Year: 1971 / Story: Waffle Mindset / Dept. of Nike Archives /
  From a kitchen experiment, for an innovation revolution." in white, with a thin white rule below.
### 3.6 "Department of / Nike Archives" stamp
- Helvetica Neue Medium ≈11 px cap@720, 2 lines, thin underline rule ≈100 px wide, a small
  hand-drawn outline swoosh scribbled across it. Bottom-right on the title card; also in the
  Cortez collage (f404–f425) and part B (over the CRT).
### 3.7 Grotesks
- Bold neo-grotesk "AirMax / Tinker / Hatf…" (f677–f720): Helvetica Bold-like (free: Inter Tight
  Bold / Archivo Bold), tracking ≈ -3 %, rough photocopy edges; the "a" in "Max" is a flipped
  glyph ("AirMɐx" — glitch-y typo as a style cue). Cap 87 px@720 (12 %H, 131 px@1080), line pitch
  ≈119 px@720 (≈0.95 em), left x≈150.
- Medium grotesk with a quirky "ə"-shaped e: "Wəll, I didn't love it. But I knew it would"
  (Knight torn-tunnel, f354–f365), cap ≈30 px@720, black, two copies (top-left large; right column
  narrow, ragged).
- "Oh yeah, / Oh yeah," (f560–f585): Helvetica Medium in accent orange #EB370C-ish, ≈22 px cap@720.
- Vintage-ad body type ("1973's fastest Mile / 3:55.0 / 1973's fastest Shoe" f292–f345;
  "…Patented Suede 'n Swoosh upper gives" white on black f346–353): scanned, slightly rotated
  (≈ -3°), letter-spaced grotesk.
### 3.8 Hand lettering
- Chalk/dry-marker handwriting on black ("Well, I didn't love it / But I knew it / would grow on
  me.") x-height ≈40–55 px@720, #B8B8B8, textured.
- Orange technical (architect) caps: "LATERAL VIEW / AIR MAX MENS SIZE 9 (left foot)", "stability
  wing", "heel cushion", "visible…" ≈12–18 px cap@720 with arrows.
- Orange stencil-ish rounded sans single letters D, Z, A, N (Carolyn Davidson's sketch
  annotation): "D" ≈80 px tall@720 at its largest.
- Distressed white brush capitals "WE", "LEA…" (f350–353) — giant (≈230 px cap@720), grunge edges.
### 3.9 How text animates (all in final position — never slides in; no fade)
- Serif headlines: **letter-by-letter typewriter on twos** for the first line (NEVER DONE: N f18, NE
  f21, NEV f23, NEVE f25, NEVER f27, D f29, O f31, N f33, E f35), **word-by-word** for the ink-bleed
  line (LEAVING f35, A f39, MARK f43, 4-frame steps). MOVEMENT: one letter per 4 frames
  (M f272, O f276, V f280, E f284, M f288, E f292, N f296, T f300). Quote card: one letter per 2
  frames (WE f427, WEL f429, WELL f431, "WELL," f433, I f435, D f437, O f439, N f441, ' f443, T f446),
  "LOVE" as a whole word f448, "IT." after. Part B: word-by-word on 3-frame steps (NEVER f1133,
  DONE f1136, BREAKING f1139, THE f1142, MOLD. f1145).
- Captions: char-by-char ≈2–3 chars per 2-frame step (≈30 chars/s), trailing "_" cursor on the
  active line, several fields typing concurrently with staggered starts ("Ye_" f6, "Year:/_" f10,
  "1971" f16, "Story" f21, "Swoosh" f27, "From a simple logo / for the next symbol of
  inspiration." f29–f62). Caption ink changes on every even frame f6–f18 (on twos from the very
  first frame), then follows the 12-fps clock; note metrics.csv labels some of these tiny text
  changes "hold" (e.g. f8, f12, f16) — its threshold hides small type changes.
- Stamp/labels: scrambled reveal — letters of "Department of Nike Archives" appear in random order
  ("D pa  me", "Nk  A  he") over ≈30 frames, then resolve.
- Bold grotesk: types with letter swaps ("AirMs" → "AirMsx"), 1 glyph per 2 frames.
- Tagline: letter-by-letter (≈1 char / 2 frames) for "Never done", then whole words ("leaving"
  f1017, "a" f1019, "mark." f1021); removed in ONE frame (f1039).
- Exits: words erased in reverse order (MARK gone f121, "LEAVING A" gone f123) or whole card shrinks
  away (quote card) or hard erase. Never fades.

## 4. Layout & composition
- Frame used edge-to-edge: hero type is anchored to the TOP edge (cropped), small caption block
  anchored bottom-left at ≈2.3 % W / 8.7 %H margins, archive stamp bottom-right (≈x 1100–1240,
  y 640–700 @720). Centre band (y 30–80 %) is the "drawing table" for swooshes/photos.
- Title card grid: headline lines 0–31 %H; scribble/logo zone 35–80 %H; captions 76–92 %H.
- Collage scenes are centred clusters (photo stacks ≈30–45 % W) floating on paper or black with
  generous negative space (30–60 % of frame empty), plus edge-bleeding photos at left/right.
- Layers per collage: 4–8 (paper bg → large photo/print → taped notes/tracing paper → cut-out product
  photo → pen lines/annotations → stamps/letters → accent scribbles on top).
- Scale contrast is extreme: 171 px-cap headline vs 16 px-cap captions (≈11:1).
- Step-and-repeat rows run horizontally (swoosh echoes at y≈50 %H; runner strips at top/bottom
  15 %H bands).
- Part B: 9:16 panel 406x720 centred (x=437–842), black bars; headline spans full panel width and
  bleeds off its top; caption block bottom of panel above a thin rule.

## 5. Textures & materials
- **Paper boil**: whole paper scan swaps every 3–4 frames (title card: f6,10,14,18,23,27,31,35,39,
  43,46,50,54,58…; tagline: f1004,1007,1011,1014,1018,1021,1024,1027,1031,…) ≈ 6–8 fps, independent
  of element animation. Correlation of empty paper between swaps only 0.07 → different scans, not a
  shift. Amplitude: mean abs diff 1–6 levels (/255), specks and faint fibres. Black cards boil the
  same way (dust specks, every 4 frames: f429,433,437,441,446,450,454,458).
- **Halftone photos**: B&W newspaper halftone, 45° screen, period ≈3.7 px@720 (≈5.5 px@1080),
  hard contrast (Carolyn Davidson photo f127–f200).
- **Crumpled paper**: real photographed white paper crumples/unfolds (stop-motion) used as reveal
  and exit (f118–127, f141–157, f177–209, shoe box leading edge f656–f668). Crease highlights
  white, shadows mid-grey, no colour.
- **Torn paper**: Knight tunnel — 5–6 concentric torn layers of the same photo, white fibrous torn
  bands 8–25 px@720 (12–37 px@1080) irregular; MJ sheet (f585–f598) torn grey edge; Prefontaine
  photo "eroded" to white by grunge brush (f350–f353).
- **Tracing paper / taped prints**: semi-transparent vellum over sketches (Cortez collage), tan
  masking-tape strips ≈50x20 px@720 at top/bottom of prints, slight rotation (±2–4°).
- **Graph paper**: 1-px grey grid, ≈21 px cells @720, darker every 5th line.
- **Riso/stipple grain**: orange echo swooshes are stippled (≈35 % dot density); "dotted/stippled
  swoosh" variant uses coarse dots.
- **Pen lines**: black ink rectangle/lines 2 px@720 (3 px@1080), wobbly, corners overshoot 10–35 px.
- **Crayon/pencil scribble**: 5–6 px@720 cross-section (≈4 px core, 7–9 px@1080), soft edge,
  semi-transparent #E07964, slightly grainy.
- **Black marker**: fat strokes 60–120 px@720 with thin white hairline streaks (dry-brush) — f414–426.
- **Film scan black** (Prefontaine): #262626 with dust, scratches and a visible image-panel edge.
- **Part B**: heavy RGB mis-registration fringes on cut-outs (magenta/blue/yellow 2–4 px outlines),
  strong grain, duotone photos (red/pink/green/B&W tiles).
- No vignette, no light leaks, no drop shadows on paper elements (cut-outs sit flat; only real
  photographed objects carry their own shadows).

## 6. Motion
### Cadence (key)
- f0–f930: **12 fps drawings conformed to 25 fps**: changes every 2 frames plus exactly one 3-frame
  step per second — every 3-frame gap ends on a frame where frame % 25 == 21 (f21, 46, 71, 96, 121,
  … 821; 31 of 33 cases). Per second: 11 x 2 + 1 x 3 = 25 frames = 12 drawings.
- Gap histogram f0–f1406 (changing frames): {1:244, 2:382, 3:33, 4+:~30}. All 1-gaps are inside
  f942–f972 (swoosh-variant swarm, on ones) and part B f1110+ (live video on ones).
- Camera moves are stepped on twos too (scale changes only on drawing frames).
### Camera
- Constant slow "breathing" scale drift ≈0.1–0.25 %/frame, stepped on twos:
  title card push-in ≈+2–3 % over f18–f75; Cortez collage push-in 1.000→1.085 over f373–f410
  (+drift −22 px x); quote card shrink ≈−4 % over f444–f466; MOVEMENT pull-back 1.000→0.942 over
  f300–f335.
- Accelerating exits (easeIn): MOVEMENT 0.942→0.933→0.923→0.878→0.818 (f335–f343, easeInCubic) then
  hard cut; quote card 1.0→0.971→0.905→0.810→0.704 (f477–f483, easeInQuad) then type vanishes;
  MJ collage 1.0→0.962→0.923→0.861→0.786→0.690 (f648–f656, easeInCubic) then gone.
- Snap push-in: f366→f368→f371 scale 1.00→1.79→2.33 (2 drawings, easeOutExpo) into the collage.
- Reveal jolt: f127–f133 photo 1.000→1.011→1.032→1.085 with translation jolts (−7,+2)→(+43,−22)→
  (+18,+19) px@720 (easeOutQuad).
### Elements
- Pencil scribbles: trim-path write-on then write-off. A stroke grows ≈200–300 px@720 per 2-frame
  step (≈2500–3750 px/s @720, 3750–5600 px/s @1080), a 600–800 px stroke draws in 3–4 drawings,
  holds ~2–4 drawings, then its START trims away (tail chases head); lifespan ≈12–16 frames;
  1–3 strokes alive at once; each step keeps 60–90 % of previous orange pixels. No jitter of
  existing strokes.
- Rectangle draw-on (f206–f240): corner-first — bottom-right corner f206, right+bottom edges
  f206–f214, top edge f218–f228, left edge f226–f240 (≈34 frames = 1.36 s for ≈1550 px perimeter).
- Underline wipe (quote card): L→R, right end x=477,567,653,729,795,850,890,900,909,916,921 on
  f448…f468 → easeOutCubic, 20 frames (0.8 s), length 523 px@720 (785 px@1080), 3–4 px thick.
- Stencil letters / logo bits: pop on at full size in one drawing (no scale-in), then jump between
  positions/scales every 2–3 frames (f916–f941 D/Z/A/N assembly: A pops tiny f918, D huge f923,
  whole group snaps to 0.5x f925, letters rearrange f927–f941).
- Swoosh variants (f71–f117, f942–f978): each drawing REPLACES the previous swoosh rendering with a
  different medium (outline, stipple, zig-zag scribble, dry-brush, ink blot dots, smooth gradient)
  — a "style boil" on twos (on ones f942–f972); big black brush strokes sweep across the frame in
  2–4 drawings to wipe.
- Step-and-repeat builds: copies are added one per drawing (MJ 1→5 copies f585–f587, offset ≈60 px@720;
  Jumpman 3 copies; Knight shoe photo cascade 5 copies stepping ≈30 px down-right; Muybridge runner
  strips gain one figure per drawing; swoosh echoes spawn L→R, ≈190 px@720 apart, alternating solid
  and grainy). Removal = copies vanish one by one (MJ f621–f641).
- Handwriting write-on: ≈1 letter per 2 frames (chalk quote f485–f585, ≈100 frames for 3 lines).
- Orange ellipse loop around shoes: drawn in ≈8 frames (f502–f516), easeOut.
- Paint splat: grows over 4 drawings (f571–f579) as hand-painted blobs.
- Air Max shoe line drawing (f256–f345): flickers between 3–4 different drawings (outline only /
  filled orange / partial) on twos — a "drawing boil".

## 7. Transitions
| frames | type | description |
|---|---|---|
| f2→f3 | hard cut | black → paper title card |
| f118–f127 | crumpled-paper burst | crumpled white paper erupts from bottom-centre (f119 ~150 px, f121 ~560x400, f123–125 frame-wide) and unfolds, revealing the halftone photo inside; headline words erased in reverse at the same time; 10 frames, on twos (+one 3-step) |
| f127–f133 | jolt push | 1.085x in 3 steps with translation jolts (metrics' "cuts" at f129/f133 are these jolts) |
| f139–f157 | unfurl | newspaper strips unroll from crumpled balls L→R (≈8 drawings) |
| f177–f209 | crumple-away | photo and strips crumple into balls and fly off (top-right / left), leaving paper + scribbles |
| f250–f256 | morph/recolour | sketch rectangle shrinks, navy swoosh turns grainy orange, becomes first swoosh of the echo row |
| f300–f345 | accelerating pull-back → hard cut f346 | easeInCubic zoom-out 1→0.818 then cut |
| f346, f354, f366 | hard cuts | rapid collage plates: Prefontaine-on-black (8 f), Knight torn tunnel (12 f), white table (5 f) |
| f366–f371 | snap zoom-through | 1→2.33x in 2 drawings into the Cortez collage |
| f414–f427 | marker scribble wipe + cut | black marker scribbles cover ≈75 % in 6 drawings (f414 swoosh stroke, f416/418 loops, f421 zig-zag fill, f423–425 fat fill) → hard cut to black quote card f427 |
| f477–f485 | shrink-out | quote card scales to 0.70 in 4 drawings, type removed, black stays; handwriting collage builds on the same black |
| f583–f598 | dual paper wipe | white sheet with straight edge slanted ≈17° (top leans right) slams in from right (edge x≈952 mid-height at f585 → 880 f589 → 748 f591, ease-out steps) while a torn-edged grey sheet with MJ step-repeat photo enters from left; black collage squeezed between and gone by f596; ≈12 frames |
| f646–f660 | zoom-out + push | collage shrinks (easeInCubic) while red shoe box with crumpled leading edge pushes in from right; at f660 everything but the box pops off |
| f720→f721 | hard cut | after an Air Max zoom-out, cut to taped-print card |
| f721–f770 | in-frame image swaps | taped print on white; picture hard-swaps every 6–10 frames (f721, 727, 737, 746, 754, 762) and card size/tape re-randomise |
| f771–f823 | ad-slap stack + reverse | vintage ads/clippings slap on top every 2–4 frames (f775, 779, 783, 787, 791, 796, 800, 804) then the stack plays back in reverse f806–f823 (ping-pong) |
| f823–f825 | brush swoosh entry | orange brush swoosh enters at right edge, ad removed, swoosh centred on blank paper; dries into broken dabs f827 |
| f831–f915 | flash-cut montage | see table below |
| f916 | hard cut | to white paper + thin outline swoosh |
| f942–f979 | swarm + brush sweep | swoosh variants multiply on ones, giant brush strokes sweep through and everything exits off-frame (bottom-left) by f979 |
| f1039 | hard erase | tagline removed in one frame (paper stays) |
| f1053 | pop-on | 50+swoosh logo appears whole |
| f1108→f1109 | hard cut | to pillarboxed vertical sub-video |
| f1187, f1208–f1222, f1223–f1290 | (part B) glitch collage, tile-mosaic dissolve (≈55 px square tiles swap B&W for colour over 14 frames on ones), tile shuffles/duotone flips |
| f1346→f1347 | (part B) cut | to magenta studio "This is not just a toy snake." |

Flash-cut montage f831–f915 (each shot is a held still, 100 % hold inside the shot):
| # | frames | len (f) | content |
|---|---|---|---|
| 1 | f831–834 | 4 | rainbow-stripe sign w/ chain |
| 2 | f835–838 | 4 | hand drawing swoosh on playbook whiteboard |
| 3 | f839–845 | 7 | swoosh painted on black tile wall |
| 4 | f846–849 | 4 | gold swoosh pendant |
| 5 | f850–853 | 4 | swoosh drawn on plaster cast |
| 6 | f854–859 | 6 | red sticker on lamp-post |
| 7 | f860–863 | 4 | skateboard |
| 8 | f864–870 | 7 | laptop sticker |
| 9 | f871–874 | 4 | swoosh painted on pipe |
| 10 | f875–878 | 4 | red swoosh in terrazzo |
| 11 | f879–884 | 6 | shaved-haircut swoosh |
| 12 | f885–888 | 4 | sticker on palm (photo rotated ≈-8° on black) |
| 13 | f889–890 | 2 | embroidered flower tee |
| 14 | f891–895 | 5 | painted eyebrow |
| 15–24 | f896–915 | 2 each | car mirror, vase, graffiti, banana, helmet, blue pole, fishbowl, purple sticker, stone, teeth |
Rhythm: 4–7-frame shots (2–3 drawings) for 2.4 s, then 2-frame strobe (1 drawing each) for 0.8 s →
accelerando. Lengths 6/7/5 contain the once-per-second 3-frame step. Swoosh always near frame centre
(≈30–45 % W) so the eye locks on it across cuts.

## 8. Recurring devices
- **Crayon scribbles** (orange, trim-path on/off, constant activity under titles) — see §6.
- **Stencil annotation logo**: outline swoosh + orange letters D, Z, A, N + underline (from
  Davidson's original sketch) — title card, Prefontaine (white version), Cortez collage, ads stack,
  end (black version).
- **Swoosh in many media** (outline, stipple, zig-zag, dry brush, dotted ink, gradient, paint dab,
  grainy riso) cycling on twos.
- **Step-and-repeat / chronophotography echo**: Muybridge runner strips, MJ x5, Jumpman x3,
  Prefontaine film-strip x6, shoe-photo cascade, swoosh echo row (solid/grainy alternating).
- **Archive caption block + "Department of Nike Archives" stamp** (typing with cursor; scrambled).
- **Oversized cropped serif headline** with clean line + ink-bleed line.
- **Black quote card** (cream serif, ink-bleed punch word, orange underline wipe).
- **Hand-drawn pen frames**: black wobbly rectangle with overshooting corners; black rule lines.
- **Technical sketch annotations** in orange: arrows, "stability wing", "heel cushion".
- **Tape strips, tracing paper, kraft cards, graph paper, newspaper strips, patent documents.**
- **Crumple / unfurl** paper physics (stop-motion).
- **Paint splat / marker scribble** as wipe or emphasis.

## 9. Scene log
| frames | time (s) | on screen | devices | motion / transition |
|---|---|---|---|---|
| f0–f2 | 0.00–0.08 | black | | hard cut f3 |
| f3–f17 | 0.12–0.68 | blank paper; caption starts typing f6 (on twos) | paper boil /4f | |
| f18–f70 | 0.72–2.80 | "NEVER DONE" (letters, 2f) + "LEAVING A MARK" (words, 4f); orange scribbles; D/Z/A/N + outline swoosh logo f43; caption completes f69 | typewriter, trim-path pencil | twos, slow push-in |
| f71–f117 | 2.84–4.68 | swoosh variants morph right-half; stamp scramble-types; black brush strokes sweep f102–f109; smooth black→dark-red gradient swoosh centred f109–f117 | style boil | twos |
| f118–f127 | 4.72–5.08 | crumpled paper bursts open → halftone Carolyn Davidson photo; headline words erased | crumple reveal | |
| f127–f177 | 5.08–7.08 | photo + newspaper strips unfurl ("Carolyn Davidson works in her P…"), patent doc, "nike" script on tape, outline swoosh, orange "stability" note | unfurl, collage | jolt push f127–133 |
| f177–f209 | 7.08–8.36 | everything crumples away; orange scribbles on paper; small paper ball | crumple-away | |
| f202–f250 | 8.08–10.00 | ball → navy swoosh; black pen rectangle draws on; '"SWOOSH" Design / 1971' handwritten label | pen draw-on | slow zoom-out |
| f250–f270 | 10.00–10.80 | swoosh turns orange/grainy → echo row of 5 swooshes; runner strips; Air Max line drawing | step-and-repeat | |
| f271–f345 | 10.84–13.80 | "MOVEMENT" types (1 letter / 4f); "Steve Prefontaine running in backwards Swoosh"; "1973's fastest Mile 3:55.0 / 1973's fastest Shoe" + nike script | drawing boil on Air Max sketch | pull-back easeInCubic → cut |
| f346–f353 | 13.84–14.12 | Prefontaine colour photo on black collage, white DNA logo, white brush swoosh, ad text; f350 grunge white "WE"/"LEA" brush type + photo eroded white | grunge brush | cuts in/out |
| f354–f365 | 14.16–14.60 | Phil Knight torn-paper tunnel (5–6 torn layers) on white/burnt-orange; "Well, I didn't love it. But I knew it would" typing in 2 places | torn paper, typing | hard cut |
| f366–f370 | 14.64–14.80 | white table, small collage card | | snap zoom 2.33x |
| f371–f413 | 14.84–16.52 | Cortez sketch collage: tracing paper notes, black Cortez cut-out, Prefontaine film strip x6, side photos, tape; pen lines draw; orange L-bracket; stamp | pen draw-on, step-repeat | push-in 1.085x |
| f414–f426 | 16.56–17.04 | black marker scribble covers collage | marker wipe | → cut |
| f427–f484 | 17.08–19.36 | black quote card "WELL, / I DON'T / LOVE IT." + orange underline | typewriter, underline wipe | slow shrink, accelerating exit |
| f485–f584 | 19.40–23.36 | black: chalk handwriting "Well, I didn't love it / But I knew it / would grow on me."; Knight B&W photo + shoe cascade; orange "LATERAL VIEW / AIR MAX MENS SIZE 9"; orange loop; f548 photo swap + more photos; "Oh yeah, Oh yeah,"; orange splat; DNA logo; MJ photo enters left | handwriting write-on | |
| f585–f597 | 23.40–23.88 | dual paper wipe to MJ collage | wipe | |
| f598–f659 | 23.92–26.36 | MJ "Hand Drawn Swoosh / Air Jordan" list on graph paper; Jumpman x3; MJ x5 → x1; basketballs; nike script; swoosh | typewriter serif, step-repeat | zoom-out f646–656 |
| f660–f720 | 26.40–28.80 | red Nike Air shoe box (photo) enters right; "1987"; orange Air Max tech sketch & arrows; "AirMax / Tinker / Hatf…" bold grotesk; black rule | annotation draw-on | zoom-out f708–720, cut |
| f721–f770 | 28.84–30.80 | taped print slideshow: Cortez on box, nike script+swoosh sketch, Moon Shoe, Air Max 1 sketch, Off-White Waffle Racer, scribble swoosh | in-frame swaps | |
| f771–f824 | 30.84–32.96 | ad stack: "FEEDS ON 80 LBS. OF OPPONENT A DAY.", Nike NEWS, "HAVE A NIKE DAY", "JUST QUIT IT.", AJ1, AF1, patent docs, DNA logos at sides — forward then reverse | slap-on | |
| f825–f830 | 33.00–33.20 | orange paint swoosh on blank paper → broken dabs | paint | cut |
| f831–f915 | 33.24–36.60 | 25-shot real-world swoosh flash montage | flash cuts | accelerando |
| f916–f941 | 36.64–37.64 | outline swoosh + D/Z/A/N assemble | pop/jump layout | |
| f942–f978 | 37.68–39.12 | swoosh variants swarm (on ones), brush sweeps, exit | style boil | |
| f979–f1000 | 39.16–40.00 | blank paper | boil only | |
| f1001–f1038 | 40.04–41.52 | "Never done leaving a mark." | typewriter | hard erase f1039 |
| f1039–f1052 | 41.56–42.08 | blank paper | | |
| f1053–f1108 | 42.12–44.32 | "50" + swoosh logo (black, ≈145x60 px@720, centred) | | hard cut |
| f1109–f1186 | 44.36–47.44 | [part B] pillarboxed red studio, CRT on Doric column; "NEVER DONE / BREAKING / THE MOLD." types word-by-word f1133–f1145; caption block + stamp type f1148–f1160 | live video on ones | |
| f1187–f1222 | 47.48–48.88 | red paper collage: Bowerman colour photo, two cut-out waffle shoes, "This is not just a coach."; tile-mosaic swap to B&W | mosaic | |
| f1223–f1285 | 48.92–51.40 | duotone photo-tile grid shuffles (red/pink/B&W/green) | tile shuffle | |
| f1286–f1346 | 51.44–53.84 | "THIS IS / A VISIONARY" (white serif, ink-bleed line 2; cap ≈33 px@720) over red paper, Bowerman with waffle iron, waffle-sole line drawing | | holds |
| f1347–f1406+ | 53.88–56.24+ | magenta studio, column, toy snake; "This is not just a toy snake." small white serif; slow push-in (continues into part B agent's range) | | |

## 10. Replication recipes
```js
// R1 — global cadence & boil
const FPS_OUT = 25;                      // or 24/30 for new work
const drawingFrames = f => {             // 12 drawings per second inside 25 fps
  const s = Math.floor(f / 25), r = f % 25;   // 11x2 + 1x3 per second, 3-step ends at r==21
  const steps = r < 19 ? Math.floor(r / 2) : (r < 21 ? 9 : 10 + Math.floor((r - 21) / 2));
  return s * 12 + steps;                  // use this as the animation clock for EVERYTHING
};
// at 24/30 fps: simply hold every element for 2 frames (24) or 2/3 alternating (30)
paperBoil = { swapEveryFrames: [3,4], scans: 6, specks: true, amplitude: "±1–6/255" };
```
```js
// R2 — Oversized cropped serif headline (title card)
headline = {
  line1: { text:"NEVER DONE", font:"EB Garamond 500", case:"upper", tracking:-0.02,
           capPx1080: 170, topY: -0.04*1080 /* serifs cut by frame top */, color:"#111",
           reveal:"letter", stepFrames:2 },
  line2: { text:"LEAVING A MARK", font:"same + inkBleed()", capPx1080:171, widthPctW:0.985,
           reveal:"word", stepFrames:4, startOffset: line1.end },
  exit: "erase words in reverse, 1 word / 2 frames, while camera pushes",
  camera: "scale +0.05%/frame stepped on twos",
};
// MOVEMENT variant: cap 257 px@1080, baseline at 14 %H (≈41 % of cap above frame), 1 letter / 4 f
```
```js
// R3 — inkBleed() for the second headline line (static)
inkBleed = { dilatePx1080: 2, blobs:{ at:"stroke terminals + joints", radiusPx1080:[4,12],
  drips:{ prob:0.3, lenPx1080:[6,20] } }, edgeNoise:{ amp:1.5, freq:0.15 }, color: same as line };
// implement: render text to mask → SDF → add circles at skeleton endpoints/junctions → smooth-union (k≈4px)
```
```js
// R4 — Archive caption block
caption = { font:"Helvetica Neue 400 / Inter 400", capPx1080:24, lineHeightPx1080:32,
  cols:[0.023*W, 0.152*W], pairPitchPx1080:111, bottomMarginPctH:0.087, color:"#000",
  fields:[["Year:","1971"],["Story::","Swoosh"],["Dept. of","Nike Archives"],
          ["From a simple logo","for the next symbol of inspiration."]],
  type:{ charsPerDrawing:2.5, cursor:"_", concurrent:true, staggerFrames:[0,15,23] } };
stamp = { text:["Department of","Nike Archives"], font:"Helvetica Neue 500", capPx1080:17,
  underlinePx1080:150, overlay:"hand-drawn outline swoosh", reveal:"random-order letters over 30 f" };
```
```js
// R5 — Crayon scribble (trim-path on/off)
scribble = { color:"#E07964", opacity:0.9, widthPx1080:[7,9], softEdge:1.5, grain:0.2,
  path:"long shallow curves / zig-zags, 600–1200 px@1080",
  head:{ speedPx1080PerDrawing:[300,450] }, hold:{ drawings:[2,4] },
  tail:{ chasesHead:true, speed:"= head" }, lifespanFrames:[12,16], concurrent:[1,3],
  spawn:"new stroke every 2–4 drawings across the middle band (35–80 %H)" };
```
```js
// R6 — Black quote card
quoteCard = { bg:"#010101", dust:{ swapEvery:4 }, color:"#E9E9D0", font:"EB Garamond 500 caps",
  capPx1080:117, linePitchPx1080:152, align:"left, block centred", lines:["WELL,","I DON'T","LOVE IT."],
  inkBleedLine:3, reveal:{ unit:"letter", stepFrames:2, lastLine:"word" },
  underline:{ color:"#B04C35", thickPx1080:5, lenPx1080:785, y:"+50px@1080 below line 3",
              wipe:"L→R 20 f easeOutCubic on twos" },
  idle:"scale −0.2 %/frame", exit:"scale 1→0.70 in 4 drawings easeInQuad, then clear" };
```
```js
// R7 — Crumpled-paper burst reveal (f118–127)
crumpleReveal = { asset:"photographed crumpled white paper sequence (6–8 stills)",
  origin:"bottom-centre", growth:[0.12,0.45,1.0,1.3] /* of frame width per drawing */,
  inside:"next plate (B&W halftone photo, 45° screen 5.5 px@1080)",
  simultaneous:"erase headline words in reverse", after:"jolt push 1.0→1.085 in 3 drawings" };
```
```js
// R8 — Step-and-repeat echo
echo = { copies:5, offsetPx1080:[90,0] /* MJ */ , addPerDrawing:1,
  alt:{ solid:"#EB421A", grainy:{ color:"#F1AE9F", stipple:0.35 } } /* swoosh row spacing 285 px@1080 */,
  removal:"one copy per drawing, from the back" };
```
```js
// R9 — Flash-cut montage (accelerando)
montage = { shots:[4,4,7,4,4,6,4,7,4,4,6,4,2,5, 2,2,2,2,2,2,2,2,2,2] /* frames @25 */,
  content:"one real-world instance of the logo per shot, logo near centre at 30–45 % W",
  hold:"each shot a still (no motion)", end:"hard cut to blank paper + outline logo" };
```
```js
// R10 — Paper wipe (dual sheet)
paperWipe = { right:{ sheet:"clean white", edgeAngleDeg:17 /* top leans right */,
                      xMidPct:[0.74,0.69,0.58,0.0] /* per drawing */ },
              left:{ sheet:"grey photo sheet", edge:"torn", from:"left" },
              durationFrames:12, ease:"big first step, then smaller (easeOut)" };
```
```js
// R11 — Marker scribble wipe to black
markerWipe = { color:"#000", strokeWidthPx1080:[90,180], texture:"dry-brush white hairlines",
  drawings:6, coverageAtEnd:0.75, then:"hard cut to black card" };
```
```js
// R12 — Camera grammar
camera = { idle:"scale ±0.1–0.25 %/frame, on twos", exitPull:"easeInCubic to 0.70–0.82 then cut",
  snapIn:"1→2.3x in 2 drawings (easeOutExpo)", noRotation:true, noBlur:true };
```

## 11. Uncertainties
- Exact typefaces are inferred visually (Garamond-family serif; Helvetica Neue) — not identified
  from metadata. The ink-bleed serif may be a custom treatment or a specific display font.
- Paper boil interval varies 3–5 frames; could be 6 fps nominal with conform jitter.
- Scribble speeds are from orange-pixel growth (new px / stroke width), ±30 %.
- Pixel-level JPEG compression limits colour accuracy to ≈±3 levels; thin orange lines are
  anti-aliased into the paper so their "true" ink is likely more saturated (≈#E85A3A) than sampled.
- Part B (f1109+) is live footage composited with collage; I logged it only coarsely because it
  continues into the other agent's range (f1407+); the "45 s shot" in metrics.csv is caused by the
  constant black pillarbox, not a real long take.
- Whether the flash-cut stills are video clips frozen or photos: every shot has 100 % hold, so they
  behave as stills.
- The metrics "cuts" at f125/f129/f133 are jolts inside the crumple reveal, not edits; the "cut" at
  f371 is the second drawing of the snap zoom.
