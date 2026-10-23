# 09 · Implementation (code)

How to build the style in code at 1080p and 4K. The reference stack is **Remotion 4 (React +
TypeScript)**, because it renders deterministic frames from code and scales to any resolution.
The same logic ports to Motion Canvas, After Effects expressions, or a canvas/WebGL renderer; see
§9.

Everything in this file was **type-checked** (`tsc --strict`) and **test-rendered** with Remotion
4.0.538. The asset script was run on test images.

## 1. Architecture

```
my-explainer/
├─ public/
│  ├─ fonts/            self-hosted .woff2 (see §4)
│  ├─ paper/            4–8 paper scans per dialect, ≥ 4096 px
│  ├─ cutouts/          PNG cut-outs with alpha, ≥ 2× their on-screen size at 1080p
│  └─ footage/          graded clips
├─ scripts/prep_assets.py   B&W, halftone, outlines (§7) · copy of references/tools/prep_assets.py
└─ src/
   ├─ index.ts / Root.tsx   compositions (1920×1080 @ 30 fps)
   ├─ vox/                  the style kit (this file)
   │  ├─ clock.ts           12 fps drawing clock, jitter, boil, wiggle
   │  ├─ ease.ts            easing tokens
   │  ├─ fonts.ts           local font loading
   │  ├─ Paper.tsx          paper ground, grid, vignette, boil
   │  ├─ HighlightBox.tsx   D1/D2 cursor → wipe
   │  ├─ CutOut.tsx         cut-outs with offset shadow / outline / echo
   │  ├─ Stroke.tsx         draw-on, tail-chase, retract, hand-drawn paths
   │  ├─ TypeOn.tsx         letter / word / scramble type-on with cursor
   │  ├─ FootageCaption.tsx D6 ▶ caption
   │  ├─ moves.tsx          settle, punch-out, exit push/pull, weave
   │  ├─ filters.tsx        ink-bleed and erode SVG filters
   │  └─ torn.ts            torn-edge clip paths
   └─ scenes/               one component per template in 08-scene-recipes.md
```

**Core principles in code:**

1. **Design in 1080p CSS pixels.** Every token is px@1080. Render 4K with `--scale=2`
   (Remotion renders at device-scale 2, so vectors and type stay sharp). Raster assets must be
   ≥ 2× their on-screen size.
2. **Graphics read `useDrawingFrame()`, never `useCurrentFrame()`.** Only camera moves on footage
   and maps, footage captions and fades use the raw frame.
3. **Tokens come from `tokens/vox-style.tokens.json`.** No hex codes inline in scenes.
4. **One component per device, one component per scene template.** Templates take content props
   (`title`, `image`, `subtitle`) and keep their timing internally, so repeated cards stay
   pixel-identical.

## 2. Clock, jitter, boil, wiggle

`src/vox/clock.ts`

```ts
import {interpolate, random, useCurrentFrame, useVideoConfig} from 'remotion';
import {noise2D} from '@remotion/noise';

export const DRAWINGS_PER_SECOND = 12;

/** The output frame held on the drawing clock: 30 fps → holds of 2,3,2,3 · 25 fps → 2×11 + 3 · 24 → 2 · 60 → 5. */
export const stepFrame = (frame: number, fps: number, dps = DRAWINGS_PER_SECOND): number =>
	Math.floor((Math.floor((frame * dps) / fps) * fps) / dps);

/** Use this instead of useCurrentFrame() for every graphic property. */
export const useDrawingFrame = (dps = DRAWINGS_PER_SECOND): number => {
	const frame = useCurrentFrame();
	const {fps} = useVideoConfig();
	return stepFrame(frame, fps, dps);
};

/** Clamped tween, the workhorse for every move. */
export const tween = (
	frame: number,
	start: number,
	duration: number,
	from: number,
	to: number,
	easing: (t: number) => number = (t) => t,
): number =>
	interpolate(frame, [start, start + Math.max(1, duration)], [from, to], {
		easing,
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
	});

/** Archive idle: a new random offset every 1/6 s for a landed graphic layer (never the paper). */
export const useHoldJitter = (seed: string, ampPx = 2, hz = 6) => {
	const frame = useCurrentFrame();
	const {fps} = useVideoConfig();
	const beat = Math.floor((frame * hz) / fps);
	const r = (k: string) => random(`${seed}-${k}-${beat}`) * 2 - 1;
	return {x: r('x') * ampPx, y: r('y') * ampPx, scale: 1 + r('s') * 0.003};
};

/** Boil index: changes every `everyFrames` output frames, stepped on the drawing clock. */
export const useBoil = (everyFrames: number): number => Math.floor(useDrawingFrame() / everyFrames);

/** Prop boil (Scrapbook): small re-placement of loose props on every boil tick. */
export const useBoilOffset = (seed: string, everyFrames = 15, ampPx = 6, rotDeg = 1.5) => {
	const tick = useBoil(everyFrames);
	const r = (k: string) => random(`${seed}-${k}-${tick}`) * 2 - 1;
	return {x: r('x') * ampPx, y: r('y') * ampPx, rotate: r('r') * rotDeg};
};

/** Postcard idle: smooth per-layer wiggle, on ones. */
export const useWiggle = (seed: string, ampPx = 6, hz = 0.8) => {
	const frame = useCurrentFrame();
	const {fps} = useVideoConfig();
	const t = (frame / fps) * hz;
	return {x: noise2D(`${seed}-x`, t, 0) * ampPx, y: noise2D(`${seed}-y`, t, 0) * ampPx};
};
```

