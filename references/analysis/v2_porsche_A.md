# v2_porsche_A — "History of Porsche" (Vox-style), frames f0–f1996 (0.00–66.53s)

Source: 640x360 @ 30 fps. **All px values are measured @360p; "@1080" = x3.** Percentages are of frame W (640) or H (360).
STATUS: complete — all sheets seq_000–seq_038 + overview_00–03 viewed; key frames opened full-res and measured.
Scratch scripts: `$VOX/tmp/v2_porsche_A/` (crop.py, grid.py, ywipe.py = yellow-box tracker, inc2.py = per-frame
scale+shift tracker, kb.py = direct Ken-Burns fit, textrows.py).
NB: inc2.py/motion.py scale grids do not contain exactly 1.000 — values like 0.9983/0.9986 per frame are grid
artefacts meaning "static", not a drift.

## 1. Overview
A YouTube "animated documentary" about Porsche built from three kinds of material: (a) modern Porsche promo footage
given a "film" grade (sepia-ish desat, heavy vignette, chromatic fringe), (b) archival B&W photos/films and period
print pages, (c) flat editorial graphics on warm off-white paper (cut-out photos, quote cards, car side-views with
price labels, year counters) or on near-black (timeline, blueprint chart). One accent colour only — a lemon
highlighter yellow **#F6FD10** — used for label boxes, ▶ bullets, offset outlines on cut-outs, drawn circles, chart
lines and caption text. Typography is a Georgia-like book serif (bold for labels, italic for quotes/keywords,
bold-italic for captions) plus a high-contrast Didone-ish serif for big years. Motion is snappy: hard cuts
every 1–3 s, graphics on paper animate on **12 fps (2s/3s)** while camera/map moves and map labels run on ones;
new stills typically enter with a **stepped zoom-out "punch" reveal** and labels with a **cursor-then-wipe
highlighter**. Range content: cold open (map → page curl → keyword montage), Stuttgart & Ferdinand Porsche, Lohner-
Porsche hybrid (1900), timeline 1900–1948, Ferry Porsche quote, Porsche 356 (price, factory, chart, top speed),
"But the true revolution came in 1963", Porsche 911 (price, archival film).

## 2. Colour
Measured by median of pixel patches (sample frames in brackets).

| role | hex | notes / share |
|---|---|---|
| Highlighter yellow (label boxes, ▶, circles) | **#F6FD10** (#F6FD12 f450, #F6FE10 f515, #F7FA16 f830, #F2F90C f1250, #F3F80A f1900, #F4FF22 ▶ f180) | lemon, slightly green; ~1–4 % of frame when present; on vignetted/crumpled paper reads #E5EC21 / #D9DB2B (global vignette+grade on top) |
| Yellow offset-shadow of cut-outs | #E3EF0A (#E1EF14, #E4ED06, #EBF300, #DFE900, f1170) | hard, opaque |
| Yellow caption text over footage | ≈#E8F010 (reads #C4D053 after AA on thin strokes) | bold-italic |
| Chart line on blueprint | ≈#E0F030 core (#CDE62A sampled incl. glow) | 2px@360 |
| Warm paper (quote / 356 / 911 cards) | centre **#F3E9E0**, mid #DED5CE–#E2D9D2, corners #CFCBC2/#C2BCB5 | 100 % bg; pinkish cream |
| Cool paper (year-counter card f729–776) | centre #E9E7DB, edges #C4C4B8, corners #B9B9AD | grey-cream, stronger vignette |
| Crumpled paper (f1673–1760) | #D2C5BC / #D0C5BB | real crumpled-paper photo texture |
| Archival print page (Egger-Lohner ad) | #FAF2EB / #EBE6DD | near white |
| Dark backgrounds (timeline, chart) | #080705 / #0F0F0A / #171310 | warm near-black, faint map / blueprint linework at ~5–20 % white |
| Video-window surround (cold open) | #010101 (bottom band), blurred copy of footage elsewhere | |
| Text on yellow | near-black warm brown ≈#2B2010 | |
| Quote text on paper | **#3A292C** (warm brown-black) | never pure black |
| Year-counter numerals | #6B6361 (warm grey) | |
| "But the true revolution" text | #64574F; dashed frame #786E65 | |
| Timeline numerals | #E5E4DB → #EFECE5 with soft white glow | |
| Gold light-line (Taycan/crest draw) | core #EFDFD0, falloff #A99A89 → #817665 | warm white/gold |
| Map (cold open) | political map: ocean #7192B4, land sand/green #A6A47C/#B7B4A8 | |
| Map (Stuttgart) | physical map sand #C6BD97, #C5C498, green #ABB082; darkened to #6E7057 under portraits | |
| Red 911 | ≈#C33516 / #D32609 | only "real" red, comes from photo |

Colour rules: yellow is the ONLY graphic colour; everything else is the photo/paper. Yellow = "attention":
names, places, years, prices, the key word. Photos are B&W (archival) or graded modern footage; colour photos only for
the hero cars on paper (356 pale blue-green, 911 red) and the crest.

## 3. Typography
Font identification (no exact match possible at 360p; judged from glyph shapes):
- **Labels / captions** = **Georgia** family look (bracketed serifs, ball terminals, old-style figures in Bold Italic
  captions "356", "1.1L", "40 hp", "140 km/h (87 mph)"). Free stand-in: **Gelasio** (Google, metric-compatible with
  Georgia). Bold for labels, Italic for quote and keyword, Bold Italic for captions.
