"""A social-media agent for Sundets Rosteri, as a plain tool-use loop.

The loop is written out rather than delegated to the SDK's tool runner so the
mechanics stay visible: send the conversation, check stop_reason, run whatever
tools the model asked for, append the results, send again.
"""

from __future__ import annotations

import argparse
import sys

import anthropic
from dotenv import load_dotenv

from . import tools
from .knowledge import KnowledgeError

MODEL = "claude-opus-5"
MAX_TOKENS = 32000
MAX_TURNS = 20

SYSTEM = """\
Du är copyagenten för Sundets Rosteri, ett mikrorosteri i Kalmar. Du skriver \
färdig copy för sociala medier på svenska.

Arbetsordning:
1. Läs brand.md för ton och plattformar.md för den kanal uppgiften gäller. \
Plattformsreglerna är hårda gränser, inte rekommendationer.
2. Titta på en tidigare post för samma kanal när det hjälper.
3. Kontrollera varje siffra, certifiering och ursprungspåstående med \
check_facts innan det hamnar i copyn.

Påstå aldrig något som inte står i fakta.md. Saknas underlag: lämna \
`[FAKTA SAKNAS]` i copyn och skriv vad som behöver bekräftas.

Leverera copyn först, därefter en kort not om vilka regler och fakta du \
stämt av mot.
"""


def run(client: anthropic.Anthropic, prompt: str, verbose: bool) -> None:
    messages: list[dict] = [{"role": "user", "content": prompt}]

    for _ in range(MAX_TURNS):
        with client.messages.stream(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM,
            output_config={"effort": "high"},
            tools=tools.TOOLS,
            messages=messages,
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)
            response = stream.get_final_message()
        print()

        if response.stop_reason == "refusal":
            print("\n[model declined this request]", file=sys.stderr)
            return

        if response.stop_reason != "tool_use":
            return

        messages.append({"role": "assistant", "content": response.content})

        results = []
        for block in response.content:
            if block.type != "tool_use":
                continue
            if verbose:
                print(f"\n[tool] {block.name} {block.input}", file=sys.stderr)
            try:
                result = tools.dispatch(block.name, block.input)
                is_error = False
            except KnowledgeError as exc:
                result, is_error = str(exc), True
            results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
                    "is_error": is_error,
                }
            )

        messages.append({"role": "user", "content": results})

    print(f"\n[stopped after {MAX_TURNS} turns]", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write social copy for Sundets Rosteri."
    )
    parser.add_argument(
        "prompt",
        nargs="*",
        help="The brief, e.g. 'Instagram-karusell om bryggkursen'.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print each tool call to stderr.",
    )
    args = parser.parse_args()

    load_dotenv()
    prompt = " ".join(args.prompt) or input("Brief: ")
    if not prompt.strip():
        parser.error("no brief given")

    run(anthropic.Anthropic(), prompt, args.verbose)


if __name__ == "__main__":
    main()
