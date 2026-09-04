"""Tool definitions and dispatch for the agent loop."""

from __future__ import annotations

from . import knowledge

TOOLS = [
    {
        "name": "read_guideline",
        "description": (
            "Read one of the five guideline documents for Sundets Rosteri. "
            "Call this before writing any copy: brand.md for tone and "
            "positioning, plattformar.md for the hard per-platform limits "
            "(length, hashtags, emoji, CTA style), fakta.md for what may be "
            "claimed, bildmaner.md for image direction, brief-mall.md for the "
            "brief template that starts the chain. Documents are in Swedish."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "doc": {
                    "type": "string",
                    "enum": sorted(knowledge.GUIDELINES),
                    "description": "Which guideline document to read.",
                }
            },
            "required": ["doc"],
            "additionalProperties": False,
        },
    },
    {
        "name": "list_posts",
        "description": (
            "List the reference posts that have already been published, with "
            "their filenames. Call this when you want an example of how a "
            "given platform has been handled before, then read_post the one "
            "that matches."
        ),
        "input_schema": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "name": "read_post",
        "description": (
            "Read one published reference post by filename. Each post has "
            "front matter with platform, format, purpose, publication date, "
            "and the result it achieved, followed by the copy itself."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Filename as returned by list_posts.",
                }
            },
            "required": ["name"],
            "additionalProperties": False,
        },
    },
    {
        "name": "check_facts",
        "description": (
            "Check a factual claim against fakta.md, which is the only "
            "permitted source of facts about Sundets Rosteri. Call this for "
            "every number, certification, origin claim, and product detail "
            "before it goes into copy. Returns the matching source lines, or "
            "tells you the claim is unsupported."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "claim": {
                    "type": "string",
                    "description": "The claim to check, in Swedish.",
                }
            },
            "required": ["claim"],
            "additionalProperties": False,
        },
    },
]


def dispatch(name: str, tool_input: dict) -> str:
    """Run one tool call and return its result as text."""
    if name == "read_guideline":
        return knowledge.read_guideline(tool_input["doc"])
    if name == "list_posts":
        return "\n".join(knowledge.list_posts())
    if name == "read_post":
        return knowledge.read_post(tool_input["name"])
    if name == "check_facts":
        return knowledge.check_facts(tool_input["claim"])
    raise knowledge.KnowledgeError(f"unknown tool: {name}")
