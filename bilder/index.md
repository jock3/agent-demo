# Bildbibliotek — Sundets Rosteri

Godkända bilder att återanvända. Kolla här **innan** du genererar eller ber om
en ny fotografering — en bild som redan klarat `bild-qa` är billigare och
träffar manéret säkrare än en ny generering.

`Kategori` följer motivkategorierna i `bildmaner.md`: **1** rosteriet i arbete,
**2** produkt i sammanhang, **3** kafét och gäster.

`QA` är datum då bilden klarade checklistan i `bildmaner.md`. En bild utan
datum är inte godkänd och får inte användas.

| Fil | Kategori | Motiv | Format | QA | Använd i | Samtycke |
|---|---|---|---|---|---|---|
| _tomt — lägg till första bilden här_ | | | | | | |

## Regler för återanvändning

- **Kolla `Använd i` först.** Samma bild går inte ut två gånger på samma kanal
  inom åtta veckor. På olika kanaler går det bra direkt.
- **Fyll i `Använd i`** med datum och plattform vid varje användning, samma
  gång som raden läggs till i `publiceringslogg.md`.
- **Beskär, generera inte om.** Behövs 9:16 av en 4:5-bild: beskär originalet.
  Ett nytt bildförhållande kräver ny `bild-qa` — beskärningen kan flytta
  motivet ut ur sin kategori eller klippa en hand.
- **Ingen text eller logotyp i filen.** Biblioteket innehåller rena bilder.
  Grafik läggs på i layoutsteget, enligt `bildmaner.md`.

## Filer

Lägg bilderna i den här katalogen. Namnge dem
`<kategori>-<motiv>-<löpnummer>.jpg`, till exempel `1-trumman-01.jpg`.

**Storlek:** långsida max 2000 px, JPEG kvalitet 80, under 500 kB per fil.
Repot är textbaserat och ska gå att klona snabbt. Originalen hör hemma
någon annanstans — det här är webbupplösning för publicering, inte ett arkiv.
Behövs råfiler i versionshantering är Git LFS rätt verktyg, inte det här.

## Samtycke

Syns en identifierbar person ska `Samtycke` fyllas i: **ja** med datum, eller
**personal** för anställda som samtyckt generellt. Tom ruta betyder att bilden
inte får publiceras, oavsett hur bra den är. Gäster i kafét fotas enligt
`bildmaner.md` snett bakifrån eller i profil — men igenkännbar är igenkännbar,
och då krävs samtycke ändå.
