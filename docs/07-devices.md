# 07 · Devices (component catalogue)

Every recurring graphic device in the references, with its anatomy, measurements and a
frame-by-frame build. Frames are at 30 fps on the 12 fps drawing clock (steps of 2,3,2,3) unless
marked *(ones)*. Sizes are px at 1080p. Each device maps to a component in
`09-implementation.md`.

| # | Device | Dialect |
|---|---|---|
| D1 | Highlighter box (cursor → wipe) | A |
| D2 | Highlight on print | A |
| D3 | Callout: disc + leader + label | A |
| D4 | Map callout + city outline | A |
| D5 | Portrait pair + name label | A |
| D6 | Footage caption with spinning ▶ | A |
| D7 | Keyword montage window | A |
| D8 | Year counter | A |
| D9 | Glowing timeline | A |
| D10 | Model / product card | A |
| D11 | Quote card + end card | A |
| D12 | Charts | A |
| D13 | Slideshow, carousel, framed footage | A |
| D14 | Slot-machine word reel | A |
| D15 | 2.5D world-space text | A |
| D16 | Desk mood board | A |
| D17 | Hand-drawn annotations | A B C |
| D18 | Chapter title on crumpled paper | A |
| D19 | Oversized headline + ink-bleed line | B |
| D20 | Archive caption block + stamp | B |
| D21 | Crayon scribbles, stencil letters, style boil | B |
| D22 | Step-and-repeat echo, flash montage | B |
| D23 | Black quote card | B |
| D24 | Brand-film type devices | E |
| D25 | Pastel spotlight shapes | C |
| D26 | Stepped headline + underscore | C |
| D27 | Brush label bar, paper slip | C |
| D28 | Doodles: arrows, sparkles, bolts | C |
| D29 | Hands, magnifier lens, living loops | C (A for x-ray) |
| D30 | Ransom-note display word | C |
| D31 | Postcard kit | D |

---

## D1 · Highlighter box (cursor → wipe)

**Anatomy:** an opaque accent rectangle with square corners and no texture, padding ≈ 0.4–0.5 ×
cap height, dark serif text. Optionally a down-pointing tail (map labels only).

**Build:**
| f | Event |
|---|---|
| 0 | cursor bar appears: **8–24 px** wide, full box height |
| 0 → 1…17 | cursor holds (1–5 f usually; up to 17 f for a "thinking" beat) |
| hold → +20…29 | right edge grows with `wipe` (easeInOutCubic). Fraction of width per 12 fps step: `.03 .06 .11 .17 .26 .52 .79 .87 .91 .96 .98 1.0` |
| — | text is **masked by the box** (cut mid-glyph at the edge) **or** already visible with the box sliding in behind it |
| exit | right edge retracts right to left over 13 f (easeInCubic) while the text fades, or the box leaves with the scene |

Variants: title box (138 px tall, 95–100 px type, 22–29 f); callout label (102 px, 69 px italic,
wipes **right to left** from the leader-line end, 8–10 f); map label (162 px, 84 px bold caps,
16–22 f *(ones)*); price highlight behind visible text (165 px, easeOutCubic 20 f); year
highlight (243 px tall, 25 f).

## D2 · Highlight on print

A **multiply** accent rectangle over existing printed words (newspaper, article, brochure). Its
height is the line box plus 3–6 px of overhang; it may overshoot the word end slightly.
Headline highlights wipe in 20 f (easeInOutCubic), body text 27 f (an accelerating ease-in),
newsprint 10 f *(ones)*. A second highlight starts **9 f after** the first ends. Pair it with a
Ken Burns push (up to 3.3× over 50 f, easeInOutCubic) onto the paragraph.

## D3 · Callout: disc + leader line + label