`stepFrame` produces exactly the measured patterns: at 30 fps the drawing frames fall on
`frame % 5 ∈ {0, 3}` (holds of 2,3,2,3); at 25 fps there are eleven 2-frame holds and one 3-frame
hold per second; at 24 fps every hold is 2 frames; at 60 fps every hold is 5 frames.

## 3. Easing tokens

`src/vox/ease.ts`

```ts
import {Easing} from 'remotion';

/** Easing tokens from docs/05-motion.md §3. */
export const ease = {
	wipe: Easing.inOut(Easing.cubic), // highlighter boxes, 20–29 f
	settle: Easing.out(Easing.cubic), // slide into place, 6–8 f
	land: Easing.out(Easing.poly(4)), // rise from below / portrait slide, 30–40 f
	punchOut: Easing.out(Easing.exp), // cut over-scaled, zoom out to rest
	reveal: Easing.inOut(Easing.quad), // stepped zoom-out reveal, 12–15 f
	underline: Easing.out(Easing.cubic),
	exit: Easing.in(Easing.cubic), // into a cut, 3–8 f
	pushOut: Easing.in(Easing.exp), // Scrapbook push transition, outgoing
	pushIn: Easing.out(Easing.poly(5)), // Scrapbook push transition, incoming sheet
	linear: Easing.linear,
} as const;

/** easeOutBack: s≈1 → 6 % overshoot, s≈2.5 → 15 %, s≈3 → 23 %. */
export const pop = (s = 1.7) => Easing.out(Easing.back(s));
```

## 4. Fonts

The Google Fonts loaders fetch at render time. Self-host instead: render farms and sandboxes
often block or proxy font CDNs, and local files make renders reproducible. Download the `.woff2`
files once into `public/fonts/`.

`src/vox/fonts.ts`

```ts
import {staticFile} from 'remotion';
import {loadFont} from '@remotion/fonts';

/** Self-hosted fonts (public/fonts) keep renders deterministic and offline-safe. */
const FACES: {family: string; file: string; weight: string; style?: string}[] = [
	{family: 'Newsreader', file: 'fonts/Newsreader-400.woff2', weight: '400'},
	// {family: 'Gelasio', file: 'fonts/Gelasio-700-italic.woff2', weight: '700', style: 'italic'},
	// {family: 'EB Garamond', file: 'fonts/EBGaramond-500.woff2', weight: '500'},
	// {family: 'Playfair Display', file: 'fonts/PlayfairDisplay-400.woff2', weight: '400'},
	// {family: 'Inter', file: 'fonts/Inter-700.woff2', weight: '700'},
];

FACES.forEach((f) => loadFont({family: f.family, url: staticFile(f.file), weight: f.weight, style: f.style ?? 'normal'}));

export const FONT = {
	title: '"Newsreader", "Source Serif 4", Georgia, serif',
	label: '"Gelasio", Georgia, serif',
	headline: '"EB Garamond", "Cormorant Garamond", Garamond, serif',
	numerals: '"Playfair Display", "Libre Caslon Display", Didot, serif',
	sans: '"Inter", "Helvetica Neue", Arial, sans-serif',
};
```

## 5. Components

### 5.1 Paper

`src/vox/Paper.tsx`

```tsx
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {useBoil} from './clock';

type Props = {
	dialect: 'archive' | 'ink' | 'scrapbook' | 'postcard';
	/** Scanned or generated paper tiles in /public; swapped on the boil clock. */
	scans?: string[];
	boilEvery?: number;
	gridPitch?: number; // 35 Archive · 31 Ink · 29 Scrapbook strip · 0 = none
	gridAlpha?: number; // 0.012 faint · 0.06 visible
};

const GROUND = {archive: '#F7EDE4', ink: '#FDFDFD', scrapbook: '#FFFFFF', postcard: '#DFE0DB'};

export const Paper: React.FC<Props> = ({dialect, scans = [], boilEvery = 4, gridPitch = 0, gridAlpha = 0.012}) => {
	const tick = useBoil(boilEvery);
	const scan = scans.length > 0 ? scans[tick % scans.length] : null;
	const line = `rgba(60, 40, 30, ${gridAlpha})`;
	return (
		<AbsoluteFill style={{backgroundColor: GROUND[dialect]}}>
			{scan ? (
				<Img
					src={staticFile(scan)}
					style={{width: '100%', height: '100%', objectFit: 'cover', mixBlendMode: 'multiply'}}
				/>
			) : null}
			{gridPitch > 0 ? (
				<AbsoluteFill
					style={{
						backgroundImage: `linear-gradient(to right, ${line} 2px, transparent 2px), linear-gradient(to bottom, ${line} 2px, transparent 2px)`,
						backgroundSize: `${gridPitch}px ${gridPitch}px`,
					}}
				/>
			) : null}
			{dialect === 'archive' ? (
				// −16…−20 % luma at the corners, starting at about 32 % radius, slightly cool
				<AbsoluteFill
					style={{
						background: 'radial-gradient(ellipse at center, rgba(0,0,0,0) 32%, rgba(28,26,26,0.2) 100%)',
						mixBlendMode: 'multiply',
					}}
				/>
			) : null}
		</AbsoluteFill>
	);
};
```

Ink & Paper: pass 6 scans and `boilEvery={4}` (or 3). Scrapbook: crumpled-sheet scans with
`boilEvery={15}`, plus `useBoilOffset` on loose props.

### 5.2 Highlighter box (D1, D2)

`src/vox/HighlightBox.tsx`

