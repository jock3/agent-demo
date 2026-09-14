"""Fotokopierar bilderna i bilder/ till bilder/punk/ (1-bit, grovt korn).

Hård kontrast, nedskalning till 55 % före dithering och uppskalning med NEAREST
ger fotokopiekornet. Kör om efter att nya bilder lagts i bilder/.
"""
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance

ROOT = Path(__file__).resolve().parent.parent
SRC, DST = ROOT / "bilder", ROOT / "bilder" / "punk"
DST.mkdir(exist_ok=True)

JOBB = [("hero.jpg","hero-x.png",2.6), ("plantage.jpg","plantage-x.png",2.2),
        ("avatar-1.jpg","p1-x.png",2.8), ("avatar-2.jpg","p2-x.png",2.8),
        ("avatar-3.jpg","p3-x.png",2.8), ("person-bred.jpg","bred-x.png",2.4),
        ("recept-bananbrod.jpg","brod-x.png",2.3), ("og-bild.jpg","klase-x.png",2.6)]

def xerox(src, dst, kontrast=2.4, bredd=1100, ner=0.55):
    im = ImageOps.autocontrast(Image.open(SRC / src).convert("L"), cutoff=2)
    im = ImageEnhance.Contrast(im).enhance(kontrast)
    h = int(im.height * bredd / im.width)
    im = im.resize((bredd, h), Image.LANCZOS)
    bw = im.resize((int(bredd*ner), int(h*ner)), Image.LANCZOS).convert("1")
    bw.resize((bredd, h), Image.NEAREST).convert("L").save(DST / dst, optimize=True)
    print(dst)

for s, d, k in JOBB:
    if (SRC / s).exists():
        xerox(s, d, k)
