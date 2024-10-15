"""Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. Metodi kasvattaa
kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. Esimerkki: auto-olion
tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan
lukemaan 2090 km."""


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 60
        self.matka = 2000

    def kiihdyta(self, muutos):
        if muutos < 0:
            if self.nopeus + muutos < 0:
                self.nopeus = 0
            else:
                self.nopeus + muutos
        else:
            if self.nopeus > self.huippunopeus:
                self.nopeus = self.huippunopeus
            else:
                self.nopeus + muutos

    def kulje(self, tuntimaara):
        self.matka = self.nopeus * tuntimaara + self.matka
        return self.matka


auto = Auto("ABC-123", 142)
print(f"Nopeus: {auto.nopeus} km/h")
print(f"Matka {auto.matka} km")
auto.kulje(1.5)
print(f"Matka {auto.matka} km")
