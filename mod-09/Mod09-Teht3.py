"""Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. Metodi kasvattaa
kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. Esimerkki: auto-olion
tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan
lukemaan 2090 km."""


# Auto-luokka (class)
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 2000  # Alustetaan matka 2000 km kohdalta

    # Kiihdytä-metodi
    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus + muutos < 0:
            self.nopeus = 0
        if self.nopeus + muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus

    # Kulje-metodi
    def kulje(self, tuntimaara):
        self.matka = self.nopeus * tuntimaara + self.matka
        return self.matka

    # Tulosta auton tiedot-metodi
    def tulosta_auton_tiedot(self):
        print(f"Auton tiedot: \n"
              f"Rekisteritunnus: {self.rekisteritunnus},\n"
              f"Huippunopeus: {self.huippunopeus},\n"
              f"Nopeus: {self.nopeus},\n"
              f"Matka: {self.matka}")


# Luodaan auto-olio (object) Rekisteritunnuksella ABC-123 ja Huippunopeuksella 142 km/h
auto = Auto("ABC-123", 142)

# Tulostetaan auton ominaisuudet (properties)
auto.tulosta_auton_tiedot()

# Kiihdytetään autoa ja tulostetaan nopeus (speed)
auto.kiihdyta(60)
print(f"Nopeus: {auto.nopeus}")

# Matkustetaan ja tulostetaan kuljettu matka (distance)
auto.kulje(1.5)
print(f"Matka {auto.matka} km")