| Step | Spec | Frames |
|---|---|---|
| 1. Disc | multiply accent circle, Ø **32–52 % H**, hard edge. Either scales from 0 in place, or flies in from a frame edge along a gentle curve while scaling 0.2 → 1 (travel ≈ 50 % H) | 7–13 f, easeOutCubic |
| 2. Leader line | `#1A1A1A`, **3–4 px**, from inside the disc: a 45° diagonal, then horizontal toward the label | ≈ 5 f (2 steps) |
| 3. Label | D1 box, 102 px, italic lower-case text, anchored at the line end and wiping **right to left** | 8–10 f |
| 4. Hold | — | 15–30 f |
| 5. Exit | the whole scene slides out left (−7 %, then −44 % W, ease-in) or is pushed | 3–5 f |

The steps never overlap. The whole build takes ≈ 22 f.

## D4 · Map callout + city outline

1. Map push-in: log-zoom **28.5× in 63 f** *(ones)*, about 65 % accelerating, with motion blur.
2. City boundary: accent stroke **6 px** with a 6 px glow, drawn as a trim path over **30 f**
   (easeInOutSine).
3. Label: the text fades in over 5 f, then a D1 box wipes in behind it (22 f *(ones)*); the tail
   pops at about 60 % of the wipe.
4. Exit: the box retracts right to left over 13 f.

The opening variant is a log zoom-out of **7.9× over 116 f** (easeOutExpo), with rounded video
cards (2 px cream border, soft shadow) playing on the map.

## D5 · Portrait pair + name label

Two rectangular B&W portraits (each ≈ 31 % W × 68 % H, symmetric, bottom at 87 % H) **rise out
of a mask at their own bottom edge** by their full height in **17 f** (easeInOutCubic, *ones*).
The second starts **+7 f** later. The map behind is darkened about 40 %. A two-line bold name
label (D1, 450 × 192 px) wipes in the centre column.

## D6 · Footage caption with spinning ▶

| f | Event |
|---|---|
| 0 | ▲ (54–60 px, accent or black) starts **135 px below** the frame edge at 10 % W |
| 0–7 | rises into place, easeOutCubic |
| 7–19 | rotates **−270°** (▲ → ◀ → ▼ → ▶), ease-out |
| 17–24 | caption text fades 0 → 1 (linear), optionally rising 2–6 px |
| … | hold |
| end −6 → end | text fades out, ending on the cut |

The text is Gelasio Bold Italic 52 px, accent `#E8F010` on dark footage or `#3B2A1C` on bright
footage, baseline at 90 % H. When the next shot continues the sentence, keep the ▶, cut the text
and fade the new text in over 6 f.

## D7 · Keyword montage window (cold open)

Footage plays in a **75 % W × 75 % H rounded window** (r 33 px, top 6 % H). Behind it is the same
clip scaled 1.15, blurred 20 px, at 35 % brightness, with ±3 px RGB split. Below the window: an
accent ▶ (D6 spin) and a white italic keyword (88 px) in a **mask slot** at 90 % H. Each word
rolls up into the slot over 9 f (easeOutCubic, 105 px travel) and leaves upward over 4 f
(easeInCubic). **Words change 3–6 f before each footage cut.** Typical words: *passion, speed,
innovation, style, quality*.

## D8 · Year counter

A cool paper card (`#E9E7DB`, vignette −19 %). The numeral (Playfair 144 px, `#6B6361`) counts
from *now* back to the target year in **12 steps on the 12 fps clock**, with the value gaps
eased in and out. Example: `2024 2018 2007 1994 1980 1965 1951 1936 1923 1911 1903 1900` at
f `0 3 5 8 10 13 15 18 20 23 25 28`. The numeral scales 0.79 → 1.0 over the first 3 steps. The D1
cursor appears at step 9 while it is still counting; the box (558 × 243 px) wipes in as it lands.

A simpler chapter card: an aged photo-card stack with a sepia numeral (140 px), and an accent
marker underline (18 px thick, 1.68× the text width) drawn left to right in 7 f.

## D9 · Glowing timeline

