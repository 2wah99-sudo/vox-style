# v5_valuable826 — part B (f1407–f2233, 56.28–89.32 s) — agent v5_valuable826_B

Source: `$VOX/src/v5_valuable826.mp4`, 1280x720 @ 25 fps. My range is entirely inside detected "scene #030"
(f1109–f2233). That scene is so long only because black pillarbox bars dilute the full-frame cut detector.
I re-ran the metrics on the content column only (`$VOX/tmp/v5_valuable826_B/box_1380_2233.csv`, box x437–842,
produced by `$VOX/tmp/v5_valuable826_B/boxmetrics.py`). Every cut listed below comes from that box pass plus
frame-by-frame inspection.

> **KEY FINDING: from f1109 to the end the video is a VERTICAL 9:16 film pillarboxed in a 16:9 frame.**
> Content column = x 437…842 (406 px) × y 0…719 (720 px), aspect 0.564 ≈ 9:16. The bars are pure #000000 (mean luma 0.00 on
> every sampled frame). **All "% of H" values below are % of the 720 px content height. "px@1080" = ×1.5 (16:9 1080p delivery,
> same pillarbox). "px@1920v" = ×2.667 (native 1080×1920 vertical).** "% of W" = % of the 406 px column width.
>
> This half is **not** the paper-collage editorial look of the opening (f0–~1108). It is a glossy live-action + CGI product
> film for Nike's 50th anniversary ("Never done breaking the mold"). The motion-graphics layer is thin: serif captions,
> serif headlines, two end cards. Those are what I measured most carefully.

---

## 1. Overview
- **What it is:** a vertical (9:16) brand film made of four "transformation" segments followed by a two-card end slate.
  The beats are: an everyday object sits on a classical pedestal in a coloured studio → the caption says "This is **not** just
  a <object>." → the object transforms (CGI) → it becomes a Nike shoe titled "THIS IS / NIKE <MODEL>". My range covers:
  toy snake → **NIKE FREE** (crimson), rubber band → **NIKE GO** (green), teddy bear → **NIKE PHYLON** (blue),
  waffle iron → **NIKE WAFFLE** (red/orange). Then come **"Never done breaking the mold."** and the **Swoosh-"50" logo**.
- **Visual identity:**
  - Each segment owns one saturated seamless backdrop colour (crimson / grass green / petrol blue / tomato red) with soft
    radial lighting.
  - Props are white fluted Doric-style columns (or a cardboard kitchen cabinet), filmed with slow push-ins.
  - Type is a refined book serif, always white on the colour.
  - The single "graphic" idea is **"breaking the mold"**: one word or line in every text block is shown eroded, chipped,
    ink-bled or brush-struck, while the rest of the type stays clean.
  - Typography never animates in. It hard-pops on in one frame and leaves with the hard cut.
- **Format:** 1280x720 at 25 fps, with a 406x720 9:16 content column. Animation is **on ones**: continuous live-action/CGI
  motion, 648 of 674 changing-frame gaps = 1 frame. There is no stop-motion cadence in this half.
- **Cross-boundary note:** the 9:16 section starts at f1109, in part A's range. Part A's overview frames show the same
  devices: "NEVER DONE / BREAKING / THE MOLD." (f1150), "THIS IS / A VISIONARY" (f1300), and the snake pedestal with
  "This is not just a toy snake." (f1350–1406). Its end slate copies the end of the 16:9 first half: "Never done leaving a
  mark." on white paper, then the 50-swoosh at f1025–1108. **The source looks like two separate Nike-50 spots joined
  together (16:9 then 9:16). Both end with tagline card → 50-logo card.**

## 2. Colour
Sampled hex values (median of 40×40 or 60×50 px patches inside the column; positions TL / TC / ML / MR / BL / BR):

| segment (frame) | backdrop samples | role |
|---|---|---|
| snake macro (f1410) | #980432, #AA1340, #A40E3B, #AA1F44, #930F36 | crimson floor and wall, deep magenta-red |
| NIKE FREE (f1590) | TL #741331 (vignette), TC #A91B49, ML #A7003E, BL #7D0028 | crimson, darker corners |
| rubber-band studio (f1600) | #246A2C (top), #4B893D, #5F9847, #348B3C | chroma-key green; the studio ceiling #C3B4B4 is visible at the top |
| CGI sculpture / NIKE GO (f1700/f1770) | #33722E (corners), #579242 / #548F40 (centre) | green with radial falloff |
| bear studio (f1800) | #051E45 (TL), #063B69, #063363, #085179 | petrol / navy blue |
| NIKE PHYLON (f1950) | #074171, #08597D, #0C6180, #0A6582 | petrol / teal blue |
| waffle room (f1990) | #671A18, #99221B, #7B090F, #8B1C16 | oxblood red room, cardboard props |
| giant-waffle room (f2025) | #9B3619, #A64726, #571905 | rust/orange patterned wallpaper, golden waffles |
| NIKE WAFFLE (f2140) | #BD311A, #CA4529, #C0422C, #D85730, #9B1512 | tomato-orange with a darker red base |
| end cards (f2160/f2210) | #C0C0C2 … #C3C4C6 (median RGB 193,193,195) | cool light-grey textured card |

