"""Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on
ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden
ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman
kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden
polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan
kolmen tunnin verran ja tulosta autojen matkamittarilukemat."""

import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

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

    def kuljee(self, tuntimaara):
        self.matka = self.nopeus * tuntimaara + self.matka
        return self.matka


class SahkoAuto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)
        pass


class PolttoMoottoriAuto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(rekisteritunnus, huippunopeus)
        pass


# sähköauton (ABC-15, 180 km/h, 52.5 kWh)
# polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan
# kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

# Pääohjelma
sahkoauto = SahkoAuto("ABC-15", 180, 52.5)
polttomoottoriauto = PolttoMoottoriAuto("ACD-123", 165, 32.3)

# Aseta kummallekin autolle haluamasi nopeus
sahkoauto.nopeus = 90
polttomoottoriauto.nopeus = 95

sahkoauto.kuljee(3)
polttomoottoriauto.kuljee(3)

print(f"Sähköauton matka: {sahkoauto.matka} km")
print(f"Polttomoottoriauton matka: {polttomoottoriauto.matka} km")