```tsx
import React from 'react';
import {useDrawingFrame, tween} from './clock';
import {ease} from './ease';

type Props = {
	children: React.ReactNode;
	start: number; // frame the cursor appears
	duration?: number; // wipe length after the cursor hold (20–29 title, 10–16 labels)
	cursorHold?: number; // 1–5 f usually, up to 17 f
	cursorPx?: number; // 8–24 px
	color?: string;
	/** true: the box reveals its own text (titles). false: text is already visible (price, year). */
	maskText?: boolean;
	/** 'rtl' for callout labels growing from the leader-line end. */
	direction?: 'ltr' | 'rtl';
	/** Multiply over printed matter (newspaper, article, map). */
	multiply?: boolean;
	padding?: string; // e.g. '33px 51px 36px 54px' for 138 px title boxes
	easing?: (t: number) => number;
};

export const HighlightBox: React.FC<Props> = ({
	children,
	start,
	duration = 24,
	cursorHold = 3,
	cursorPx = 24,
	color = '#F6FA0E',
	maskText = true,
	direction = 'ltr',
	multiply = false,
	padding = '0.45em 0.5em 0.4em 0.5em',
	easing = ease.wipe,
}) => {
	const f = useDrawingFrame();
	const p = tween(f, start + cursorHold, duration, 0, 1, easing);
	const hidden = `calc(${(1 - p).toFixed(4)} * (100% - ${cursorPx}px))`;
	const clip = direction === 'ltr' ? `inset(0 ${hidden} 0 0)` : `inset(0 0 0 ${hidden})`;
	const visible = f >= start;
	return (
		<div style={{position: 'relative', display: 'inline-block'}}>
			<div
				style={{
					position: 'absolute',
					inset: 0,
					background: color,
					clipPath: clip,
					mixBlendMode: multiply ? 'multiply' : 'normal',
					opacity: visible ? 1 : 0,
				}}
			/>
			<div
				style={{
					position: 'relative',
					padding,
					clipPath: maskText ? clip : undefined,
					opacity: maskText && !visible ? 0 : 1,
				}}
			>
				{children}
			</div>
		</div>
	);
};
```

```tsx
// Title box (D10): 138 px tall, text masked by the box
<HighlightBox start={12} duration={24} padding="33px 51px 36px 54px">
  <span style={{fontFamily: FONT.title, fontSize: 98, lineHeight: '69px', color: '#2B2010'}}>Porsche 911</span>
</HighlightBox>

// Callout label (D3): grows right-to-left from the leader line
<HighlightBox start={40} duration={9} direction="rtl" cursorHold={0} padding="21px 33px 15px 39px">…</HighlightBox>

// Highlight on print (D2): multiply, text already visible
<HighlightBox start={0} duration={20} maskText={false} multiply padding="0 4px">…</HighlightBox>
```

### 5.3 Cut-outs

`src/vox/CutOut.tsx`

```tsx
import React from 'react';
import {Img, staticFile} from 'remotion';

type Edge =
	| {kind: 'none'}
	| {kind: 'offsetShadow'; color?: string; dx?: number; dy?: number} // Archive: hard accent copy, no blur
	| {kind: 'outline'; color: string; width?: number} // Postcard sticker (#FFF, 14 px) or accent outline (13 px)
	| {kind: 'echo'; color: string; dx?: number}; // Scrapbook misregistered colour copy

type Props = {src: string; width: number; edge?: Edge; style?: React.CSSProperties};

/** Pre-baked outlines (scripts/outline.py) look best; the SVG filter is fine for previews. */
export const CutOut: React.FC<Props> = ({src, width, edge = {kind: 'none'}, style}) => {
	const id = `vox-outline-${src.replace(/[^a-z0-9]/gi, '')}`;
	let filter: string | undefined;
	if (edge.kind === 'offsetShadow') {
		filter = `drop-shadow(${edge.dx ?? 18}px ${edge.dy ?? 2}px 0 ${edge.color ?? '#E3EF0A'})`;
	}
	if (edge.kind === 'echo') {
		filter = `drop-shadow(${edge.dx ?? 27}px 0 0 ${edge.color})`;
	}
	if (edge.kind === 'outline') {
		filter = `url(#${id})`;
	}
	return (
		<>
			{edge.kind === 'outline' ? (
				<svg width={0} height={0} style={{position: 'absolute'}}>
					<filter id={id} x="-15%" y="-15%" width="130%" height="130%">
						<feMorphology in="SourceAlpha" operator="dilate" radius={edge.width ?? 14} result="grown" />
						{/* soften the square corners of feMorphology, then re-threshold */}
						<feGaussianBlur in="grown" stdDeviation={(edge.width ?? 14) * 0.25} result="soft" />
						<feComponentTransfer in="soft" result="round">
							<feFuncA type="linear" slope={6} intercept={-2.5} />
						</feComponentTransfer>
						<feFlood floodColor={edge.color} result="ink" />
						<feComposite in="ink" in2="round" operator="in" result="stroke" />
						<feMerge>
							<feMergeNode in="stroke" />
							<feMergeNode in="SourceGraphic" />
						</feMerge>
					</filter>
				</svg>
			) : null}
			<Img src={staticFile(src)} style={{width, filter, display: 'block', ...style}} />
		</>
	);
};
```

```tsx
<CutOut src="cutouts/ferry.png" width={520} edge={{kind: 'offsetShadow'}} />                 // Archive portrait
<CutOut src="cutouts/print.png" width={1340} edge={{kind: 'offsetShadow', dx: 6, dy: 6}} />  // photo card rim
<CutOut src="cutouts/truck.png" width={600} edge={{kind: 'outline', color: '#FFFFFF'}} />    // Postcard sticker
<CutOut src="cutouts/padlock.png" width={500} edge={{kind: 'echo', color: '#F07457'}} />      // Scrapbook echo
```

### 5.4 Strokes (circles, underlines, scribbles, arrows)

`src/vox/Stroke.tsx`

```tsx
import React from 'react';
import {random} from 'remotion';
import {getLength} from '@remotion/paths';
import {useDrawingFrame, tween} from './clock';
import {ease} from './ease';