- **Backdrop rule:** one saturated hue per segment. The pedestal shot and the final shoe shot share it (snake/FREE =
  crimson, rubber band/GO = green, bear/PHYLON = blue, waffle/WAFFLE = red-orange). Corners fall off by about 25–40% in
  luma (e.g. crimson #A91B49 centre → #741331 corner; blue #063B69 → #051E45), so it reads as a soft spotlight on a seamless.
- **Text colours:** headline and caption text is nominally white but tinted toward the backdrop. The look is graded
  together with the plate, not pure #FFFFFF:
  - headline on crimson #FFF0FB (10th percentile #FFCEE0), on green #E6FEE1, on orange #FFE9D9;
  - captions #E2FFD8 on green, #D2FFFF on blue, #FFF0E1 on red.
  - **Recipe:** white text with about 8–12% of the backdrop hue mixed in (or a "screen"-blended 90% white).
- **Brush underline / stroke:** #DAFECE on green (tinted white); on red the pigment reads pure white #FEFCF9.
- **End card text:** near-black. Dark-pixel median (39,40,41) = **#272829**; darkest core #060606. **Logo #000002**
  (pure black).
- **Pedestal (column):** warm grey plaster. Shaft in shadow #5D564A (green set) / #616157 (blue set); lit faces read
  off-white.
- **Product accents** (these come from the products, not the design system): neon volt #B4DC28 (CGI sculpture), salmon pink,
  lilac, orange band; teal + yellow vintage Nike; white/red/royal-blue Waffle One.
- **Screen share (my range):** the black pillarbox is always ≈68% of the 16:9 frame. Inside the column, the backdrop hue
  covers about 50–70% in pedestal/headline shots.

## 3. Typography
All type is centred on the column's vertical axis (x ≈ 203 of 406). There are four styles:

**A. Headline "THIS IS / NIKE <MODEL>"** (FREE f1530–1596, GO f1749–1774, PHYLON f1926–1972, WAFFLE f2123–2146)
- Two lines, ALL CAPS, centred. Measured on f1590 / f1770 / f2140:
  - Line 1 "THIS IS": rows 60–63 → 93–97, so **cap height 34–35 px = 4.8% H** (≈52 px@1080, ≈92 px@1920v). Width is
    always **160 px = 39.4% W**. Clean typeface.
  - Line 2 "NIKE FREE / NIKE GO / NIKE WAFFLE": rows 103–105 → 138–140, **cap height 36 px** (the distress bleed adds about
    1 px each side). Widths 241 / 203 / 319 px = 59% / 50% / 79% W.
  - Gap between lines 7–10 px, so the **baseline-to-baseline pitch is 42–43 px = 5.9% H ≈ 1.22 × cap height**. With cap
    height ≈ 0.68 em that is a font size ≈ 50 px@720 (≈75 px@1080, ≈135 px@1920v) and leading ≈ 0.85 em (tight).
  - Block top at y 60–63 (**8.5% H from the top**), bottom at y 138–140 (**19.3% H**).
- **Typeface:** a high-contrast transitional/book serif with bracketed serifs and a long-legged R. It looks like Lyon
  Display / Tiempos Headline. Free stand-ins: **Newsreader Display (Regular)**, Source Serif 4 Display, or Libre Caslon
  Display. Weight Regular, tracking about 0 to +10.
- **Line 2 "broken mold" treatment:** the same face, but every glyph edge is eroded and ink-bled. The edges are blobby with
  drip-like nubs, and the inside of the letters is mottled with grey speckle (≈10–20% darker patches). A tiny "SM" or "™"
  sits after the model name.
  - **Recipe:** displacement map on the glyph edges (amplitude ≈1–2 px@720 ≈ 2–3 px@1080), threshold a blurred noise mask,
    then multiply in a grunge texture inside the fill.
  - Line 1 is always clean. The contrast between clean and broken is the point.
- **Animation:**
  - **ON is a hard pop in 1 frame:** white-pixel count 2 → 1115 between f1529 → f1530, 0 → 1104 at f1749, 0 → 1195 at
    f1926, 0 → 967 at f2123. There is no fade, scale or slide.
  - The pop either lands **on a hard cut** (GO f1749, PHYLON f1926) or **mid-shot** once the shoe has resolved
    (FREE f1530, 5 frames after the morph ends; WAFFLE f2123, 35 frames after the whip settles).
  - **OFF: it leaves with the next hard cut** (no exit animation).
  - Time on screen: FREE 67 f (2.68 s), GO 26 f (1.04 s), PHYLON 47 f (1.88 s), WAFFLE 24 f (0.96 s).
  - The text is **screen-locked**: it stays fixed while the camera and shoe move under it.
  - Layer order: the text sits above the plate. The PHYLON midsole rises up "through" the headline; the white text stays
    readable over the white foam.

**B. Pedestal caption "This is not just a <object>."** (rubber band f1597–1662, bear f1775–1838, waffle iron f1973–2012;
the toy snake is in part A)
- Sentence case, one line, centred:
  - Caption widths: rubber band 296 px (73% W), bear 222 px (55% W), waffle iron 300 px (74% W).
  - **Cap height 15–16 px = 2.2% H** (≈23 px@1080, ≈41 px@1920v). **x-height 10–11 px = 1.4% H**. Font ≈ 22–23 px@720
    (≈34 px@1080, ≈60 px@1920v).
  - **Baseline y ≈ 376–379 = 52.5% H.** The caption floats in the empty backdrop just above the object or column top, and
    the push-in brings the object up under it.
- **Face:** the same book serif in Regular (Lyon/Tiempos Text-like). Free stand-ins: **Newsreader Text Regular** /
  Source Serif 4. Tracking 0.
- **The word "not" always gets a different material treatment:**
  - toy snake: chipped/eroded semibold;
  - rubber band: a heavy rounded ink-bled bold "not" plus a **white dry-brush underline**. The underline runs under "is not
    just", rows 381–386 (≈5 px = 0.7% H thick, 3 px below the baseline). It starts as a dotted spray on the left and ends
    in a round paint blob ≈8 px across on the right;
  - bear: eroded "not" in the regular weight with chunks missing and a lighter centre;
  - waffle iron: eroded "not" plus a **thick white impasto brush stroke** under "not just a waffle iron." (x 120–360 of
    406, rows 380–398). Its core is ≈7 px thick with a drip/bulge at the left and a round blob at the right end.
- **Animation:** **none.**
  - Caption and underline are fully present on the first frame of the shot. White-pixel counts are constant over every
    frame (e.g. waffle 2300–2318 px f1973–1990), so there is no draw-on and no wipe.
  - The caption is screen-locked while the camera pushes in.
  - **OFF is a 1-frame cut:**
    - rubber band: the caption disappears at f1663 while the plate continues (2 clean frames f1663–1664, then the
      transformation starts at f1665);
    - bear: off with the hard cut at f1839;
    - waffle iron: off with the hard cut at f2013.
  - Durations: 66 f (2.64 s), 64 f (2.56 s), 40 f (1.60 s). They get shorter as the film speeds up.

**C. End tagline "Never done breaking the mold."** (f2147–2189)
- One line, sentence case, near-black #272829 on the grey card, centred:
  - bbox x 48–358 (**310 px = 76% W**), y 347–371;
  - **cap height 18 px = 2.5% H** (27 px@1080, 48 px@1920v); x-height 12 px; **baseline y 365 = 50.7% H** (optically
    centred).
- Same book serif, Regular.
- **"Broken mold" again:**
  - "Never done" is clean;
  - in "breaking" the first letters are chipped, "eaki" fades to mid-grey (≈40–60% opacity) and the strokes break up;
  - "the mold" is rough and ink-bled.
  - The erosion increases left to right inside the word: a progressive-distress gradient.
- Static. On/off by hard cut. No typing and no fade.

**D. Logo** (f2190–2233): Nike Swoosh with a heavy italic grotesque "50" set into its curve. Solid black, bbox 119×65 px =
**29% W / 9% H** (178×98 px@1080), centred at x 201, y 367 (51% H). Static. Hard cut on, and held to the last frame.

## 4. Layout & composition
- **Canvas:** 9:16 column centred in 16:9 with pure-black side bars (x 0–436 and 843–1279). Build natively at 1080×1920;
  for 16:9 delivery, pillarbox it at 1080 px height (column 607.5 px wide, centred).
- **Vertical zones of the 9:16 frame:**
  - **Headline zone 8.5–19.5% H** (top), centred.
  - **Caption line ≈ 50–53% H** (dead centre band). The object top or column capital sits just under it, about 55–65% H,
    after the push-in.
  - End-card text and logo sit on the **centre line (50–51% H)**.
  - Horizontal margins: the widest text (NIKE WAFFLE) leaves 41 px each side = 10% W. Captions leave 13–27% W per side.
- **Pedestal shots:**
  - The column is centred on the vertical axis, with the capital at ≈58–66% H.
  - The studio is deliberately "behind the scenes": light stands, LED tubes and a key light enter from the frame edges, and
    the studio ceiling or white cyc edge shows at the top 15% (green and blue shots).
  - The object is small (≈20–25% W) until the push-in brings it to ≈60–65% W.
- **Product (headline) shots:**
  - The shoe floats in the centre third (≈30–75% H), angled or rotating, often overlapping the bottom of the headline block.
  - Background = clean backdrop colour with a vignette.
- **Layers (back to front):** backdrop plate (or the CGI scene) → product/object → screen-locked white type. There are no
  drop shadows, boxes or lower-third bars.
- **Negative space:** large. Each text card holds one line or one two-line block, with ≥60% of the column left as plain
  colour.

## 5. Textures & materials
- **Product footage:** clean, glossy, high-saturation CGI/photography with shallow depth of field. Heavy motion blur and
  defocus appear on the object-wipe frames.
  - **No added film grain:** temporal noise in static moments is ≈0. For example, the frozen NIKE WAFFLE tail
    f2139–2146 has box diff 0.24–0.47.
  - No halftone, no paper, no cut-out outlines and no drop shadows in this half.
- **Distressed type** is the only "texture" device:
  - eroded/ink-bled glyph edges, ≈1–2 px@720 deviation;
  - mottled fill (grey speckle) on headline line 2;
  - chipped glyphs on "not";
  - progressive erosion on "breaking the mold".
- **Brush marks:** white dry-brush/impasto strokes with a speckled spray start, bristle streaks and a round blob end
  (rubber band: 5 px thick, ≈90 px long; waffle iron: ≈7–18 px thick, 240 px long).
- **End card paper:**
  - Light grey **#C1C1C3** with a **static vertical striation**, like brushed card or a ribbed paper scan. Column-mean
    std 1.1 levels vs row-mean std 0.2. Dominant stripe periods ≈34, 45, 68, 81 px plus fine ≈9 px. The stripe profile
    correlates 0.97–0.99 across frames, so it is static.
  - **Live grain on ones:** the frame-to-frame diff has std 3.45 → per-frame grain σ ≈ 2.4 luma levels, re-randomised
    every frame (a few near-identical frames: f2169, 2173, 2185, 2197).
  - Slow luma breathing 192.5 → 194.6 → 193.0 over 3.5 s (±1 level). The same texture and grain continue unbroken across
    the tagline → logo cut.
  - No vignette on the end card.
- **Dip-to-dark:** at f2074–2078 the outsole fills the lens and luma drops 78 → 16. This is a physical shadow, not an
  added overlay.

## 6. Motion
- **Cadence:** footage is **on ones** at 25 fps. Gaps between changing frames: {1: 648, 2: 16, 4: 1, 6: 2, 10: 1, 15: 1,
  19: 1, 43: 1}. The long gaps are end-of-shot freezes and the end cards.
  - **Retime artefacts (not a style choice):**
    - exact duplicate frames every 14–15 frames during NIKE FREE (f1521, 1535, 1550, 1565; box diff ≈0.01);
    - every 3rd frame during the NIKE GO settle (f1756, 1759, 1762);
    - these come from slowed or frame-rate-converted clips. Do not copy them.
- **End-of-shot freeze holds:** most product and pedestal shots end in a held frame before the cut:
  - NIKE FREE f1579–1596 (18 f, 0.72 s);
  - rubber-band pedestal f1654–1662 (9 f);
  - NIKE GO f1770–1774 (5 f);
  - bear f1834–1838 (5 f);
  - waffle-iron close-up f2014–2016 (3 f);
  - NIKE WAFFLE f2133–2146 (14 f, 0.56 s).
  - **Recipe:** ease the move to a full stop, then hold 5–18 frames (0.2–0.7 s) before the hard cut.
- **Pedestal push-ins** (measured from the column-capital width; scripts `capw.py` and inline snippets):
  - *Rubber band f1597–1660:* capital width 103 → 270 px = **2.62× apparent scale in 63 f (2.52 s)**. It grows ≈7 px per
    3 f, accelerates to 12–13 px per 3 f around f1636–1642, then eases to 0 by f1657. That is a constant-speed dolly
    toward the object (apparent size accelerates) with an **ease-out over the last ≈15 f (0.6 s)**. The capital drifts
    down from y 423 → 474 (58.8 → 65.8% H): the camera tilts down slightly / cranes so the object stays under the caption.
  - *Bear f1775–1838:* capital 97 → 260 px = **2.68×**, and the curve is **front-loaded**. Progress is 0.15 / 0.26 / 0.37 /
    0.45 / 0.50 at +2/+4/+6/+8/+10 f; 0.64 at +18 f; 0.80 at +30 f; 0.94 at +42 f; 1.0 at +52 f (2.08 s). That is ≈ easeOutQuart
    (a fast lunge then a slow creep). The capital moves y 394 → 476.
  - *Waffle iron f1973–2012:* very slow creep only (mean box diff 1.79/frame).
  - `motion.py` on the rubber-band shot (box 437,0,843,350) gave zoom 0.485× with easeOutCubic as the best fit (rms 0.219).
    The per-frame shifts are noisy because of parallax from the foreground lights, so trust the capital-width numbers.
- **Product reveals:**
  - NIKE FREE sole f1525–1578: rotates from sole-up to side profile while drifting up. Box diff decays 24.8 → 2.6 over
    25 f (≈ easeOutQuad), then rises again for the flip (to 8.7 at f1566) and settles.
  - NIKE GO f1749–1769: shoe recedes and settles (diff 14 → 1 over 20 f, ease-out).
  - NIKE PHYLON f1926–1972: foam "petals" fold into one midsole, which floats upward; a debossed swoosh fades up on it
    around f1958–1966.
  - NIKE WAFFLE f2079–2087: decelerating tilt/crane-up with a blurred foreground slab sliding out downward (9 f,
    ease-out), then a near-static creep f2088–2132 (box diff ≈1.8–4).
- **CGI transformation beats** (live action → CGI, all on ones):
  - band drop f1665–1673 (9 f);
  - sculpture slow orbit f1674–1741 (68 f). The sculpture's height grows 427 → 649 px (f1680 → f1715, camera approaches), then shrinks to 367 px by f1741 (−43%, pull-back) just before the GO shoe sweeps in;
  - bear shatter f1839–1879: orange shell shards burst outward, white foam bear underneath, camera orbit, box diff ≈15/f;
  - foam bear → disc stack f1880–1925;
  - giant waffle bursts into an avalanche f2029–2078: camera follows the falling shoe, diff ≈25/f.
- **Typography motion:** none. Pop on, hold screen-locked, cut off (see §3).

## 7. Transitions
All frame numbers are exact (from the box metrics). Types and how often they occur:

1. **Hard cut** (most common; 12 in my range):
   - f1407 (hdist 0.63, pedestal → macro snake);
   - f1500 (inside the morph);
   - f1597 (0.97, NIKE FREE → green studio);
   - f1749 (0.41, into NIKE GO + headline pop);
   - f1775 (0.97, → blue bear studio);
   - f1839 (0.54, bear → CGI shatter);
   - f1880 (0.38, → foam bear);
   - f1926 (0.50, → NIKE PHYLON + headline pop);
   - f1973 (0.92, → red waffle room);
   - f2013 (0.49, → waffle-iron close-up), f2017 (0.26, → giant waffle);
   - f2079 (0.89, out of the dark outsole);
   - f2147 (0.98, → grey end card), f2190 (text → logo; only the text area changes).
2. **Object-past-lens wipe** (3 times): an object swings into the lens, fills the frame with motion blur, and a cut or
   scene change hides inside it.
   - f1495–1499: snake head into lens (5 f) → cut f1500.
   - f1665–1673: giant rubber band drops from the top and slides down past the lens (9 f), revealing the CGI sculpture.
   - f1742–1748: huge Nike GO shoe sweeps in from the top-left (7 f) → hard cut f1749 to the wide shoe + headline.
   - **Recipe:** 5–9 frames; the occluder covers >80% of the frame for ≥2 frames; directional blur ≈ 20–40 px@720 along the
     travel.
3. **Texture-scroll morph** (1×, f1500–1524, 25 f): a macro of the snake's segment grooves scrolls rapidly upward (a
   groove passes every ≈2–3 f). The material shifts wood (f1500–1503) → white (f1504–1506) → pink rubber (f1507+). The
   camera then pulls back (f1510–1524) to reveal that the grooves are the flex grooves of the Nike Free sole: a match-cut
   by surface pattern.
