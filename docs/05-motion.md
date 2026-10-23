# 05 · Motion

Motion is what makes this style read as hand-made editorial collage rather than slick
corporate motion graphics. Four rules carry most of the effect:

1. **Graphics move at 12 drawings per second; cameras and footage move at full rate.**
2. **Nothing that has landed is perfectly still.** It jitters, boils or wiggles.
3. **Entrances are fast ease-outs with no overshoot. Exits are short ease-ins straight into a cut.**
4. **Every highlight, box and stroke starts as a thin cursor or a point, then grows.**

All numbers below were measured frame by frame on the reference videos. Frames are given at
**30 fps** unless marked otherwise, with seconds alongside. Distances are **px at 1920×1080**.

---

## 1. Cadence: the 12 fps drawing clock

| What | Cadence | Evidence |
|---|---|---|
| Graphic elements on paper (boxes, type-on, cut-outs, strokes, charts, carousel, stepped zooms) | **12 fps** | Porsche, Nike Swoosh and wallfive all change on a 2-3-2-3 frame pattern at 30 fps, or 2-2-…-3 at 25 fps |
| Stop-motion scrapbook shots | **12 fps**, sometimes **8 fps** | schaapening: 12 fps in shot 1, 8 fps (gaps 4,4,4,3) in shots 2–3 |
| Camera moves on maps, live footage, footage zooms, map labels | **on ones** (every frame) | Porsche map zooms, Taycan footage |
| Long slow push-ins on graphics, and the hold jitter | **6 fps** (every 5 frames at 30) | Porsche CRT creep, hold weave |
| Smooth postcard collage (dialect D) | **on ones** | mdriturana |

**Rule:** compute every graphic animation from a *stepped* frame, never from the raw frame. One
clock per scene; all graphic layers share it so they step together.

```ts
// Works for any output fps: 30 → gaps 2,3,2,3 · 25 → 2×11 + one 3 · 24 → 2 · 60 → 5
export const stepFrame = (frame: number, fps: number, drawingsPerSec = 12) =>
  Math.floor(Math.floor((frame * drawingsPerSec) / fps) * fps / drawingsPerSec);
```

There is **no motion blur** on stepped graphics: each drawing is crisp. Motion blur appears
only on full-rate camera moves (map zooms, whip pans) and in live footage.

---

## 2. Idle: nothing that has landed is perfectly still

Pick **one** idle behaviour per dialect and apply it to every landed graphic layer. The paper
background is excluded unless the idle is a paper boil.

| Idle type | Parameters | Used in |
|---|---|---|
| **Hold jitter ("weave")** | Every **5 frames (6 Hz)**, each graphic layer gets a new random offset of **±0.5–3 px** and scale **±0.2–0.5 %**. Text layers jitter about 1.5× more than images. The paper stays fixed. No rotation. | Archive (Porsche): every held model card, map, card and quote |
| **Paper boil** | The whole paper scan is swapped for a different scan every **3–4 frames (~8 fps)**. Specks and fibres change; amplitude 1–6/255. Black cards boil their dust the same way. | Ink & Paper (Nike Swoosh) |
| **Drawing boil** | A line drawing alternates between 3–4 hand-redrawn versions on 12 fps steps. | Nike Swoosh (Air Max sketch, swoosh "style boil") |
| **Prop boil** | Every **15 f (0.5 s)**, the crumpled-paper crease overlay is swapped or re-offset, and loose props get new offsets: sparkles and tape **±3–9 px**, loose props up to ±30 px, ±1.5°. Headlines and hero photos stay **pixel-locked**. Busy shots boil every 7–8 f. | Scrapbook (wallfive) |
| **Stop-motion jitter** | Every animation step, a cut-out shifts **±3–8 px** (it can also squash ±1–2 %). Doodle squiggles redraw at a new random spot each step. | Scrapbook (schaapening) |
| **Living loops** | A small action repeats like a GIF: an arrow redraws every ~25 f, a bill flies along an arc every ~25 f, a hanging object swings and bobs (±42 px x, ±75 px y, rotation ≤ ±2°, sine-like, period 1.5–2 s) sampled on the 12 fps ticks, or a cut-out mirror-flips briefly as a cheap "head turn". | Scrapbook (wallfive) |
| **Smooth wiggle** | Per-layer independent position noise at **0.7–1 Hz, ±4–8 px**, translation only, on ones. The front-most layer moves most. Sun, title, birds and paper don't move. | Postcard (mdriturana) |
| **Slow scale drift** | **+0.1–0.25 % per frame** push or pull, stepped on the drawing clock. | Nike Swoosh title cards, schaapening (about +1 %/s) |