- "Porsche 356 / 911" price labels use **lining** figures in a regular-weight book serif → Georgia does not fit;
  closest free: **PT Serif** or **Source Serif 4** (regular).
- **Big years** (counter f729–776, timeline f940–1040, "1963"): high-contrast transitional/Didone serif, lining
  figures, ball-terminal 9/3/6 → free: **Playfair Display** (lining) or **Libre Caslon Display**.

| style | where | size @360 → @1080 | weight/case | colour | alignment / decoration | animation |
|---|---|---|---|---|---|---|
| Keyword | f171–341 "passion / speed / innovation / style / quality" | x-height 14 → 42px; font ≈29 → 88px (8 % H); word bbox "passion" 114×30px@360 | serif **italic** (semi-bold), lower case | white, chromatic fringe (B shifted −1px, R +1px @360) | centred at x≈320, baseline y≈325 (90 % H); yellow ▶ 17×20px@360 at x 210–227, 36px gap | slot roll from below (§6) |
| Map label | "STUTTGART" f420–479 | cap ≈28 → 84px (7.8 % H) | Georgia **Bold**, caps | #2B2010 on yellow | box x180–456 y91–144 (276×54 → 828×162@1080), padding ≈10px L/R, 13 top; down-pointing triangle tail under box centre (to y≈161) | text fades in, box wipes behind |
| Name label | "Ferdinand / Porsche" f498–529 | cap ≈19 → 57px; line pitch 30 → 90px | Georgia Bold, 2 lines, centred | dark on yellow | box x245–395 y89–152 (150×64 → 450×192) | box reveals text |
| Small name label | "Ferry Porsche" f1069–1104 | cap ≈12 → 36px | Georgia Bold | dark on yellow | box x311–440 y245–269 (130×25 → 390×75) bottom-right of photo | wipe |
| Highlight caption | "one of the first *hybrid* vehicles" f789–846 | x-height 12 → 36px; font ≈25 → 75px | roman with keyword in *italic* | dark on yellow | box x153–484 y274–304 (331×31 → 993×93), left at 24 % W, bottom at 84 % H | wipe |
| Quote | f1113–1215 | x-height 9 → 27px; asc 14 → 42px; font ≈19 → 56px; line pitch 22.7 → 68px (leading ≈1.2) | Georgia **Italic**, sentence case, straight quotes `"` | #3A292C | 4 lines **fully justified**, block x137–378 (241px → 723px, 38 % W, left edge 21 % W), top y100 = aligned with head of cut-out | word-by-word fade (§6) |
| Attribution | "-Ferdinand Anton Ernst Porsche" | x-height ≈4 → 12px | Georgia Bold, small | #3A292C | right-aligned to quote block, 1 blank line below | fade after quote |
| Price label | "Porsche 356" / "Porsche 911" f1221+, f1871+ | cap ≈21 → 63px | regular book serif | dark on yellow | box x222–417 y60–105 (196×46 → 588×138), centred at x≈320, top 17 % H | cursor + wipe, text masked by box |
| Price subtitle | "The price at launch is $3,750 / $6,500" | x-height ≈5 → 15px | regular | dark grey ≈#4A4440 | centred under box, 6px gap | letters fade in L→R |
| ▶ caption over footage | f1288–1335, f1611–1668, f1970+ | x-height ≈7 → 21px | **Bold Italic**, old-style figs | yellow | baseline y≈328 (91 % H), x from 30 (5 % W); black ▶ ≈10px | ▶ spins, line fades up |
| Year counter | f729–776 | figure height 48 → 144px (13.3 % H) | Didone-ish regular, lining | #6B6361 | centred; final year gets yellow box x228–414 y140–221 (186×81 → 558×243) | count-down (§8) |
| Timeline year | f940–1040 | figure height 39 → 117px (10.8 % H) | same Didone-ish | #EFECE5 + glow | above glowing line y212; numeral centred on ring dot | pops at positions (§8) |
| Chart labels | f1485–1594 | tick labels cap ≈7 → 21px; title cap ≈9 → 27px | serif regular, lining | white ticks; yellow title | title centred top (y≈47) | title types on |
| Title card | "But the true *revolution* / came in [1963]" f1677–1760 | cap ("B") 18 → 54px; 2 lines, pitch 33 → 99px | regular + *italic* keyword | #64574F | centred inside dashed rectangle | per-character type-on, then highlight on 1963 |

General type rules: one serif family for all running text; the **emphasised word goes italic** inside roman text
("hybrid", "revolution"); keywords in captions are lower case italic; labels are bold. No sans-serif anywhere.

## 4. Layout & composition
- Safe margins: captions start at x≈30 (5 % W) and sit on y≈328 (91 % H); labels centred horizontally.
- **Video window** (f137–341): rounded rect x80–560, y22–292 (480×270 = 75 % W × 75 % H, exactly 16:9),
  horizontally centred, top margin 6 % H, bottom 19 % H reserved for ▶ + keyword. Corner radius ≈ 11px@360
  (≈33px@1080). Behind: same footage full-bleed, scaled up, blurred, darkened (luma ~30), RGB-split.
- **Two-portrait layout** (f484–529): portraits x40–238 and x405–602 (each ≈31 % W, ≈68 % H, bottom edge y≈312),
  symmetric; the centre column holds the name label + yellow city outline on the darkened map.
- **Cut-out + quote** (f1105–1215): figure bottom-right (x382–555, cropped by frame bottom), quote block left of
  centre (x137–378). Head top and quote top share y≈100. Lots of negative paper space top/left.
