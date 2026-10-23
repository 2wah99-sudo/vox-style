# 03 · Layout & composition

All positions are given as fractions of the frame (W = width, H = height), so they hold at 1080p
and 2160p. Pixel values are at 1920×1080.

## Canvas

| Setting | Value |
|---|---|
| Master | **1920×1080, 30 fps** (render 3840×2160 with a ×2 scale) |
| Vertical | 1080×1920. Put the 16:9 layout inside, or follow the 9:16 zones below |
| Graphic cadence | 12 drawings/s regardless of the master fps |
| Title-safe | Text stays inside 9 % W left/right and 8 % H top/bottom, **except** deliberate bleeds (oversized headlines, display words, collage material) |

## Global rules

1. **Centred axis by default** (Archive): labels, cards, cars and charts are centred on x = 50 %.
   Callouts and captions are the exceptions; they use a left-hand anchor.
2. **Asymmetric thirds** (Scrapbook): the hero cut-out takes one third with its pastel spotlight
   circle behind it, and the headline sits in the empty opposite third.
3. **30–60 % empty paper** in every frame. Text goes only there.
4. **Edge bleed is intentional**: collage material, display words and foreground objects bleed off
   the frame edges. Text blocks (other than hero words) never touch an edge.
5. **Same layout per recurring template.** A model card, quote card or caption is pixel-identical
   every time it appears, so the viewer learns it.

## Key zones (16:9)

| Zone | Position | Holds |
|---|---|---|
| **Top title band** | box top **16.5 % H**, box height 12.8 % H | highlighter title box |
| **Subtitle line** | 57 px below the box, ≈ 34–38 % H | price or subtitle |
| **Hero object band** | 55–90 % H, object width **55–60 % W**, bottom at 86–90 % H | car or product cut-out |
| **Caption line** | baseline **90 % H**; ▶ at 9–12 % W; text from 14–16 % W; ≤ 77 % W long | footage captions |
| **Callout label** | top 21–24 % H, left 9–16 % W | label box at the end of a leader line |
| **Quote block** | left **19–21 % W**, top **31 % H**, width **38 % W** | quote + attribution |
| **Cut-out portrait** | bottom-right, 60–84 % W, bleeding off the bottom edge; head top aligned with the quote top | quote cards |
| **Archive caption block** | bottom-left, columns at **2.3 % W / 15.2 % W**, last baseline at 91.3 % H | Ink & Paper caption fields |
| **Archive stamp** | bottom-right (86–97 % W, 89–97 % H) | department stamp |
| **Hero headline** | anchored to the **top edge**: line 1 cropped by y = 0, lines 0–31 % H | Ink & Paper title cards |
| **Drawing table** | 30–80 % H centre band | swooshes, photos and scribbles in Ink & Paper |
| **Timeline rule** | y = **59 % H**, x 22–77 % W | year above, ring-dot on the line |
| **Chart plot** | x 24–80 % W, baseline 73 % H, gridlines at 42 / 57.5 / 73 % H | bar and line charts |
| **Video window** | 75 % W × 75 % H rounded rect (r = 33 px), top 6 % H; the bottom 19 % H is kept for ▶ + keyword | keyword montage |
| **Framed footage** | 90 % W × 90.5 % H, r = 9 px | footage on paper |
| **Photo card / print** | 70–76 % W × 88–93 % H, centred, r = 24 px | slideshow, carousel |
| **Dashed title frame** | 69 % W × 36 % H, centred slightly above the middle | chapter title on crumpled paper |
| **Watermark** | top-right, 1.4 % W right margin, 5.4 % H top margin, 5 % H tall, 75 % opacity | channel logo |

## Composition templates

### Model / product card (Archive)
```
┌──────────────────────────────────────────────┐
│                                              │
│             ███ Porsche 911 ███              │  ← title box, top 16.5 %H, 138 px tall
│        The price at launch is $6,500         │  ← subtitle 46 px, #554949
│                                              │
│                                              │  ← about 45 % empty paper
│          ▄▄▄▄▄██████████████▄▄▄▄             │
│        ▄█████████ car cut-out █████▄         │  ← 55–60 %W wide, bottom at 86–90 %H
└──────────────────────────────────────────────┘
paper #F7EDE4 + vignette −18 % + faint 35 px grid
```

