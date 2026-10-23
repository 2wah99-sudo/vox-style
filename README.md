# vox-style

An instruction system for making **Vox-style editorial collage motion graphics in code**:
explainer and documentary animations rendered at 1080p and 4K. Every rule and number in it was
measured frame by frame from five reference videos (10,904 frames). See
[`references/`](references/README.md).

> Archival photos cut out with scissors and laid on paper. One highlighter colour. Serif type that
> types itself on. Graphics that move at 12 drawings per second and never freeze completely.

## Start here

| Read | When |
|---|---|
| [`docs/00-style-dna.md`](docs/00-style-dna.md) | **First.** What the style is, the 12 non-negotiables, the 4 dialects, do/don't |
| [`docs/01-color.md`](docs/01-color.md) | Palettes and colour rules per dialect |
| [`docs/02-typography.md`](docs/02-typography.md) | Fonts, type scale, decoration, how text appears |
| [`docs/03-layout.md`](docs/03-layout.md) | Zones, margins, composition templates, layer stacks |
| [`docs/04-textures.md`](docs/04-textures.md) | Paper, photo treatments, cut-out edges, shadows, torn paper, ink |
| [`docs/05-motion.md`](docs/05-motion.md) | The 12 fps clock, idle behaviour, easing tokens, entrances, type-on rates, camera |
| [`docs/06-transitions.md`](docs/06-transitions.md) | 20 transitions with frame specs and when to use each |
| [`docs/07-devices.md`](docs/07-devices.md) | 31 components (highlighter, callout, ▶ caption, year counter, timeline…) |
| [`docs/08-scene-recipes.md`](docs/08-scene-recipes.md) | 23 scene templates with frame timelines, and a 60 s example |
| [`docs/09-implementation.md`](docs/09-implementation.md) | Remotion/TypeScript kit (type-checked and test-rendered), asset scripts, 4K rendering, porting |
| [`docs/10-qa-checklist.md`](docs/10-qa-checklist.md) | Frame-step review before delivery |
| [`tokens/vox-style.tokens.json`](tokens/vox-style.tokens.json) | All measured values, machine-readable |

## The style in ten lines

1. **Paper ground**: warm off-white `#F7EDE4` with an 18 % vignette and a faint 35 px grid (Archive dialect).
2. **One accent**: lemon highlighter `#F6FA0E`, used only to mark what to read.
3. **Real material**: B&W archival photos and documents, cut out with hard edges and a hard
   accent offset shadow (+18 px).
4. **Serif type**: Georgia-like labels and captions, a high-contrast serif for years, italic
   for the key word.
5. **12 fps graphics** (holds of 2,3,2,3 at 30 fps); cameras on maps and footage run on ones.
6. **Never dead still**: a 6 Hz hold jitter of ±0.5–3 px on landed graphics.
7. **Cursor, then wipe**: every box starts as an 8–24 px bar and grows easeInOutCubic over 20–29 f.
8. **Fast in, accelerating out**: a 6–8 f settle in, a 3–8 f ease-in exit straight into a hard cut.
9. **Hard cuts disguised as motion**: zoom-throughs, slide-swaps, photo drops and paper wipes.
10. **End on a typed quote**, then a 49-frame linear fade to black.

## Dialects

| | Use for | Look |
|---|---|---|
| **A · Archive Explainer** *(default)* | history, companies, people, data | warm paper, lemon highlighter, archival B&W, Georgia serif |
| **B · Ink & Paper Editorial** | brand and design stories, manifestos | scanned white paper boiling, giant cropped Garamond, orange pencil, halftone |
| **C · Scrapbook Collage** | product and finance explainers, promos | crumpled sheets, grid strips, pastel spotlights, bold grotesk, B&W cut-outs with one red hero |
| **D · Postcard Collage** | places, travel, culture | sticker cut-outs, flat sun disc, parallax dolly, smooth wiggle |

## Quick start (code)

```bash
npx create-video@latest my-explainer   # choose the blank template
cd my-explainer
npm i @remotion/paths @remotion/noise @remotion/fonts
# copy the kit from docs/09-implementation.md into src/vox/,
# self-host the fonts in public/fonts/, and prep assets with references/tools/prep_assets.py
npx remotion studio
npx remotion render src/index.ts Explainer out/explainer-2160.mp4 --scale=2 --codec=h264 --crf=16
```
