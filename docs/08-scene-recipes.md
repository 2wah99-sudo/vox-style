# 08 · Scene recipes (explainer templates)

Ready-to-use scene templates built from the devices in `07-devices.md`. Each one gives its
purpose, layout, a frame timeline at **30 fps** (graphics on the 12 fps clock), and its in/out
transitions. Chain them to build an explainer.

## Pacing rules

| Rule | Value |
|---|---|
| Average shot length | **2–3 s** (true cuts every 1.5–4 s); montages 1 s per item |
| One idea per shot | one label, one number or one quote |
| Build, then hold | the build takes 0.7–1.3 s; **the hold is ≥ 0.5 s after the last element lands** (≥ 1 s for quotes) |
| Start on motion | every shot starts mid-move (settle, punch-out or slide) |
| End on motion | every shot ends with a 3–8 f ease-in exit into the cut |
| Narration lead | text and keywords land **3–6 f before** the word is spoken, or before the cut they belong to |
| Rhythm breaks | one flash montage or dark montage per 1–2 minutes; one paper-transition chapter break per 45–60 s |

## Scene spec format

Describe each scene with this structure. The implementation reads it directly.

```jsonc
{
  "id": "s05_model_card_911",
  "dialect": "archive",
  "template": "ModelCard",
  "durationFrames": 75,
  "in":  { "transition": "hardCutIntoMotion" },
  "out": { "transition": "pullAwayCut", "frames": 4 },
  "content": {
    "title": "Porsche 911",
    "subtitle": "The price at launch is $6,500",
    "image": "assets/cutouts/911_side.png"
  },
  "narration": "In 1963 the 911 arrived, priced at six and a half thousand dollars."
}
```

---

## R1 · Cold open: map zoom → page curl → keyword montage *(Archive)*

| f | Event |
|---|---|
| 0–116 | world map with rounded video cards; log zoom-out ×7.9 (easeOutExpo, on ones); radial blur on f0 |
| 116–132 | page curl from the bottom-right (16 f, easeInQuad) |
| 132 | keyword window (D7) with footage |
| 139–159 | ▶ rises and spins |
| 165–174 | word 1 rolls into the slot |
| every 24–26 f | footage cut; the next word rolls in 3–6 f **before** the cut |
| after 5 words | zoom-through into R2 |

## R2 · Place intro: map push → city outline → label *(Archive)*

| f | Event |
|---|---|
| 0–63 | log push-in ×28.5 to the city (on ones, motion blur in the middle) |
| 65–95 | city outline trim path (30 f) |
| 82–104 | label: text fades in, then the box wipes in behind it (22 f); the tail pops at 60 % |
| 104–124 | hold |
| 124–137 | label retracts right to left |
| 142 | cut to R3 (portraits on the same map, darkened) |

## R3 · Person intro: portraits rise + name label *(Archive)*

| f | Event |
|---|---|
| 0 | map darkens by 40 % |
| 1–18 | portrait 1 rises through its bottom mask (17 f) |
| 8–25 | portrait 2 (+7 f) |
| 14–30 | two-line bold name label wipes in the centre column |
| 30–45 | hold, then a 4 f dissolve or a cut to an archival photo with a pull-back and push into the cut |

## R4 · Fact on an archival photo: stepped reveal + highlight caption *(Archive)*

| f | Event |
|---|---|
| 0 | cut in at 1.75–2.0× on the subject |
| 0–12 | stepped zoom-out to 1.0 (12 fps, no blur) |
| 12–15 | highlight-caption cursor |
| 15–38 | caption box wipe; the keyword inside is italic ("one of the first *hybrid* vehicles") |
| 38–70 | hold with a slow push of +2.4 %/s |
| 70 | 5 f dissolve or cut |

## R5 · Callout on an object *(Archive)*

Photo or technical drawing (full bleed or on graph paper) → D3 disc (7–13 f) → leader (5 f) →
label (8–10 f) → hold 15–30 f → slide-swap to the next callout on the same paper (T3). Chain
2–3 callouts for "three features" beats.

## R6 · Year jump *(Archive)*

