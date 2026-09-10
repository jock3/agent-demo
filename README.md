# agent demo

Social-media copy for a fictional demo client, Sundets Rosteri — a micro coffee
roastery in Kalmar. Driven from Claude Code: open the repo and ask for a post.
Nothing to install.

```
Skriv en Instagram-karusell om bryggkursen i kafét
LinkedIn-post om att vi tar över serviceavtalet på maskinparken
```

Output is in Swedish, because the knowledge base is.

## The chain

```
brief → copy → granskning → leverans → logg
```

`CLAUDE.md` drives it. The brief is filled from `brief-mall.md` one question at
a time and written to `output/`; copy is written against the brand and platform
rules; three review subagents check the result; a QA report decides whether it
ships; the post is logged.

The review agents are read-only and report in fixed formats — they never edit
the copy, so a pass is a claim you can check rather than a rewrite you have to
trust.

| Agent | Checks | Against |
| --- | --- | --- |
| `faktakoll` | Every standing claim | `fakta.md` |
| `plattformskoll` | Length, hashtags, emoji, pronouns, CTA, banned words | `plattformar.md`, `brand.md` |
| `bild-qa` | The generated image, point by point | `bildmaner.md` |

## The fact rule

`fakta.md` is the only permitted source of standing facts — service area,
prices, certifications, origin, capacity. Anything not stated there may not be
claimed, and the copy gets a `[FAKTA SAKNAS]` gap with a note on what needs
confirming rather than a plausible invented number. Per-event data (dates,
one-off quantities) comes from the brief and is exempt.

`qa.md` makes the gap survive delivery: copy ships *with* the gap in it. Filling
one to get past the gate is the failure the rule exists to prevent.

## Layout

```
CLAUDE.md              the workflow
publiceringslogg.md    what shipped, and the 70/20/10 mix
bilder/                approved photos, reusable across posts
.claude/agents/        the three review subagents
sundets-rosteri/       client knowledge base
output/                briefs and QA reports, per assignment
```

Knowledge base:

- `brand.md` — brand platform (tone, positioning, pronouns, banned words)
- `plattformar.md` — hard per-platform limits, cadence, content mix
- `fakta.md` — verified facts, permitted claims, forbidden claims
- `bildmaner.md` — image direction, Higgsfield templates, QA checklist
- `brief-mall.md` — brief template that opens the chain
- `qa.md` — QA report format and the delivery gate
- `20*.md` — five published reference posts, each with its result

## Images

`bilder/index.md` is a library of photos that have already passed `bild-qa`.
The chain checks it before generating anything: reusing an approved shot is
cheaper than a new one and lands the manér more reliably. Shooting comes
second, generating last — `bildmaner.md` wants images that look like someone
was there.

Text and logos are never in the image files. They go on afterwards in layout,
which is a hard point on the QA checklist.

## Bananrådet

`docs/` holds a second, unrelated demo: **Bananrådet**, a fictional banana
industry campaign — graphic profile, design system and a one-page site, all in
Swedish. It is deliberately generic: it shows what an AI default looks like
when nobody steers it. `docs/CLAUDE.md` states the one rule that matters —
do not improve the design.

Published with GitHub Pages straight from `docs/` on `main`, no build step:
https://jock3.github.io/agent-demo/
