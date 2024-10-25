"""Tehtävä on jatkoa autokilpailutehtävälle.
Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun
nimi, pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen,
kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo
kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia. tulosta_tilanne, joka tulostaa kaikkien
autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna. kilpailu_ohi, joka palauttaa True, jos jokin autoista
on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle annetaan
kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla
toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu
ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen
jälkeen, kun kilpailu on päättynyt."""

import random


# Auto-luokka (class)
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    # Kiihdytä-metodi (funktio)
    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus + muutos < 0:
            self.nopeus = 0
        if self.nopeus + muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus

    # Kuljee-metodi (funktio)
    def auto_kuljee(self, tuntimaara):
        self.matka = self.nopeus * tuntimaara + self.matka
        return self.matka


class Kilpailu:
    def __init__(self, nimi, pituus_km, auto_lista):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot_lista = auto_lista

    def tunti_kuluu(self):
        for k_auto in self.autot_lista:
            k_auto.kiihdyta(random.randint(-10, 15))
            # print(f"Auto {k_auto.rekisteritunnus} | Nopeus {k_auto.nopeus} km/h")
            k_auto.auto_kuljee(1)

    def tulosta_tilanne(self):
        print(f"{'Rek.tunnus':<10} | {'Huippunopeus':<14} | {'Nopeus':<10} | {'Matka':<10}")
        for k_auto in self.autot_lista:
            print(f"{k_auto.rekisteritunnus:<10} | {k_auto.huippunopeus} "
                  f"{'km/h':<10} | {k_auto.nopeus} {'km/h':6} | {k_auto.matka} "
                  f"km")

    def kilpailu_ohi(self):
        for k_auto in self.autot_lista:
            if k_auto.matka >= self.pituus_km:
                return True
        return False


# Pääohjelma
# Luodaan auto-olio (object) ja tulostetaan auton ominaisuudet (properties)
autot_lista = []
for i in range(10):
    maxnopeus = (random.randint(100, 200))
    autot_lista.append(Auto(f"ABC-{i + 1}", maxnopeus))

# Luodaan kilpailu-olio (object)
kilpailu = Kilpailu("Suuri romuralli", 8000, autot_lista)

# Kilpailu
kilpailu_ohi = False
tunti = 0
while not kilpailu_ohi:
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        print(f"Tilanne {tunti} tunnin jälkeen:")
        kilpailu.tulosta_tilanne()
        kilpailu_ohi = kilpailu.kilpailu_ohi()
    if kilpailu_ohi:
        print(f"Kilpailu on päättynyt {tunti} tunnin jälkeen.")
        print(f"Kilpailun tulokset:")
        kilpailu.tulosta_tilanne()
        break
