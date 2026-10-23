# 02 · Typography

Sizes are **px at 1080p** (multiply by 2 for 2160p). "Cap" means cap height; font size ≈ cap ÷ 0.68
for these serifs and ≈ cap ÷ 0.73 for Inter. Typefaces were identified from glyph shapes at
360–720p, so the free fonts listed are **close stand-ins**, not confirmed originals.

## Type families

| Role | Look in the references | Free stand-in (Google Fonts) | Commercial equivalent |
|---|---|---|---|
| **Label / caption / quote serif** (Archive) | Georgia: bracketed serifs, ball terminals, old-style figures in bold italic | **Gelasio** (metric-compatible with Georgia) | Georgia |
| **Title serif** (Archive model cards, chart titles) | transitional/editorial serif with lining figures | **Newsreader**, **Source Serif 4**, PT Serif, Libre Caslon Text | Tiempos, Publico, Lyon |
| **Big numerals** (years, prices) | high-contrast Didone/Caslon, lining figures, ball-terminal 3/6/9 | **Playfair Display** (lining), **Libre Caslon Display** | Didot, Caslon Display |
| **Hero headline serif** (Ink & Paper) | Garamond/Sabon caps: wide D/O, long-legged R | **EB Garamond 500**, Cormorant Garamond 600 | Sabon, Adobe Garamond |
| **Archive caption sans** (Ink & Paper) | Helvetica Neue Regular/Medium | **Inter 400/500**, Arimo | Helvetica Neue |
| **Scrapbook headline** | bold neo-grotesk, double-storey a, tight apertures | **Inter 700 / Inter Display 700**, tracking −2 to −3 % | SF Pro Display Bold, Helvetica Now Display Bold |
| **Scrapbook display word** | condensed bold caps | **Oswald 600–700**, Bebas Neue | Trade Gothic Bold Cond. No. 20, Knockout |
| **Label caps on brush** | geometric semibold, tracking +10 % | **Inter 600**, Montserrat 600 | |
| **Local-script title** (Postcard) | heavy rounded display | e.g. **Hind Siliguri 700** or Noto Sans Bengali Black for Bengali | |
| **Brand-film serif** (reference E) | Lyon/Tiempos-like book serif | **Newsreader Display / Text** | Lyon, Tiempos |

Rules:

- **Archive uses one serif family for all running text.** No sans anywhere in Archive.
- **Emphasis = change of treatment, never a different font family.** Use italic inside roman
  ("one of the first *hybrid* vehicles"), a highlighter box, an ink-bleed or distressed cut of
  the same face, or a `_` prefix (Scrapbook).
- Keywords in captions are lower case italic; labels are bold; headlines are caps (Ink & Paper)
  or sentence case ending with a full stop (Scrapbook).
- Use old-style figures in italic captions and lining figures in prices, years and charts.

---

## Type scale (1080p)

| Style | Size | Weight / case | Colour | Placement | Dialect |
|---|---|---|---|---|---|
| **Oversized cropped headline** | cap **156–257 px** (14–24 % H) | serif caps 500, tracking −2 % | `#111` / `#222931` | anchored to the **top edge**; up to 41 % of the cap height *above* the frame; bleeds off the sides | B |
| **Ink-bleed second line** | cap **171 px**, spans 98 % W | same face + ink-bleed filter | same | directly under line 1 | B |
| **Scrapbook H1** | cap **89 px**, size **122 px**, line-height **0.93** | Inter 700, sentence case, ends with "." | `#121213` | left-aligned in the empty third, 2–3 lines of 1–2 words | C |
| **Scrapbook H2** | cap 66 px, size 90 px | Inter 700 | `#121213` | | C |
| **Scrapbook caption line** | size 93 px, one line about 71 % W | Inter 700, lower case | `#121213` | top band | C |
| **Condensed display word** | cap **236–294 px** (22–27 % H) | Oswald 700 caps, one letter at a time | spot colour, opaque or multiply | crossing the frame **behind** the hero, bleeding off both edges, baseline jitter ±7 % H, tilt ±8° | C (schaapening) |
| **Year numerals** | figure height **117–156 px** | Playfair Display 400, lining | `#6B6361` on paper / `#EFECE5` + glow on dark / `#F0F595` on montage | centred | A |
| **Black quote card** | cap **117 px**, pitch 152 px (1.3× cap) | EB Garamond 500 caps; last line ink-bleed | `#E9E9D0` on `#010101` | left-aligned block, centred on frame | B |
| **Model / price title** | size **95–100 px** (cap 69 px) on a **138 px** box | Newsreader / Libre Caslon 400, Title Case | `#2B2010` on accent | box top at **16.5 % H**, centred | A |
| **Map label** | cap **84 px** on a **162 px** box with a down-pointing tail | Gelasio 700 caps | `#2B2010` on accent | above the location | A |
| **Callout label** | size **69 px** on a **102 px** box | Gelasio Italic, lower case | `#2B2010` on accent | top-left quadrant, at the end of a leader line | A |
| **Highlight caption** | x-height 36 px, size ≈ 75 px on a 93 px box | roman with the keyword in *italic* | `#2B2010` on accent | lower third, left edge 24 % W | A |
| **Keyword (montage)** | size **88 px** | Gelasio Italic 600, lower case | white, chromatic fringe ±3 px | baseline **90 % H**, centred, after a ▶ | A |
| **Justified quote** | size **56 px**, leading 68 px (1.2) | Gelasio Italic, sentence case, straight quotes `"` | `#3A292C` | **fully justified**, width 38 % W, left edge 21 % W, top aligned with the cut-out's head | A |
| **End-card quote** | size **52 px**, leading 69 px | Gelasio/Libre Baskerville Italic | `#564A4B` | left 19 % W, top 31 % H, 3 lines | A |
| **Attribution** | 18–26 px | serif **Bold** upright | quote ink | right-aligned to the quote block, one blank line below | A |
| **Footage caption** | size **52 px** (cap 36 px) | Gelasio **Bold Italic**, old-style figures | `#E8F010` on dark / `#3B2A1C` on bright | baseline **90 % H**, text from 14–16 % W, after a ▶ (54–60 px) | A |
| **Subtitle / price line** | size **46 px** | serif 400, sentence case | `#554949` | centred, 57 px below the title box | A |
| **Chart title** | size 42 px | serif 600 | `#3A2B2B` (or accent on dark) | top band | A |
| **Chart axis / labels** | 21–32 px | serif 400, lining | `#4E4540` / white on dark | | A |
| **Small serif list** | cap 37 px, pitch 51 px, leading ≈ 0.85 | serif 400 mixed case | `#29292B` | left-aligned | B |
| **Archive caption block** | cap **24 px**, line **32 px**, pair pitch 111 px | Inter 400 | `#000` (or white on dark) | two columns at 2.3 % W and 15.2 % W; bottom margin 8.7 % H | B |
| **Archive stamp** | cap ≈ 17 px, 2 lines + 150 px rule | Inter 500 | `#000` | bottom-right | B |
| **Brush label** | cap **34 px**, tracking +10 % | Inter 600 caps | `#FFF` on an 80 px black dry-brush bar | | C |
| **Paper-slip caption** | ≈ 50 px | Inter 400, lower case | accent red | on a torn white slip rotated −3° | C |
| **Local-script title** | matra-to-baseline **128 px** (11.8 % H) | heavy display | `#26873A` | top-right negative space (68 % W, 18 % H) | D |