4. **Dip-through-dark + whip reveal** (1×):
   - f2072–2078: the camera tracks along the vintage waffle outsole until it fills the frame and goes dark (luma 78 → 16
     over 5 f, ≈ linear);
   - hard cut f2079 into a bright, heavily motion-blurred tilt-up that decelerates over 9 f (f2079–2087, ease-out) onto
     the NIKE WAFFLE hero.
5. **Caption cut-off before action** (1×, f1663): the caption vanishes on a still plate 2 frames before the transformation
   starts. In the other two cases the caption dies with the hard cut.
6. **End slate** (1×): hard cut f2147 from the colour product shot to the grey card (no fade). Tagline held 43 f (1.72 s);
   hard cut to the logo, held 44 f (1.76 s) to the final frame f2233. **No fade to black at the end.**
- Not observed in my range: dissolves/crossfades, paper wipes, torn-paper reveals, flash-cut montages, slides and push
  transitions. The fastest cut run is f2013–2016 (4-frame insert) → f2017.

## 8. Recurring devices
- **"This is not just a ___." pedestal card:**
  - one object on a white classical column (or a cardboard cabinet);
  - a single-colour studio with visible light stands;
  - the caption screen-locked at 52% H;
  - the word "not" materially distorted (eroded / bold-inked / brush-underlined);
  - a slow push-in of ≈2.6–2.7× in 2–2.5 s.
  - Used 4× in total (snake in part A; rubber band, bear and waffle iron in mine). The durations shrink: 2.64 s → 2.56 s →
    1.60 s.