| f | Event |
|---|---|
| 0 | cut to the cool paper card |
| 0–28 | year counter: 12 steps from now back to the target year (D8) |
| 20 | highlight cursor appears |
| 28–48 | box wipes in on the target year |
| 48–58 | hold |
| 55–58 | the next photo pre-laps at 30 % for 3 f, then a hard cut |

## R7 · Era timeline *(Archive, dark)*

`#080705` background with a faint map and a glowing rule at 59 % H. Years pop along the line
(about 7 f each, 8–13 years). The final year slides to the centre (10 f), then a photo card slides
in over it from the right (10 f) → R8.

## R8 · Who's who: drawn circle + small label *(Archive)*

Group photo → accent circle draws around one face (17 f) → small bold name label wipes in
(bottom-right of the face, about 22 f) → hold → the circle **un-draws in 8 f** → cut.

## R9 · Quote *(Archive)*

Warm paper → cut-out portrait with an accent offset shadow scales 1.6 → 1.0 into the bottom-right
(14 f) → justified italic quote word by word (1 word per 2.5 f) → bold attribution (+6 f) → hold
about 1 s → nudge (−8 px) and cut to the next card on the same paper.

## R10 · Product card *(Archive)* → footage + caption

| f | Event |
|---|---|
| 0–7 | product settles (D10) |
| 12–41 | title box: cursor, then wipe |
| 17–31 | subtitle wipe |
| 41–71 | hold with weave |
| 71–75 | pull-away (0.9×) → **cut to footage** |
| footage 3–24 | ▶ rises and spins, caption fades in (D6) |
| footage end −6 | caption fades out with the cut |

## R11 · Data beat *(Archive)*

- **Bar chart:** enters at 0.83 → 1.0 (7 f); bars staggered 5 f apart (15 f each); value labels pop
  on; red circle around the highlighted bars (11 f); hold 15 f; slide-left exit (3 f) and cut.
- **Line chart on blueprint:** axes visible on the cut; data line draws linearly over 73 f while
  the title types; hold 30 f; slight push into the cut.
- **Big number on a still (2.5D):** D15.

## R12 · Document highlight *(Archive)*

Archival article page lands (8 f settle) → Ken Burns push 3.3× over 50 f onto the headline →
multiply highlight on the headline phrase (20 f) → +9 f → highlight on a body phrase (27 f) → slow
drift → push +8 % → zoom-through cut.

## R13 · Clipping montage *(Archive)*

Newspaper ad with a push-in (1.14×, easeOutExpo 7 f) → multiply highlight on the keyword (10 f)
→ **17 clippings, 5 f each**, keyword locked inside the fixed highlight (T14) → the last one zooms
out → cut.

## R14 · Dark industrial montage *(Archive)*

Near-black with blueprint linework and grungy edges; 5–7 photos linked by organic matte dissolves
(13–40 f) under a continuous push of +0.11 %/f. It ends on a year reveal: a hard left-to-right
wipe (5 f) with a black dry-brush ellipse drawn around it (5 f) → product card (R10).

## R15 · Chapter title *(Archive)*

Footage → crumpled paper pushed up in stop-motion steps (27 f) → it becomes the card → dashed
frame → title types 1 character per frame with an *italic* keyword → highlight on the year
(10 f) → hold 20 f → cut.

## R16 · Brand / logo history title card *(Ink & Paper)*

| f | Event |
|---|---|
| 0–3 | black → cut to paper (boil starts) |
| 6–69 | archive caption block types (D20) |
| 18–35 | headline line 1, 1 letter per 2 f (D19) |
| 35–47 | ink-bleed line 2, 1 word per 4 f |
| 18–110 | orange scribbles live in the middle band; stencil letters and the outline motif pop on (f43) |
| 71–117 | the motif style-boils; the stamp scramble-types |
| 102–109 | black brush strokes sweep |
| 118–127 | crumpled-paper burst reveals the next plate; headline words erased in reverse |

## R17 · Photo story *(Ink & Paper)*