On a `#080705` background with a faint map at 6 %, a thin rule at **59 % H** (2 px core, 18 px
glow, x 22–77 % W). Each year pops at a new x along the line (fade 1–2 f, hold 5–8 f, fade out;
1–3 blank frames between), with an 18 px ring-dot under it. About 7 f per year. The final year
**slides to the centre** over 10 f (easeOutCubic). Next, a photo card slides in from the right
over the timeline (10 f, ease-out).

## D10 · Model / product card

| f (from cut) | Event |
|---|---|
| 0 | cut onto paper; the product cut-out is about 90 % in place, offset +75…190 px right |
| 0–7 | product settles left, `settle` (easeOutCubic). Taycan variant: scale 0.79 → 1.0 |
| 7–20 | read beat |
| ≈ 9–20 | D1 title box: cursor, then wipe over 20–29 f; text masked |
| box start + 5…8 | subtitle wipe left to right (feather 45 px), 12–15 f, finishing ≈ 10 f before the box |
| … | hold with 6 Hz weave, about 2 s in total |
| last 3–5 f | product shrinks to 0.88–0.95× (ease-in), or the scene pushes +7 %, then hard cut to footage |

Used 9× identically in the Porsche reference. **Keep it pixel-identical every time.**

## D11 · Quote card (Archive) and end card

**Mid-film quote:** a B&W cut-out portrait with an accent offset shadow (+18 px) scales **1.6 →
1.0** while moving into the bottom-right over 14 f (easeInOutQuad). Starting as the figure
settles, the quote reveals **word by word every 2.5 f** (25 → 100 % fade over 3–5 f, small
rise). It is fully justified Gelasio Italic 56 px, `#3A292C`, 38 % W wide. The bold attribution
follows 6 f after the last word. Hold about 1 s.

**End card:**
| f | Event |
|---|---|
| 0 | cut to grid paper (`#F4EBE2`, 35 px grid, vignette) |
| 3–21 | crop marks draw out from their corners (2 Ls, 5 px, 45 % ink) |
| 3–43 | B&W portrait slides in from the right, 40 f, easeOutQuart; an accent silhouette copy lags 4–6 f and settles as a 9–15 px rim |
| 6–56 | quote types at **34 characters/s**, each new character fading in over 2 f |
| 56–76 | attribution types at 45 characters/s |
| +30 | hold |
| → +49 | **linear fade to black**, then 23 f of black |

## D12 · Charts

- **Bar chart on paper:** accent gridlines (8 px; the baseline 12 px), bars `#31312F` 77 px wide
  at a 127 px pitch with 6 px rounded tops. The chart enters at 0.83× → 1.0 over 7 f. Bars grow
  from the baseline **5 f apart**, each over 13–18 f with easeOutCubic. Value labels (small,
  reddish) pop on as each bar finishes. Then a red marker circle draws around the key bars (D17)
  and the chart slides out left (ease-in) into a cut.
- **Blueprint line chart on dark:** white serif axes (6 px) with an 18 px glow over a faint
  technical drawing. The accent data line (6 px, 9 px glow) draws left to right **linearly over
  73 f** while the accent title types at about 1 character per 1.2 f.

## D13 · Slideshow, carousel, framed footage

- **Photo drop slideshow:** 1 photo per **30 f**, centred at 70–76 % W, with an accent offset rim
  (+6, +6 px) and 24 px rounded corners. Each photo eases to rest over 8 f (from 0.87–0.92× or
  1.12–1.21×, alternating), holds 14 f, then eases away over 6–7 f. The cut lands mid-move (T4).
- **Carousel:** rounded cards at 75 % W × 88 % H with a 10 % W gap; the strip advances one card
  every **20 f** in 7 f (easeInOutCubic). The first card arrives with a stepped zoom-out from 1.75×.
- **Framed footage:** a 90 % W rounded rect (r 9 px, 1 px dark edge, accent offset rim) slides
  in from +10 % W over 6 f *(ones)*. The footage cuts inside the frame while the frame stays.
- **3D print carousel** (dark): Polaroid-style prints (cream border; the bottom is 2.4× thicker)
  at different depths with depth-of-field blur. The camera trucks right about 2 frame widths in
  51 f (easeInOutSine), then pulls back to a 2-over-3 mosaic.

