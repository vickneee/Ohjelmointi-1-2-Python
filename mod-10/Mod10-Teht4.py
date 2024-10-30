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

    # Kiihdytä-metodi
    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus + muutos < 0:
            self.nopeus = 0
        if self.nopeus + muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus

    # Kuljee-metodi
    def auto_kuljee(self, tuntimaara):
        self.matka = self.nopeus * tuntimaara + self.matka
        return self.matka


class Kilpailu:
    def __init__(self, nimi, pituus_km, autojen_lkm):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autojen_lkm = autojen_lkm
        self.kilpailu_autot = []
        self.luo_kilpailu_autot()

    def luo_kilpailu_autot(self):
        for k_auto in range(self.autojen_lkm):
            max_nopeus = (random.randint(100, 200))
            self.kilpailu_autot.append(Auto(f"ABC-{k_auto + 1}", max_nopeus))
            print(f"Auto: {self.kilpailu_autot[k_auto].rekisteritunnus} | Huippunopeus "
                  f"{self.kilpailu_autot[k_auto].huippunopeus} "
                  f"km/h")

    def tunti_kuluu(self):
        for k_auto in self.kilpailu_autot:
            k_auto.kiihdyta(random.randint(-10, 15))
            # print(f"Auto {k_auto.rekisteritunnus} | Nopeus {k_auto.nopeus} km/h")
            k_auto.auto_kuljee(1)

    def tulosta_tilanne(self):
        print(f"{'Rek.tunnus':<10} | {'Huippunopeus':<14} | {'Nopeus':<10} | {'Matka':<10}")
        for k_auto in self.kilpailu_autot:
            print(f"{k_auto.rekisteritunnus:<10} | {k_auto.huippunopeus} "
                  f"{'km/h':<10} | {k_auto.nopeus} {'km/h':6} | {k_auto.matka} "
                  f"km")

    def kilpailu_ohi(self):
        kilpailu_ohi = False
        tunti = 0
        while not kilpailu_ohi:
            kilpailu.tunti_kuluu()
            tunti += 1
            if tunti % 10 == 0:
                print(f"Tilanne {tunti} tunnin jälkeen:")
                self.tulosta_tilanne()
            for k_auto in self.kilpailu_autot:
                if k_auto.matka >= self.pituus_km:
                    kilpailu_ohi = True
                    break
        print(f"Kilpailu on päättynyt {tunti} tunnin jälkeen.")
        print(f"Kilpailun tulokset:")
        self.tulosta_tilanne()
        return True


# Pääohjelma
# Luodaan kilpailu-olio (object)
kilpailu = Kilpailu("Suuri romuralli", 8000, 10)

# Aloitetaan kilpailu ja tarkistetaan, onko kilpailu ohi
kilpailu.kilpailu_ohi()
