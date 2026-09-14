"""Bygger BananaBoard-site-punk-en.html: index-punk-en.html med bilder inbäddade som base64."""
import base64, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
html = (ROOT / "human.html").read_text(encoding="utf-8")

def embed(m):
    p = ROOT / m.group(1)
    mime = "png" if p.suffix == ".png" else "jpeg"
    return f"url('data:image/{mime};base64,{base64.b64encode(p.read_bytes()).decode()}')"

out = re.sub(r"url\('(bilder/[^']+)'\)", embed, html)
(ROOT / "BananaBoard-site-punk-en.html").write_text(out, encoding="utf-8")
print("Klar: BananaBoard-site-punk-en.html")
