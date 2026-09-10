"""Renderar src/designsystem.html till Bananradet-designsystem.pdf (1920x1080 per sida)."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "designsystem.html"
OUT = ROOT / "Bananradet-designsystem.pdf"

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1920, "height": 1080})
    pg.goto(SRC.as_uri())
    pg.wait_for_timeout(800)
    pg.pdf(path=str(OUT), width="1920px", height="1080px", print_background=True)
    b.close()
print(f"Klar: {OUT}")
