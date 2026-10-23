# 06 · Transitions

The style is built on **hard cuts**. The cleverness lies in *disguising* them: a cut lands on an
element that is already moving, momentum carries across the cut, or a piece of paper physically
covers the frame. Plain dissolves are rare and short. Fades exist only at the very end.

Frame counts are at 30 fps unless noted.

## Frequency in the references

| Transition | Share | Notes |
|---|---|---|
| Hard cut into motion | **~70 %** | The incoming shot is already settling, sliding or zooming. In Scrapbook, almost every cut is a push (T19). |
| Zoom-through cut | ~8 % | The most characteristic "Vox" transition. |
| Slide-swap / photo drop / carousel | ~8 % | Content swaps while the paper ground stays fixed. |
| Paper transitions (crumple, torn, page curl, paper wipe) | ~5 % | One or two per piece, used at chapter breaks. |
| Short dissolves (4–8 f) and organic matte dissolves | ~5 % | Mostly inside dark montages. |
| Flash-cut montage | 1 per piece | An accelerando of 25 stills. |
| Fade to black | 1 per piece | Only at the end. |

---

## T1 · Hard cut into motion (default)

Never cut to a static frame. The incoming shot starts mid-move:

- a **settle**: the element is about 90 % in place and slides the last 4–10 % W in 6–8 f;
- a **stepped zoom-out** from 1.7–2.4×;
- a **zoom-out reveal**, e.g. a map cut in at 181 % and eased to 100 % in 6 f.

The outgoing shot usually ends with an **exit move** (pull to 0.88–0.95× or push +5–8 % over 3–5 f, ease-in).

## T2 · Zoom-through cut

```
Shot A: scale 1.00 → 1.06…1.19 over the last 3–8 f (easeInQuad, accelerating)
CUT
Shot B: either continues pushing in (×1.075 per drawing for 4 drawings, decelerating),
        or starts at 0.71–0.93 and eases out to 1.0 over 6–9 f (easeOutExpo)
```

The eye reads one continuous camera push through two shots. Used before maps, CRT screens,
desks and slideshows.

## T3 · Slide-swap on fixed paper

The paper background never moves. The outgoing content slides left −7 px, then −44 px
(about −7 % W, 2 drawings, ease-in). Cut. The incoming content slides from +12 % W → 0 in 5 f
(easeOutCubic). Total about 12 f.

## T4 · Photo drop

Print A shrinks to 0.92–0.95 over 1–3 f (ease-in). Cut. Print B lands from **1.15–1.2×** to 1.0
in 5–7 f (easeOutCubic). In a slideshow, alternate the scale direction of each photo so motion
continues through every cut: one photo eases in from 0.92, the next from 1.16, and so on, with a
14 f hold in between and a cut every 30 f.

## T5 · Carousel advance

A strip of rounded photo cards. Every **20 f**, the strip moves left one card (85 % W) in
**7 f**, easeInOutCubic on 12 fps steps. The next card waits off-screen right with a 10 % W gap.

## T6 · Crumpled-paper burst / wipe

- **Burst reveal (Ink & Paper):** a photographed crumpled sheet erupts from the bottom centre.
  It grows to about 12 %, 45 %, 100 % and then 130 % of the frame width on successive drawings,
  and unfolds to reveal the next plate (often a halftone photo) inside it. 10 f on 12 fps.
  Headline words are erased in reverse at the same time. A jolt push follows: 1.0 → 1.085 in
  3 drawings with ±20–40 px translation jolts.
- **Paper wipe (Archive):** a crumpled white sheet is pushed up from the frame bottom in
  stop-motion steps (about every 2–5 f across 27 f) until it covers the footage. **The sheet
  itself becomes the next card's background.**
- **Crumple-away:** photos and strips crumple into balls and fly off-frame, leaving the paper.

## T7 · Torn-paper tunnel

5–6 concentric torn layers of the same photo. Each layer is a slightly larger copy with a
**white fibrous torn band 12–37 px** wide. Cut in, hold about 12 f, cut out. Use it for a single
dramatic portrait beat.

## T8 · Dual paper-sheet wipe

A clean white sheet with a **straight edge slanted about 17°** (top leaning right) slams in from
the right. Its edge reaches 74 %, 69 %, 58 % and then 0 % W on successive drawings (ease-out),
while a torn-edged grey sheet carrying the next collage enters from the left. The old scene is
squeezed between them and gone in about **12 f**.

## T9 · Page curl