## Decoration rules

- **Highlighter box** (Archive): opaque accent rectangle with square corners. Padding ≈ 0.4–0.5 ×
  cap height left and right, ≈ 0.45 × cap height above, slightly less below. Title-box padding
  is 36–54 px left, 33 px top and 36 px bottom. Optionally a down-pointing triangular tail
  (0.35 × box height wide, 0.3 × box height tall) for map callouts.
- **Highlighter on print** (Archive): multiply accent over existing printed words. Its height is
  the line height of the target words plus 3–6 px of overhang.
- **Ink-bleed** (Ink & Paper): every stroke end and joint swells into liquid blobs (radius 4–12 px)
  with occasional drips (6–20 px). It is static and does not boil. Use it on the second line or
  punch word only.
- **Distressed / eroded word** (brand film): chipped edges with 2–3 px displacement, mottled fill,
  and optionally erosion that increases left to right across the phrase.
- **Underscore prefix** (Scrapbook): a static `_` glyph of the headline font placed before the key
  word on the last line (`_investment.`). It is about 0.8 × cap wide and does **not** blink.
- **Full stop**: every Scrapbook headline ends with "." as part of the voice.
- **Never:** outline strokes, drop shadows, gradients or bevels on type. Glow is allowed only on
  dark backgrounds (σ ≈ 40 px).

## How text appears

| Text | Reveal |
|---|---|
| Text in a highlighter box | Masked by the growing box (cursor, then wipe); letters are cut mid-glyph at the moving edge |
| Text that is already visible and then highlighted | The box wipes in **behind** it (prices, map label, year) |
| Hero serif headline | Typewriter: 1 letter per 2 f (line 1), 1 word per 4 f (ink-bleed line). Exit by erasing words in reverse. |
| Quote | Word by word every 2.5 f with a 25 → 100 % fade, or character by character at 34 characters/s |
| Archive caption block | Character by character (2–3 per drawing) with a trailing `_` cursor; fields type at the same time with staggered starts |
| Footage caption | ▶ spin, then the line fades in over 5–9 f |
| Scrapbook headline | Stepped drop-in (1.85×, then 1.27×, then 1.0×), or it rides in on its paper sheet |
| Condensed display word | Letters fly in from the nearest side, staggered, and all land on the same frame |
| Local-script title | Each grapheme cluster slides up and fades in over 5 f, 10–11 f apart |
| Brand-film headline | Pops on in one frame and leaves on the cut |

**Never** fade a whole paragraph in, slide a text block in from off-screen, or animate letters
with a bounce.

## Copy rules (voice)

- Short. Captions are one line (≤ 77 % W); labels are 1–4 words; headlines are 2–3 lines of
  1–2 words.
- One fact per caption, with numbers in the original units plus a conversion in parentheses:
  "a top speed of around 210 km/h (130 mph)".
- Quotes are typed and attributed: `-Firstname Middle Lastname`, in bold, right-aligned.
- Prices read "The price at launch is $3,750", in the same sentence frame every time.
- Archive caption fields: `Year: / 1971`, `Story: / Swoosh`, `Dept. of / Nike Archives`.