- **"THIS IS / NIKE ___" headline card:** a two-line caps serif at the top, with line 2 eroded. It pops on at a cut or once
  the shoe resolves and holds until the next cut. Used 4× in my range, plus "THIS IS / A VISIONARY" and "NEVER DONE /
  BREAKING / THE MOLD." in part A.
- **"Broken mold" type distress:** erosion/ink bleed applied to exactly one word or line per text block. It is the
  campaign's visual metaphor and the main reusable graphic idea.
- **White brush stroke underline:** 2 variants, thin dotted-to-blob (rubber band) and thick impasto with a drip (waffle
  iron). Static, with no draw-on.
- **Colour-matched segments:** the backdrop hue carries from the pedestal shot through the transformation into the shoe
  hero.
- **Classical column / pedestal** as the "museum plinth" motif.
- **End slate pair:** tagline on textured grey card → 50-swoosh logo on the same card. This mirrors the 16:9 first half's
  ending ("Never done leaving a mark." → 50 logo, f1025–1108, part A).
- Not present in my range: highlighter, pencil scribbles, maps, pins, counters, tape, stickers, caption blocks, B&W
  archival photos, torn paper, black quote cards.

## 9. Scene log
| frames | time (s) | on screen | devices | motion / transition |
|---|---|---|---|---|
| (part A) f1350–1406 | 54.00–56.24 | pink/crimson studio, white column, toy snake, caption "This is not just a toy snake." | pedestal caption, eroded "not" | push-in; f1397–1406 near-hold |
| f1407–1435 | 56.28–57.40 | macro: toy snake head on crimson floor; a wooden fence/loom prop enters from the top | — | HARD CUT in; snake slithers, camera drifts (box diff 0.4 → 6, accelerating) |
| f1436–1457 | 57.44–58.28 | camera cranes up over a tangle of segmented snakes, loom with strings, wavy segmented "crown" | — | global move (box diff ≈26–30/f) |
| f1458–1494 | 58.32–59.76 | hold on the loom + coiled snakes; one snake head rises toward the lens | — | local motion (diff ≈11) |
| f1495–1499 | 59.80–59.96 | snake head swings into the lens, blurred, fills the frame | object-past-lens wipe | 5 f |
| f1500–1524 | 60.00–60.96 | macro grooves scroll; wood → white → pink rubber; pull back to the pink Nike Free sole | texture-scroll morph | hard cut f1500, then continuous; dup frame f1521 |
| f1525–1578 | 61.00–63.12 | pink Nike Free sole rotates to profile (dark upper, pink swoosh) on crimson; **"THIS IS / NIKE FREE" pops on f1530** | headline (line 2 eroded) | ease-out rotation; dup frames f1535/1550/1565 |
| f1579–1596 | 63.16–63.84 | frozen hero frame | headline | 18 f freeze hold |
| f1597–1662 | 63.88–66.48 | green-screen studio, LED tube lights on stands, column with a pile of coloured rubber bands; caption "This is not just a rubber band." | bold inky "not" + white dotted-to-blob brush underline | HARD CUT in; dolly push 2.62× (f1597–1657); freeze f1654–1662 |
| f1663–1664 | 66.52–66.56 | same plate, caption gone | — | caption 1-frame cut-off |
| f1665–1673 | 66.60–66.92 | a giant white/orange rubber band drops from the top past the lens | object-past-lens wipe | 9 f, motion blur |
| f1674–1741 | 66.96–69.64 | CGI sculpture: volt-yellow, salmon, lilac and white shoe parts bound by an orange band, black swoosh, on green | — | slow orbit; height 427 → 649 px (approach, to f1715), then 649 → 367 px (pull-back) |
| f1742–1748 | 69.68–69.92 | huge pale-yellow Nike GO sweeps in from the top-left and fills the frame | object-past-lens wipe | 7 f |
| f1749–1774 | 69.96–70.96 | yellow Nike GO FlyEase on green; **"THIS IS / NIKE GO"** | headline pops on the cut | HARD CUT; shoe recedes and settles; freeze f1770–1774 |
| f1775–1838 | 71.00–73.52 | petrol-blue studio, LED tubes, grey column with an orange teddy bear; caption "This is not just a bear." | eroded "not", no underline | HARD CUT; easeOutQuart push 2.68× over 52 f; freeze f1834–1838 |
| f1839–1879 | 73.56–75.16 | CGI: the bear's orange shell shatters into shards, revealing a white foam bear | — | HARD CUT; orbit, shards fly |
| f1880–1925 | 75.20–77.00 | foam bear; its legs fan into a stack of foam discs (Phylon) | — | HARD CUT; slow move |
| f1926–1972 | 77.04–78.88 | foam petals fold into a single white Phylon midsole rising through the title; debossed swoosh appears ≈f1960; **"THIS IS / NIKE PHYLON"** | headline pops on the cut | HARD CUT |
| f1973–2012 | 78.92–80.48 | oxblood room; cardboard kitchen-cabinet "pedestal" with a waffle iron and utensils; caption "This is not just a waffle iron." | eroded "not" + thick white impasto brush stroke | HARD CUT; slow creep |
| f2013–2016 | 80.52–80.64 | close-up of the waffle iron | — | HARD CUT; 4-frame insert (3 f hold) |
| f2017–2040 | 80.68–81.60 | giant waffle in a rust-patterned room; it cracks and waffles burst out | — | HARD CUT |
| f2041–2071 | 81.64–82.84 | waffle avalanche; a teal/yellow vintage Nike tumbles; camera follows | — | global, diff ≈25/f |
| f2072–2078 | 82.88–83.12 | tracking along the waffle outsole, which goes dark | dip-through-dark | luma 78 → 16 in 5 f |
| f2079–2087 | 83.16–83.48 | whip tilt-up past a blurred foreground slab onto the Nike Waffle One on a red waffle-iron/plate stand | whip reveal | HARD CUT; 9 f ease-out |
| f2088–2146 | 83.52–85.84 | hero: white/red/blue Nike Waffle One on tomato-orange; **"THIS IS / NIKE WAFFLE" pops on f2123** | headline | slow creep; freeze f2133–2146 |
| f2147–2189 | 85.88–87.56 | grey striated card, "Never done breaking the mold." | progressive erosion on "breaking the mold" | HARD CUT; live grain on ones |
| f2190–2233 | 87.60–89.32 | the same card, black Swoosh "50" logo centred | logo | HARD CUT; held to the end, no fade |

