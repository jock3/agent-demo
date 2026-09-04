"""Access to the Sundets Rosteri knowledge base.

Every path the model supplies is resolved and checked against KB_ROOT before
any file is opened, so a crafted filename cannot read outside the directory.
"""

from __future__ import annotations

from pathlib import Path

KB_ROOT = Path(__file__).resolve().parents[2] / "sundets-rosteri"

GUIDELINES = {
    "brand": "brand.md",
    "bildmaner": "bildmaner.md",
    "fakta": "fakta.md",
    "plattformar": "plattformar.md",
    "brief-mall": "brief-mall.md",
}


class KnowledgeError(Exception):
    """Raised when a requested document is missing or out of bounds."""


def _resolve(name: str) -> Path:
    """Resolve a knowledge-base filename, refusing anything outside KB_ROOT."""
    candidate = (KB_ROOT / name).resolve()
    if not candidate.is_relative_to(KB_ROOT):
        raise KnowledgeError(f"path escapes the knowledge base: {name}")
    if not candidate.is_file():
        raise KnowledgeError(f"no such document: {name}")
    return candidate


def read_guideline(doc: str) -> str:
    """Read one of the five guideline documents, by key or filename."""
    filename = GUIDELINES.get(doc, doc)
    if filename not in GUIDELINES.values():
        known = ", ".join(sorted(GUIDELINES))
        raise KnowledgeError(f"unknown guideline: {doc}. Known: {known}")
    return _resolve(filename).read_text(encoding="utf-8")


def list_posts() -> list[str]:
    """Filenames of the reference posts, oldest first."""
    return sorted(p.name for p in KB_ROOT.glob("20*.md"))


def read_post(name: str) -> str:
    """Read one reference post by filename."""
    if name not in list_posts():
        raise KnowledgeError(f"unknown post: {name}. Use list_posts first.")
    return _resolve(name).read_text(encoding="utf-8")


def check_facts(claim: str) -> str:
    """Search fakta.md for lines relevant to a claim.

    Naive term matching on purpose — the model does the judging, this only
    puts the relevant source lines in front of it. The rule from fakta.md is
    that anything not stated there may not be claimed.
    """
    text = read_guideline("fakta")
    terms = [t.strip(".,:;!?\"'()").lower() for t in claim.split()]
    terms = [t for t in terms if len(t) > 3]

    hits = [
        line.strip()
        for line in text.splitlines()
        if line.strip() and any(t in line.lower() for t in terms)
    ]
    if not hits:
        return (
            "No lines in fakta.md matched this claim. Per fakta.md, a claim "
            "with no support there may not be made — flag it and leave "
            "`[FAKTA SAKNAS]` in the copy."
        )
    return "Matching lines from fakta.md:\n" + "\n".join(f"- {h}" for h in hits)
