# 04 · Textures & materials

The material layer is what makes a frame read as *paper on a desk* rather than *pixels on a
screen*. Each material below lists what was measured, then how to build it (procedurally or from
scanned assets). Implementation code is in `09-implementation.md`.

> **Asset rule:** at 4K, every raster texture and photo must be ≥ 2× its on-screen size at 1080p.
> Scan real paper at 600 dpi, or generate textures at 4096 px and tile them.

## 1. Paper grounds

| Material | Measured | Build |
|---|---|---|
| **Warm vignetted paper** (Archive) | centre `#F7EDE4`; radial falloff starts at **30–35 %** of the half-diagonal and reaches **−16…−20 % luma** at the corners, slightly cooler; high-pass noise σ ≈ 1 (almost clean); sparse 1–2 px dust specks; soft mottled stains near the edges | flat fill + radial gradient (multiply) + a very faint fibre texture at ≤ 2 % contrast + a few stain blobs at 3–5 % |
| **Faint graph grid** (Archive) | pitch **35 px**, 1–2 px lines only **1–3 luma** darker (barely visible); a stronger variant at −15 luma (`#E9E3D5`) | `repeating-linear-gradient` in both axes; multiply under the vignette |
| **Scanned white** (Ink & Paper) | `#FDFDFD`, σ 1–2, sparse grey fibres and specks; **a different scan every 3–4 f** (frame-to-frame correlation of empty paper is only 0.07) | 6 scanned or generated paper tiles; swap on the boil clock (not a shift) |
| **Crumpled sheet** (Scrapbook, Postcard) | luma 220–240 with crease lines down to ~170; fine grain σ ≈ 5; torn edges with a thin darker rim; rotated 0–2° | photographed crumpled paper (2–8 variants); multiply crease overlay at 60–90 % opacity; boil every 15 f |
| **Grid paper** (Scrapbook) | cool `#CFCFD7` with lines `#ABA9B2` at **29 px**, or light `#F1F3F8` with `#D6D8DE` at **25 px**; one stock has a red margin line; Ink & Paper uses **31 px** cells with every 5th line darker | procedural grid + torn mask |
| **Coloured paper** | green `#90C372` / coral `#F68168` with pulp grain σ 6–8 | flat fill + noise, multiply |
| **Black card** (Ink & Paper) | `#010101` with white dust specks that boil every 4 f | black + sparse white specks re-seeded every 4 f |
| **Kraft / manila** | `#F3DBB9` | flat fill + fibre noise |
| **Newsprint** | `#D1D1D6` greyscale printed columns | real scans, cropped, torn |

## 2. Photo treatments

| Treatment | Parameters | Use |
|---|---|---|
| **Archival B&W** | Neutral grey, contrast +30–40 %, crushed blacks (`#1F1D18`), blown highlights; keep the native grain (σ 10–11 at 360p in old film) and native flicker | Archive, Scrapbook |
| **Newspaper halftone** | B&W, **45° screen, period ≈ 5.5 px@1080** (10 px in coarse scans), hard contrast | Ink & Paper photos; decorative patches |
| **CMYK halftone** | visible rosette, ~8–10 px period | Scrapbook background photos (house rows) |
| **Duotone** | maroon `#440F02` → highlight `#F6AC9C` for people; olive `#292904` → `#ECEFBC` for devices | Scrapbook portraits and devices |
| **Hero in colour** | one object per shot in saturated colour; others B&W; an object can switch B&W → colour when "picked" | Scrapbook |
| **Hand-tinted part** | B&W photo with one area tinted (`#90C0BF` mint) | Scrapbook (schaapening) |
| **Colour window** | a torn-edge colour photo (sky `#8ABFF9`) behind a B&W cut-out | Scrapbook (schaapening) |
| **Modern footage "film" grade** | desaturate about 40 %, warm/sepia bias, strong dark corner vignette (corners at about 25 % of centre luma), chromatic aberration ±3 px (blue on left edges, orange on right), slight bloom, highlights rolled off | Archive cold opens |
| **Faded 70s/80s colour** | lifted blacks, saturation −30 %, warm cast | Archive mid-century photos |

## 3. Cut-out edges

| Edge | Parameters | Dialect |
|---|---|---|
| **Hard scissor edge** | clean alpha, 1–2 px anti-alias, no feather | all |
| **Accent offset shadow** | a solid accent copy of the silhouette, offset **+18 px x, +2 px y** for portraits and **+6, +6 px** (up to +9, +12) for photo cards. **No blur, 100 % opacity.** Visible only on the right and bottom edges | Archive |
| **Lagging accent silhouette** | the accent copy follows the cut-out's slide-in 4–6 f late (spring-like), then rests as a 9–15 px rim on the right | Archive end card |
| **Sticker border** | white `#FFFFFF`, **13–16 px**, outside only, round joins, no gap, no shadow | Postcard |
| **Accent outline** | accent colour `#F6E916`, **13 px**, outside only, round joins | Postcard (landmark) |
| **Misregistered colour echo** | an accent-coloured copy of the cut-out offset **15–20 px** right, behind the B&W photo | Scrapbook |
| **Backing scraps** | the cut-out sits on torn newsprint or black paper with a 2 px lighter fibre rim | Scrapbook (schaapening) |
| **RGB misregistration** | 2–4 px magenta/blue/yellow fringes | brand-film collages only |