---

## 3. Easing tokens

Use these names everywhere (code, storyboards, reviews). They are fitted from measured curves.

| Token | Curve | Typical duration | Used for |
|---|---|---|---|
| `wipe` | easeInOutCubic: slow start, peak speed at 50–60 %, long settle | 20–29 f (0.67–0.97 s) | highlighter boxes, title boxes, focus windows |
| `wipeFast` | easeInOutCubic | 10–16 f | highlighter on newsprint, map labels |
| `settle` | easeOutCubic | 6–8 f (0.2–0.27 s) | car/cut-out slide into place, photo drop, slide-in |
| `land` | easeOutQuart | 30 f (1 s) | hero rising from below, portrait slide-in (40 f) |
| `punchOut` | easeOutExpo | 15 f (stepped) to 64 f | cut to an over-scaled hero, then zoom out to rest |
| `reveal` | easeInOutQuad, stepped | 12–15 f | stepped zoom-out reveal of a new still from 1.7–2× |
| `underline` | easeOutCubic | 7–20 f | marker underline, price highlight behind visible text |
| `exit` | easeInCubic / easeInQuad | 3–8 f | pull-back to 0.70–0.95× or push +5–19 %, then hard cut |
| `pop` | easeOutBack, s≈1 (6 % overshoot) to s≈3 (23 %) | 12–20 f | Scrapbook objects (house, laptop); in Archive, at most one photo pop per piece (about 15 %) |
| `push` | easeInExpo out, then easeOutQuint/Expo in | 8–12 f out, 27–36 f in | Scrapbook push transitions (see Transitions T19) |
| `linear` | linear | — | fades (captions 8–9 f, fade to black 49 f), chart line draw, sun scale, constant-speed dolly |
| `logZoom` | ease applied to **log(scale)** | 63–116 f | map zooms (an asymmetric in-out going in, easeOutExpo going out) |

**Overshoot depends on the dialect.** In Archive and Ink & Paper, everything lands with a hard
stop; one photo pop at about 15 % is the only exception in 4.5 minutes of footage. Scrapbook is
more playful: object pops overshoot 6–23 %, and one emphasis move goes big, holds, then settles
(0.6 → **1.67×** in 8 f, hold 8–10 f, → 1.0 in 10 f). Even there, type, paper and photos never
bounce.

---

## 4. Entrances

