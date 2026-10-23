# 01 · Colour

Every value here was sampled from reference frames using the median of a pixel patch, not picked
by eye. Thin strokes and text on yellow are affected by JPEG chroma subsampling, so for those the
table gives the *intended* value and notes the sampled range. Machine-readable tokens are in
`tokens/vox-style.tokens.json`.

## Colour rules (all dialects)

1. **One accent colour per film.** It marks what to read: highlighter boxes, underlines, circles,
   ▶ bullets, offset rims, chart lines, the hero object. It is never a large background.
2. **Everything else is paper, ink or the photo's own colour.** Archival photos are B&W or
   faded colour. Only the *hero* object of a scene may be in full colour.
3. **Text is never pure black on paper.** Use warm near-blacks (`#2B2010`, `#3A292C`, `#121213`)
   and warm greys (`#554949`) for secondary lines.
4. **Paper is never pure white,** except for the scanned-white Ink & Paper ground (`#FDFDFD`),
   which is kept alive by its texture.
5. **No gradients on graphics.** The only gradients allowed are the paper vignette, glows on dark
   backgrounds and photographic shading.
6. **Red is reserved.** In Archive, red appears only inside photos and once as a chart-circle
   marker. In Ink & Paper and Scrapbook, red-orange *is* the accent, so no other red is used.

---

## A · Archive Explainer palette

| Token | Hex | Role | Notes |
|---|---|---|---|
| `paper.center` | **#F7EDE4** | card background at centre | measured #F3E9E0 / #F8EEE5 / #FAF0E7 |
| `paper.mid` | #E6DCD3 | radial falloff | |
| `paper.corner` | **#C8C3BF** | vignette corners (about −18 % luma, slightly cooler) | range #C0BCB3–#CFCBC2 |
| `paper.cool` | #E9E7DB → corners #B9B9AD | alternative cool card (year counter) | stronger vignette (−19 %) |
| `paper.grid` | paper −1 to −3 luma (faint) / **#E9E3D5** (visible) | 35 px graph grid | |
| `accent` | **#F6FA0E** | highlighter boxes, ▶, circles, gridlines, tape | measured #F6FD10 / #F7FA0A / #F2F709; lemon with a slight green bias, never orange |
| `accent.multiply` | #F6FA0E @ multiply | highlights on photos, prints and maps; callout discs | fitted: R′≈0.88R, G′≈0.92G, B′≈0.14B |
| `accent.shadow` | **#E3EF0A** | hard offset shadow behind cut-outs | |
| `accent.caption` | #E8F010 | bold-italic caption text over footage | reads #C4D053–#E2EE48 on thin strokes |
| `accent.glow` | #E7FF21 core + glow | years and boxes on dark backgrounds | |
| `ink.onAccent` | **#2B2010** | text on yellow boxes | never pure black |
| `ink.quote` | **#3A292C** | quotes and long text on paper | |
| `ink.secondary` | **#554949** | subtitles ("The price at launch is…") | |
| `ink.muted` | #6B6361 | big year numerals on paper | |
| `ink.source` | #908784 | source and attribution lines | |
| `ink.chart` | #31312F | chart bars | |
| `marker.red` | #7E1029 (core #61000A) | hand-drawn chart circle (used once) | |
| `dark.bg` | **#080705** | timeline and montage background | faint map/blueprint linework at 5–20 % white |
| `dark.line` | #EFECE5 + white glow | timeline rule and numerals | |
| `pale.year` | #F0F595 | pale yellow numerals over dark montage | |

**Photo treatment (Archive):**

- Archival photos: neutral B&W, high contrast, blown highlights; native grain only.
- Archival film: a slight green tint is fine (G about +15 over R and B).
- Hero product photos on paper cards: clean full colour.
- Modern footage: desaturated warm grade, strong dark corner vignette, chromatic fringe ±3 px,
  highlights rolled off (p99 ≈ 210–240).

## B · Ink & Paper Editorial palette

| Token | Hex | Role |
|---|---|---|
| `paper` | **#FDFDFD** (#F9F9F7–#FCFCFB) | scanned paper with sparse grey specks; boils every 3–4 f |
| `card.black` | **#010101** | quote cards and handwriting collage; white dust specks boil |
| `ink.headline` | #111111 / blue-black **#222931** | serif headlines, photocopy edges |
| `ink.cream` | **#E9E9D0** | serif on black cards |
| `ink.chalk` | #B8B8B8 | chalk handwriting on black |
| `accent` | **#E94812** (#DE4B1B–#EE4612) | stencil letters, underline bar, solid swooshes |
| `accent.pencil` | **#E07964** (intended ≈#E85A3A) | crayon/pencil scribbles, semi-transparent |
| `accent.echo` | #F1AE9F | grainy riso "echo" copies at about 35 % density |
| `accent.onBlack` | #B04C35 | underline on black cards |
| `kraft` | #F3DBB9 | kraft/manila cards |
| `tape` | #D8C9A0 | semi-opaque masking tape |
| `grid` | #FAFBF7 + grey 1 px lines, every 5th darker | graph paper (31 px cells) |