- **Car on paper** (f1216–1270, f1858–1930): car side view centred horizontally at lower 55–90 % H
  (car x115–522, y200–323), label box centred at top 17–29 % H, subtitle under it. ~45 % of frame is empty paper.
- **Photo cards on paper** (carousel f1336–1484): card ≈ x80–560 × y12–336 (75 % W × 90 % H), rounded r≈8px@360,
  centred; next card waits off-screen right with ≈ 10 % W gap.
- **Dark timeline**: one horizontal rule at y=212 (59 % H), x141–491 (55 % W), centred; numeral above.
- **Blueprint chart**: axes from x≈115 to 530, y≈55 to 300 (≈65 % W × 68 % H), title centred top.
- **Title card on crumpled paper**: dashed rectangle x99–538 × y115–243 (69 % W × 36 % H), centred slightly above
  middle; dashes ≈30px long, 31px pitch, 2px thick @360 (90/93/6 @1080), corners are open (no corner dash).
- Depth/layers (max seen): bg (paper/map/blur) → photo/card (+yellow offset shadow) → highlight box → text →
  vignette/grain/grade on top.

## 5. Textures & materials
- **Paper cards are clean**: high-pass std 0.9–1.4 (JPEG noise floor); held frames differ by only 0.3–0.5/255 →
  **no animated grain / no boil** on graphic scenes. Faint grid-paper pattern (cell ≈23px@360 → ≈69px@1080,
  ±1–2 levels) + soft mottled stains near the edges of the warm paper.
- **Vignette on paper** (radial median luma from centre to corner): quote card 240 → 219 (r≈0.9) → 201 (corner),
  ≈ −16 %; year card 229 → 211 → 186, ≈ −19 %. Smooth, centred, starts at ~35 % radius. → radial gradient multiply
  0 % at r=0.35, ≈18 % darker at corners.
- **Cut-out portrait treatment** (Ferry, f1105–1215): B&W photo cut along the silhouette, with a **hard solid
  yellow offset shadow** to the RIGHT only: dx ≈ +6px@360 (**+18px@1080**), dy ≈ 0…+1, visible band 5–7px@360
  (15–21px@1080) on right-facing edges, 0 px on left edges, 1–2px AA edge, **no blur, 100 % opacity**, colour #E3EF0A.
  No dark drop shadow.
- **Photo cards on paper**: rounded corners r≈8px@360 (24@1080), same yellow offset shadow but thin: dx=dy≈+2px@360
  (6px@1080) right+bottom.
- **Portrait pair on map** (f484–529): rectangular B&W photos with thin light/olive border, map behind darkened ~40 %.
- **Archival photos/films**: B&W, mid-high contrast, some sepia; films have native grain (high-pass std 10–11 @360 on
  factory/mountain film) and luma flicker (frame-to-frame |ΔL| mean 0.4–0.85, max 3.7–8.7 levels, std of mean luma
  2–5 over a shot). This comes from the sources — no added grain detected on stills.
- **Modern footage film-look** (918 window, Taycan, crest): desaturated warm/sepia grade, strong dark corner vignette
  (Taycan floor centre #A19690 vs left edge #6F6C67 vs top corner #252420), chromatic aberration ±1px@360 (≈±3px@1080,
  blue fringe on left edges, orange on right), slight bloom. Taycan/crest footage runs partly on 2s/3s.
- **Blueprint bg**: black with faint white technical drawing of a 356 (≈10–20 % white lines), faint grid,
  white axes ≈2px@360 with ~6px glow.
- **Timeline bg**: warm near-black with a faint dark map texture (≈ +10 levels), slight vignette.
- **Crumpled paper**: photographic crumpled white sheet (strong creases, shading) — used both as wipe and card bg.
- **Cold-open map cards**: rounded video cards with ≈2px cream border and soft drop shadow, on a political world map.

## 6. Motion
Cadence (gaps between changing frames from metrics.csv, f0–1996: {1:782, 2:188, 3:127, 5:52, …}):
- **Ones**: cold-open zoom (f0–121: all 1s), map push to Stuttgart (342–403: all 1s), map labels/portraits (404–529:
  mostly 1s), crumpled-paper wipe region, ring transition, live footage.
- **Twos/threes = 12 fps** (2,3,2,3 pattern): year counter (729–776: {2:8,3:8}), quote word reveal, 356/911 label
  wipes, carousel steps, chart line + title, stepped zoom-outs on stills, Lohner/Egger reveals. → **graphics on paper
  are animated at 12 fps; camera moves on map at 30 fps.**
- Live footage at ~24 fps conformed to 30 (occasional duplicate frame, e.g. f136, f142).

Per element:
- **Opening zoom-out** f0–f116: log-zoom with exponential decay. Per-frame scale factor 0.872 (f2), 0.925 (f5),
  0.942 (f8), 0.955 (f11), 0.963 (f14), 0.968 (f17), 0.977 (f23), 0.981 (f32), 0.985 (f44), 0.990 (f50–71),
  0.994 (f74–83), 0.997 (f96), 0.9985 (f104), 1.000 (f116). Total ≈ 7.9× zoom-out in 3.9 s; f0 has a strong radial
  zoom blur. motion.py best fit easeOutExpo (rms 0.30). Video cards on the map keep playing.
- **Page curl** f122–138 (16 f, 0.53 s): map peels from bottom-right corner toward top-left, cream backside,
  accelerating (ease-in), revealing the next shot already playing.
