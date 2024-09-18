Tässä on opiskeluohjeet ensimmäisen, toisen ja kolmannen asteen yhtälöiden ratkaisemiseen markdown-kielellä:

```markdown
# Yhtälöiden Ratkaiseminen

## 1. Ensimmäisen asteen yhtälöt

Ensimmäisen asteen yhtälöt ovat muotoa:
ax + b = 0
missä (a) ja (b) ovat vakioita, ja (x) on tuntematon.

### Ratkaisuvaiheet:
1. Siirrä vakio oikealle puolelle:
   ax = -b 
2. Jaa molemmat puolet kertoimella \(a\):
   x = \frac{-b}{a}

### Esimerkki:
Ratkaistaan yhtälö \(3x + 6 = 0\):
1. Vähennä 6 molemmilta puolilta:
   \[ 3x = -6 \]
2. Jaa molemmat puolet 3:lla:
   \[ x = -2 \]

---

## 2. Toisen asteen yhtälöt ja \(\Delta\)

Toisen asteen yhtälöitä ratkaistaan usein käyttämällä toisen asteen yhtälön ratkaisukaavaa:
\[ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \]

### Tapaus 1: \(\Delta > 0\)
Tämä tarkoittaa, että yhtälöllä on kaksi erilaista reaaliratkaisua.

#### Esimerkki: \(x^2 - 3x + 2 = 0\)
1. Lasketaan diskriminantti \(\Delta\):
   \[ \Delta = (-3)^2 - 4(1)(2) = 9 - 8 = 1 \]
2. Käytetään ratkaisukaavaa:
   \[ x = \frac{-(-3) \pm \sqrt{1}}{2(1)} = \frac{3 \pm 1}{2} \]
3. Ratkaisut:
   \[ x_1 = \frac{3 + 1}{2} = 2, \quad x_2 = \frac{3 - 1}{2} = 1 \]

### Tapaus 2: \(\Delta = 0\)
Tämä tarkoittaa, että yhtälöllä on yksi reaaliratkaisu.

#### Esimerkki: \(x^2 - 4x + 4 = 0\)
1. Lasketaan diskriminantti \(\Delta\):
   \[ \Delta = (-4)^2 - 4(1)(4) = 16 - 16 = 0 \]
2. Käytetään ratkaisukaavaa:
   \[ x = \frac{-(-4) \pm \sqrt{0}}{2(1)} = \frac{4}{2} = 2 \]

### Tapaus 3: \(\Delta < 0\)
Tämä tarkoittaa, että yhtälöllä on kaksi kompleksiratkaisua.

#### Esimerkki: \(x^2 + x + 1 = 0\)
1. Lasketaan diskriminantti \(\Delta\):
   \[ \Delta = 1^2 - 4(1)(1) = 1 - 4 = -3 \]
2. Käytetään ratkaisukaavaa:
   \[ x = \frac{-1 \pm \sqrt{-3}}{2(1)} = \frac{-1 \pm i\sqrt{3}}{2} \]
3. Ratkaisut:
   \[ x_1 = \frac{-1 + i\sqrt{3}}{2}, \quad x_2 = \frac{-1 - i\sqrt{3}}{2} \]

---

## 3. Kolmannen asteen yhtälöt

Kolmannen asteen yhtälön yleinen muoto on:
\[ ax^3 + bx^2 + cx + d = 0 \]

### Esimerkki: \(x^3 - 6x^2 + 11x - 6 = 0\)

#### Ratkaisuvaiheet:
1. **Etsi rationaalinen juuri** käyttämällä **Rationaalisten juurien testiä**: Ehdokkaat ovat kaikki luvut, jotka jakavat termin \(d = -6\). Tarkistetaan juurten arvoja \(x = 1\), \(x = 2\), jne.
   - Kun \(x = 1\):
     \[ 1^3 - 6(1)^2 + 11(1) - 6 = 1 - 6 + 11 - 6 = 0 \]
     Joten \(x = 1\) on juuri.
2. **Jaa polynomi** tekijällä \(x - 1\). Tämä voidaan tehdä joko pitkässä jakolaskussa tai synteettisessä jakolaskussa. Jaon tulos on:
   \[ x^3 - 6x^2 + 11x - 6 = (x - 1)(x^2 - 5x + 6) \]
3. Ratkaistaan jäljelle jäänyt toisen asteen yhtälö \(x^2 - 5x + 6 = 0\) käyttämällä toisen asteen ratkaisukaavaa:
   \[ x = \frac{-(-5) \pm \sqrt{(-5)^2 - 4(1)(6)}}{2(1)} = \frac{5 \pm \sqrt{25 - 24}}{2} = \frac{5 \pm 1}{2} \]
4. Ratkaisut:
   x_1 = \frac{5 + 1}{2} = 3, \quad x_2 = \frac{5 - 1}{2} = 2 

Joten yhtälöllä on kolme reaaliratkaisua:
x = 1, x = 2, x = 3

---

Nyt sinulla on esimerkit kaikista asteen yhtälöistä, ja ne kattavat erityyppisiä ratkaisuja eri tapauksissa!
```