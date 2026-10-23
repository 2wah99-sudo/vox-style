# v3_v4_short: notes for v3_mdriturana + v4_schaapening

Conversions: v3 is 736x414, so ×2.609 gives px@1080. v4 is 714x408, so ×2.647 gives px@1080.
All frame numbers are 0-indexed source frames. v3 runs at 24 fps and v4 at 30 fps.
Every number below comes from pixel sampling or tracking (scripts are in `$VOX/tmp/v3_v4_short/`): NCC template matching with a scale search (`scalematch.py`, `zoomtrack.py`), sub-pixel SSD tracking (`track.py`), blob detection (`blobs.py`) and change heatmaps (`heat.py`).

---

## 1. Overview

**v3 (mdriturana)**: one continuous 15.2 s shot (364 f @24 fps, no cuts). It is a "postcard" collage for the city of Rangpur. A white colonial palace photo cut-out sits on crumpled off-white paper, framed by a thick **yellow outline**. A huge flat **yellow sun disc** stands behind the dome and a flock of black bird silhouettes flies past. Full-colour photo cut-outs of a truck, a cycle-rickshaw and a CNG auto-rickshaw sit in the foreground, each with a **white sticker border**. A green Bengali title রংপুর types on at the top right.
- The motion is smooth and on ones. A 3D-style **camera dolly-out** runs f0→f99 with real parallax between layers, so the vehicles are "revealed" rising from the bottom edge. The sun scales up from behind the dome.
- After the camera stops, every cut-out keeps a slow independent **wiggle drift** of 1–3 px. This drift, not a texture boil, accounts for the 57% "local" frames.
- Style family: bright, saturated, sticker-like travel collage. It has no stop-motion stepping and no grain.

**v4 (schaapening)**: 10.5 s at 30 fps in 3 shots: roadside cafe, jukebox and radio.
- The look is a monochrome scrapbook: near-white paper, grey **grid-paper** and **newsprint** scraps with torn edges, and B&W photo cut-outs with only small spot colours. Those are a blue-sky photo inside a torn shape, mint-tinted jukebox tubes, **condensed bold caps** (blue "JUKEBOX", teal "RADIO"), a red hand-drawn **X**, and black newsprint **lightning-bolt** doodles with flickering zap squiggles.
- All animation is **posterised stop-motion**: 12 fps steps in shot 1 and 8 fps steps in shots 2–3, never on ones.
- Each shot starts on a hard cut with the hero object oversized, then settles with a stepped **easeOutExpo zoom-out**.
- A faint white "Vox" logo watermark sits top-right.

**Shared:** cut-out photography on paper, centred hero compositions, oversized type used as a graphic layer, layers that keep moving slightly after landing (never a dead freeze), and entrances that are mostly slides/zooms with strong ease-out and no overshoot.

---

## 2. Colour

### v3
| role | hex (sampled) | share / notes |
|---|---|---|
| paper background (crumpled) | #DFE0DB (range #D0D1CB–#E9EAE6, luma 189–238, σ≈7) | ≈50% of frame. Neutral warm grey-white with no hue cast. |
| sun disc | **#F6E50D** (flat, no gradient) | ≈7% |
| palace outline | **#F6E916** (≈ same yellow as the sun) | thin band |
| palace photo | greys #7E8087 / #8F8D88, warm right wing #DCCCB8; low saturation but still colour (the flag is red/green) | ≈25% |
| vehicle sticker border | #FFFFFF | |
| title text | **#26873A** (dark core #217E33) | ≈2% |
| birds | ≈#1C1B17 near-black (dark core rgb 41,37,6) | small |
| vehicles | saturated photo colours: truck yellow ≈#EDC720, blue bed, rickshaw red/green/yellow, CNG green ≈#2E3936 | ≈20% |

Rules for v3:
- Yellow is the single accent. It is used **only** for the sun and the outline of the main landmark, which ties the landmark to the sun.
- The green title colour echoes the green on the CNG and rickshaw (and the Bangladesh flag).
- Saturated colour is reserved for foreground "life" objects (vehicles). The landmark stays near-greyscale.

### v4
| role | hex | notes |
|---|---|---|
| white paper | **#FEFCFF** (shot 1), #F6F4F7 (shot 2) | slight lilac cast (B ≥ R > G). It dominates: palette #FCFAFD 24% + #F7F5F8 17% + #F0EFF3 13% |
| grid paper | cells #E2E0E3, lines ≈#C8C6CA down to luma ~40 where lines are dark | cell ≈13 px@408 (≈35 px@1080) |
| newsprint scraps | light grey #D1D1D6 with grey text | top-right and bottom-left in shot 2; bottom-left in shot 3 |
| B&W photo cut-outs | full greyscale range, blacks #232225 / #39383C | cafe, jukebox, radio |
| sky photo inside torn shape | **#8ABFF9** | the only "natural" colour in shot 1 |
| jukebox tube tint | #90C0BF (hand-tinted mint on B&W) | |
| "JUKEBOX" letters | **#5C5CD0** (#5959C7–#5C5CD0) | opaque |
| "RADIO" letters | **#7FCCCD** over white; #72B4B3 over grid | multiply/translucent (grid lines show through, see §5) |
| red X | sampled #C15561 core (thin JPEG-smeared strokes); probably ≈#D44A55 originally | multiply blend |
| lightning bolts | dark #413E41 with light newsprint stripes, or flat light grey ≈#C8C8C8 | |
| "Vox" watermark | white at ~70–80% opacity | |