- **▶ bullet** (f145–165): rises from below frame (y359 → 310) in 8 f (≈6.5px/frame, linear), then rotates **270°
  counter-clockwise** (up → left f156 → down f159 → right f164) over 11 f, ease-out, settles as ▶. Size 17×20px@360.
  Same spin used for the black ▶ on archival captions (f1284–1293).
- **Keyword slot roll**: word rises into a mask slot (y299–335): first pixels f171, centroid y332.5→316.8 over f172–180
  (9 f, 0.3 s), steps 3.3,2.2,3.2,2.5,1.6,1.3,1.0,0.6px → easeOutCubic, travel ≈35px@360 (105px@1080 ≈ 10 % H).
  Swap: old word exits upward f191–195 (4 f, ease-in), new word follows from below with ~1 f overlap, settles in ≈8 f.
  Words change 3–6 f BEFORE the footage cut (words f171/194/218/243/271 vs cuts f200/224/249/275).
- **Map push-in to Stuttgart** f342–f407: log-zoom 28.5× in 63 f (2.1 s); per-frame factor 1.00 (f347) → 1.033 (f357)
  → 1.063 (f369) → 1.111 (peak f383–387) → 1.067 (f395) → 1.016 (f403) → 1.000 (f407). Asymmetric ease-in-out on
  log(scale): ~40 f acceleration, ~20 f deceleration (peak at ~65 %). Motion blur during fast part.
- **City outline** (yellow, Stuttgart boundary) draws on ≈ f407–436 (~30 f) as a trim-path, ~2px@360 stroke, slight
  glow.
- **Highlighter label wipe** (general shape): a thin vertical yellow bar (the box's left edge, 4–9px@360 wide, full box
  height) appears instantly ("cursor"), then the right edge travels with a slow start, fast middle, long settle:
  - STUTTGART (ones): right edge x183→199 (f424–428), 207, 214, 224, 238, 258, 307 (f435), 377 (f436), 400, 415, 424,
    432, 439, 444, 447, 451, 453, 456 (f446) → 22 f (0.73 s), peak 70px/frame at 55–60 %. Pointer tail pops at f436.
  - Ferdinand (ones): x251 (f498) → 254, 256, 260, 264, 271, 282, 307, 355 (f506), 368, 376, 382, 385, 389, 391, 393,
    395 (f514) → 16 f, peak at 50–55 %.
  - "hybrid" caption (2s/3s): x161 (f789) → 171 (792), 185 (794), 210 (797), 268 (799), 414 (802), 447 (804),
    465 (807), 476 (809), 484 (812) → 23 f.
  - 1900 (2s/3s): x233 (f749) → 242 (752), 263 (754), 361 (757), 392 (759), 404 (762), 410 (764) … 414 (774) → ~25 f.
  - Porsche 356 (2s/3s): x231 (f1221) → 240, 252, 269, 316, 376 (f1233), 392, 403, 411, 417 (f1243) → 22 f.
  - Porsche 911 (2s/3s): x237 (f1871) → 249, 264, 293, 369 (f1881), 389, 401, 409, 416, 417 (f1893) → 22 f.
  - 1963 (ones): x340 (f1715) → 342, 346, 354, 369, 385, 393, 397, 399, 400 (f1725) → 10 f.
  ⇒ duration ≈ 10–25 f; curve ≈ easeInOutCubic/Expo with peak velocity at 50–60 %. Text either already present (map
  label, year, 1963) or revealed by the box as a mask (price labels, "Ferdinand Porsche").
- **Label exit** (STUTTGART f466–479, 13 f): box right edge retracts 456→307 (R→L) while the text/box fade; gone f479.
- **Portrait rise** f485–502: portrait slides up out of a horizontal mask at its own bottom edge (y≈312): top edge
  306, 296, 285, 270, 254, 240, 216, 190, 164, 140, 118, 104, 90, 82, 76, 70, 69, 68 → 17 f (0.57 s), travel = full
  portrait height (≈240px@360), easeInOutCubic (peak 26px/f at f491–493). Second portrait staggered **+7 f**.
- **Drafting photo move** f534–557 (after a 4 f dissolve): zoom-out 1.00→0.71 with translate (−116, +84)px@360,
  easeInOut (peak f545–548 at 3 %/frame), hold f557–560, then accelerating push-in (1.005→1.025/frame) f562–569 into
  a hard cut — "pull back to reveal, then push into the cut".
- **Stepped zoom-out reveal on stills** (12 fps, recurring): new still starts 1.7–2.0× too tight and steps out to rest:
  - Lohner photo f777–789: per-step scale 0.884 (cut), 0.961, 0.918, 0.895, 0.895, 0.930 → total 0.575 in 12 f, with
    shift toward the subject.
  - Pointing photo f662–674: 0.894, 0.875, 0.875, 0.915, 0.978 → ≈0.58 in 12 f.
  - Egger-Lohner page f892–907: 0.973, 0.941, 0.910, 0.887, 0.873, 0.880, 0.903 → 0.49 in 15 f (anchor top-left:
    content moves (−206, −120)px@360), revealing a photo collage to the right.
  - Carousel first card f1336–1348: steps at f1338, 1341, 1343, 1346, 1348 = 0.965, 0.865, 0.782, 0.903, 0.973 → 0.57.
  Step sizes are small-large-small → eased (inOut) but rendered in 2–3-frame holds, no motion blur.
- **Ken Burns on held stills**: very little. Lohner photo after its reveal: slow push-in +4.4 % over f792–846
  (1.8 s) ≈ **+2.4 %/s, linear**. Quote card, Ferry photo, Egger hold, 356/911 cards: static (±0.2 %).