Rules: authored colour is limited to black, white, cream, grey and the one orange. Other colour
comes only from real product photos.

## C · Scrapbook Collage palette

| Token | Hex | Role |
|---|---|---|
| `table` | **#FFFFFF** | the white "table" behind sheets |
| `paper.crumpled` | **#E9E8E9** (#DCDADC–#F0EFF0, creases to #BABBB7) | crumpled sheets covering 60–85 % of the frame |
| `grid.cool` | paper **#CFCFD7**, lines **#ABA9B2** | blue-grey grid strip (29 px pitch) |
| `grid.light` | paper #F1F3F8, lines #D6D8DE | light grid (25 px pitch) |
| `grid.margin` | thin red/maroon line | margin rule on grid stock |
| `pastel.salmon` | **#E4ADA2** | flat half-discs and 3/4 discs behind the hero |
| `pastel.salmonGrid` | fill **#FAC9BE**, grid #E87C66 | salmon grid-paper circle behind the hero (Ø ≈ 65 % H) |
| `pastel.pink` | #FDEDF0 | soft halo circle |
| `pastel.green` | **#BFD4B3** (about 70 % opacity, multiply) | circles and wedges at frame edges |
| `pastel.mint` | #AEE192 | big flat semicircle |
| `paper.green` | **#90C372** (grainy) | border strips at frame edges |
| `paper.coral` | #F68168 (grainy) | border strips |
| `tape.olive` | **#B9BA73** | 2–4 masking-tape strips per scene |
| `hero` | **#E5533A** (#D93624–#F25A45) | the one coloured object the narration is about |
| `duotone.maroon` | shadow #440F02 → highlight #F6AC9C | presenter portraits |
| `duotone.lime` | #292904 → #ECEFBC | devices (laptop, phone) |
| `ink` | **#121213** | headlines |
| `brush` | #2E2E2E (text #FFFFFF) | black dry-brush label bar |
| `scan.dark` | #48281C / greenish-black | photocopy scan strips at the left edge |

**schaapening variant (spot-colour scrapbook):**

| Token | Hex | Role |
|---|---|---|
| paper | #FEFCFF | slightly lilac white |
| grid cells / lines | #E2E0E3 / #C8C6CA | 35 px pitch |
| newsprint | #D1D1D6 | greyscale scraps |
| spot (one per shot) | **#5C5CD0** blue · **#7FCCCD** teal (multiply) | condensed caps word |
| marker | #D44A55 (multiply) | hand-drawn X |
| colour window | #8ABFF9 | sky photo inside a torn shape |
| tint | #90C0BF | hand-tinted part of a B&W photo |

Rules: about 90 % of the screen is white or grey paper; colour is spent in small doses. Pastel
shapes are flat or multiply, never gradients, and always sit *behind* the hero as a spotlight.
Saturated colour is reserved for one hero object per shot. A B&W object may **turn colour at
the moment it is picked**.

## D · Postcard Collage palette

| Token | Hex | Role |
|---|---|---|
| paper | **#DFE0DB** | crumpled warm-grey paper, static |
| accent | **#F6E70F** | flat sun disc (Ø 50 % H) and landmark outline |
| sticker | #FFFFFF | 14 px border around foreground cut-outs |
| title | **#26873A** | local-script title (picks up the flag/vehicle green) |
| silhouettes | #1C1B17 | bird flock |

The landmark stays near-greyscale; saturated colour is reserved for the foreground "life"
objects (vehicles, people).

## E · Brand-film backdrops (reference only)

One saturated seamless colour per segment, with radial falloff of about −30 % luma at the
corners: crimson `#A91B49`, green `#579242`, petrol `#0C6180`, tomato `#D85730`. White text is
tinted 8–12 % toward the backdrop. The end card is `#C1C1C3` with near-black type `#272829`.

## Contrast checks

| Pair | Ratio | Use |
|---|---|---|
| `#2B2010` on `#F6FA0E` | ≈ 14.9 : 1 | labels on highlighter |
| `#3A292C` on `#F7EDE4` | ≈ 11.9 : 1 | quotes |
| `#554949` on `#F7EDE4` | ≈ 7.7 : 1 | subtitles |
| `#E8F010` on dark footage (luma < 60) | ≥ 8 : 1 | captions; on bright footage, switch to `#3B2A1C` |
| `#E9E9D0` on `#010101` | ≈ 16 : 1 | black quote cards |
| `#121213` on `#E9E8E9` | ≈ 15.5 : 1 | Scrapbook headlines |