Rules for v4:
- Overall saturation is 0.057 (very low). Each shot gets **one** spot colour for its type: blue for JUKEBOX, teal for RADIO.
- Red is used only for the hand-drawn mark.
- Photos are B&W, except one tinted element per shot (sky, jukebox tubes).

### Shared
- Paper is near-neutral off-white, with a warm grey in v3 and a cool lilac white in v4.
- Accents are flat, fully saturated spot colours with no gradients.
- There are no vignettes and no colour grading on the paper.

---

## 3. Typography

### v3: Bengali title "রংপুর" (Rangpur)
- Typeface: bold Bengali sans with rounded, heavy strokes. Candidates are **Hind Siliguri Bold**, **Noto Sans Bengali Black** and **Baloo Da 2 ExtraBold**. The exact face is unknown.
- Colour #26873A. It is flat, with no outline, shadow or box.
- Size: the matra (headline) to baseline is **49 px@414 = 11.8% H ≈ 128 px@1080**. The bbox including the dot below and the u-kar is 125×59 px (17% W × 14.3% H ≈ 326×154 px@1080).
- Position: bbox x 498–623 / y 76–135 → left edge at **67.7% W**, top at **18.4% H**. The title floats in the empty paper top-right, between the sun and the right tower.
- Animation (per grapheme cluster, three clusters: রং, পু, র):
  - Each cluster slides **up** and **fades in** over **5 frames (0.21 s)**.
  - Top edge below its final position by frame: >55 px, 47, 38, 27, 0 px@414. The start offset is ≈13% H, about 1 glyph height (≈143 px@1080).
  - Opacity by frame: ≈0.13, 0.24, 0.40, 0.71, 1.0.
  - Both curves **accelerate** (ease-in) and land with a hard stop, with no overshoot.
  - Starts: রং f104 (lands f108), পু f114 (f118), র f125 (f128). That is a **10–11 frame stagger (0.42–0.46 s)**. The whole word takes f103→f128 (1.04 s), right after the camera stops (f99).
- The text never moves after landing. It is excluded from the idle wiggle.

### v4: display caps "JUKEBOX" (blue) and "RADIO" (teal)
- Typeface: condensed bold grotesque, all caps. It has straight-legged R, rounded-rectangle O and flat terminals. Closest free fonts are **Oswald SemiBold/Bold** or **Bebas Neue**; the original may be Trade Gothic Bold Condensed No. 20 or Knockout.
- Tracking is wide and irregular because letters are placed individually, like a ransom-note collage.

**JUKEBOX:**
- Cap height ≈111 px@408 = **27% H ≈ 294 px@1080**. Letter width ≈68 px (≈180 px@1080), aspect ≈0.6.
- Colour #5C5CD0, opaque.
- The word spans the **full frame width and bleeds off both edges**: J is cut by the left edge and X ends at 687/714.
- The jukebox photo sits in the middle and covers the gap between E and B. E is half hidden behind the jukebox.
- The baseline is bouncy. Letter tops sit at y 91 / 114 / 113 / 128 / 142 / 132 / 153 (±30 px ≈ ±7% H), and each letter tilts 0–8°.

**RADIO:**
- Cap height **89 px@408 = 21.8% H ≈ 236 px@1080**. Word bbox x 363–627 (37% W), y 77–188. Letters ≈50–55 px wide.
- The word is tight and almost evenly baselined: tops at 77–103, a 26 px stagger rising toward the left.
- Colour #7FCCCD, multiply. The word sits **behind** the radio cut-out.

Animation:
- JUKEBOX: letters slide in horizontally (see §6).
- RADIO: letters assemble from a scattered, rotated, lower position (see §6).
- Neither word uses fades.

Note: the shop signage in the cafe photo ("ROADSIDE", "CAFE", "BENTON'S CAFE") is part of the photo, not live type.

**Shared:** one big word per scene, set as a graphic object. It is either a local-language place name (v3) or a label for the hero object (v4). Neither clip has body copy, subtitles or lower-thirds.

---

## 4. Layout & composition

### v3 (final layout, f150+)
Everything is centred on the vertical axis x ≈ 50% W, stacked as a pyramid:
1. Sun disc: centre (49.9% W, 37% H), diameter 50% H (≈537 px@1080). Its top is at 12% H. The lower ~35% of the disc is hidden behind the palace.
2. Palace cut-out with outline: x 9.6–93.8% W, y ≈20.5% (spire) to ≈80% H.
3. Vehicles cluster: x ≈18–80% W, y 50% H to **bleeding off the bottom edge**. In front, the truck is left-of-centre, the rickshaw is dead centre and front-most, and the CNG is right-of-centre and behind.
4. Title: top-right negative space at 68–85% W, 18–33% H.
5. Birds: a scatter of ≈14 in the sky band, x 28–66% W, y 7–30% H, overlapping the sun.

- Margins: about 10% W left and 6% W right to the palace outline. There is no bottom margin, because the vehicles bleed off.
- Negative space is the top-left and top-right corners of paper (≈25% of frame).
- Depth order, back to front: paper → sun → palace (+yellow outline) → birds → title → CNG → truck → rickshaw.
- Scale relations: palace width ≈84% W; sun diameter ≈ ⅓ of the palace width; vehicles ≈ ½ the palace height each.

### v4
- **Shot 1 (cafe):**
  - Cut-out composite centred: x 12–81% W, y 6–86% H.
  - The left half is a white torn-paper sheet. A grid-paper sheet is visible on the right ~15% W, with a ragged vertical torn edge.
  - Lightning bolts flank the sign: grey at the left (21–29% W, 26–38% H), black at the right (58–67% W, 28–43% H).