type Props = {
	d: string;
	start: number;
	drawFrames: number;
	holdFrames?: number;
	/** 'chase': the tail follows the head (pencil scribbles) · 'retract': un-draw back to the start (face circles) · 'none': stays */
	exit?: 'none' | 'chase' | 'retract';
	exitFrames?: number;
	color?: string;
	width?: number;
	opacity?: number;
	multiply?: boolean;
	easing?: (t: number) => number;
	viewBox?: string;
};

export const Stroke: React.FC<Props> = ({
	d,
	start,
	drawFrames,
	holdFrames = 0,
	exit = 'none',
	exitFrames = 8,
	color = '#F6FA0E',
	width = 6,
	opacity = 1,
	multiply = false,
	easing = ease.underline,
	viewBox = '0 0 1920 1080',
}) => {
	const f = useDrawingFrame();
	const length = getLength(d);
	const exitStart = start + drawFrames + holdFrames;
	let head = tween(f, start, drawFrames, 0, length, easing);
	let tail = 0;
	if (exit === 'chase') tail = tween(f, exitStart, exitFrames, 0, length, ease.linear);
	if (exit === 'retract') head = Math.min(head, tween(f, exitStart, exitFrames, length, 0, ease.exit));
	const visible = head - tail;
	if (f < start || visible <= 0.5) return null;
	return (
		<svg viewBox={viewBox} style={{position: 'absolute', inset: 0, width: '100%', height: '100%', overflow: 'visible'}}>
			<path
				d={d}
				fill="none"
				stroke={color}
				strokeWidth={width}
				strokeLinecap="round"
				strokeLinejoin="round"
				strokeDasharray={`${visible} ${length}`}
				strokeDashoffset={-tail}
				opacity={opacity}
				style={{mixBlendMode: multiply ? 'multiply' : 'normal'}}
			/>
		</svg>
	);
};

type Pt = [number, number];

/** Smooth Catmull-Rom path through points, each jittered by ±amp px (stable per seed). */
export const handDrawnPath = (pts: Pt[], amp: number, seed: string): string => {
	const p = pts.map(([x, y], i): Pt => [
		x + (random(`${seed}-x-${i}`) * 2 - 1) * amp,
		y + (random(`${seed}-y-${i}`) * 2 - 1) * amp,
	]);
	let d = `M ${p[0][0].toFixed(1)} ${p[0][1].toFixed(1)}`;
	for (let i = 0; i < p.length - 1; i++) {
		const p0 = p[Math.max(0, i - 1)];
		const p1 = p[i];
		const p2 = p[i + 1];
		const p3 = p[Math.min(p.length - 1, i + 2)];
		const c1: Pt = [p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6];
		const c2: Pt = [p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6];
		d += ` C ${c1[0].toFixed(1)} ${c1[1].toFixed(1)} ${c2[0].toFixed(1)} ${c2[1].toFixed(1)} ${p2[0].toFixed(1)} ${p2[1].toFixed(1)}`;
	}
	return d;
};

/** Points of a hand-drawn ellipse. Angles in screen space: -120° = 11 o'clock, 90° = 6 o'clock; turns > 1 leaves an open, overshooting loop. */
export const ellipsePoints = (cx: number, cy: number, rx: number, ry: number, startDeg = -120, turns = 1.08, n = 28): Pt[] =>
	Array.from({length: n + 1}, (_, i) => {
		const a = ((startDeg + (360 * turns * i) / n) * Math.PI) / 180;
		const drift = 1 + 0.04 * (i / n); // the end lands slightly outside the start
		return [cx + Math.cos(a) * rx * drift, cy + Math.sin(a) * ry * drift];
	});
```

```tsx
// D17 circle around a face: drawn in 17 f, un-drawn in 8 f before the cut
<Stroke d={handDrawnPath(ellipsePoints(1210, 300, 120, 140), 4, 'ferry')} start={10} drawFrames={17}
        holdFrames={30} exit="retract" exitFrames={8} width={14} color="#F6FA0E" />

// D21 pencil scribble: the tail chases the head
<Stroke d={handDrawnPath([[300, 640], [700, 560], [1100, 700], [1500, 600]], 18, 'sc1')} start={20}
        drawFrames={6} holdFrames={6} exit="chase" exitFrames={6} width={8} color="#E07964" opacity={0.9} />
```

### 5.5 Type-on

`src/vox/TypeOn.tsx`

```tsx
import React from 'react';
import {random} from 'remotion';
import {useDrawingFrame} from './clock';

type Props = {
	text: string;
	start: number;
	unit: 'char' | 'word' | 'scramble';
	/** Frames per unit on the drawing clock: 2 = 1 letter per drawing, 0.8 ≈ 2.5 chars per drawing, 4 = 1 word per 2 drawings. */
	framesPerUnit: number;
	/** Trailing cursor while typing, e.g. '_' for archive caption blocks. */
	cursor?: string;
	style?: React.CSSProperties;
};

