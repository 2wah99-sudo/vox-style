# 00 · Style DNA

This is the core of the system. Read it before anything else. The other documents give exact
numbers; this one tells you what you are building and which rules you can't break.

## What the style is

An **editorial documentary collage**: real-world material (archival photos, film, newsprint,
product shots) is cut out, laid on paper, and annotated by hand with a highlighter, a marker and
a typewriter. It should feel like a smart designer's desk filmed one drawing at a time, not like
a software template.

Three ideas run through every reference:

1. **Evidence on paper.** Content is real material (photos, documents, footage) placed on a
   physical-looking ground (paper, grid paper, black card). Graphics are mostly *annotations* on
   that material.
2. **One voice of emphasis.** Each piece has **a single accent colour** and **one way of marking
   the key word** (a highlighter box, an italic, an ink-bleed or a full stop). Everything else is
   monochrome or the photo's own colour.
3. **Hand-made time.** Graphics move at 12 drawings per second, land fast without bouncing, and
   never freeze completely. A highlight or stroke starts as a cursor or a point and grows, as if
   someone were drawing it.

## The 12 non-negotiables

| # | Rule | Detail |
|---|---|---|
| 1 | **Paper ground** | Warm off-white (`#F7EDE4` Archive), pure scanned white (`#FDFDFD` Ink), crumpled white plus grid strips (Scrapbook), or black card for chapter breaks. Never a flat digital colour field, a gradient or a glossy UI background. |
| 2 | **One accent colour** | Lemon highlighter `#F6FA0E` (Archive), red-orange `#E94812` (Ink & Paper / Scrapbook), or one flat spot colour (Postcard). The accent marks what to read; it is never the background. |
| 3 | **Real material** | Archival photos (B&W or faded colour), newsprint, documents, footage. Cut out with hard scissor edges. Never stock 3D renders, icons or clip-art. |
| 4 | **Serif editorial type** | A Georgia/Caslon-like book serif for labels, quotes and captions; a high-contrast serif for big numbers and headlines. A sans is allowed only as an archival label (Helvetica-like) or as the Scrapbook headline (one bold grotesk). |
| 5 | **Emphasis by treatment, not size** | The key word is *italic*, sits in a highlighter box, is ink-bled or distressed, or is circled. One treatment per scene. |
| 6 | **12 fps graphics** | Every graphic property is sampled on the 12 fps drawing clock (2-3-2-3 at 30 fps). Cameras on maps and live footage run on ones. |
| 7 | **Never dead still** | Landed graphics get hold jitter (6 Hz, ±0.5–3 px), paper boil, or wiggle. |
| 8 | **Cursor then grow** | Boxes, highlights and windows start as an 8–24 px bar; strokes start as a point. A box's reveal masks its own text. |
| 9 | **Fast ease-out in, ease-in out to a cut** | Entrances take 0.2–1.0 s with an ease-out. Exits take 3–8 f, accelerating into a hard cut. No fade-outs. |
| 10 | **Hard cuts disguised as motion** | Cut into something already moving. Zoom-throughs, slide-swaps, photo drops and paper wipes. Dissolves only in dark montages; fade to black only at the end. |
| 11 | **No soft digital effects on graphics** | No bevels, gradients, lens flares or glossy shadows. Shadows are a **hard accent-coloured offset**, a dithered paper shadow or none at all. Glow is allowed only on dark backgrounds. |
| 12 | **Text sits in negative space** | 30–60 % of every frame is calm paper. Type goes there, never over busy photo detail, unless it is boxed. |

## Dialects

The references form one family with four dialects. Choose one per film and keep to it. Mixing
dialects inside one film is the fastest way to lose the look.

| | **A · Archive Explainer** *(default "Vox")* | **B · Ink & Paper Editorial** | **C · Scrapbook Collage** | **D · Postcard Collage** |
|---|---|---|---|---|
| Reference | History of Porsche (196 s) | Nike Swoosh 50 (16:9 half) | wallfive (bank / investing), schaapening (jukebox) | mdriturana (Rangpur) |
| Best for | History, companies, people, data | Brand stories, design history, manifestos | Product and finance explainers, promos, social | Places, travel, culture intros |
| Ground | Warm paper `#F7EDE4` + vignette −18 % + faint 35 px grid; near-black for timelines | Scanned white `#FDFDFD`, boiling every 3–4 f; black cards | White table, crumpled sheets, grid strips, coloured paper borders | Crumpled warm-grey paper `#DFE0DB` |
| Accent | Lemon `#F6FA0E` | Red-orange `#E94812` (pencil lines `#E07964`) | Red-orange hero object `#E5533A` + pastel salmon/green shapes; or one spot colour per shot | Yellow `#F6E70F` sun + outline |
| Photos | B&W archival + faded colour hero cars | B&W halftone press photos | B&W high-contrast cut-outs; only the hero object in colour | Full-colour sticker cut-outs |
| Type | Georgia-like serif (Gelasio); Didone years | Giant cropped Garamond caps + ink-bleed line; Helvetica archive captions | Bold grotesk (Inter 700), sentence case with a full stop; or condensed caps (Oswald) | A local-script bold display face |
| Emphasis | Highlighter box | Ink-bleed second line, orange underline | Underscore prefix `_word`, black brush label | Accent outline |
| Cut-out edge | Hard yellow offset shadow (+18 px) | None (flat on paper) | None; a misregistered colour echo; or backing scraps | White sticker border (14 px) or accent outline (13 px) |
| Cadence | 12 fps graphics, ones on cameras | 12 fps everything, paper boil about 8 fps | 12 fps (8 fps for heavier stop-motion) | On ones, with smooth wiggle |
| Idle | Hold jitter 6 Hz | Paper and drawing boil | Prop boil every 0.5 s | Wiggle 0.8 Hz |
| Signature transitions | Zoom-through, photo drop, ring focus, crumpled paper | Crumple burst, torn tunnel, marker wipe, flash-cut accelerando | Push (ease-in out, ease-out in, with parallax) | Single long dolly; no cuts |

> **E · Brand-film type** (the 9:16 half of the Nike reference) is live-action/CGI with type on
> top. It is documented only for its type devices (distressed emphasis word, pop-on headlines,
> end slate). See `07-devices.md` → D24.

## Do / Don't

| Do | Don't |
|---|---|
| Put one highlighted word per sentence | Highlight whole sentences |
| Let a headline bleed off the frame (Ink & Paper) | Shrink a hero word to fit "safely" |
| Use B&W photos with one hero in colour | Colour-grade everything to the accent |
| Jump between stepped poses with no in-betweens | Smooth 60 fps tweens on graphics |
| Cut on movement | Cut on a static frame |
| Keep the paper fixed while graphics jitter | Shake the whole frame |
| Ground each scene with a real document or photo | Use icons or flat vector illustrations as content |
| End with a typed quote or a tagline card, then fade to black | Use end-screen templates or logo stingers with light streaks |

## Where to go next

- Exact colours → `01-color.md`
- Type scale and type-on rules → `02-typography.md`
- Grids, margins and layer stacks → `03-layout.md`
- Paper, halftone, cut-outs and shadows → `04-textures.md`
- Cadence, easing, entrances and the camera → `05-motion.md`
- Transition catalogue → `06-transitions.md`
- Component specs (highlighter, callout, ▶ caption, year counter…) → `07-devices.md`
- Scene templates and storyboard timing → `08-scene-recipes.md`
- Code architecture and snippets → `09-implementation.md`
- Review checklist → `10-qa-checklist.md`
