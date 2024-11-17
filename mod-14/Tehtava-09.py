class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tuntimaara):
        self.matka += self.nopeus * tuntimaara
        return self.matka

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}\n"
              f"Huippunopeus: {self.huippunopeus}\n"
              f"Nopeus: {self.nopeus}\n"
              f"Matka: {self.matka}")


# Luodaan auto-olio (object) Rekisteritunnuksella ABC-123 ja Huippunopeuksella 142 km/h
auto = Auto("ABC-123", 142)

# Tulostetaan auton ominaisuudet (properties)
auto.tulosta_tiedot()

# Kiihdytetään autoa ja tulostetaan nopeus (speed)
auto.kiihdyta(90)
print(f"Nopeus: {auto.nopeus}")

# Matkustetaan ja tulostetaan kuljettu matka (distance)
auto.kulje(1.5)
print(f"Matka {auto.matka} km")