/** Types text in its final position (the unrevealed rest is laid out but invisible, so nothing shifts). */
export const TypeOn: React.FC<Props> = ({text, start, unit, framesPerUnit, cursor, style}) => {
	const f = useDrawingFrame();
	const steps = f < start ? 0 : Math.floor((f - start) / framesPerUnit) + 1;

	if (unit === 'scramble') {
		// letters appear in random order (archive stamps), resolving after text.length units
		const order = Array.from(text, (_, i) => i).sort((a, b) => random(`s${a}${text}`) - random(`s${b}${text}`));
		const shown = new Set(order.slice(0, steps));
		return (
			<span style={style}>
				{Array.from(text, (ch, i) => (
					<span key={i} style={{opacity: shown.has(i) ? 1 : 0}}>
						{ch}
					</span>
				))}
			</span>
		);
	}

	const units = unit === 'char' ? Array.from(text) : text.split(' ');
	const count = Math.min(units.length, steps);
	const joiner = unit === 'char' ? '' : ' ';
	const shown = units.slice(0, count).join(joiner);
	const rest = text.slice(shown.length);
	const typing = count > 0 && count < units.length;
	return (
		<span style={style}>
			{shown}
			{cursor ? <span style={{opacity: typing ? 1 : 0}}>{cursor}</span> : null}
			<span style={{opacity: 0}}>{rest}</span>
		</span>
	);
};
```

```tsx
<TypeOn text="NEVER DONE" unit="char" framesPerUnit={2} start={18} />          // headline line 1
<TypeOn text="LEAVING A MARK" unit="word" framesPerUnit={4} start={35} />      // ink-bleed line 2 (+ filter)
<TypeOn text="Swoosh" unit="char" framesPerUnit={0.8} start={27} cursor="_" /> // caption block
<TypeOn text="Department of Nike Archives" unit="scramble" framesPerUnit={1.1} start={71} />
```

For ink-bleed, wrap the line in `<span style={{filter: 'url(#vox-ink-bleed)'}}>` and mount
`<VoxFilters />` once per composition.

### 5.6 Footage caption (D6)

`src/vox/FootageCaption.tsx`

```tsx
import React from 'react';
import {useCurrentFrame} from 'remotion';
import {tween} from './clock';
import {ease} from './ease';

type Props = {
	text: string;
	start: number; // frame the ▲ starts rising (3–7 f after the cut)
	end: number; // the cut that ends the caption
	onBright?: boolean; // bright footage → dark text
	fontFamily: string; // Gelasio
	keepBullet?: boolean; // the sentence continues in the next shot: no bullet animation
};

/** D6: ▲ rises (7 f), spins −270° to ▶ (12 f), text fades in (7 f), fades out over the last 6 f. On ones. */
export const FootageCaption: React.FC<Props> = ({text, start, end, onBright = false, fontFamily, keepBullet = false}) => {
	const f = useCurrentFrame();
	const rise = keepBullet ? 0 : tween(f, start, 7, 135, 0, ease.settle);
	const rot = keepBullet ? -360 : tween(f, start + 7, 12, -90, -360, ease.settle);
	const textStart = keepBullet ? start : start + 17;
	const opacity = Math.min(tween(f, textStart, 7, 0, 1), tween(f, end - 6, 6, 1, 0));
	return (
		<div style={{position: 'absolute', left: '10%', right: '9%', top: '90%', transform: 'translateY(-100%)', display: 'flex', alignItems: 'center', gap: 36}}>
			<svg width={57} height={57} viewBox="0 0 10 10" style={{transform: `translateY(${rise}px) rotate(${rot}deg)`, flex: 'none'}}>
				<path d="M1 0.5 L9.5 5 L1 9.5 Z" fill={onBright ? '#F6FA0E' : '#0A0A0A'} />
			</svg>
			<div
				style={{
					fontFamily,
					fontStyle: 'italic',
					fontWeight: 700,
					fontSize: 52,
					color: onBright ? '#3B2A1C' : '#E8F010',
					opacity,
					transform: `translateY(${(1 - opacity) * 4}px)`,
					whiteSpace: 'nowrap',
				}}
			>
				{text}
			</div>
		</div>
	);
};
```

### 5.7 Moves (settle, punch-out, exits, weave)

`src/vox/moves.tsx`

```tsx
import React from 'react';
import {AbsoluteFill, useCurrentFrame} from 'remotion';
import {useDrawingFrame, useHoldJitter, tween} from './clock';
import {ease} from './ease';

type Wrap = {children: React.ReactNode; style?: React.CSSProperties};

/** Slide the last 4–10 % W into place at the start of a shot (6–8 f, easeOutCubic, stepped). */
export const Settle: React.FC<Wrap & {start?: number; dx?: number; dy?: number; frames?: number}> = ({
	children,
	start = 0,
	dx = 100,
	dy = 0,
	frames = 7,
	style,
}) => {
	const f = useDrawingFrame();
	const p = tween(f, start, frames, 1, 0, ease.settle);
	return <div style={{transform: `translate(${dx * p}px, ${dy * p}px)`, ...style}}>{children}</div>;
};

/** Cut in 1.7–2.4× too tight and step out to rest (stepped zoom-out reveal / hero punch-out). */
export const PunchOut: React.FC<Wrap & {start?: number; from?: number; frames?: number; origin?: string; easing?: (t: number) => number}> = ({
	children,
	start = 0,
	from = 1.8,
	frames = 13,
	origin = '50% 50%',
	easing = ease.reveal,
}) => {
	const f = useDrawingFrame();
	const s = tween(f, start, frames, from, 1, easing);
	return <AbsoluteFill style={{transform: `scale(${s})`, transformOrigin: origin}}>{children}</AbsoluteFill>;
};

/** Zoom-through, outgoing half: accelerate +5…19 % over the last 3–8 f before `end` (on ones). */
export const ExitPush: React.FC<Wrap & {end: number; frames?: number; to?: number; origin?: string}> = ({
	children,
	end,
	frames = 6,
	to = 1.12,
	origin = '50% 50%',
}) => {
	const f = useCurrentFrame();
	const s = tween(f, end - frames, frames, 1, to, ease.exit);
	return <AbsoluteFill style={{transform: `scale(${s})`, transformOrigin: origin}}>{children}</AbsoluteFill>;
};