| Entrance | Spec | Notes |
|---|---|---|
| **Cursor then wipe** (boxes, highlights, windows) | A thin bar (**8–24 px wide**, full box height) appears in 1 frame and holds **1–17 frames**. The right edge then grows with `wipe`. Text inside is revealed by a **hard mask at the box edge**, so letters are cut mid-glyph. | Every highlight in Porsche. Measured widths in 12 fps steps, as a fraction of final width: `.03 .06 .11 .17 .26 .52 .79 .87 .91 .96 .98 1.0` |
| **Slide-settle** (cut-out cars, illustrations, cards) | The element is already at about 90 % of its final position at the cut. It slides the last **4–10 % W** (75–190 px) in **6–8 f**, `settle`. Direction is usually from the right. | Model cards: about +100 px → 0 in 7 f |
| **Stepped zoom-out reveal** (new still photo or page) | It cuts in **1.7–2.0×** too tight, then steps out to 1.0 over **12–15 f** on the 12 fps clock (step sizes small, large, small), anchored on the subject. No blur. | Porsche, 4 times in the first minute |
| **Hero punch-out** (scrapbook) | Cut to the hero at **1.4–2.4×**, hold one step (4–5 f), then `punchOut` to 1.0 in 15–64 f, pivoting on the hero centre. | schaapening jukebox and radio |
| **Rise from below** | The element rises from **+70 % H** below to rest in **30 f** with `land`, on 12 fps steps. | schaapening cafe |
| **Portrait rise through a mask** | It slides up out of a horizontal mask at its own bottom edge over its full height in **17 f**, easeInOutCubic. The second portrait follows **+7 f** later. | Porsche portrait pair |
| **Photo drop** | The incoming print starts at **1.15–1.2×** and settles to 1.0 in **5–7 f**, `settle`. | Porsche slideshows |
| **Scale from zero** (discs, suns, doodles) | Linear or ease-out. Discs take **7–13 f**, a sun disc **1 s linear**, lightning bolts **2–3 steps** from a speck. | |
| **Stepped headline drop-in** | The headline appears fully set but **oversized and displaced**, then jumps with no in-betweens through 3 poses: **1.85×** (offset +17 % W, +12 % H) held 8 f → **1.27×** held 5 f (it may be cropped by the frame edge) → **1.0×** at rest. About 13 f in total. If a pose overlaps a dark photo, that pose is set in white. | wallfive: "Be the Bank.", "Robert Hytha" |
| **Spin-in** (paper props: contract, cheque) | Scale **0.25 → 1.0** while rotating **−10° → −3°**, 8–10 f, easeOutQuart, with a dithered shadow. | wallfive |
| **Slide-in with parallax** | Layers of the incoming collage start under the cut and arrive at different speeds. The paper sheet takes **28 f** (easeOutQuint) and travels ≥51 % W; the hero object takes **36 f** (easeOutExpo, slower). The headline rides on its sheet. Small props pop on 2–5 f later. | wallfive |
| **Hand from the edge** | A B&W hand cut-out enters from a frame edge in 3–4 drawings (ease-out), acts, then leaves through the same edge (ease-in). | wallfive |
| **Pop on** (type in brand films, logos) | Present at full size in 1 frame. | Nike end slate, headline cards |
| **Per-glyph slide and fade** | Each grapheme cluster rises **one glyph height** while fading 0→1 over **5 f** with an ease-in. Clusters are **10–11 f** apart. | mdriturana Bengali title |

## 5. Type-on rates

| Text kind | Unit | Rate |
|---|---|---|
| Hero serif headline, line 1 | letter | 1 letter per **2 f** (1 drawing) |
| Hero serif headline, ink-bleed line 2 | word | 1 word per **4 f** (2 drawings) |
| Big single word ("MOVEMENT") | letter | 1 letter per **4 f** |
| Black quote card | letter, last line by word | 1 letter per 2 f |
| Archive caption block (sans) | characters, with a trailing `_` cursor | **2–3 characters per drawing** (about 30 characters/s); several fields type at once with staggered starts (0, 15 and 23 f) |
| End-card quote (italic serif) | character, newest one fades in over 2 f | **34 characters/s**; attribution 45 characters/s |
| Justified italic quote | word, fading 25 %→100 % over 3–5 f with a slight rise | 1 word per **2.5 f** |
| Chapter title on crumpled paper | character pop | 1 character per frame |
| Scrambled stamp | letters appear in random order | about 30 f to resolve |

Text **never slides in** as a block and never fades in as a whole paragraph, except for footage
captions (below).

## 6. Footage captions (lower third)

1. A **▶ bullet** rises from below the frame (about 45–60 px@360 source, i.e. 135 px@1080) in **6–8 f**, with `settle`.
2. It **rotates 270° counter-clockwise** (▲ → ◀ → ▼ → ▶) over **10–14 f**, ease-out.
3. The caption line **fades in over 5–9 f** (linear), with an optional 2–6 px rise.
4. Fade-out takes 6 f and ends on the cut. If the next shot continues the sentence, the ▶ stays, the old text cuts out and the new text fades in over 6 f.

## 7. Hand-drawn strokes