- **Shot 2 (jukebox):**
  - Jukebox centred (x 38–62% W, centre 50.4% W), **80% H tall**, top at 10% H.
  - The letter row crosses the frame at 22–65% H and bleeds off both sides.
  - Behind it are a horizontal torn grid-paper band (y 30–70% H) and newsprint scraps at the top-right (x 68–100%, y 0–30%) and bottom-left/bottom edge.
  - A bolt sits above-left of the jukebox at 28–38% W, 2–20% H.
- **Shot 3 (radio):**
  - Radio dial cut-out centred low: centre (46% W, 61% H), width ≈60% W.
  - It sits on a torn black paper backing (ragged top edge) plus a newsprint scrap at the bottom-left.
  - RADIO word sits upper-right of the radio, with the X immediately left of the R.
  - Bolt pair at the top-left (8–21% W, 13–38% H).
  - Background: grid paper on the left ~55% W (torn right edge), white paper on the right.
- Depth order (shot 3): paper/grid → RADIO letters → torn black backing + newsprint → radio photo. The bolt and X sit on top of the paper. JUKEBOX letters are behind the jukebox.
- Watermark: top-right at x 646–704, y 22–43 px. That is right margin 1.4% W and top margin 5.4% H.

**Shared:**
- Centred hero object with ≥60% frame coverage.
- Type is giant and allowed to bleed off-frame.
- Foreground objects bleed off the bottom edge.
- Doodles fill the upper-left/upper-right quadrants.

---

## 5. Textures & materials

### v3
- **Paper:** crumpled off-white paper scan with soft crease shading. Luma is 189–238 (σ≈7) and there is no visible fibre grain. It is static after f99 (frame diff 0.00), so there is **no paper boil and no animated grain/flicker**. There is no vignette: corner medians are #E0E1DD / #D9DAD5 / #E1E2DD / #DFE0DA.
- **Palace cut-out:** clean photo silhouette. The outline is a **solid yellow #F6E916 stroke, 5 px@414 (≈13 px@1080, 1.2% H)**, outside only.
  - It hugs the silhouette with rounded joins and slightly smoothed corners.
  - The edge is 1 px anti-aliased, with **no gap** between photo and stroke.
  - There is **no drop shadow**: paper luma right outside the stroke equals the paper elsewhere.
- **Vehicle cut-outs:** **white #FFFFFF sticker border, 5–6 px@414 (≈13–16 px@1080)**, outside only, rounded. There is no drop shadow (paper next to the border is ≤3 luma darker, which is negligible).
- **Sun:** perfectly flat vector disc with no texture and no outline.
- **Birds:** flat black silhouettes (stock flying-flock footage, keyed).
- **Title:** flat vector fill.
- No halftone, no scan artefacts, no light leaks.