/** Pull-away before a cut: shrink to 0.88–0.95× in the last 3–5 f. */
export const ExitPull: React.FC<Wrap & {end: number; frames?: number; to?: number}> = ({children, end, frames = 4, to = 0.9}) => {
	const f = useCurrentFrame();
	const s = tween(f, end - frames, frames, 1, to, ease.exit);
	return <AbsoluteFill style={{transform: `scale(${s})`}}>{children}</AbsoluteFill>;
};

/** Archive idle: wrap any landed graphic layer (not the paper). */
export const Weave: React.FC<Wrap & {seed: string; amp?: number}> = ({children, seed, amp = 2, style}) => {
	const j = useHoldJitter(seed, amp);
	return <div style={{transform: `translate(${j.x}px, ${j.y}px) scale(${j.scale})`, ...style}}>{children}</div>;
};
```

### 5.8 Ink-bleed and erode filters

`src/vox/filters.tsx`

```tsx
import React from 'react';

/**
 * Mount once per composition, then use `filter: url(#vox-ink-bleed)` / `url(#vox-erode)` on text.
 * Ink-bleed = dilate + noise wobble + "gooey" blur/threshold, which swells stroke ends into blobs.
 * Erode = noise holes punched into the glyphs + rough edges (distressed emphasis word).
 */
export const VoxFilters: React.FC<{inkColor?: string}> = ({inkColor = '#111111'}) => (
	<svg width={0} height={0} style={{position: 'absolute'}}>
		<filter id="vox-ink-bleed" x="-10%" y="-20%" width="120%" height="140%">
			<feMorphology in="SourceAlpha" operator="dilate" radius={1.5} result="fat" />
			<feTurbulence type="fractalNoise" baseFrequency={0.06} numOctaves={2} seed={3} result="noise" />
			<feDisplacementMap in="fat" in2="noise" scale={7} xChannelSelector="R" yChannelSelector="G" result="wobble" />
			<feGaussianBlur in="wobble" stdDeviation={2.4} result="soft" />
			<feComponentTransfer in="soft" result="blobs">
				<feFuncA type="linear" slope={7} intercept={-2.6} />
			</feComponentTransfer>
			<feFlood floodColor={inkColor} result="ink" />
			<feComposite in="ink" in2="blobs" operator="in" />
		</filter>
		<filter id="vox-erode" x="-5%" y="-5%" width="110%" height="110%">
			<feTurbulence type="fractalNoise" baseFrequency={0.45} numOctaves={2} seed={7} result="grain" />
			<feColorMatrix in="grain" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -3 1.9" result="holes" />
			<feComposite in="SourceGraphic" in2="holes" operator="in" result="pitted" />
			<feTurbulence type="turbulence" baseFrequency={0.12} numOctaves={1} seed={11} result="edgeNoise" />
			<feDisplacementMap in="pitted" in2="edgeNoise" scale={3} xChannelSelector="R" yChannelSelector="G" />
		</filter>
	</svg>
);
```

The SVG ink-bleed is a good approximation for motion. For a hero title held on screen for
seconds, bake the ink-bleed into a PNG or SVG instead (render the text, add circles at stroke
terminals and joints, smooth-union them, then threshold), so it stays perfectly static and boil-free.

### 5.9 Torn edges

`src/vox/torn.ts`

```ts
import {random} from 'remotion';
import {noise2D} from '@remotion/noise';

type Side = 'top' | 'right' | 'bottom' | 'left';

/**
 * CSS clip-path polygon for a rectangle with torn sides.
 * amp: torn depth in px (6–20) · step: sample spacing in px · grow: push the edge outward (use for the white fibre band, 12–37 px).
 */
export const tornRect = (w: number, h: number, seed: string, sides: Side[], amp = 12, step = 7, grow = 0): string => {
	const edge = (len: number, side: Side) => {
		const pts: number[] = [];
		for (let s = 0; s <= len; s += step) {
			const torn = sides.includes(side);
			const low = noise2D(`${seed}-${side}`, s / 90, 0) * amp; // long wavy tear
			const high = (random(`${seed}-${side}-${s}`) - 0.5) * amp * 0.5; // fibre jaggies
			pts.push(torn ? low + high - grow : 0);
		}
		return pts;
	};
	const out: string[] = [];
	edge(w, 'top').forEach((o, i) => out.push(`${Math.min(w, i * step)}px ${o}px`));
	edge(h, 'right').forEach((o, i) => out.push(`${w - o}px ${Math.min(h, i * step)}px`));
	edge(w, 'bottom').forEach((o, i) => out.push(`${w - Math.min(w, i * step)}px ${h - o}px`));
	edge(h, 'left').forEach((o, i) => out.push(`${o}px ${h - Math.min(h, i * step)}px`));
	return `polygon(${out.join(', ')})`;
};
```

```tsx
// White fibre band behind, torn photo in front (T7 tunnel: repeat 5–6× at +4 % scale)
<div style={{position: 'absolute', inset: 0, background: '#FBFAF6', clipPath: tornRect(1200, 800, 'p1', ['right'], 14, 7, 24)}} />
<Img src={staticFile('cutouts/knight.png')} style={{clipPath: tornRect(1200, 800, 'p1b', ['right'], 12)}} />
```

## 6. A complete scene: model card (D10)

`src/scenes/ModelCard.tsx`

```tsx
import React from 'react';
import {AbsoluteFill} from 'remotion';
import {FONT} from '../vox/fonts';
import {Paper} from '../vox/Paper';
import {HighlightBox} from '../vox/HighlightBox';
import {CutOut} from '../vox/CutOut';
import {Settle, ExitPull, Weave} from '../vox/moves';
import {useDrawingFrame, tween} from '../vox/clock';

