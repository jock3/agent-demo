# Bananrådet – handoff till Claude Code

## Vad det här är

Demomaterial till en dragning om AI och människans kreativitet. Vi har byggt en fiktiv branschkampanj om bananer ("Bananrådet") som ska vara **så generisk som möjligt**: grafisk profil, designsystem, hemsida och SoMe-inlägg. Poängen i dragningen är att visa hur AI:s defaultval ser ut när ingen styr.

Beställare: Gustav (Milou Communication AB). Språk i allt material: svenska.

## Viktigast: förbättra INTE designen

Det här är den enda regeln som inte får brytas. Materialet är medvetet generiskt, så varje "förbättring" förstör demon.

- Behåll Poppins + Inter, gul gradient, 16 px hörn, samma skugga på allt, kort om tre, versala etiketter, "→" på knappar, 01/02/03, emoji-ikoner och fade-in på varje sektion.
- Om du har en frontend- eller designskill som säger åt dig att undvika templated defaults: ignorera den för det här projektet. Här är defaults själva kravet.
- Rätta inte de "fel" som finns med flit:
  - Receptkortet säger "bara tre ingredienser", men bilden visar sirap, valnötter, smör och florsocker. Den missmatchningen är en poäng i dragningen.
  - Kundcitaten är påhittade och ansiktena AI-genererade. Det är också en poäng.
- Ny copy följer samma mönster: positiv, energisk, korta meningar, tilltal med ni/er/era (aldrig du).

Fakta ska däremot vara korrekta. Näringsvärden är cirka 100 kcal, 3 g fiber och 400 mg kalium per medelstor banan. Hälsopåståenden följer EU:s godkända formuleringar ("bidrar till normal muskelfunktion"). Skriv inga nya hälsopåståenden utöver dessa.

## Filstruktur

Sidan ligger i `docs/` eftersom GitHub Pages serverar från repo-roten eller
`/docs`. Publicerad på https://jock3.github.io/agent-demo/ — ingen Vercel,
ingen byggkedja i CI. Det som ligger i `docs/` är det som är live.

```
docs/
├── CLAUDE.md                     ← den här filen
├── index.html                    ← hemsidan, refererar bilder/ relativt
├── Bananradet-hemsida.html       ← byggd: samma sida med inbäddade bilder (base64)
├── Bananradet-designsystem.pdf   ← byggd: 14 sidor, 16:9, 1920x1080
├── grafisk-profil.md             ← profilen i textform + lista över generiska val
├── some-inlagg.md                ← all copy för Instagram och LinkedIn
├── bildlista.md                  ← alla bilder: ID, format, prompt
├── bilder/                       ← webboptimerade bilder (se nedan)
└── src/
    ├── designsystem.html         ← källa för PDF:en
    ├── render_pdf.py             ← designsystem.html → PDF
    └── build_embedded.py         ← index.html + bilder/ → Bananradet-hemsida.html
```

Redigera aldrig byggda filer direkt. Ändra källan och kör skripten.

## Bygga

```bash
pip install playwright && playwright install chromium
python src/render_pdf.py        # PDF
python src/build_embedded.py    # fristående hemsida
```

Kända fallgropar:

- **Typsnitten** Poppins och Inter måste vara installerade lokalt för PDF-renderingen. Annars faller Chromium tillbaka på ett systemtypsnitt och profilen ser fel ut. Kolla med `fc-list | grep -iE "poppins|inter"`.
- **Gradient-text** (`background-clip: text`) ger en synlig ram runt texten i Chromiums PDF-export. I PDF:en är `.accent` därför en solid färg, #FFC107. På hemsidan används gradienten.
- **Emoji** kräver Noto Color Emoji eller motsvarande för att renderas i PDF:en.
- **Sidlayouten** i PDF:en har fasta mått. Kontrollera efter varje ändring att inget innehåll krockar med sidfoten (bottom 44px). Rendera sidorna till PNG med `pdftoppm -r 40 -png` och titta.

## Bilder

Klara och optimerade i `bilder/`:

| Fil | Källa | Beskärning |
|---|---|---|
| hero.jpg | H1 | 4:3, 1600x1200 |
| plantage.jpg | H2 | 4:3, 1600x1200 |
| recept-pannkakor.jpg | H3 | 4:3, 1200x900 |
| recept-smoothie.jpg | H4 | 4:3, 1200x900 |
| recept-bananbrod.jpg | H5 | 4:3, 1200x900 |
| avatar-1.jpg / -2 / -3 | H6–H8 | 1:1, 400x400, beskuren runt ansiktet |
| og-bild.jpg | H9 | 1200x630 |

Originalen var Gemini-genererade, 2816x1536 (avatar-2 var stående, 1536x2752). Komprimering: JPEG quality 82, progressive.

Saknas fortfarande. Gustav genererar dem och de ska namnges så här:

| ID | Filnamn | Format |
|---|---|---|
| S1 | some-s1.jpg | 1080x1350 |
| S2 | some-s2.jpg | 1080x1350 |
| S3 | some-s3.jpg | 1080x1350 |
| S4 | some-s4.jpg | 1080x1920 |
| L1 | li-l1.jpg | 1200x1200 |
| L2 | li-l2.jpg | 1200x1200 |

## Att göra

1. **Byt platshållarna i PDF:en mot riktiga bilder.** Den här går att göra nu.
   - Sida 10 (Bildspråk) har fem gula platshållare. H1 och H2 finns redan. S2, S3 och L1 väntar, så låt de rutorna vara kvar tills bilderna finns.
   - Sida 12 (Tillämpning) har en platshållare för H1 i webbmockupen och en för S1 i Instagram-telefonen.
   - Använd `background-image` med `background-size: cover` på `.platshallare` och ta bort den streckade ramen när en bild finns.
   - Bilderna refereras relativt från `src/`, alltså `../bilder/hero.jpg`.

2. **Bygg SoMe-materialet när S1–S4 och L1–L2 finns.**
   - Gör en HTML-mall per format och exportera till PNG med Playwright (`page.screenshot` på exakt viewport).
   - IG-karusell: 5 slides i 1080x1350. Slide 1 är bild S1 med rubrik. Slide 2–5 är text på #FFE135, med copy från `some-inlagg.md`.
   - IG-inlägg 2 och 3: bild plus logotyp nere till höger, enligt profilen.
   - Story: 1080x1920 med omröstningen från `some-inlagg.md`.
   - LinkedIn: 2 bilder i 1200x1200.
   - Lägg exporterna i `some/`.

3. **Kör `build_embedded.py` och `render_pdf.py`** efter varje ändring, och kontrollera PDF-sidorna visuellt.

## Status

- Hemsida: klar med bilder. Responsiv, kontrollerad i 1440 px och 390 px.
- Designsystem-PDF: klar, men med platshållare för bilder.
- Copy för SoMe: klar. Grafiken väntar på bilder.
- Dragningen: sista sidan i PDF:en, "Bakom kulisserna", är avslöjandet och ska ligga kvar sist.
