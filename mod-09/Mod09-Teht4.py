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

    # Kiihdytä-metodi
    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus + muutos < 0:
            self.nopeus = 0
        if self.nopeus + muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus

    # Kuljee-metodi
    def auto_kuljee(self, tuntimaara):
        self.matka += self.nopeus * tuntimaara
        return self.matka


# Pääohjelma
def luo_kilpailu_autot():
    autot = []
    for i in range(10):
        maxnopeus = (random.randint(100, 200))
        autot.append(Auto(f"ABC-{i + 1}", maxnopeus))
        print(f"Auto: {autot[i].rekisteritunnus} | Huippunopeus {autot[i].huippunopeus} km/h")
    return autot


def kilpailu():
    autot = luo_kilpailu_autot()
    kilpailu_kaynissa = True

    while kilpailu_kaynissa:
        for auto in autot:  # 10 kierrosta
            auto.kiihdyta(random.randint(-10, 15))
            auto.auto_kuljee(1)
            if auto.matka >= 10000:
                print(f"Voittaja: {auto.rekisteritunnus} ja se on kulkenut {auto.matka} km.")
                kilpailu_kaynissa = False
                break
    return autot


def tulosta_kilpailu_tulokset():
    autot = kilpailu()
    print("Kilpailun tulokset:")
    print("Rek-tunnus | Huippunopeus | Nopeus | Matka")
    for auto in autot:
        print(f"{auto.rekisteritunnus:<10} | {auto.huippunopeus:<12} | {auto.nopeus:<6} | {auto.matka}")


tulosta_kilpailu_tulokset()