The current shot peels from the **bottom-right corner toward the top-left**, showing a cream
backside and a soft shadow. **16 f**, easeInQuad. The next shot is already playing underneath.
Use it once, as the cold-open → title transition.

## T10 · Marker-scribble wipe to black

Black marker strokes **90–180 px** wide, with white dry-brush hairline streaks, cover about 75 %
of the frame in 6 drawings: a swoosh stroke, then loops, then a zig-zag fill, then fat fills.
Then a hard cut to a black card.

## T11 · Object-past-lens wipe (live-action / brand film)

An object swings into the lens and covers >80 % of the frame for at least 2 frames, with
directional motion blur of 30–60 px. The cut hides at peak coverage. **5–9 f**.

## T12 · Ring focus transition (graphic → archival film)

1. Three concentric thin white rings (3 px, 80 % white) appear centred and grow ×1.3 over 7 f.
2. Meanwhile the card blurs 0 → 20 px and cross-dissolves to a *blurred* film frame over 9 f.
3. The rings then collapse to the centre (easeInCubic, 12 f) while the film racks into focus
   (20 px → 0 over 6 f).

**19 f total.**

## T13 · Organic ink/smoke matte dissolve (dark montages)

A spatial matte from a smoke or ink texture (mostly 0 or 1, soft edges). Coverage grows roughly
linearly over **13–40 f** on 12 fps steps, under a continuous slow push (+0.11 %/f).

## T14 · Fixed-highlight match-cut montage

A multiply highlight rectangle is fixed dead centre (35 % W × 18 % H). It wipes on over the first
item in 10 f. Then **17 newspaper clippings swap underneath every 5 f**, each aligned so the
keyword ("Porsche") lands exactly inside the highlight. The last clipping zooms out.

## T15 · Flash-cut accelerando

Each shot is a still, one real-world instance of the motif per shot, with the motif kept near
the frame centre (30–45 % W) so the eye locks onto it. Shot lengths at 25 fps:
`4,4,7,4,4,6,4,7,4,4,6,4,2,5`, then **ten shots of 2 f each**. End with a hard cut to blank paper
and the motif drawn as an outline.

## T16 · Shape morph

A highlight box stretches horizontally (122 → 150 px@360 over 5 f) and *becomes* the frame of the
next photo, which then pops with about 15 % overshoot. A related variant: a single photo splits
into a **triptych**, with two copies sliding out to the left and right from behind the centre
panel over 8 f with ease-out.

## T17 · Texture-scroll match cut (brand film)

A macro surface pattern scrolls fast (one groove every 2–3 f), changes material, then pulls back
to reveal the same pattern on the product. 25 f.

## T18 · Dip through dark + whip reveal

The object fills the lens and luma drops 78 → 16 in 5 f (linear). Hard cut into a 9 f
motion-blurred tilt-up that decelerates (easeOutCubic) onto the hero.

## T19 · Push transition (Scrapbook)

Every scene change in wallfive is a hard cut on the 12 fps grid, dressed up as a push:

```
Outgoing: x → −0.5…−1.0 W (or scale 1 → 1.3–1.4) over 8–12 f, easeInExpo
CUT (on a drawing boundary)
Incoming: the layers start under the cut and are already 50–85 % arrived on their first
          visible frame.
          paper sheet from +0.9 W, 28 f, easeOutQuint
          hero object from +1.3 W, 36 f, easeOutExpo (slower, giving parallax)
          headline rides on its sheet; tape and doodles pop on 2–5 f later
```

Variants: push-in through the cut (outgoing scale 1.0 → 1.07 → 1.31 over 9 f, easeInExpo); cut and
rebuild (a persistent hero stays while background layers swap one drawing at a time); cut and pop
(an empty background, then the hero pops with easeOutBack).

## T20 · Fade to black (outro only)

A linear fade over **49 f (1.63 s)**, then **23 f of pure black**. Never use it mid-piece.

## Choosing a transition

| Moving from → to | Use |
|---|---|
| Card → card on the same paper | T3 slide-swap or T4 photo drop |
| Anything → map, screen or document detail | T2 zoom-through |
| Footage → chapter title | T6 crumpled-paper wipe (Archive) or T10 marker wipe (Ink & Paper) |
| Graphic → archival film | T12 ring focus |
| A run of related photos | T5 carousel or T4 photo-drop slideshow on the beat |
| Montage of many sources | T13 matte dissolves (dark) or T14 / T15 |
| Scene to scene in Scrapbook | T19 push |
| Everything else | T1 hard cut into motion |