## D14 · Slot-machine word reel

Inside a CRT frame (bezel `#1A1712`, screen `#D4CBBD` with a vignette), a column of serif words
(54 px Bold, 111 px pitch) sits ghosted at 12 % opacity.
1. A 1 px cursor holds for 17 f.
2. A focus window (4 px outline) grows from the cursor to 636 × 126 px over 30 f (easeInOutCubic).
3. Meanwhile the reel spins **down** about 6 words over 35 f (ease in-out) and **lands on the
   keyword** ("Legacy").
4. A dry-brush accent highlighter paints left to right behind it over 27 f.
5. Punch-in 1.0 → 1.35 over 12 f (easeOutCubic); creep to 1.46 stepped every 5 f; then an
   accelerating zoom to 1.64 over 8 f into a zoom-through cut.

## D15 · 2.5D world-space text

On a still photo with layers *plate → text → cut-out foreground*, the text sits in world space
**behind** the foreground objects. The camera pushes 1.0 → 1.16 over 8 f, then tilts up and pulls
back (foreground moves down 222 px, 0.84×) to reveal the year from behind the roofs. Hold 1.4 s.
It then tilts down and pushes in (×1.45) so the year scrolls out the top and a price scrolls in
from the bottom, where a D1 box (easeOutCubic 20 f) highlights it. Exit by zoom-through.

## D16 · Desk mood board

A top-down `#E4DBD3` desk with prints (18 px cream border, shadow 7/7/9 px at 35 %, rotated
−12…+10°), accent tape, stamp-edged serif labels, pencils and clippings. The camera pans in a 12 fps
zig-zag at **36–52 px per frame**, about 1.2 s per group, with momentum carried in from the
previous zoom-through. It ends with a pull-back to 0.76× and a cut.

## D17 · Hand-drawn annotations

| Mark | Draw | Timing |
|---|---|---|
| Circle around a face | 2 offset strokes, accent, clockwise from 11 o'clock | on 17 f, **off 8 f** before the cut |
| Chart circle | red marker, from 6 o'clock clockwise, open loop overshooting the start | 11 f |
| Ellipse around a year | black dry brush 18–30 px, clockwise from the upper left | 5 f |
| Underline | accent marker, left to right, tapered | 7–20 f, easeOutCubic |
| Quote-card underline | orange `#B04C35`, 5 px, 785 px long, 50 px below the line | 20 f@25 (0.8 s), easeOutCubic |
| Pen rectangle | black 3 px, corner first, corners overshoot | ≈ 34 f |
| Red X | "\\" then "/", multiply | 3 × 4 f |
| Crop marks | Ls grow from their corners | 18 f |
| Trim-path outline | accent 6 px + glow | 30 f |

## D18 · Chapter title on crumpled paper

A crumpled-paper wipe pushes up from the bottom in stop-motion steps (T6) and becomes the card.
Inside a dashed rectangle (69 % W × 36 % H; dashes 90 px long at a 93 px pitch, 6 px thick, open
corners, `#786E65`), the line types **one character per frame**: "But the true *revolution* /
came in **1963**". The italic keyword is part of the sentence; the year then gets a D1 highlight
(10 f *(ones)*).

## D19 · Oversized headline + ink-bleed line (Ink & Paper)

Line 1 is EB Garamond caps with cap height **156–257 px**, tracking −2 %, its **top cut by the
frame edge**, typed **1 letter per 2 f**. Line 2 is the same face with ink-bleed (blobs and drips
at the stroke ends), 98 % W, typed **1 word per 4 f** starting when line 1 completes. The camera
pushes in slowly (+0.05 %/f on twos). Exit: words are erased in reverse (1 per 2 f) while a
crumple reveal (T6) or an accelerating pull-back (to 0.818×, easeInCubic) takes over.

## D20 · Archive caption block + stamp (Ink & Paper)