- **Cut-out figure entrance** f1105–1119: figure (with yellow shadow) scales DOWN ≈1.6→1.0 and moves right/down
  (bbox x205→382, y26→104) in 14 f (0.47 s), speed peak f1111–1112 (easeInOutQuad). Quote starts appearing at f1113
  while the figure settles.
- **Quote word reveal** f1113–1153: words appear one at a time every ≈2.5 f (12 fps), each fading 25 %→100 % over 3–5 f
  with slight upward settle/blur; 4 lines + attribution in ≈40 f (1.33 s) for 20 words.
- **Car slide-in** (356, f1216–1223): car side view enters from the right and settles x177→129→117→115 (ease-out, 7 f).
- **Price subtitle**: letters fade in L→R behind the label wipe, f1226–1241 (≈1 char/frame).
- **Timeline numeral/dot** (f940–1040): each year appears at a new x on the line (fade-in 1–2 f), holds 5–8 f, fades
  out, sometimes 1–3 blank frames; final "1948" slides right→centre x427→380→347→324→319 over f1014–1024 (ease-out).
- **Photo card slide-in over timeline** f1039–1049: card left edge 472 → 289 → 214 → 191 → 189 (ease-out, 10 f, 2s/3s).
- **Drawn circle** f1049–1066 (17 f): yellow ring drawn clockwise from ~11 o'clock around Ferry's head; erased
  (un-drawn) f1096–1104 (8 f) just before the cut.
- **Carousel slide** (every 20 f = 0.667 s at f1361, 1381, 1401, 1421, 1441, 1461): strip moves left one card
  (≈545px@360, 85 % W) in 7 f on 2s/3s: new card left edge 640→625 (+0) → 367 (+2) → ~110 (+5) → 80 (+7). Ease-in-out,
  no blur.
- **Chart** f1485–1558: axes visible at f1485; yellow line draws L→R x118→527 in 73 f (2.43 s), ≈5.6px/frame,
  near-linear (follows data), on 2s/3s; title types on f1490–1525 (≈1 char / 1.2 f). Hold to f1588, slight drift/push
  f1588–1594, cut f1595.
- **▶ caption over footage** (f1284–1300): black ▶ spins into place (f1284–1293), whole caption line fades in over 5 f
  (f1292–1296) with ~2px upward drift.
- **Title card type-on** (crumpled paper): line 1 "But the true revolution" types f1677–1700 (≈1 char/frame, chars
  pop in), line 2 f1701–1713, then 1963 highlight wipe f1715–1725.
- **Photo strip push** (f1801–1813): next archival photo slides in from the right in 1–2 f (seam x389 at f1801), cut to
  a 3-photo strip whose seam eases 556→538→508→499→494→491 (f1806–1811, ease-out). Similar push f1853–1856.

## 7. Transitions
| frames | type | details | count in range |
|---|---|---|---|
| f122–138 | **page curl** | bottom-right corner peels to top-left, cream back, ease-in, 16 f | 1 |
| f200, 224, 249, 275, 342, 570, 594, 690, 729, 939, 1105, 1271, 1336, 1485, 1595, 1761, 1858 | **hard cut** | dominant transition; editorial cuts ≈ every 1.5–4 s | ≈18 |
| f529–533 | cross-dissolve | portrait/map scene → drafting photo, 4 f | 1 |
| f620–650 / f654–662 | fade-up / staggered dissolve | crest fades in on 12 fps over ~30 f; then footage → archival photo 8 f dissolve with crest fading ~4 f later | 1 |
| f774–777 | pre-lap dissolve + cut | photo appears at ~30 % over year card for 3 f, then hard cut | 1 |
| f777–789, 662–674, 892–907, 1336–1348 | stepped zoom-out reveal | see §6; reads as a series of rapid reframes (the cut detector flags each step) | 4 |
| f847–852 | cross-dissolve | Lohner photo → Egger page, 5 f | 1 |
| f1039–1049 | slide-in (push over) | photo card from right over the timeline, 10 f | 1 |
| f1213–1216 | nudge + cut | quote card shifts −8px then cuts to car on the same paper (bg continuous) | 1 |
| f1361…1466 | carousel slide | 7 f per card, every 20 f | 6 |
| f1657–1684 | **crumpled-paper wipe** | crumpled white sheet pushed up from frame bottom in stop-motion steps (f1657 edge appears, f1662, 1666, 1669, 1673, 1677, 1680, 1684), covering footage bottom→top; the sheet itself becomes the title card. 27 f, steps every 2–5 f | 1 |
| f1801–1813, 1853–1858 | photo-strip push | new photo pushes in from right, ease-out 5–7 f | 2 |
| f1931–1950 | **ring focus transition** | 3 concentric thin white rings (1px@360, ~80 % white) appear centred, grow (outer r 96→124px@360, f1931–1938) while the card blurs and cross-dissolves to blurred film (9 f), then film racks into focus f1940–1946 while rings collapse to the centre (outer r 124→117→101→97→82→31→14→10, f1938–1949) and vanish f1950 | 1 |

## 8. Recurring devices
- **Highlighter label box**: opaque yellow rectangle behind dark serif text, square corners, padding ≈ 0.35–0.5 × cap
  height; optional down-pointing triangular tail (map callout). Animates cursor-then-wipe (§6), exits by R→L retract.
