# agent demo

A tool-use agent that writes social-media copy for a fictional demo client,
Sundets Rosteri — a micro coffee roastery in Kalmar. The agent reads the
client's brand, platform, and fact guidelines before writing, and checks every
factual claim against the one document allowed to contain facts.

## Run it

```sh
uv sync
cp .env.example .env        # then add your ANTHROPIC_API_KEY
uv run agent-demo "Instagram-karusell om bryggkursen i kafét"
uv run agent-demo -v "LinkedIn-post om driftsäkerhet"   # -v prints tool calls
```

Output is in Swedish, because the knowledge base is.

## How it works

`src/agent/main.py` runs the agentic loop by hand rather than using the SDK's
tool runner, so the mechanics are visible: send the conversation, check
`stop_reason`, run whatever tools the model asked for, append the results as
`tool_result` blocks, send again. It stops when the model stops asking for
tools.

Four tools, all reading from `sundets-rosteri/`:

| Tool | What it does |
| --- | --- |
| `read_guideline` | Read one of the five guideline documents |
| `list_posts` | List the published reference posts |
| `read_post` | Read one reference post, with its published result |
| `check_facts` | Look up a claim in `fakta.md` and return the matching lines |

`check_facts` is the interesting one. `fakta.md` states that nothing outside it
may be claimed, so the tool returns either the supporting lines or an explicit
"unsupported" answer — which the system prompt turns into a `[FAKTA SAKNAS]`
gap in the copy rather than an invented number.

Filenames coming from the model are resolved and bounds-checked against the
knowledge-base directory before any file is opened.

## sundets-rosteri/

Knowledge base for the demo client. Written in Swedish.

Guidelines read by the agent:

- `brand.md` — brand platform (tone, positioning, pronouns)
- `bildmaner.md` — image style, read before generation and by QA
- `fakta.md` — verified facts; nothing outside this may be claimed
- `plattformar.md` — hard per-platform limits
- `brief-mall.md` — brief template that starts the chain

Reference posts with published results:

- `2026-03-instagram-rostprotokoll.md`
- `2026-04-linkedin-driftstopp.md`
- `2026-04-tiktok-ines-svarar.md`
- `2026-05-facebook-bryggkurs.md`
- `2026-05-instagram-lansering.md`
