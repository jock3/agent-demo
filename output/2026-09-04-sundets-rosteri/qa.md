# QA — Sundets Rosteri — 2026-09-04 — Instagram

Granskningarna kördes inline i huvudloopen, inte som subagenter. Subagenterna
i `.claude/agents/` registreras vid sessionsstart och fanns inte när den här
sessionen började. Kriterierna är desamma; körsättet är det inte.

## Faktakoll

Efter rättning av två underkända påståenden i första passet.

| Påstående | Typ | Bedömning | Källa |
|---|---|---|---|
| 34 företag i Kalmar län och Blekinge | stående | godkänd | fakta.md:11 |
| varenda ett inom nittio minuters bilväg | stående | godkänd | fakta.md:12 |
| utryckning ingår i abonnemanget | stående | godkänd | fakta.md:12–13 |
| sex personer, två rostar | stående | godkänd | fakta.md:9 |
| trumman tar tolv kilo | stående | godkänd | fakta.md:10 |
| "hela tillväxtplanen" | positionering | ej påstående | — |

Rättat i pass 1 → 2:

- *"åker någon av oss ut"* framställdes som villkorslöst. `fakta.md` säger att
  utryckning ingår i abonnemang. Villkoret tillagt.
- *"vi blir aldrig billigast"* — prisjämförande påstående utan underlag i
  `fakta.md`. Struket. Baksidan står kvar utan marknadspåståendet.

## Plattformskoll

| Kontrollpunkt | Uppmätt | Bedömning |
|---|---|---|
| Captionlängd | 113 ord | godkänd (80–150) |
| Hook före brytpunkt | 42 tecken | godkänd (max 45) |
| Antal hashtags | 7 | godkänd (6–10) |
| Hashtags i första kommentaren | ja | godkänd |
| Emoji | 0 | godkänd (max 2) |
| Pronomen | du, B2C | godkänd |
| CTA | fråga, ingen köpuppmaning | godkänd |
| Förbjudna ord ur brand.md | 0 träffar | godkänd |
| Smaknoter | 0 | godkänd (max 2) |
| Captionen upprepar inte bilden | ja | godkänd |

## Bild-QA

Ingen bild i den här leveransen. Prompt och format levererade i stället, se
`copy.md`.

## Luckor

Inga `[FAKTA SAKNAS]`.

## Utfall

**Levererbar.** Bilden är utestående och kräver krediter eller egen fotografering.