Crumple-revealed halftone photo with a jolt push → newspaper strips unfurl left to right (8
drawings) → the strip headline is legible → orange annotation note → everything crumples away
(about 30 f) → the scribbles remain → the next motif forms from a paper ball.

## R18 · Quote beat *(Ink & Paper)*

Marker-scribble wipe (6 drawings) → black quote card (D23) types 1 letter per 2 f with an
ink-bleed last line → orange underline wipe (20 f@25) → slow shrink → exit to 0.70× over 4
drawings → chalk handwriting on the same black.

## R19 · Flash montage → assembly *(Ink & Paper)*

25 real-world instances of the motif (T15 accelerando) → hard cut to blank paper with an outline
motif → stencil letters pop and rearrange → style-boil swarm on ones → brush sweep → blank paper →
tagline types ("Never done leaving a mark.") → erased in 1 frame → logo pops → hard cut.

## R20 · Scrapbook explainer beat *(Scrapbook)*

| f | Event |
|---|---|
| 0 | hard cut; incoming layers already 50–85 % in (T19 push) |
| 0–28 | paper sheet decelerates in (easeOutQuint); the hero object arrives more slowly (36 f, easeOutExpo) |
| 3–15 | grid strip, pastel spotlight and tape pop on with a 2–5 f stagger |
| 15–30 | hand enters from an edge, picks the hero (it turns colour and tilts 10–15°) |
| 30–43 | headline stepped drop-in (1.85× → 1.27× → 1.0×) |
| 43–58 | arrow draws on and loops; sparkle appears |
| every 15 f | prop boil |
| last 8–12 f | push out (easeInExpo) → cut |

**Variants:** cut-and-pop (empty background, then the hero pops with easeOutBack at 6–23 %
overshoot); spin-in prop (contract or cheque 0.25 → 1, −10° → −3°) with brush labels
(PRINCIPAL/INTEREST); zoom-out reveal from 2.5×; magnifier sweep over the headline.

## R21 · Scrapbook object spotlight *(Scrapbook, schaapening)*

Cut to the hero object at 1.4–2.4× → hold 1 step → stepped easeOutExpo zoom-out (15–64 f, 8 fps)
→ condensed display word letters fly in behind it and land together → lightning bolts pop with
zap squiggles → red X drawn by the word (3 × 4 f) → per-step jitter → accelerating zoom-out
(0.955) → cut to the next object.

## R22 · Place postcard *(Postcard)*

Single shot: dolly-out with parallax (99 f@24) while the sun disc scales in (24 f) and birds flap
→ camera stops → the landmark settles slightly → local-script title slides up cluster by cluster
(5 f each, 10–11 f apart) → hold with wiggle (≥ 8 s possible).

## R23 · Outro *(Archive)*

Desk mood-board pan (D16, about 6 s) → pull-back → end quote card (D11) → hold 1 s → linear fade to
black (49 f) → 23 f of black.

---

## Example: a 60-second Archive explainer

| # | t (s) | Template | Content |
|---|---|---|---|
| 1 | 0.0–4.4 | R1 | map zoom-out + page curl |
| 2 | 4.4–11.0 | R1 | keyword montage: *history · risk · money · power* |
| 3 | 11.0–16.0 | R2 | push into the city + label |
| 4 | 16.0–19.0 | R3 | founder portraits + name |
| 5 | 19.0–21.5 | R4 | archival photo + highlight caption |
| 6 | 21.5–23.2 | R6 | year counter → founding year |
| 7 | 23.2–27.0 | R5 ×2 | two callouts on the first product |
| 8 | 27.0–31.0 | R9 | founder quote |
| 9 | 31.0–34.5 | R10 | product card + price |
| 10 | 34.5–38.0 | R10 | footage + ▶ caption |
| 11 | 38.0–42.0 | R11 | bar chart of sales + red circle |
| 12 | 42.0–46.0 | R12 | newspaper article highlight |
| 13 | 46.0–49.0 | R15 | chapter title: "But the real *turn* came in 1998" |
| 14 | 49.0–53.0 | R14 | dark montage → year reveal |
| 15 | 53.0–60.0 | R23 | desk pan → quote → fade to black |
