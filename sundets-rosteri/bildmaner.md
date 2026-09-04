# Bildmanér — Sundets Rosteri

Läses av bildagenten före generering och av QA-agenten efter.

## Grundprincip

Bilderna ska se ut som att någon var där, inte som att någon riggade det.
Arbetsmiljö framför produktuppställning.

## Ljus och färg

- Naturligt sidoljus, gärna fönsterljus. Aldrig hårt frontblixt.
- Matt kontrast, lyft svärtan lätt. Ingen crushed black.
- Kall grundton med varm accent — grå-blått rum, varmt ljus i motivet.
- Lätt kornighet accepterad och önskad. Ren digital skärpa ser stelt ut.

## Motivkategorier

**1. Rosteriet i arbete** (60% av bildbehovet)
Händer, maskiner, säckar, temperaturloggar. Ines vid rostmaskinen.
Rörelseoskärpa är okej.

**2. Produkt i sammanhang** (25%)
Påsen på ett köksbord med annat på bordet. Aldrig produkt på vit bakgrund.

**3. Kafét och gäster** (15%)
Halvfulla lokaler, sett snett bakifrån eller i profil. Aldrig poserande.

## Absolut inte

- Flat lay med kaffebönor utspridda i hjärtform
- Latte art fotad rakt uppifrån
- Jutesäck med bönor på rustik träyta
- Leende personer som tittar in i kameran med kaffekopp
- Solnedgång över hav med kaffekopp i förgrunden
- Text renderad i bilden (läggs på i efterhand, alltid)

## Higgsfield — promptmallar

**Mall A, rosteriet:**
```
documentary photograph, hands of a roaster adjusting a drum roaster dial,
industrial workshop interior, large window side light from left, muted cool
grey-blue walls, warm tungsten glow on the machine, visible film grain,
shallow depth of field, 35mm, natural unposed moment, no text
```

**Mall B, produkt i sammanhang:**
```
still life photograph, matte paper coffee bag on a worn kitchen table beside
a used ceramic cup and a folded newspaper, morning window light, cool grey
tones with warm sand accents, slight grain, 50mm, shot from a seated eye
level angle, lived-in not styled, no text, no logo
```

**Mall C, kafét:**
```
candid interior photograph, half-full neighbourhood cafe, people seen from
behind and in profile, soft overcast daylight through large windows, muted
palette, motion blur on one figure, 35mm documentary style, no eye contact
with camera, no text
```

Lägg alltid till: `no text, no watermark, no logo`
Format: 4:5 för Instagram-feed, 9:16 för Reels/TikTok/Stories, 1.91:1 för LinkedIn.

## QA-checklista för bild

Hårda kriterier. Agenten svarar godkänd/underkänd per punkt, inte i fritext.

- [ ] Rätt bildförhållande för plattformen
- [ ] Ingen renderad text eller pseudotext i bilden
- [ ] Ingen felaktig hand- eller fingeranatomi i förgrunden
- [ ] Färgtemperaturen matchar palett (kall grund, varm accent)
- [ ] Motivet faller inom en av de tre motivkategorierna
- [ ] Inget motiv från listan "Absolut inte"
- [ ] Om produkt syns: förpackningen har ingen påhittad text

Bedöm inte om bilden är "bra". Det avgör Gustav.