- **Highlighter on print**: same yellow swiped over a word in an archival page (EGGER-LOHNER, f857–882: left edge 20,
  right edge 47 (f857) → 54, 72, 98, 142, 253 (f869), 586 (f872) … 592 (f882); ≈25 f, overshoots the word slightly).
- **Yellow ▶ bullet** before keyword (cold open) / black ▶ before captions on archival film; spins 270° CCW into place.
- **Yellow offset shadow** behind cut-outs and photo cards (hard, right/down offset, no blur).
- **Drawn yellow circle**: hand-drawn ring (2 overlapping slightly offset strokes, ~4–5px@360 total), around a face,
  draw-on 17 f, hold, un-draw 8 f.
- **Year count-down card**: numeral steps backwards on 12 fps: 2024, 2018, 2007, 1994, 1980, 1965, 1951, 1936, 1923,
  1911, 1903, 1900 at f729, 732, 734, 737, 739, 742, 744, 747, 749, 752, 754, 757 (deltas 6, 11, 13, 14, 15, 14, 15, 13,
  12, 8, 3 → ease-in-out on value). Numeral scales in 0.79→1.0 over the first 3 steps (h38→45→48px). Highlight cursor
  appears at f749 while still counting; box wipes in as it lands on 1900.
- **Glowing timeline**: thin bright rule (2px@360 core, ±6px glow) on dark map; small ring-dot (≈6px@360) under the
  current year; years 1900, 1902, 1907, 1919, 1924, 1931, 1933, 1936, 1938, 1940, 1943, 1945, 1948 pop at varying x
  (dot jumps with them), ≈7 f per year; final 1948 slides to centre.