The caption block is Inter 400 with cap 24 px and line 32 px, in two columns at 2.3 % W / 15.2 % W,
bottom-left:
```
Year:     Story::      Dept. of
1971      Swoosh       Nike Archives
From a simple logo
for the next symbol of inspiration.
```
Fields **type at the same time** (2–3 characters per drawing, starts staggered 0 / 15 / 23 f), each
with a trailing `_` cursor on its active line. The **stamp** ("Department of / Nike Archives",
Inter 500, a 150 px rule and a hand-drawn outline swoosh across it) sits bottom-right and
resolves from **randomly ordered letters over about 30 f**.

## D21 · Crayon scribbles, stencil letters, style boil (Ink & Paper)

- **Scribbles:** 1–3 orange pencil strokes alive at once across the 35–80 % H band (see
  `05-motion.md` §7). A new stroke spawns every 2–4 drawings.
- **Stencil letters:** single rounded orange letters (D, Z, A, N, up to 120 px) **pop on at full
  size** in one drawing, then jump between positions and scales every 2–3 f (the group snaps to
  0.5×, then the letters rearrange).
- **Style boil:** each drawing **replaces** the motif with a version in a different medium
  (outline, stipple, zig-zag scribble, dry brush, ink dots, smooth gradient); on ones during a
  climax. Big black brush strokes sweep across in 2–4 drawings to clear it.

## D22 · Step-and-repeat echo, flash montage (Ink & Paper)

- **Echo row:** copies of a photo or motif are added **one per drawing** (MJ ×5 offset 90 px;
  swoosh row 285 px apart, alternating solid `#EB421A` and grainy `#F1AE9F` at 35 % stipple).
  Copies are removed one per drawing from the back. Muybridge runner strips gain one figure per
  drawing.
- **Flash montage:** see `06-transitions.md` T15.

## D23 · Black quote card (Ink & Paper)

`#010101` with boiling dust. Cream `#E9E9D0` EB Garamond caps with cap height 117 px, pitch 152 px,
a left-aligned block centred on the frame: `WELL, / I DON'T / LOVE IT.`, with the last line
ink-bled. Letters type every 2 f; the last line arrives by word. An orange underline (`#B04C35`,
5 px) wipes left to right in 20 f@25 (easeOutCubic). The card shrinks slowly (−0.2 %/f) during the
hold, then exits by scaling 1 → 0.70 over 4 drawings (easeInQuad) and clearing. Chalk handwriting
(`#B8B8B8`) can follow on the same black, written about 1 letter per 2 f.

## D24 · Brand-film type devices (reference E)

- **Distressed emphasis word:** in "This is **not** just a …", one word gets a material
  treatment (eroded, ink-bled bold, white dry-brush underline or impasto stroke) while the rest
  stays clean. Captions are present on the first frame and cut off in 1 frame.
- **Pop-on headline:** "THIS IS / NIKE ___", 2 lines of caps (cap 4.8 % H), line 2 eroded. It
  pops on in 1 frame (on a cut or 5–35 f after the product settles) and leaves on the cut.
- **End slate:** grey card `#C1C1C3` with static vertical striation and grain σ 2.4. The tagline
  erodes progressively left to right ("Never done **breaking the mold**."), holds 43 f, then a hard
  cut to the logo held 44 f to the end. No fade.

## D25 · Pastel spotlight shapes (Scrapbook)

Behind every hero cut-out sits a flat pastel shape: a salmon grid-paper circle (Ø ≈ 65 % H,
`#FAC9BE` with a red grid), a salmon half-disc or 3/4 disc (`#E4ADA2`), a pale-green circle or
wedge (`#BFD4B3`, multiply, about 70 %), or a mint semicircle (`#AEE192`) growing from the bottom
edge. They enter by **scaling from the centre over 2–4 drawings**, or a wedge **rotates open
about 30°** while scaling 0.3 → 1. A split circle (half B&W scan texture, half pale green) grows
0.3 → 1 over 3 drawings.

