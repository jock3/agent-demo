# agent demo

Social-media copy for a fictional demo client, Sundets Rosteri — a micro coffee
roastery in Kalmar. Meant to be driven from Claude Code: open the repo and ask
for a post. `CLAUDE.md` carries the workflow, `sundets-rosteri/` carries the
source material. Nothing to install.

```
Skriv en Instagram-karusell om bryggkursen i kafét
LinkedIn-post om att vi tar över serviceavtalet på maskinparken
```

Output is in Swedish, because the knowledge base is.

## The workflow

`CLAUDE.md` sets the order of work: read the brand and platform rules for the
channel first, look at a comparable published post, and check every number,
price, certification, and origin claim against `fakta.md` before it reaches the
copy.

`fakta.md` is the only permitted source of facts. Anything not stated there may
not be claimed — the copy gets a `[FAKTA SAKNAS]` gap and a note on what needs
confirming, rather than a plausible invented number.

## sundets-rosteri/

Guidelines:

- `brand.md` — brand platform (tone, positioning, pronouns)
- `plattformar.md` — hard per-platform limits (length, hashtags, emoji, CTA)
- `fakta.md` — verified facts, permitted claims, forbidden claims
- `bildmaner.md` — image style, read before generation and by QA
- `brief-mall.md` — brief template that starts the chain

Reference posts, each with its published result in front matter:

- `2026-03-instagram-rostprotokoll.md`
- `2026-04-linkedin-driftstopp.md`
- `2026-04-tiktok-ines-svarar.md`
- `2026-05-facebook-bryggkurs.md`
- `2026-05-instagram-lansering.md`
