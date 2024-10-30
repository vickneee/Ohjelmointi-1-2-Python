"""Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu
matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin
arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma,
jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun
auton kaikki ominaisuudet."""


# Auto-luokka (class)
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def tulosta_auton_tiedot(self):
        print(f"Auton tiedot: \n"
              f"Rekisteritunnus: {self.rekisteritunnus},\n"
              f"Huippunopeus: {auto.huippunopeus},\n"
              f"Nopeus: {auto.nopeus},\n"
              f"Matka: {auto.matka}")


# Luodaan auto-olio (object)
auto = Auto("ABC-123", 142)
# Tulostetaan auton ominaisuudet (properties)
auto.tulosta_auton_tiedot()