## 4. Shadows

| Shadow | Parameters | Use |
|---|---|---|
| **None** | — | **default** for cut-outs, cars, people, type |
| **Dithered paper shadow** | black multiply, **75 % opacity at the edge**, offset 0–15 px x and 9–22 px y, falloff over **150–240 px**, filled with heavy monochrome noise (σ ≈ 18/255, 1 px grain) so it reads as stipple, not a smooth blur | Scrapbook paper props (contract, cheque, paper slip, sheet edges) only |
| **Print shadow** | down-right 7 px, 9 px blur, 30–40 % opacity, slightly brown | Archive desk prints and Polaroids |
| **Card-stack shadow** | 10 px blur, 30 % black | aged photo-card stacks |
| **Glow** (dark scenes only) | accent or white, Gaussian **σ ≈ 40 px**, ~35 % opacity at 20 px out | year numerals, "SUV" boxes, neon photo borders (2 px accent stroke + 9 px glow), timeline rule |

## 5. Torn & crumpled paper

| Element | Parameters |
|---|---|
| **Torn edge** | an irregular edge with fractal noise (amplitude 6–20 px, two octaves) and a **white fibrous band 12–37 px** wide outside the printed area, plus a 2 px slightly darker rim |
| **Torn tunnel** | 5–6 concentric torn layers of one photo, each about 4 % larger, each with its own white band |
| **Crumpled reveal** | photographed crumple sequence (6–8 stills), stepped on the drawing clock |
| **Deckle / stamp edge** | scalloped edges on photo cards and label cards (perforation radius 6–8 px) |
| **Masking tape** | semi-opaque (70–85 %) `#D8C9A0` or olive `#B9BA73`, 60–180 × 15–25 px at 1080 (wider at 4K), ends torn, rotated 10–60°, with a faint highlight streak; Archive desk tape is accent yellow `#F3F80B` |
| **Tracing paper** | white at 60–70 % opacity over sketches, with tape |

## 6. Ink, pencil & brush

| Mark | Parameters |
|---|---|
| **Crayon/pencil scribble** | `#E07964`, width **7–9 px**, 1.5 px soft edge, about 90 % opacity, 20 % grain along the stroke |
| **Pen line / frame** | black, **3 px**, wobbly (±1.5 px low-frequency noise), corners overshoot 10–35 px |
| **Marker circle** | 2 overlapping strokes 4–6 px apart, total 12–15 px wide, accent colour, open loop |
| **Marker underline** | **15–18 px** thick, tapered and thicker at the start, 30 px below the baseline, 1.6–1.7× the text width |
| **Dry-brush highlighter** | ragged streaky stroke, bristle gaps, blobby start, tilted +2–3°, height 1.7× the window, overhang 120 px each side (multiply on prints) |
| **Black dry-brush bar** | `#2E2E2E`, **80 px** tall, ragged streaky ends extending 40–60 px past the text |
| **Black marker wipe** | strokes 90–180 px wide with white hairline dry-brush streaks |
| **White impasto underline** | brand-film variant: 13–19 px core, spray-dot start, round blob end |
| **Thin arrow** | black, 2.5 px, open V head 18 px, 140–280 px long |
| **Sparkle ✧ / crosshair + / ×** | 1.5–2.5 px outline, 30–60 px |
| **Lightning bolt** | cut from inverted newsprint (black with light text stripes) or flat `#C8C8C8`, 160–240 px; "zap" squiggles 5 px `#2A2A2E` redrawn every step |
| **Dotted flow line** | dots 4–5 px, gaps 6 px, along an arc |

## 7. Grain, flicker, weave

| Effect | Value | Note |
|---|---|---|
| Added grain on **graphics** | **none** in Archive or Scrapbook (held frames are identical within codec noise) | The paper texture *is* the grain. |
| Grain on **end cards / brand film** | σ ≈ 2.4 luma, regenerated every frame | Optional for B/E. |
| Archival film grain and flicker | keep it native; don't add it to stills | If a clean source needs ageing: grain σ 8–10, luma flicker ±2–5 % per frame, dust and scratches |
| Hold weave | 6 Hz, ±0.5–3 px, per layer | see `05-motion.md` |
| Vignette on footage | dark corners at about 25–40 % of centre luma | modern footage only |
| Light leaks, lens flares, bokeh overlays | **never** | |

## 8. Dark-scene materials (Archive)

- Background `#080705` with faint white linework at 5–20 %: maps, blueprints, cursive handwriting.
- Grungy burnt or scratched overlay at the edges of montage frames.
- Thin white axes with a 6 px glow; accent data line 6 px with a 9 px glow.
