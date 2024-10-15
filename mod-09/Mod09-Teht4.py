"""Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman
alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan
100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään
kutsumalla kiihdytä-metodia. Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla
kulje-metodia. Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan
kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna."""

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
        if muutos < 0:
            if self.nopeus + muutos < 0:
                self.nopeus = 0
            else:
                self.nopeus += muutos
        else:
            if self.nopeus + muutos > self.huippunopeus:
                self.nopeus = self.huippunopeus
            else:
                self.nopeus += muutos

    # Kulje-metodi (funktio)
    def kulje(self, tuntimaara):
        self.matka = self.nopeus * tuntimaara + self.matka
        return self.matka


# Luodaan auto-olio (object) ja tulostetaan auton ominaisuudet (properties)
auto = []
for i in range(10):
    huippunopeus = (random.randint(100, 200))
    auto.append(Auto(f"ABC-{i+1}", huippunopeus))
    # print(f"Rekisteritunnus: {auto[i].rekisteritunnus} \n"
    #       f"Huippunopeus: {auto[i].huippunopeus} km/h")

# Kilpailu
kilpailu = True
while kilpailu:
    for i in range(10):
        auto[i].kiihdyta(random.randint(-10, 15))
        auto[i].kulje(1)
        if auto[i].matka >= 10000:
            kilpailu = False
            break

# Tulostetaan kilpailun tulokset
print("\nKilpailun tulokset:")
print(f"{'Rek.tunnus':<10} | {'Huippunopeus':<14} | {'Nopeus':<10} | {'Matka':<10}")
for i in range(10):
    print(f"{auto[i].rekisteritunnus:<10} | {auto[i].huippunopeus} "
          f"{'km/h':<10} | {auto[i].nopeus} {'km/h':6} | {auto[i].matka} "
          f"km")
