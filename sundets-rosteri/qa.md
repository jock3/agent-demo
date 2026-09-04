# QA — leveransgrind

Ingen copy och ingen bild går till Gustav utan QA-rapport. Rapporten är
formatet som avgör om något är levererbart, inte en sammanfattning av arbetet.

## Vem kör vad

| Granskning | Körs av | Underlag |
|---|---|---|
| Faktapåståenden | `faktakoll` | `fakta.md` |
| Plattform, ton, förbjudna ord | `plattformskoll` | `plattformar.md`, `brand.md` |
| Bild | `bild-qa` | `bildmaner.md` |

De tre körs var för sig och rapporterar var för sig. Kör dem parallellt när
både copy och bild finns — de delar inget underlag och behöver inte varandras
resultat.

## Rapportens delar

```markdown
# QA — <kund> — <datum> — <plattform>

## Faktakoll
<tabellen från faktakoll oförändrad>

## Plattformskoll
<tabellen från plattformskoll oförändrad>

## Bild-QA
<tabellen från bild-qa, eller "Ingen bild i den här leveransen">

## Luckor
<varje [FAKTA SAKNAS] i copyn, med vad som behöver bekräftas och av vem>

## Utfall
Levererbar / Ej levererbar
```

Klistra in granskarnas tabeller som de kom. Skriv aldrig om dem till löptext
och plocka aldrig bort rader som blev godkända — rapporten ska gå att läsa som
en fullständig kontroll, inte som en lista över problem.

## Leveransregel

**Ej levererbar** om något av följande gäller:

- Ett stående påstående är underkänt av `faktakoll`
- En hård plattformsgräns är underkänd av `plattformskoll`
- En bild är underkänd av `bild-qa`

**Levererbar med lucka** om copyn innehåller `[FAKTA SAKNAS]` men allt annat är
godkänt. Luckan ska stå kvar i den levererade copyn — fyll den aldrig med en
gissning för att få igenom leveransen. Gustav bekräftar eller stryker.

**Levererbar** när allt är godkänt och inga luckor finns.

## Vid underkänt

Rätta och kör om granskningen. Argumentera inte mot en underkänd punkt i
rapporten — antingen ändras copyn, eller så ändras underlaget i `fakta.md`,
`plattformar.md` eller `brand.md` efter beslut från Gustav. En regel som visar
sig vara fel rättas i sin källfil, inte i det enskilda ärendet.
