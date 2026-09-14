# The Banana Board — B-side site (English) — handoff

## Context

Demo material for a talk about AI and human creativity. A fictional trade body for bananas, produced twice over:

- **A-side** — deliberately generic. Yellow, friendly, every AI default left untouched. Swedish only.
- **B-side** — steel industry and British punk. Dark, hard, every choice made by a person. Swedish and English.

This file covers the **English B-side site** only. `CLAUDE.md` (Swedish) covers the whole project and is still the source of truth for everything else.

The point of the talk is the comparison between the two sides. Never merge them, never soften the B-side toward the A-side, and never delete either.

## Files

```
human.html                       ← source, references bilder/ relatively
BananaBoard-site-punk-en.html    ← built: same page, images inlined as base64
src/build_embedded_punk_en.py    ← builds the above
bilder/punk/                     ← 1-bit photocopied images, shared with the Swedish version
```

The source file was named `index-punk-en.html` when it was handed over. In this
repo it is `human.html`, because it is served by GitHub Pages as the "human"
half of the switch described below, and the URL is visible during the talk.
`src/build_embedded_punk_en.py` reads the new name.

Build:

```bash
python src/build_embedded_punk_en.py
```

Never edit `BananaBoard-site-punk-en.html` directly — it is generated.

## Do not improve the design

This is the single rule that must not be broken. The B-side is a deliberate aesthetic, not a draft.

- **No yellow.** The palette is slag `#101010`, cold-rolled `#7C858C`, oxide `#A8340F`, scream pink `#FF1E6F`, bleached `#D8D2C2`. Yellow belongs to the A-side and never comes back.
- **Zero rounded corners.** `border-radius: 0 !important` sits in the `*` rule and stays there.
- **No soft shadows, no gradients, no animation.** Depth is a hard offset block in flat colour (`12px 12px 0`), a riveted steel plate, or a hazard band. Buttons move into their own shadow on click. That is the entire interaction model.
- **Grain everywhere.** A fixed `feTurbulence` layer sits over the whole page at `opacity .3, mix-blend-mode: multiply`. Keep it.
- **Photos are 1-bit.** Hard photocopy, no greyscale, produced by `src/punk_bilder.py`. No lifestyle photography, no smiling models, no studio light — the design system forbids all three, so they must not appear on the page either.
- **Stencils are hand-drawn inline SVG.** The pistol, the telephone and the slip are the same paths used in the B-side PDF. If you redraw one, redraw it in both places. Do not swap them for icon-library clipart.
- **Ransom-note headings** (a different font per word, rotated) are a tool, not a bug.

Fonts: Anton (headings), Staatliches (stencil, labels), Special Elite (fanzine text), Archivo (body). All four load from Google Fonts. Without them the whole expression collapses to a fallback sans.

## The switch

Both sides carry a fixed control in the bottom-left corner: **Non-human** on the
left (the A-side, `index.html`, the default) and **Human** on the right (this
page). It is an ordinary link, so it works without JavaScript and the knob
position is static — nothing animates.

The control belongs to the talk, not to either design. It is deliberately
neutral: square, monospace, greyscale, identical markup and CSS on both pages,
prefixed `hm-`. That is the point — it is the only constant while everything
around it changes. Do not restyle it to match either side.

Square corners are not a coincidence either: the B-side's `border-radius: 0
!important` would flatten a rounded control on this page only, and the two
would stop matching.

## Voice

Second person, imperative, short. Never a sentence that asks permission. British English — "fibre", "shop", "bin", "carry on". This deliberately breaks the agency's usual formal-pronoun convention for ad copy; that is the point of the B-side.

The Swedish A-side says "Nature's own energy boost". The English B-side strikes that exact line through in the myths block. Keep that connection intact.

## Facts are load-bearing

The `#fakta` section carries six claims that can all be looked up: potassium-40 and the banana equivalent dose (~0.1 µSv), the 2014 Ig Nobel Prize in physics and the ~0.07 friction coefficient, Cavendish as a clone and Gros Michel, banana as a berry and the plant as a herb, it floats, it curves towards the light.

Below it, a myths block strikes out three claims that cannot be evidenced: hangover cure, sex drive, "nature's own energy boost".

Rules:

- Never add a fact that cannot be sourced.
- Never promote anything out of the myths block into the facts boxes.
- Health claims on food are regulated. Potassium and B6 may only be described in the authorised wording ("contributes to normal muscle function", "contributes to the reduction of tiredness and fatigue"). Everything else stays out.

This section is the one place where accuracy outranks tone. The whole talk rests on it.

## Translation notes

- **Bananrådet → The Banana Board.** Chosen to echo a British marketing board, which fits the setting better than a literal "Banana Council". The wordmark is set in Staatliches, so the longer name still fits the nav.
- **`hej@bananradet.se` → `hello@bananaboard.co.uk`**, to match.
- **"a tenner a kilo" → "about a pound a kilo."** If the page is ever localised for a non-UK market, revisit that line and the `.co.uk` address together.
- One joke could not survive translation: the Swedish "no tub with English writing on it" became "no tub with a bodybuilder on the label."
- The English page is a full copy of the Swedish one, not a shared template. Any copy change has to be made in both places. Note that only the English B-side was brought into this repo — `index-punk.html` and the Swedish B-side PDF stay outside it, so that second copy does not exist here to keep in sync.

## State

- English B-side site: done. Responsive, checked at 1440 px and 390 px.
- Not done: an English B-side design system PDF. Only the Swedish one exists (`Bananradet-designsystem-punk.pdf`).
- Not done: social assets for either B-side. The copy in `some-inlagg.md` was written for the A-side and would need rewriting from scratch — second person, no emoji, no hashtag stacks.