### v4
- **White paper** #FEFCFF: almost texture-free. Its torn edges show soft white fibre.
- **Grid paper:** cells ≈13.3 px@408 (≈35 px@1080) with thin grey lines. In shot 1 it is rotated ≈15–20°. It appears as whole sheets with ragged torn edges and as torn horizontal strips.
- **Newsprint scraps:** greyscale printed columns and headlines, cropped by the frame, with straight or torn edges.
- **Torn black paper:** backing behind the radio. It has a jagged torn top edge with a lighter fibre rim (~2 px).
- **Photo cut-outs** (cafe, jukebox, radio): B&W, contrasty, with clean hard-cut edges. They have **no outline and no drop shadow**. The cut-outs stand out because they sit on backing paper (newsprint under the cafe, black torn paper under the radio).
- **Colour inside a torn shape:** the cafe sits in front of a **torn-edge colour sky photo** (#8ABFF9 sky with clouds and mountains). It is a classic "colour window in a mono collage" device.
- **Hand-tinting:** the jukebox tubes are mint #90C0BF on B&W, and the "16" on the radio dial is teal at the start of shot 3.
- **Lightning bolts:** cut from **inverted newsprint**, i.e. black with light diagonal text stripes. There are also flat light-grey bolts. In shot 3 each black bolt has a pale-grey duplicate shape slightly offset behind it (paper backing).
- **Blend modes:**
  - RADIO letters are multiplied: over grid the fill drops from #7FCCCD to #72B4B3 and luma σ rises from 2 to 8.5, because the grid lines show through.
  - The red X is multiplied: where it crossed the teal R (f235–243) the stroke turned near-black.
  - JUKEBOX blue reads as opaque (luma σ 2.5–5 everywhere).
- No animated grain. 68% of frames are exact holds, so there is no per-frame noise.

**Shared:**
- The paper ground is mostly flat and static.
- Cut-outs are separated from it either by a **solid coloured or white offset-free stroke** (v3) or by **backing scraps** (v4). Neither clip uses soft drop shadows.

---

## 6. Motion

### Cadence
- **v3:** on **ones** at 24 fps. Camera, birds and wiggles change every frame. The f99 change is continuous sub-pixel motion (phase-correlation and SSD tracks are smooth curves). Measured gaps {1:287, 2:9} agree.
- **v4:**
  - Shot 1 (f0–118) changes on frames 3,5,8,10,13,15… with gaps alternating 3/2. That is **12 fps posterised in 30 fps**.
  - Shots 2–3 (f119–315) change on 123,127,130,134,138,142,145… with gaps 4,3,4,4,4,3… (15 frames per 4 steps). That is **8 fps**.
  - Never on ones. Every animated property, including slow drifts, updates only on these steps.

### v3: camera pull-back (f0→f99, 4.13 s)
- **Palace scale 1.88 → 1.00** (tracked dome patch, NCC + scale search vs f200).
- The **inverse scale is linear in time** (rms 0.009, against 0.045 for easeOutSine on plain scale). This is a constant-speed 3D camera dolly in Z, which reads as an ease-out zoom.
- The stop is abrupt at f99, with no ease-in at the end because the dolly is linear.
- Sampled palace scale: f0 1.88, f12 1.69, f24 1.56, f36 1.42, f48 1.315, f60 1.22, f72 1.145, f84 1.07, f93 1.01, f99 1.00.
- **Parallax** (relative depth k: palace = 1; smaller is nearer). Formula: `scale_L(t) = 1/(1 − u(t)/k_L)`, `u(t) = 0.468·(1 − f/99)`.
  - Paper k≈1.28: 1.59x → 1.00 (measured 1/0.63 at f0, 1/0.77 at f49).
  - Palace k=1.00: 1.88x → 1.00.
  - Sun k≈0.9: zooms slightly more than the palace (r/r_final 1.45 at f40 against 1.375 for the palace).
  - Truck k≈0.80: measured 1.29 / 1.21 / 1.11 at f60 / 70 / 80.
  - Rickshaw k≈0.66: measured 1.37 / 1.25 / 1.15 / 1.07 at f60 / 70 / 80 / 90.
  - The vehicles start at ≈3.4x and are **off-frame below**. They rise into view from the bottom edge (canopy enters ≈f22–25) purely from the dolly, with no separate slide keyframe.
- **Zoom fixed point** ≈ (372 px, 52–65 px) = **(50.5% W, 13–16% H)**. The dome barely moves while the bottom of the frame opens up. Dome centre goes (363,163) → (367,117)@414.

### v3: sun entrance (f1→f24)
- The sun **scales up from 0 about its own centre**, which is hidden behind the dome. It becomes visible at f8–9 and reaches full size at f24.
- Visible radius grows linearly at ≈7.2 px/frame (r 122 → 168 px between f17 and f24, centre fixed at (368,216) in the zoomed view). It is a linear scale (1 s) with a hard stop and no overshoot.
- After f24 it simply rides the camera.
- Final radius 103 px@414 (≈269 px@1080).

### v3: birds
- ≈14 near-black birds from a stock flock clip. They **flap on ones** (the wing pose changes every frame) and drift right/up across the sky during f0–f99, while also riding the camera zoom.
- **They freeze completely from f100**: 0 changed pixels in the bird area f100–f363. The clip or its time-remap ends when the camera stops.

### v3: vehicles
- No own entrance (see parallax above): their apparent rise from the bottom is the dolly.
- After landing they drift ≤4 px during f95→f200.

### v3: palace post-settle drift (f99→f157, 2.4 s)
- After the camera stops, the palace layer alone slides **down ≈15 px@414 (3.7% H, ≈39 px@1080) and right 5 px**, approximately linearly at ≈0.27 px/f.
- Paper, sun and title are static during this move (tracked to ±0.05 px).
- The effect: the sun "rises" a little more behind the building.

### v3: idle wiggle (≈f150→end; also underneath from ≈f110)
- Palace, truck, rickshaw and CNG each **translate independently on every frame** with smooth random paths, like an AE `wiggle(freq, amp)` on position. Translation only: rickshaw top and bottom boxes move identically, so there is no rotation or scale.
- Measured ranges at 414p (vs f250):

| layer | x range (px) | y range (px) | std (px) | mean speed (px/f) |
|---|---|---|---|---|
| truck | −1.7…+1.7 | −0.8…+1.6 | 0.65–0.75 | 0.12 |
| rickshaw | −0.9…+2.9 | −0.4…+3.1 | 0.85 | 0.15 |
| palace | −2…+0.3 | ±1.7 (excluding the f99–157 slide) | 0.6–1.0 | 0.09 |
| CNG | ±1.1 | −1.25…0 | 0.4 | 0.06 |

- The autocorrelation's first zero falls at 9–14 frames, which gives a frequency of **≈0.7–1 Hz**. Amplitude is **≈±1.5–3 px@414 ≈ ±4–8 px@1080**.
- The front-most layer (rickshaw) wiggles most.
- Sun, title, birds and paper do **not** wiggle.
- The short `hold` runs in metrics (e.g. f158–162, f166–174, f264–271) are just moments where all drifts are below JPEG noise.

### v3: title
See §3: per-cluster slide-up plus fade, 5 f each, 10–11 f stagger, ease-in.

### v4: shot 1, cafe (f0–118)
- **Cut-out rise:** the composite rises from below the frame. Offsets vs final (x +13, y +290 px@408 = **+71% H**, ≈768 px@1080) step down as follows:

| frame | f0 | f3 | f5 | f8 | f10 | f13 | f15 | f18 | f20 | f23 | f25 | f28 | f30 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| y offset (px) | 290 | 193 | 133 | 91 | 62 | 41 | 25 | 15 | 8 | 4 | 1 | 1 | 0 |

  - Best fit: **easeOutQuart over 30 f (1.0 s)**, rms 0.019. easeOutCubic over 25 f gives rms 0.022.
  - Stepped at 12 fps. No scale, no rotation, no overshoot.
- **White torn-paper sheet** slides **right** in sync. Its edge goes 465→517→568→595→613→624→630→632→633 px (f0…f20), i.e. ≈170 px (24% W) with the same ease-out. It then keeps creeping right +7 px until f118.
- **Idle:** the whole cafe collage slowly **scales up ≈+1%/s** (f30→60 +1.0%, f60→118 +1.7%) and drifts ≈3 px left. It is a slow push-in, updated on the 12 fps steps.
- **Bolt pops:**
  - Grey bolt: speck at f3 → full at f8 (2 steps).
  - Second small grey bolt: f18–20.
  - Black newsprint bolt: speck f28 → f30 → f33 → full at f35 (3 steps, ≈7 f).
  - Second small black bolt: f40 → f45.
  - All are scale-from-zero pops with no overshoot.
  - A white/grey "puff" shape flashes beside the sign at f30–33.
- **Zap squiggles:** see §8.

### v4: shot 2, jukebox (f119–216)
- **Zoom-out entrance:** the cut lands at **2.38x** (held f119–122). Then scale goes 1.44 (f123), 1.18 (f127), 1.065 (f130), 1.015 (f134).
  - That is ≈easeOutExpo with a time constant ≈3.5 f, settling in 15 f (0.5 s).
  - Fixed point ≈ (357,132) px = (50% W, 32% H).
  - A small rebound to 1.03 at f142–153 then eases back to 1.00 by f190.
- **Exit move:** the zoom-out accelerates 1.00 (f190) → 0.995 (f202) → 0.98 (f209) → 0.955 (f213/216), then the cut comes.
- **Letter fly-ins:**
  - E is present at the cut and is swept in by the zoom. It then slides right to tuck behind the jukebox (x 148 → 248 px between f134 and f153).
  - The others enter from off-frame, horizontally toward the centre, decelerating:

| letter | side | first visible | settled |
|---|---|---|---|
| K | left | f127 | f157 |
| B | right | f130 | f157 |
| O | right | f142 | f157 |
| U | left | f142 | f157 (rotation settles 110° → 94° at f160–168) |
| J | left | f145 | f157 |
| X | right | f149 | f157 |

  - **Starts are staggered but all letters land together at ≈f157** (1.27 s after the cut). Travel time is 8–30 f.
  - Example path, B x by step: 689*, 643, 599, 553, 514, 483, 473, 470, 469. That is ≈11.5 px/f (≈30 px/f@1080) constant, then ease-out over the last 2 steps (*partly off-frame).
  - Letters arrive tilted ±5–20° and straighten while sliding.
- **Background strips:**
  - Torn grid-paper band appears tilted at f134 and rotates/slides to near-horizontal by f142–149.
  - Newsprint strips slide in at the top-right (f142–157) and along the bottom edge (f153–157).
- **Idle:**
  - The jukebox jitters on each 8 fps step: top and bottom halves shift independently by up to 3 px in y. That is a random ±1–2% vertical scale/position jitter (≈±3–8 px@1080).
  - The bolt jitters ±2–3 px per step.
  - Letters only follow the slow zoom.

### v4: shot 3, radio (f217–315)
- **Zoom-out entrance:** cut at **1.41x**, held ≈5 f. Then **easeOutExpo from ≈f222 over ≈64 f (2.1 s)** to 1.00 (rms 0.018).
  - Fixed point is the radio centre (330,248) = (46% W, 61% H).
  - Sampled scale: f224 1.35, f228 1.23, f232 1.15, f235 1.11, f239 1.08, f243 1.06, f247 1.04, f250 1.03, f254 1.02, f258 1.01, f277 1.00.
  - It then drifts to 0.99 by f314.
- **RADIO assembly:** at the cut the letters are spread wide, low, partly hidden behind the radio, and rotated (R ≈25–60° off vertical, D ≈35°).
  - In layer space (zoom removed) they move together: R +93 px, A +73, D +32, I +15, while O moves left from the right edge.
  - All rise 30–50 px and rotate upright.
  - Settled by f250; D finishes straightening at f262–277.
  - Total ≈33–45 f (1.1–1.5 s), ease-out, on 8 fps steps.
- **Bolts:** pop from small at f220 to full at f224 (2 steps). A second smaller bolt appears at f235–239.
- **Red X:** draw-on f235 → f239 → f243, clean at f247 (see §8).
- **Object micro-animation:**
  - The radio's red tuning needle sweeps along the dial: x 150 (f220) → 395 (f262) → back to ≈200 (f284) → 325 (f310).
  - The push-buttons toggle pressed/unpressed states.
  - Both update on 8 fps steps.
- **Idle:** the black torn backing and the bolt jitter by ≈1–2 px per step.

### Shared motion vocabulary
- Entrances are slides from off-frame (v3 glyphs from below; v4 cafe from below and letters from the sides) or scales from zero (sun, bolts). The hard stop has **no overshoot**, except a tiny 3% rebound on the v4 jukebox zoom.
- Scene openers are camera zoom-outs from an oversized framing:
  - v3: linear 3D dolly with parallax.
  - v4: stepped easeOutExpo.
- After landing, nothing is perfectly still:
  - v3 uses smooth per-layer wiggle (0.7–1 Hz, ±4–8 px@1080).
  - v4 uses a slow 1%/s scale drift plus per-step positional jitter.

---

## 7. Transitions

**v3:** none. It is a single shot that opens mid-camera-move (f0 is already at 1.88x and moves from f1).

**v4:**
1. **f118 → f119: hard cut** (cafe → jukebox), landing on an **oversized close-up of the next hero** (jukebox at 238%). The close-up holds 4 frames (f119–122), then a stepped easeOutExpo zoom-out settles in 15 f. The metrics flag a "cut" at f123, but that is **not** a cut: it is the first, largest zoom step (2.38→1.44) of the same shot.
2. **f216 → f217: hard cut** (jukebox → radio). It is preceded by an accelerating zoom-out of the outgoing shot (1.00 → 0.955 over f190–216, an ease-in exit) and lands on the new hero at 141%. That holds ≈5 f, then a 2.1 s easeOutExpo zoom-out.
3. **Shot-1 opening (f0–f30):** the hero rises from below (+71% H, easeOutQuart 1 s) while a white torn-paper sheet slides right 24% W. This is likely the tail of a paper-slide transition from the preceding (unseen) shot.

Frequency: 2 hard cuts in 10.5 s. Both use the same "cut to oversized hero → zoom-out settle" device. There are no wipes, dissolves or whip-pans.

---

## 8. Recurring devices

### Coloured outline on the landmark (v3)
- A solid 13 px@1080 stroke in the accent colour, outside only, around the main landmark cut-out. It matches the sun disc.
- Animation: none of its own. It is part of the cut-out layer.

### White sticker border (v3)
- 13–16 px@1080 pure white, rounded, around every foreground object photo.
- Animation: none.

### Flat sun / disc behind the landmark (v3)
- A giant flat circle in the accent colour, ≈50% H diameter, centred behind the landmark's top.
- It scales from 0 about a hidden centre (linear, 1 s).

### Bird flock (v3)
- Black silhouettes flapping on ones. They freeze when the camera settles.

### Per-glyph type-on (v3)
- Each grapheme slides up 1 glyph height and fades in over 5 f with an accelerating ease. Stagger is 10–11 f.

### Ransom-note display word (v4)
- Giant condensed caps with each letter placed individually.
- Bouncy baseline (±7% H), tilt 0–8°, bleeding off the frame edges and partially hidden behind the hero object.
- Letters slide or assemble in on 8 fps steps.

### Lightning-bolt doodles (v4, every shot)
- Pairs of a big bolt and a small bolt, about 60–90 px@408 (≈160–240 px@1080) for the big one.
- Cut from inverted black newsprint or flat light grey, angled ≈30–45°.
- **Pop** (scale from speck) in 2–3 stop-motion steps (5–7 f). They do not draw on.
- Around each bolt are **thin (≈2 px@408 ≈ 5 px@1080) dark wavy zap squiggles and short dashes**. These are **re-drawn at a new random position/shape every step** (12 or 8 fps) as a looping hand-drawn "electric" sprite, and are sometimes absent.
  - Shot 1: the squiggles keep looping through the whole shot.
  - Shot 3: they run f228–254, then disappear.
- The bolts themselves jitter ±2–3 px per step.

### Hand-drawn red X (v4)
- Marker-style strokes, 34×56 px@408 (≈90×148 px@1080). Stroke ≈4–5 px@408 (≈12 px@1080) with slightly tapered ends.
- **Written on stroke by stroke** in 3 steps of 4 f each (f235, f239, f243; clean f247 = 0.4 s): first "\" grows, then "/".
- Multiply blend. Placed just left of the word it annotates.
- Afterwards it drifts only with the scene (≈6 px down).

### Torn paper strips and scraps (v4)
- Grid paper, newsprint and black paper with ragged edges.
- They slide/rotate into place on stop-motion steps and are cropped by the frame.

### Colour window (v4)
- A torn-edge colour photo (blue sky) behind a B&W cut-out.

### Tinted B&W object (v4)
- A B&W photo with one hand-tinted part (jukebox tubes).

### Object micro-animation (v4)
- The real mechanism moves (radio needle sweep, buttons toggling) on the step cadence.

### Watermark (v4)
- White "Vox" serif logo, top-right, ≈5% H tall, ~75% opacity.

v3 has none of: highlighter, maps, pins, arrows, counters.

---

## 9. Scene log

### v3_mdriturana (24 fps, one shot)
| frames | time | on screen | devices | motion / notes |
|---|---|---|---|---|
| f0 | 0.00 | close on palace dome + facade at 1.88x, yellow outline, birds left | outline, birds | first frame held 1 f |
| f1–f8 | 0.04–0.33 | camera dolly-out begins, birds flapping | | 1/scale linear, on ones |
| f8/9–f24 | 0.33–1.00 | sun disc grows from behind the dome to full | flat sun | linear scale from 0, hard stop f24 |
| f22–f99 | 0.92–4.13 | truck, rickshaw, CNG rise into frame from the bottom (parallax, nearer layers) | white sticker borders | revealed by the dolly; palace 1.88→1.0, paper 1.59→1.0 |
| f99/100 | 4.13 | camera stops; birds freeze | | abrupt stop |
| f99–f157 | 4.13–6.54 | palace slides down 15 px, right 5 px | | ≈linear 0.27 px/f |
| f103–f108 | 4.29–4.50 | "রং" slides up + fades in | per-glyph type-on | 5 f, ease-in |
| f114–f118 | 4.75–4.92 | "পু" | | +10–11 f stagger |
| f125–f128 | 5.21–5.33 | "র" completes রংপুর | | |
| f110–f363 | 4.6–15.1 | final postcard; vehicles and palace wiggle independently | | wiggle 0.7–1 Hz, ±1.5–3 px@414; text, sun, birds static |

### v4_schaapening (30 fps)
| frames | time | on screen | devices | motion / notes |
|---|---|---|---|---|
| f0–f30 | 0–1.0 | ROADSIDE CAFE B&W cut-out (with sky colour window, newsprint backing) rises from below; white torn paper slides right over grid paper | colour window, torn paper | +71% H → 0, easeOutQuart 1 s, 12 fps steps |
| f3–f8 | 0.1–0.27 | grey bolt pops (left); f18–20 small grey bolt | bolt pop, zap squiggles | 2 steps |
| f28–f45 | 0.93–1.5 | black newsprint bolt pops (right), small bolt f40–45, white puff f30–33 | | 3 steps |
| f30–f118 | 1.0–3.93 | idle: zap squiggles redraw every step, slow +1%/s push-in | | 12 fps |
| **f119** | 3.97 | **hard cut**: jukebox at 238%, blue "E" at left | | hold 4 f |
| f123–f134 | 4.1–4.47 | stepped zoom-out to 100%; bolt above-left | | easeOutExpo, 8 fps |
| f127–f157 | 4.23–5.23 | K, B, O, U, J, X fly in from the sides; grid strip rotates in (f134–149); newsprint strips slide in (f142–157) | ransom-note word, torn strips | staggered starts, common landing f157 |
| f157–f198 | 5.23–6.6 | JUKEBOX layout idle; jukebox and bolt jitter per step | | 8 fps |
| f198–f216 | 6.6–7.2 | accelerating zoom-out to 95.5% | | exit move |
| **f217** | 7.23 | **hard cut**: radio dial at 141%, scattered teal RADIO letters behind it | | hold ≈5 f |
| f222–f286 | 7.4–9.5 | zoom-out to 100% (easeOutExpo 2.1 s); RADIO letters converge, rise and straighten (settled f250–277) | | 8 fps |
| f220–f239 | 7.33–7.97 | bolt pair pops at top-left; zap squiggles f228–254 | bolt pop | |
| f235–f247 | 7.83–8.23 | red X written on left of R | hand-drawn X (multiply) | 3 steps, 0.4 s |
| f220–f315 | 7.3–10.5 | tuning needle sweeps, buttons toggle, slight jitter, drift to 99% | object micro-anim | 8 fps |

---

## 10. Replication recipes

```js
// R1. 3D dolly-out with parallax (v3). Scale per layer; 1/scale is linear in time.
const DOLLY = { start: 0, end: 99 /* frames @24fps = 4.13 s */, u0: 0.468, // palace starts at 1/(1-0.468)=1.88x
  anchor: { x: 0.505, y: 0.14 } /* fraction of frame; dome stays put, bottom opens up */ };
const depth = { paper: 1.28, palace: 1.0, sun: 0.9, cng: 0.85 /*est*/, truck: 0.80, rickshaw: 0.66 };
function layerScale(k, f) {
  const t = Math.min(1, Math.max(0, (f - DOLLY.start) / (DOLLY.end - DOLLY.start)));
  const u = DOLLY.u0 * (1 - t);          // linear camera travel, hard stop at the end
  return 1 / (1 - u / k);                // rickshaw starts ~3.4x and off-frame below
}
// transform: translate(anchor) scale(s) translate(-anchor) applied to each layer's final layout
```

```js
// R2. Idle wiggle on cut-outs after the camera settles (v3). Smooth, every frame, translation only.
wiggle = { freqHz: 0.8 /*0.7–1.0*/, ampPx1080: { rickshaw: 7, truck: 5, palace: 5, cng: 3 },
           octaves: 1, independentSeedPerLayer: true, rotate: 0, scale: 0,
           exclude: ['sun', 'title', 'birds', 'paper'] }
// AE: position + wiggle(0.8, 5)  (amp in px@1080)
```

```js
// R3. Landmark cut-out with accent outline + sun disc (v3)
palace.stroke = { color: '#F6E916', widthPx1080: 13, position: 'outside', join: 'round', gapPx: 0, shadow: null };
vehicle.stroke = { color: '#FFFFFF', widthPx1080: 14 /*13–16*/, position: 'outside', join: 'round', shadow: null };
sun = { shape: 'circle', fill: '#F6E50D', diameterPctH: 50, center: { xPctW: 50, yPctH: 37 }, z: 'behind palace',
        enter: { prop: 'scale', from: 0, to: 1, frames: 24 /*1 s @24*/, easing: 'linear', pivot: 'own centre (behind dome)' } };
paper = { color: '#DFE0DB', texture: 'crumpled scan, luma 189–238', animated: false };
```

```js
// R4. Per-grapheme type-on (v3 Bengali title; works for any script by grapheme cluster)
title = { text: 'রংপুর', font: 'Hind Siliguri Bold | Noto Sans Bengali Black', color: '#26873A',
          sizePctH: 11.8 /* matra→baseline ≈128 px@1080 */, pos: { leftPctW: 67.7, topPctH: 18.4 } };
perCluster = { frames: 5 /*@24fps = 0.21 s*/, staggerFrames: 10.5, startAfterCameraStopFrames: 4,
  y: { fromPctH: +13, to: 0, easing: 'easeInQuad' }, opacity: { from: 0, to: 1, easing: 'easeInQuad' }, overshoot: false };
```

```js
// R5. Stop-motion posterisation (v4). Render the animation at full rate, then sample-and-hold.
const STEP = { shot1: 12, shot2: 8, shot3: 8 }; // animation fps inside a 30 fps timeline
const heldTime = (f, fps30, animFps) => Math.floor(f * animFps / fps30) / animFps; // 12fps → gaps 3,2,3,2; 8fps → 4,4,4,3
// apply to EVERY property (position, scale, slow drifts, doodle frames); never update on ones
```

```js
// R6. Shot opener: cut to oversized hero, hold one step, stepped easeOutExpo zoom-out (v4)
heroZoomOut = { startScale: 2.38 /*jukebox*/ /* or 1.41 radio */, holdFrames: 4 /*one 8fps step*/,
  to: 1.0, easing: 'easeOutExpo', durationFrames: 30 /*jukebox: 98% done in 15 f*/ /* radio: 64 f */,
  pivot: 'hero centre (jukebox ~50%W,32%H; radio 46%W,61%H)', posterize: 8 };
idleDrift = { scalePerSecond: +0.01 /*shot1 push-in*/ /* or −0.005 slow pull-out */, posterize: true };
exitMove = { lastFrames: 26, scaleTo: 0.955, easing: 'easeInQuad' }; // jukebox shot before the cut
```

```js
// R7. Rise-from-below entrance + paper slide (v4 shot 1)
heroRise = { fromYPctH: +71, fromXPx1080: +34, to: 0, frames: 30 /*1 s @30*/, easing: 'easeOutQuart', posterize: 12 };
paperSheet = { layer: 'white torn paper over grid paper', dxPctW: +24, frames: 20, easing: 'easeOutQuart',
               thenCreepPxPerSec: 2, posterize: 12 };
```

```js
// R8. Ransom-note display word (v4 JUKEBOX / RADIO)
word = { font: 'Oswald Bold / Bebas Neue', case: 'upper', capHeightPctH: 27 /*JUKEBOX*/ /*21.8 RADIO*/,
  color: '#5C5CD0' /*or #7FCCCD with blend:'multiply'*/, z: 'behind hero cut-out',
  perLetter: { baselineJitterPctH: 7, tiltDeg: [-8, 8], bleedOffFrame: true } };
flyIn = { from: 'nearest frame side (off-frame)', axis: 'x', speedPx1080PerFrame: 30, easeLastSteps: 2,
  startTiltDeg: [5, 20], endTilt: 'final tilt',
  staggerStartsFrames: { K: 0, B: 3, O: 15, U: 15, J: 18, X: 22 } /*E already on screen at the cut*/, landTogether: true, posterize: 8 };
assemble /*RADIO variant, layer-space x offsets R,A,D,I,O (O est.)*/ = { startSpreadPx1080: [-246, -193, -85, -40, +40], startDropPctH: 10, startRotDeg: [25, 60],
  frames: 36, easing: 'easeOutExpo', posterize: 8 };
```

```js
// R9. Lightning-bolt doodle with zap squiggles (v4)
bolt = { texture: 'inverted newsprint (black + light text stripes)' /* or flat #C8C8C8 */, sizePx1080: [160, 240],
  pair: { smallScale: 0.45, offsetPx1080: [-60, 50], appearsAfterFrames: 12 },
  enter: { prop: 'scale', from: 0.1, to: 1, steps: [2, 3] /*5–7 f*/, overshoot: false },
  idleJitterPx1080: 6 /*random per step*/ };
zaps = { strokePx1080: 5, color: '#2A2A2E', shapes: 'wavy lines 40–120 px + short dashes', count: [1, 4],
  redrawEveryStep: true /*new random path each 12/8 fps step*/, lifetime: 'whole shot or ~1 s' };
```

```js
// R10. Hand-drawn X annotation (v4)
xMark = { color: '#D44A55', blend: 'multiply', sizePx1080: [90, 148], strokePx1080: 12, taper: true,
  writeOn: [{ stroke: '\\', steps: 2 }, { stroke: '/', steps: 1 }], stepFrames: 4 /*8 fps*/, totalFrames: 12,
  place: 'immediately left of annotated word, cap-height aligned' };
```

```js
// R11. Watermark (v4)
watermark = { text: 'Vox (serif logo)', color: '#FFFFFF', opacity: 0.75, heightPctH: 5,
  rightMarginPctW: 1.4, topMarginPctH: 5.4 };
```

---

## 11. Uncertainties

- **v3 dolly geometry:** the fixed point's y (52–65 px) differs slightly between paper and palace. There may be a small Y camera move as well as Z. The sun's depth (k≈0.9, nearer than the palace) is odd for a "sky" element; it may instead have its own scale keyframe. The CNG depth was not measured (≈0.85 estimated).
- **v3 palace slide f99–157** (15 px down): this could be a deliberate position keyframe or a very low-frequency wiggle. Its linearity and the fact that it happens only once suggest a keyframe.
- **v3 bird freeze at f100:** it may be the end of a stock clip rather than a design choice.
- **v3 Bengali font:** not identified exactly. The opacity/position curve of each glyph is only 4–5 samples, so the "ease-in" shape is approximate. Motion blur may hide the earliest (faintest) frame.
- **v3 outline colour:** the yellow is ≈#F6E916 and the sun #F6E50D. They are probably the same swatch with JPEG differences.
- **v4 shot-1 opening** might be the tail of an incoming transition (the clip starts at f0 mid-move). Timing starts and durations before f0 are unknown.
- **v4 jukebox idle jitter:** the per-step top/bottom differences (≈3 px) could come from the jukebox photo having its own subtle animation (lights) instead of transform jitter.
- **v4 colours:** the red X hex is uncertain because thin strokes are chroma-smeared by JPEG. The sampled core is #C15561 and the true value is probably more saturated. The RADIO multiply vs. ~85% opacity call is based on grid lines showing through R; JUKEBOX blue looks opaque.
- **v4 letter fly-in curves:** early positions are partial (letters clipped by the frame edge and occluded by the jukebox), so the travel start points and exact easing are approximate.
- **Typeface IDs** (condensed grotesque in v4) are visual matches, not confirmed.
