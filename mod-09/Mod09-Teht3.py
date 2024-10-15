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

    # Kiihdytä-metodi (funktio)
    def kiihdyta(self, muutos):
        if muutos < 0:
            if self.nopeus + muutos < 0:
                self.nopeus = 0
            else:
                self.nopeus += muutos
        else:
            if self.nopeus > self.huippunopeus:
                self.nopeus = self.huippunopeus
            else:
                self.nopeus += muutos

    # Kulje-metodi (funktio)
    def kulje(self, tuntimaara):
        self.matka = self.nopeus * tuntimaara + self.matka
        return self.matka


# Luodaan auto-olio (object)
auto = Auto("ABC-123", 142)

# Tulostetaan auton ominaisuudet (properties)
print(f"Rekisteritunnus: {auto.rekisteritunnus} \n"
      f"Huippunopeus: {auto.huippunopeus} km/h \n"
      f"Alkunopeus: {auto.nopeus} \n"
      f"Matka: {auto.matka}")

# Kiihdytetään autoa ja tulostetaan nopeus (speed)
auto.kiihdyta(60)
print(f"Nopeus: {auto.nopeus}")

# Matkustetaan ja tulostetaan kuljettu matka (distance)
auto.kulje(1.5)
print(f"Matka {auto.matka} km")