### Quote card (Archive)
```
┌──────────────────────────────────────────────┐
│                                              │
│      "In the beginning I looked   ┌──────┐   │  ← quote: left 21 %W, top aligned
│      around and, not finding the  │ head │   │     with the head, justified italic
│      automobile of my dreams,     │      │▌  │  ← cut-out with a hard yellow
│      decided to build it myself." │ body │▌  │     offset shadow (+18 px right)
│          -Ferdinand Anton E. P.   │      │▌  │
└───────────────────────────────────┴──────┴───┘  ← portrait bleeds off the bottom
```

### Callout on a photo (Archive)
```
┌──────────────────────────────────────────────┐
│ ███ rear-engine design ███────╮              │  ← label box (102 px) top-left quadrant
│                                ╲             │  ← leader line 3–4 px, 45° then horizontal
│                                 ╲  ◯◯◯◯      │
│        full-bleed photo          ◯ disc ◯    │  ← multiply disc Ø 32–52 %H on the detail
│                                   ◯◯◯◯       │
└──────────────────────────────────────────────┘
```

### Hero title card (Ink & Paper)
```
━━NEVER DONE━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ← cap tops cut by the frame edge
 LEAVING A MARK                                 ← ink-bleed line, 98 %W
          ~~~ orange pencil scribbles ~~~       ← 35–80 %H drawing table
              D   ◜swoosh◝  Z
                    ‾‾‾‾‾ A
 Year:   Story::                  Department of  ← caption block bottom-left,
 1971    Swoosh                   Nike Archives  ← stamp bottom-right
```

### Scrapbook scene (Collage)
```
┌──────────────────────────────────────────────┐ layer stack, back → front:
│▓▓│ ░░grid strip░░ ┌─crumpled sheet───────┐ ▒ │ 0 white table #FFFFFF
│▓▓│                │ Be the        ◯◯◯◯◯  │ ▒ │ 1 paper border (green/coral) at an edge
│▓▓│  scan block    │ Bank.       ◯ hero  ◯│   │ 2 grid strip 15–35 %W
│▓▓│                │       ✧    ◯ cut-out◯│   │ 3 crumpled sheet 60–85 % of frame, rotated 0–2°
│▓▓│      ▬tape▬    │             ◯◯◯◯◯    │   │ 4 scan-noise block at the left edge
└──────────────────────────────────────────────┘ 5 halftone/stipple patch
                                                 6 pastel shape(s) (spotlight behind the hero)
                                                 7 B&W cut-outs → 8 colour hero object
                                                 9 doodles → 10 headline → 11 tape on top
```

## Layer counts

| Dialect | Layers per shot | Max |
|---|---|---|
| Archive | 3–5: paper → media (+ offset rim) → highlight shape → type → bullet | 5 |
| Ink & Paper | 4–8: paper → print → taped notes/tracing paper → cut-out → pen lines → stamps/letters → accent scribbles | 8 |
| Scrapbook | 8–12 (see the stack above) | 12 |
| Postcard | paper → sun → landmark (+ outline) → birds → title → vehicles back to front | 8 |

## Scale relationships

- Title type ≈ 2× caption type ≈ 2.5× chart type (Archive).
- Hero headline : caption block cap height is about **11 : 1** (Ink & Paper). Extreme contrast is
  the point.
- Hero object 35–60 % H tall; spotlight circle Ø **55–75 % H**; doodles 25–40 px; arrows
  140–280 px long (Scrapbook).
- A highlight rectangle covers exactly the line height of the words it marks.
- Callout disc Ø 32–52 % H.

## 9:16 zones (from the brand-film reference)

| Zone | Position |
|---|---|
| Headline block | top **8.5–19.5 % H**, centred, 2 lines, cap 4.8 % H |
| Caption line | baseline **52.5 % H**, cap 2.2 % H |
| Object | capital or top at 55–66 % H after the push-in |
| End-card text and logo | centred at 50–51 % H |
| Horizontal margin | ≥ 10 % W for the widest line |