**Segment timing template** (from my range):

| segment | pedestal (caption) | transformation | object-wipe | shoe hero (headline) |
|---|---|---|---|---|
| rubber band | 68 f (66 f caption) | 77 f | 7 f | 26 f (26 f) |
| bear | 64 f | 41 + 46 f | — | 47 f (47 f) |
| waffle iron | 40 f | 4 + 62 f | dark-dip 7 f + whip 9 f | 59 f (24 f) |
| snake (from f1407) | — | 90 f | 4 f | 72 f (67 f) |

## 10. Replication recipes
```js
// R1 — vertical canvas inside 16:9
canvas = { w: 1080, h: 1920, fps: 25 }            // author natively at 9:16
deliver16x9 = { w: 1920, h: 1080, content: { w: 607.5, h: 1080, x: 656.25 }, bars: '#000000' }
// all type sizes below are given for 1080x1920 (multiply by 0.5625 for the pillarboxed 1080p column)

// R2 — segment backdrop palette (one per segment, radial falloff to corners ≈ -30% luma)
backdrops = {
  crimson: { centre: '#A91B49', edge: '#741331' },
  green:   { centre: '#579242', edge: '#33722E' },
  petrol:  { centre: '#0C6180', edge: '#051E45' },
  tomato:  { centre: '#D85730', edge: '#9B1512' },
}
radialVignette = { centre: [0.5, 0.45], innerStop: 0.25, outerStop: 0.95, darken: 0.30 }

// R3 — headline card "THIS IS / NIKE X"
headline = {
  font: 'Newsreader Display' /* Lyon/Tiempos-like book serif */, weight: 400, case: 'upper', align: 'center',
  capHeight: 92 /*px @1920v = 4.8% H*/, fontSize: ~135, lineHeight: 0.85 /*em; baseline pitch ≈ 1.22×cap = 113px*/,
  tracking: 0, top: 0.085 * H, color: mix('#FFFFFF', backdrop, 0.10),
  line2: { distress: { edgeDisplace: 2.5 /*px@1080w*/, noiseScale: 6, speckleInFill: 0.15, inkBleed: true } },
  in: { type: 'pop', frames: 1 }, out: { type: 'cut' },     // hold 24–67 f, screen-locked
  trigger: 'on hard cut OR ~5–35 f after the shoe settles',
}

// R4 — pedestal caption "This is not just a <object>."
caption = {
  font: 'Newsreader Text', weight: 400, case: 'sentence', align: 'center',
  capHeight: 41 /*px @1920v = 2.2% H*/, xHeight: 28, fontSize: ~60, baselineY: 0.525 * H,
  color: mix('#FFFFFF', backdrop, 0.10),
  emphasisWord: { text: 'not', variants: ['eroded-semibold', 'inkbled-bold', 'eroded-regular'] },
  underline: { kind: 'dryBrush', color: '#FFFFFF', thickness: [13, 19] /*px@1920v*/, offsetBelowBaseline: 8,
               startStyle: 'spray-dots', endStyle: 'round-blob', drawOn: false },
  in: 'present on first frame of shot', out: { type: 'cut', frames: 1 }, hold: [40, 66] /*frames*/,
}

// R5 — pedestal push-in
pushIn = { scaleFrom: 1.0, scaleTo: 2.65, frames: 52, ease: 'easeOutQuart', // bear variant (front-loaded)
           altVariant: { ease: 'linear-dolly + easeOut last 15f', frames: 60 }, // rubber-band variant
           tiltDown: 0.07 * H /* object drifts from 58% → 66% H */, thenHold: [5, 9] }

// R6 — object-past-lens wipe
objectWipe = { frames: [5, 9], coverage: '>80% for >=2 frames', motionBlur: { px: 30, dir: 'along travel' },
               cutHiddenAt: 'peak coverage frame' }

// R7 — dip-through-dark + whip reveal
dipWhip = { darken: { frames: 5, lumaFrom: 0.31, lumaTo: 0.06, ease: 'linear' }, cut: true,
            whip: { frames: 9, dir: 'tilt up', ease: 'easeOutCubic', blurStartPx: 60, blurEndPx: 0 } }

// R8 — end slate
endCard = { bg: '#C1C1C3', stripes: { orientation: 'vertical', amplitude: 1.1 /*luma levels std*/, periods: [9, 34, 45, 68, 81] /*px@720*/, static: true },
            grain: { sigma: 2.4 /*luma*/, regen: 'every frame' }, breathe: { amp: 1, periodSec: 3.5 },
            tagline: { text: 'Never done breaking the mold.', font: 'Newsreader Text', capHeight: 48 /*@1920v*/,
                       color: '#272829', baselineY: 0.507 * H, width: 0.76 * W,
                       distress: 'progressive left→right across "breaking the mold" (chipped → faded 50% → ink-bled)' },
            taglineFrames: 43, logo: { color: '#000000', width: 0.29 * W, centreY: 0.51 * H }, logoFrames: 44,
            transitions: 'hard cuts only; no fade-out at end' }

// R9 — end-of-shot freeze
freezeHold = { frames: [5, 18], rule: 'ease every move to a dead stop, hold, then hard cut' }
```