## D26 · Stepped headline + underscore (Scrapbook)

Inter 700 at 122 px, line-height 0.93, `#121213`, sentence case ending with a full stop, 2–3
lines of 1–2 words, set in the empty third. Enters with the **stepped drop-in** (1.85× → 1.27× →
1.0×, held 8 and 5 f) or rides in on its paper sheet. The key word on the last line may carry a
static `_` prefix: `Safe & / predictable / _investment.` A pose over a dark photo switches to white.

## D27 · Brush label bar, paper slip (Scrapbook)

- **Brush label:** a black dry-brush bar (80 px) with Inter 600 caps (cap 34 px, tracking +10 %,
  white) centred. Revealed by a **hard left-to-right mask in 3 drawings (25 % → 70 % → 100 %)**.
  A second label follows 13 f later (PRINCIPAL → INTEREST).
- **Paper slip:** a torn white slip rotated −3°, red lower-case text, dithered shadow. It pops on
  in one drawing.

## D28 · Doodles: arrows, sparkles, bolts

- **Thin arrow** (2.5 px, open V head): draws on over 3–4 drawings with the stroke end
  **overshooting about 10 %** then snapping back; it holds about 0.7 s, disappears for 1 drawing
  and redraws (loop). Point it at the subject: → ↑ ↓.
- **Sparkle ✧, crosshair +, ×:** appear in one drawing and nudge ±3–9 px on every boil.
- **Lightning bolt pair** (schaapening): a big bolt (160–240 px) and a small one (0.45×) pop from a
  speck over 2–3 steps; thin "zap" squiggles redraw at a new random place every step; ±6 px jitter.

## D29 · Hands, magnifier lens, living loops

- **Hands:** B&W hand cut-outs cropped at the wrist enter from a frame edge (3–4 drawings), give,
  pick or pull something, then leave the way they came. A picked object turns from B&W to colour
  and tilts 10–15°.
- **Magnifier lens:** a B&W magnifier cut-out sweeps across content; **inside the lens the content
  is really magnified about 1.6×** (Scrapbook). The Archive variant is an **x-ray**: the lens
  shows a different masked image (engine bay, cabin) while sweeping left to right at 14 px/f in
  12 fps steps.
- **Living loops:** money flying along an arc every 25 f (6–8 curl drawings); dotted water arcs
  growing from a spout; bills sprouting 3–6 per drawing; a balloon inflating in 3 pump pulses and
  popping in 2 frames of shards; a cut-out mirror-flipping as a "head turn".

## D30 · Ransom-note display word (Scrapbook)

Oswald 700 caps with cap height 236–294 px in the shot's spot colour, letters placed
individually (baseline jitter ±7 % H, tilt ±8°), crossing the frame **behind** the hero cut-out
and bleeding off both edges. Letters fly in horizontally from the nearest side at about 30 px/f,
easing over the last 2 steps, with **staggered starts and a common landing frame**. They arrive
tilted 5–20° and straighten. Variant: letters start scattered, low and rotated 25–60°, then
converge, rise and straighten over 33–45 f (easeOutExpo, 8 fps).

## D31 · Postcard kit (dialect D)

- **Camera:** a single constant-speed dolly-out (1/scale linear) with per-layer depth `k`
  (paper 1.28, landmark 1.0, sun 0.9, vehicles 0.66–0.85), pivot at (50 % W, 14 % H). Nearer
  layers rise into view from the bottom edge.
- **Sun disc:** flat accent circle (Ø 50 % H) centred behind the top of the landmark, scaling
  0 → 1 linearly over 1 s.
- **Cut-outs:** landmark with a 13 px accent outline; foreground objects with a 14 px white
  sticker border. No shadows.
- **Bird flock:** black silhouettes flapping on ones while the camera moves, frozen when it stops.
- **Title:** per-grapheme slide and fade (5 f each, 10–11 f apart), starting 4 f after the camera
  stops.
- **Idle:** independent wiggle per cut-out at 0.8 Hz, ±4–8 px.
