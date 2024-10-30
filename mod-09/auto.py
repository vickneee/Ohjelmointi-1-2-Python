import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def tulosta_auton_tiedot(self):
        print(f"Auton tiedot: \n"
              f"Rekisterinumero: {self.rekisteritunnus},\n"
              f"Huippunopeus: {self.huippunopeus},\n"
              f"Nopeus: {self.nopeus},\n"
              f"Matka: {self.matka}")

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus >= self.huippunopeus:
            self.nopeus = self.huippunopeus
        return

    def kulje(self, tuntimaara):
        self.matka += self.nopeus * tuntimaara
        return self.matka