## 11. Uncertainties
- **Typeface identity:** the serif looks like Lyon / Tiempos / a Nike custom serif. I could not confirm it at 720p.
  Newsreader and Source Serif 4 are look-alikes, not matches. The distressed variants could be a separate "grunge" font or
  per-shot effects; the glyph shapes match the clean face, so I assume effects.
- **Text tint:** I cannot tell whether the white type was tinted by a grade, blended with "screen", or set at about 90%
  opacity. Only the resulting colours are measured.
- **Push-in curves:** these are inferred from the capital width of a 3D column under perspective and parallax, so they
  combine dolly and zoom. `motion.py` gave noisy shifts here (parallax from the foreground light stands); its easing fit
  (easeOutCubic) is weak evidence.
- **Duplicate frames** (every 14–15 f in NIKE FREE, every 3 f in the NIKE GO settle): I attribute them to retiming or
  frame-rate conversion of the source clips, not to a deliberate stepped cadence.
- **End-card grain:** it might be encoder noise on a filmed paper card rather than an added grain layer. Either way it is
  ≈σ 2.4 levels and refreshes every frame.
- **The toy-snake pedestal shot** (f1350–1406) and the start of the 9:16 section (f1109) belong to part A. My statements
  about the snake caption come from one frame (f1400) only.
- **CGI internals** (shard counts, physics) were described, not measured. They are product renders rather than
  reproducible motion-graphics.