const serif = FONT.title;

type Props = {title: string; subtitle: string; image: string; durationInFrames: number};

/** D10 · Model / product card, 75 f at 30 fps. */
export const ModelCard: React.FC<Props> = ({title, subtitle, image, durationInFrames}) => {
	const f = useDrawingFrame();
	const subtitleReveal = tween(f, 17, 14, 0, 1); // starts 5 f after the box cursor, finishes before it
	return (
		<AbsoluteFill>
			<Paper dialect="archive" gridPitch={35} />
			<ExitPull end={durationInFrames} to={0.9}>
				<AbsoluteFill style={{alignItems: 'center'}}>
					<Weave seed="title" style={{marginTop: 178 /* 16.5 % of 1080 — % margins resolve against width */}}>
						<HighlightBox start={12} duration={24} cursorHold={2} padding="33px 51px 36px 54px">
							<span style={{fontFamily: serif, fontSize: 98, lineHeight: '69px', color: '#2B2010', whiteSpace: 'nowrap'}}>{title}</span>
						</HighlightBox>
					</Weave>
					<Weave seed="subtitle" style={{marginTop: 40}}>
						<div
							style={{
								fontFamily: serif,
								fontSize: 46,
								color: '#554949',
								WebkitMaskImage: `linear-gradient(to right, #000 ${subtitleReveal * 120 - 20}%, transparent ${subtitleReveal * 120}%)`,
							}}
						>
							{subtitle}
						</div>
					</Weave>
				</AbsoluteFill>
				<AbsoluteFill style={{justifyContent: 'flex-end', alignItems: 'center', paddingBottom: '11%'}}>
					<Settle dx={100} frames={7}>
						<Weave seed="car">
							<CutOut src={image} width={1100} />
						</Weave>
					</Settle>
				</AbsoluteFill>
			</ExitPull>
		</AbsoluteFill>
	);
};
```

`src/Root.tsx`

```tsx
import React from 'react';
import {Composition, Series} from 'remotion';
import {ModelCard} from './scenes/ModelCard';
import {VoxFilters} from './vox/filters';

const Explainer: React.FC = () => (
	<>
		<VoxFilters />
		<Series>
			<Series.Sequence durationInFrames={75}>
				<ModelCard title="Porsche 911" subtitle="The price at launch is $6,500" image="cutouts/911_side.png" durationInFrames={75} />
			</Series.Sequence>
		</Series>
	</>
);

export const RemotionRoot: React.FC = () => (
	// Design at 1920×1080 CSS px; render 4K with --scale=2
	<Composition id="Explainer" component={Explainer} durationInFrames={75} fps={30} width={1920} height={1080} />
);
```

Test render of frame 40, checked by pixel measurement: the title box top is at 16.7 % H and the
box is 137 px tall (reference: 16.5 % / 138 px); paper centre `#F7EDE4`; corners about 18 % darker.

## 7. Asset preparation

Treat photos **before** they enter the composition. It is faster to render, and the look is
consistent.

`scripts/prep_assets.py`

```python
"""Asset prep for the vox style: archival B&W, newspaper halftone, round-join outlines.

usage:
  python3 prep_assets.py bw       in.png out.png [--contrast 1.35]
  python3 prep_assets.py halftone in.png out.png [--period 11] [--angle 45]
  python3 prep_assets.py outline  in.png out.png [--width 28] [--color #FFFFFF]
Inputs with transparency (cut-outs) keep their alpha. Sizes are in output pixels:
at 4K use period 11 / width 28 (= 5.5 px and 14 px at 1080p).
"""
import argparse
import math

import numpy as np
from PIL import Image, ImageDraw, ImageOps


def archival_bw(img, contrast=1.35):
    alpha = img.getchannel("A") if img.mode == "RGBA" else None
    g = np.asarray(ImageOps.grayscale(img), np.float32) / 255.0
    g = np.clip((g - 0.5) * contrast + 0.5, 0, 1)          # +35 % contrast
    g = np.clip((g - 0.06) / 0.92, 0, 1)                    # crush blacks, blow highlights
    out = Image.fromarray((g * 255).astype(np.uint8)).convert("RGB")
    if alpha is not None:
        out.putalpha(alpha)
    return out


def halftone(img, period=11, angle=45):
    """Black dots on white, 45° screen; dot area proportional to darkness."""
    alpha = img.getchannel("A") if img.mode == "RGBA" else None
    g = ImageOps.grayscale(img)
    w, h = g.size
    diag = int(math.hypot(w, h)) + 2 * period
    rot = g.rotate(angle, expand=True, fillcolor=255, resample=Image.BICUBIC)
    rot = ImageOps.pad(rot, (diag, diag), color=255)
    small = rot.resize((diag // period, diag // period), Image.BOX)
    dots = Image.new("L", (diag * 2, diag * 2), 255)        # 2× supersampling for clean dots
    d = ImageDraw.Draw(dots)
    s = np.asarray(small, np.float32) / 255.0
    cell = period * 2
    for j in range(s.shape[0]):
        for i in range(s.shape[1]):
            dark = 1.0 - s[j, i]
            if dark < 0.02:
                continue
            r = cell * 0.5 * math.sqrt(dark) * 1.12          # area ∝ darkness, full cells touch
            cx, cy = (i + 0.5) * cell, (j + 0.5) * cell
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=0)
    dots = dots.resize((diag, diag), Image.LANCZOS).rotate(-angle, resample=Image.BICUBIC, fillcolor=255)
    left, top = (diag - w) // 2, (diag - h) // 2
    out = dots.crop((left, top, left + w, top + h)).convert("RGB")
    if alpha is not None:
        out.putalpha(alpha)
    return out


def outline(img, width=28, color="#FFFFFF"):
    """Outside-only stroke with round joins (true disc dilation), no gap, no shadow."""
    img = img.convert("RGBA")
    a = np.asarray(img.getchannel("A")) > 127
    pad = width + 2
    a = np.pad(a, pad)
    grown = np.zeros_like(a)
    for dy in range(-width, width + 1):
        for dx in range(-width, width + 1):
            if dx * dx + dy * dy <= width * width:
                grown |= np.roll(np.roll(a, dy, 0), dx, 1)
    rgb = tuple(int(color.lstrip("#")[k:k + 2], 16) for k in (0, 2, 4))
    stroke = Image.new("RGBA", grown.shape[::-1], rgb + (0,))
    stroke.putalpha(Image.fromarray((grown * 255).astype(np.uint8)))
    base = Image.new("RGBA", stroke.size, (0, 0, 0, 0))
    base.alpha_composite(stroke)
    base.alpha_composite(img, (pad, pad))
    return base


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["bw", "halftone", "outline"])
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--contrast", type=float, default=1.35)
    ap.add_argument("--period", type=int, default=11)
    ap.add_argument("--angle", type=float, default=45)
    ap.add_argument("--width", type=int, default=28)
    ap.add_argument("--color", default="#FFFFFF")
    o = ap.parse_args()
    im = Image.open(o.src)
    im = im.convert("RGBA") if "A" in im.getbands() else im.convert("RGB")
    if o.mode == "bw":
        res = archival_bw(im, o.contrast)
    elif o.mode == "halftone":
        res = halftone(im, o.period, o.angle)
    else:
        res = outline(im, o.width, o.color)
    res.save(o.dst)
    print(f"{o.mode}: {o.src} -> {o.dst} {res.size}")
```

