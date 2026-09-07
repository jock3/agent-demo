# QA — Sundets Rosteri — 2026-09-07 — Instagram (lansering/presentation)

## Faktakoll

Omkörning efter rättning. Föregående runda underkände två punkter
("många batcher i veckan" utan stöd, "restauranger och kontor" som
kundtyp utan stöd) — båda rättade innan denna omkörning.

| Påstående | Typ | Bedömning | Källa |
|---|---|---|---|
| "Sex personer. Ett rosteri på Ängö." | stående | godkänd | "Sex anställda, varav två rostar" / "Rosteri på Ängögatan, Ängö, Kalmar" |
| "Ines Halvorsen och Petter Ljung startade Sundets Rosteri 2019" | stående | godkänd | "Grundat 2019 av Ines Halvorsen och Petter Ljung" |
| "i en lokal på Ängögatan i Kalmar" | stående | godkänd | "Rosteri på Ängögatan, Ängö, Kalmar" |
| "Sedan 2021 ligger kaféet i samma hus" | stående | godkänd | "Kafé i samma lokal sedan 2021" |
| "Vi är sex anställda, två av oss rostar." | stående | godkänd | "Sex anställda, varav två rostar" |
| "Trumman tar 12 kg per gång." | stående | godkänd | "Rostkapacitet 12 kg per batch" |
| "Kaffet säljer vi i kaféet, via webbshop och till 34 företagskunder i Kalmar län och Blekinge." | stående | godkänd | "Levererar till 34 företagskunder i Kalmar län och Blekinge" / "Webbshop skickar inom 24 timmar på vardagar" |

Alla påståenden har stöd i fakta.md.

## Plattformskoll

Omkörning efter samma rättning.

| Kontrollpunkt | Uppmätt | Bedömning |
|---|---|---|
| Längd inom kanalens intervall (80–150 ord) | 86 ord | Godkänd |
| Antal hashtags inom intervallet (6–10) | 7 st | Godkänd |
| Hashtags på rätt plats för kanalen | Första kommentaren | Godkänd |
| Emoji: antal och placering | 0 st | Godkänd |
| Pronomen rätt för kanalen (du i B2C) | "du" används | Godkänd |
| CTA i rätt form (mjuk, fråga/länk i bio) | Fråga + "Länk i bio" | Godkänd |
| Inga förbjudna ord ur brand.md | 0 träffar | Godkänd |
| Max två smaknoter, verifierade | 0 smaknoter | Godkänd |
| Ingen romantisering av odlarled utan ursprungsinfo | Ej förekommande | Godkänd |
| Instagram: hook max 45 tecken före brytpunkt | 34 tecken | Godkänd |
| Instagram: Captionen upprepar inte bilden | Ingen bildbeskrivning i text | Godkänd |
| Instagram: Mjuk CTA, aldrig "köp nu" | "Länk i bio" | Godkänd |

Copyn håller sig innanför kanalens gränser.

## Bild-QA

### Bild 1: `1-rosteriet-vid-rosten-01.jpg` (kategori 1 — rosteriet i arbete)

| Punkt | Bedömning | Iakttagelse |
|---|---|---|
| Rätt bildförhållande (4:5 feed) | Godkänd | |
| Ingen renderad text eller pseudotext | Underkänd | Otydlig pseudotext på affischer/lappar och kalenderliknande blad på väggen, övre vänstra hörnet |
| Ingen felaktig hand- eller fingeranatomi i förgrunden | Godkänd | |
| Färgtemperatur matchar palett (kall grund, varm accent) | Godkänd | |
| Motivet inom en av tre motivkategorier | Godkänd | |
| Inget motiv från "Absolut inte" | Godkänd | |
| Produktförpackning utan påhittad text | Godkänd | |
| Ingen logotyp över ansikte eller kaffeyta | Godkänd | |

**Underkänd — 1 punkt**

### Bild 2: `3-kafe-halvfullt-rum-01.jpg` (kategori 3 — kafét och gäster)

| Punkt | Bedömning | Iakttagelse |
|---|---|---|
| Rätt bildförhållande (4:5 feed) | Godkänd | |
| Ingen renderad text eller pseudotext | Godkänd | |
| Ingen felaktig hand- eller fingeranatomi i förgrunden | Godkänd | |
| Färgtemperatur matchar palett (kall grund, varm accent) | Underkänd | Hela rummet har varm/sepiaton — väggar, tak och golv är brunt/gulaktigt, ingen kall grå-blå grundton syns |
| Motivet inom en av tre motivkategorier | Godkänd | |
| Inget motiv från "Absolut inte" | Godkänd | |
| Produktförpackning utan påhittad text | Godkänd | |
| Ingen logotyp över ansikte eller kaffeyta | Godkänd | |

**Underkänd — 1 punkt**

Ingen av bilderna klarar alla punkter — inget förslag till `bilder/index.md`
lämnas för någon av dem. Copyagenten har verifierat granskarens iakttagelser
mot bilderna direkt och håller med på båda punkterna.

## Luckor

Inga `[FAKTA SAKNAS]` i copyn.

## Avvikelse — bild levererad trots underkänt

Enligt leveransregeln i `qa.md` är ärendet **ej levererbart** när en bild är
underkänd av `bild-qa`. Gustav har uttryckligen bett att posten levereras
ändå, med bilderna som de är, märkt som en avsiktlig avvikelse för den här
demon — inte en tyst nedgradering av kravet. Reglerna i `bildmaner.md`
ändras inte av detta enskilda beslut.

## Utfall

**Levererbar — med avvikelse godkänd av Gustav.** Copy: alla punkter
godkända. Bild: två underkända punkter, levererade på uttrycklig begäran.
Bilderna förs inte in i `bilder/index.md` eftersom de inte klarade
checklistan.
