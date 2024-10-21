"""Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h). Jos
nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton
nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton
nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee
sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä
päivittää."""


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


# Luodaan auto-olio (object) Rekisteritunnuksella ABC-123 ja Huippunopeuksella 142 km/h
auto1 = Auto("ABC-123", 142)

# Tulostetaan auton ominaisuudet (properties)
print(f"Rekisteritunnus: {auto1.rekisteritunnus} \n"
      f"Huippunopeus: {auto1.huippunopeus} km/h \n"
      f"Alkunopeus: {auto1.nopeus} \n"
      f"Matka alussa: {auto1.matka}")

# Kiihdytetään autoa 30 km/h
auto1.kiihdyta(+30)
# print(f"Auto nopeus: {auto1.nopeus}")
# Kiihdytetään autoa vielä 70 km/h
auto1.kiihdyta(+70)
# print(f"Auto nopeus: {auto1.nopeus}")
# Kiihdytetään autoa vielä 50 km/h
auto1.kiihdyta(+50)
# Tulostetaan nopeus (speed) 30 + 70 + 50 = 150 km/h
print(f"Nopeus: {auto1.nopeus}")

# Hätäjarrutus ja tulostetaan nopeus (speed)
auto1.kiihdyta(-200)
print(f"Nopeus: {auto1.nopeus}")