| Job | Command (4K-ready sizes) |
|---|---|
| Archival B&W | `python3 scripts/prep_assets.py bw in.png out.png --contrast 1.35` |
| Newspaper halftone | `python3 scripts/prep_assets.py halftone in.png out.png --period 11 --angle 45` |
| Sticker outline | `python3 scripts/prep_assets.py outline cutout.png out.png --width 28 --color "#FFFFFF"` |
| Accent outline | `python3 scripts/prep_assets.py outline cutout.png out.png --width 26 --color "#F6E916"` |

**Cut-outs:** mask by hand, or use a background remover (e.g. `rembg`) and then clean the edges.
Hard edges only: erode the matte 1 px and don't feather it.

**Paper scans:** scan at 600 dpi, or photograph under flat light. Make 4–8 variants per stock so
the boil has material to swap between. Remove colour casts to match the dialect palette.

## 8. Rendering

```bash
# preview
npx remotion studio

# 1080p master (H.264, visually lossless)
npx remotion render src/index.ts Explainer out/explainer-1080.mp4 --codec=h264 --crf=16

# 4K from the same 1080p design
npx remotion render src/index.ts Explainer out/explainer-2160.mp4 --scale=2 --codec=h264 --crf=16

# mezzanine for editing / grading
npx remotion render src/index.ts Explainer out/explainer.mov --codec=prores --prores-profile=hq

# a single frame for review
npx remotion still src/index.ts Explainer out/f40.png --frame=40
```

**Pitfalls found while testing:**

- **Percentage margins resolve against the *width*.** `marginTop: '16.5%'` puts a box at 29 % H,
  not 16.5 % H. Use px (16.5 % × 1080 = 178 px) or `top: '16.5%'` on an absolutely positioned
  element.
- **Zero-length dashes still draw round caps**, so `Stroke` returns `null` until there is about
  0.5 px of visible stroke.
- **`feMorphology` dilates with a square kernel**, which gives square corners. The CutOut filter
  rounds them with blur and threshold; for final renders, bake the outline with `prep_assets.py`
  (a true disc dilation).
- **Web fonts can fail behind proxies** (certificate errors in headless Chrome). Self-host them (§4).
- Don't animate `filter: blur()` on large layers at 4K. Blur stills once, or use the montage
  sparingly.

## 9. Porting to other tools

| Concept | After Effects | Motion Canvas | Canvas / WebGL |
|---|---|---|---|
| 12 fps clock | `posterizeTime(12)` on every graphic property, or render the comp at 12 fps and nest it with *Preserve frame rate* | `const t = Math.floor(time() * 12) / 12` in signals | quantise `t` before evaluating tweens |
| Hold jitter 6 Hz | `posterizeTime(6); wiggle(6, 2)` on position | `random.gauss` reseeded per 1/6 s | hash(seed, floor(t × 6)) |
| Cursor → wipe | rectangle mask with the right-edge path keyframed, easy ease (influence 75 %) | `rect.width(…, 0.8, easeInOutCubic)` | scissor rect |
| Offset shadow | Drop Shadow, softness 0, opacity 100 %, distance 18, direction 90° | duplicate node with `filters.colorize` | draw the silhouette twice |
| Draw-on | Trim Paths | `line.end(1, 0.6)` | dash offset |
| Ink-bleed | Roughen Edges + Simple Choker | SVG filter | SDF smooth-union shader |
| Paper boil | Time-remap a layer of scans with `posterizeTime(8)` | swap texture every 4 frames | swap texture index |
