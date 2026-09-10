"""Bygger Bananradet-hemsida.html: index.html med alla bilder från bilder/ inbäddade som base64."""
import base64, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
html = (ROOT / "index.html").read_text(encoding="utf-8")

def embed(m):
    data = base64.b64encode((ROOT / "bilder" / m.group(1)).read_bytes()).decode()
    return f"url('data:image/jpeg;base64,{data}')"

out = re.sub(r"url\('bilder/([^']+)'\)", embed, html)
(ROOT / "Bananradet-hemsida.html").write_text(out, encoding="utf-8")
print("Klar: Bananradet-hemsida.html")