- **City outline + map callout**: yellow polygon outline (trim-path draw) on a physical map, plus label with tail.
- **Price card**: car side-view cut-out on warm paper + yellow name label + small grey price line.
- **Photo carousel on paper**: rounded photo cards with yellow offset shadow, horizontal strip, step-advance every 20 f.
- **Blueprint line chart**: white serif axes on technical-drawing bg, yellow data line drawn L→R, yellow title typed.
- **Dashed frame title card** on crumpled paper with one italic word and a highlighted year.
- **Gold light-streak drawing**: a short comet-like warm-white line (core #EFDFD0) traces car/crest outlines over
  modern footage (Taycan f571–593, crest f594–620) before the crest fades in.
- **Keyword montage window**: footage inside rounded 75 % window over its own blurred copy, ▶ + italic word below.

## 9. Scene log
| frames | time | on screen | devices | motion / transition |
|---|---|---|---|---|
| f0–121 | 0.00–4.03 | colour political world map, ~10 rounded video cards (traffic footage) | map, video cards | log zoom-out ≈7.9× easeOutExpo (radial blur f0) |
| f122–138 | 4.07–4.60 | page curl reveals Porsche 918 on bridge | page curl | 16 f |
| f138–199 | 4.6–6.6 | 918 in rounded window over blurred copy; ▶ rises+spins; "passion" | keyword montage | ▶ f145–165, word f171–180 |
| f200–341 | 6.7–11.4 | 918/911/… clips, words "speed", "innovation", "style", "quality" | keyword montage | cuts f200/224/249/275, word swaps lead cuts by 3–6 f |
| f342–403 | 11.4–13.4 | physical Europe map, log push-in to SW Germany | map | 28.5× in 63 f, asymmetric ease |
| f404–483 | 13.5–16.1 | Stuttgart: yellow city outline, "STUTTGART" callout label | outline, label | draw-on ~30 f; label wipe f424–446; exit f466–479 |
| f484–529 | 16.1–17.6 | two portraits of Ferdinand Porsche rise; "Ferdinand Porsche" label; map darkened | portraits, label | rise 17 f, stagger 7 f; wipe f498–514 |
| f529–569 | 17.6–19.0 | archival photo: F. Porsche at drafting board | — | 4 f dissolve; pull-back easeInOut f534–557; push-in to cut |
| f570–593 | 19.0–19.8 | Taycan in studio, film look, gold light streaks | light-line | cut |
| f594–653 | 19.8–21.8 | PORSCHE lettering close-up; gold line draws shield; crest fades in | crest | cut; fade ~30 f on 12 fps |
| f654–689 | 21.8–23.0 | archival photo: F. Porsche pointing at drawing | stepped zoom-out | 8 f dissolve, punch-out f662–674 |
| f690–728 | 23.0–24.3 | archival film: F. Porsche in garden | — | cut |
| f729–776 | 24.3–25.9 | cool paper card, year count-down 2024→1900, yellow box on 1900 | year counter, highlight | 12 fps steps |
| f774–846 | 25.8–28.2 | archival photo Lohner-Porsche car; caption "one of the first *hybrid* vehicles" | highlight caption | pre-lap 3 f + cut; stepped zoom-out f777–789; push +2.4 %/s |
| f847–938 | 28.2–31.3 | Egger-Lohner print advert; highlight on EGGER-LOHNER; zoom-out reveals collage of archival photos at right | print highlight | 5 f dissolve; wipe f857–882; stepped zoom-out f892–907 |
| f939–1038 | 31.3–34.6 | dark map bg, glowing timeline 1900→1948 | timeline | cut; year pops ~7 f each |
| f1039–1104 | 34.6–36.8 | photo of Ferdinand & Ferry slides in; yellow circle on Ferry; "Ferry Porsche" label | circle, label | slide 10 f; circle f1049–1066; label f1069–1091; un-draw f1096–1104 |
| f1105–1215 | 36.8–40.5 | warm paper, cut-out Ferry w/ yellow offset shadow; justified italic quote + attribution | cut-out, quote | cut; scale-in 14 f; word reveal 40 f |
| f1216–1270 | 40.5–42.3 | 356 side view on paper; "Porsche 356" label + "The price at launch is $3,750" | price card | car slide 7 f; label wipe f1221–1243 |
| f1271–1335 | 42.4–44.5 | archival factory film (356 bodies); black ▶ + yellow "Porsche 356 featured a 1.1L flat-four engine producing 40 hp." | ▶ caption | cut; ▶ spin f1284–93; fade f1292–96 |
| f1336–1484 | 44.5–49.5 | photo carousel: 6 archival 356 photos as rounded cards on paper | carousel | stepped zoom-out f1336–48; slides every 20 f |
| f1485–1594 | 49.5–53.1 | blueprint-bg line chart "Porsche 356 units manufactured", 1948–1965, 0–76000 | chart | cut; line 73 f; title typing |
| f1595–1668 | 53.2–55.6 | archival film: 356 on mountain road; ▶ "Porsche 356 had a top speed of around 140 km/h (87 mph)." | ▶ caption | cut; ▶ f1611–19, text f1619–27 |
| f1657–1684 | 55.2–56.1 | crumpled paper pushed up over the footage | paper wipe | stop-motion steps |
| f1673–1760 | 55.8–58.7 | crumpled paper, dashed rectangle, "But the true *revolution* / came in [1963]" | dashed frame, highlight | type-on f1677–1713; highlight f1715–1725 |
| f1761–1855 | 58.7–61.8 | archival photos: design office (men at drafting tables); three men in suits holding drawings (identities not captioned) | photo strip | cut; push f1801–1813, f1853–56 |
| f1856–1930 | 61.9–64.3 | red 911 side view on paper; "Porsche 911" label + "$6,500" | price card | cut; wipe f1871–1893 |
| f1931–1949 | 64.4–65.0 | concentric rings + blur dissolve to 911 hood film | ring focus transition | 19 f |
| f1950–1996 → | 65.0–66.5 → | archival 911 film (greenish mono), black ▶ + yellow "Porsche 911 had a top speed of around 210 km/h (130 mph)" | ▶ caption | **continues into agent B's range (f1997+)** |

## 10. Replication recipes
```js
// 0. Global
const FPS = 30; const GFX_STEP = [2,3]; // graphics on paper: hold frames alternating 2,3 (= 12 fps)
const YELLOW = '#F6FD10', INK = '#2B2010', QUOTE_INK = '#3A292C', PAPER = {center:'#F3E9E0', edge:'#DED5CE', corner:'#C8C2BA'};
const SERIF = {label:'Gelasio 700', quote:'Gelasio italic 400', caption:'Gelasio italic 700', price:'PT Serif 400', years:'Playfair Display 400 lnum'};
// paper vignette: radial gradient multiply, 0% at r=0.35, -18% luminance at corners. No animated grain on graphics.
// stepped motion helper: sample the eased value only on frames where (frame - start) hits the 2,3,2,3 pattern; hold otherwise.

// 1. Highlighter label (cursor + wipe)
label = { box:{fill:YELLOW, radius:0, padX:0.4*capH, padY:0.45*capH}, text:{font:SERIF.label, color:INK},
  tail:{type:'triangle-down', w:0.35*boxH, h:0.3*boxH, popAt:0.6} /* map callouts only */,
  in:{ cursorW:0.012*W /*~23px@1080*/, cursorFrames:2..5 /*bar alone, may grow slowly*/,
       wipe:{dur:16..25 frames, ease:'easeInOutCubic' /*peak velocity at 55%*/, cadence: onPaper?GFX_STEP:'ones'},
       textMode: 'maskedByBox' /*price, names*/ | 'preFade' /*map label: text fades in 5f before the bar*/ },
  out:{ retractRightToLeft:true, dur:13, ease:'easeInCubic' } };

// 2. Stepped zoom-out reveal for any new still
reveal = { startScale:1.75..2.0, endScale:1.0, dur:12..15, anchor:'subject' /*or top-left for pages*/,
  ease:'easeInOutQuad', cadence:GFX_STEP, motionBlur:false };   // then optional KB push +2.4%/s linear

// 3. Cut-out portrait with yellow offset shadow
cutout = { photo:'B&W matte', shadow:{color:'#E3EF0A', dx:+18, dy:+2 /*@1080*/, blur:0, opacity:1} ,
  in:{ fromScale:1.6, fromOffset:[-0.28*W, -0.22*H], dur:14, ease:'easeInOutQuad', cadence:'ones' } };
photoCard = { radius:24, shadow:{color:YELLOW, dx:6, dy:6, blur:0} /*@1080*/ };

// 4. Justified italic quote, word-by-word
quote = { font:SERIF.quote, size:56, leading:68, color:QUOTE_INK, align:'justify', width:0.38*W, left:0.21*W,
  topAlignedTo:'cutout head', perWord:{every:2.5 /*frames, on 12fps*/, fade:[0.25,1], dur:4, rise:6},
  attribution:{font:'Gelasio 700', size:18, align:'right', delayAfterQuote:6} };

// 5. Keyword montage (cold open)
window = { rect:[0.125*W, 0.061*H, 0.75*W, 0.75*H], radius:33, bg:'same clip, scale 1.15, blur 20px, brightness 0.35, RGB split ±3px' };
keyword = { font:'Gelasio italic 600', size:88, color:'#FFF', chroma:{b:-3, r:+3}, baselineY:0.90*H,
  bullet:{shape:'▶', size:[51,60], color:YELLOW, gap:108, enter:{riseFromBottom:true, dur:8, then:'rotate -270deg', rotDur:11, ease:'easeOutCubic'}},
  roll:{slotMask:true, travel:105, in:{dur:9, ease:'easeOutCubic'}, out:{dur:4, ease:'easeInCubic', dir:'up'}, leadCut:4} };

// 6. Log-scale map zooms
mapZoomIn  = { total:28.5, dur:63, interp:'log', ease:'asymmetric inOut (accel 65%, decel 35%)', blur:'motion/zoom blur ∝ dlog(s)/dt' };
mapZoomOut = { total:1/7.9, dur:116, interp:'log', ease:'easeOutExpo', startRadialBlur:true };
cityOutline = { stroke:YELLOW, width:6 /*@1080*/, glow:{r:6, a:0.4}, trimPath:{dur:30, ease:'easeInOutSine'} };

// 7. Year count-down card
yearCounter = { font:SERIF.years, figH:144 /*@1080*/, color:'#6B6361', bg:'cool paper #E9E7DB + vignette',
  values:[2024,2018,2007,1994,1980,1965,1951,1936,1923,1911,1903,1900], frames:[0,3,5,8,10,13,15,18,20,23,25,28],
  scaleIn:{from:0.79, steps:3}, highlight:{startAtIndex:8, box:[558,243]/*@1080*/, wipe:'recipe 1'} };

// 8. Glowing timeline on dark map
timeline = { bg:'#0C0B08 + faint map 6%', line:{y:0.59*H, x:[0.22*W,0.77*W], core:'2px→6px@1080 #F0EBE0', glow:18},
  dot:{ring:18 /*@1080*/}, year:{font:SERIF.years, figH:117, color:'#EFECE5', glow:'0 0 12px rgba(255,255,255,.35)'},
  sequence:[1900,1902,1907,1919,1924,1931,1933,1936,1938,1940,1943,1945,1948], hold:5..8, fade:1..2, gapFrames:0..3,
  finale:{slideToCenter:true, dur:10, ease:'easeOutCubic'} };

// 9. Photo carousel on paper
carousel = { card:[0.75*W, 0.88*H], gap:0.10*W, advanceEvery:20, slide:{dur:7, ease:'easeInOutCubic', cadence:GFX_STEP},
  firstCardReveal:'recipe 2' };

// 10. Blueprint line chart
chart = { bg:'black + white blueprint drawing 12% + grid', axes:{color:'#FFF', w:6 /*@1080*/, glow:18, labels:'serif lnum 21px'},
  line:{color:YELLOW, w:6, glow:9, drawDur:73, ease:'linear', cadence:GFX_STEP}, title:{color:YELLOW, typeOn:'1 char / 1.2 f'} };

// 11. Ring focus transition (card → footage)
rings = { radii0:[288,90,30] /*@1080, approx*/, stroke:3, color:'rgba(255,255,255,.8)',
  phase1:{dur:7, grow:1.3, crossBlur:'A blur 0→20px, dissolve to B (blurred) over 9f'},
  phase2:{dur:12, collapseTo:0, ease:'easeInCubic', rackFocusB:'20px→0 over f+9..f+15'} };

// 12. Crumpled-paper wipe → title card
paperWipe = { asset:'photo of crumpled white sheet, ragged top edge', from:'bottom', steps:[0,5,9,12,16,20,23,27], cadence:'stop-motion holds 2–5f',
  becomes:{card:'crumpled paper bg', frame:{dash:[90,93], w:6, color:'#786E65', openCorners:true, rect:[0.69*W,0.36*H]},
           text:{typeOn:'1 char/frame', italicWord:'revolution', highlight:'recipe 1 on year, 10f, ones'}} };

// 13. Page curl (cold open → montage): corner peel from bottom-right, 16 f, easeInQuad, cream backside, soft shadow.
```

## 11. Uncertainties
- **Exact typefaces**: 360p source; Georgia family is a strong guess for labels/quote/captions (old-style figures in
  bold-italic captions), but price labels have lining figures (different face, maybe PT Serif/Source Serif), and the big
  years are a high-contrast face I could not pin down (Playfair/Didot-like).
- Yellow tone varies with grade/vignette (#E5EC21–#F7FA16); whether boxes use a multiply blend on paper is unclear
  (crumpled-paper 1963 box looks flat → probably normal blend at ~90–100 %).
- Map push-in and cold-open zoom are probably zooms through a pre-rendered or tiled map; sub-pixel scale numbers
  from per-frame matching have ±1–2 % error at high speed (motion blur).
- Quote word-reveal: could be per-word opacity or a soft L→R mask moving word by word — at 12 fps both look alike.
- The gold light-line drawing on the Taycan/crest is likely part of a stock "logo reveal" template (light streak +
  crest fade) — parameters only approximate.
- Grain: no synthetic grain/boil detected on graphic scenes (held frames identical within JPEG noise); film grain on
  archival material is native. If the original had a subtle animated grain, it was lost in compression.
- Carousel slide positions between steps were read from edges/thumbnails, ±10px@360.
- Exact page-curl geometry and crumpled-paper wipe are probably stock overlays (After Effects CC Page Turn / a filmed
  paper element) rather than procedural.
- Scene f1931–1996 continues into agent B's range (911 archival film + caption); the ring transition and caption
  fade belong to my range, the rest of the 911 sequence to B.