| Stroke | Spec |
|---|---|
| **Circle around a face** | Two slightly offset overlapping strokes. Drawn clockwise from about 11 o'clock in **17 f**; **un-drawn in 8 f** right before the cut. |
| **Chart circle** (red marker) | Starts at 6 o'clock, clockwise, about 11 f; the loop is left open with a slight overshoot past the start. |
| **Ellipse around a year** | Black dry brush, clockwise from the upper left, **5 f**. |
| **Underline** | Left to right, 7–20 f, `underline`; tapered and thicker at the start. |
| **Pencil/crayon scribble** | Trim-path write-on: the head advances **300–450 px per drawing**. It holds 2–4 drawings, then the **tail chases the head** until the stroke disappears. Lifespan 12–16 f; 1–3 strokes alive at once. Existing strokes never jitter. |
| **Pen rectangle** | Corner-first: one corner, then its two edges, then the opposite edges. About 34 f for a 1550 px perimeter. Corners overshoot 10–35 px. |
| **Red X** | Stroke by stroke ("\\" then "/"), **3 steps of 4 f**. Multiply blend. |
| **City outline / trim path** | About 30 f, easeInOutSine, slight glow. |
| **Crop marks** | Each L grows from its corner, about 18 f. |

## 8. Camera grammar

| Move | Spec |
|---|---|
| **Map zoom out (cold open)** | About **7.9×** over **116 f (3.9 s)**, `logZoom` with easeOutExpo. Radial zoom blur on the first frame. |
| **Map push in (to a city)** | **28.5×** over **63 f (2.1 s)**. Log-scale ease with about 65 % acceleration and 35 % deceleration. Motion blur in the fast middle. |
| **Document push (Ken Burns on a page)** | Up to **3.3×** over **50 f**, easeInOutCubic, then a slow drift (−1.8 px/f x, −0.6 px/f y, +0.05 %/f scale). |
| **Still-photo drift** | Mostly none. When used: **+2.4 %/s linear**, or **+0.11 %/f** on montages. |
| **Postcard dolly-out** | Inverse scale is **linear in time** (a constant-speed Z dolly) with parallax by depth `k`: `scale = 1 / (1 − u(t)/k)`. Palace 1.88× → 1.0 in **99 f @24 fps**. Nearer layers start off-frame and rise into view. |
| **2.5D tilt on a still** | Background plate, then text, then the cut-out foreground, which hides the text. The camera tilts up to reveal text hidden behind the cut-out (22 f, easeInOutSine), holds, then tilts down and pushes in (28 f, easeInOutCubic). |
| **Desk pan** | 12 fps zig-zag across a top-down desk of prints at **36–52 px per frame**, about 1.2 s per group, then a pull-back to 0.76× and a cut. |
| **Exit pull** | Accelerating zoom-out to **0.70–0.95×** over **3–8 f** (`exit`), then a hard cut. |
| **Exit push** | Accelerating push of **+5 to +19 %** over 3–8 f, then a hard cut, often continued in the next shot (see Transitions). |
| **Snap zoom** | 1 → 2.3× in **2 drawings** (easeOutExpo) into a detail. |
| **End-of-shot freeze** | Ease to a dead stop, **hold 5–18 f**, then cut (brand-film dialect). |

## 9. Stagger and sequencing

- **Strict order for callouts:** disc, then leader line, then label, with no overlap. Disc 7–13 f, line about 5 f, label wipe 8–10 f; the whole build takes about 22 f (0.75 s).
- **Bars in a chart:** each starts **5 f** after the previous one; each grows over 13–18 f with easeOutCubic. The value label pops on when its bar finishes.
- **Model card:** the car settles (7 f), then **12–20 f later** the title box starts its cursor. The subtitle wipe starts **5–8 f after** the box starts and finishes about 10 f before it.
- **Letters flying in:** staggered starts, but they **all land on the same frame**.
- **Step-and-repeat echoes:** add **one copy per drawing** and remove them one per drawing from the back.
- **Words in a keyword montage** change **3–6 f before** the footage cut, so the word leads the picture.

## 10. Timing budget

| Unit | Duration |
|---|---|
| Highlight or title box | 0.67–0.97 s |
| Settle or slide | 0.2–0.27 s |
| Read hold after a build completes | 0.5–1.0 s; quotes about 1.0 s after the last word |
| Typical shot | 1.5–4 s (Porsche median for true cuts is about 2 s) |
| Slideshow or montage on the beat | 1 photo per **30 f (1.0 s)**; carousel advances every **20 f** |
| Flash-cut accelerando | 4–7 f per shot for about 2.4 s, then **2 f** per shot for about 0.8 s |
| Clipping montage under a fixed highlight | 1 clipping per **5 f** (17 clippings) |
| Fade to black (outro only) | 49 f linear + 23 f of black |
