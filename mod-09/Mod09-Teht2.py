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


# Luodaan auto-olio (object)
auto = Auto("ABC-123", 142)

# Tulostetaan auton ominaisuudet (properties)
print(f"Rekisteritunnus: {auto.rekisteritunnus} \n"
      f"Huippunopeus: {auto.huippunopeus} km/h \n"
      f"Nopeus: {auto.nopeus} \n"
      f"Matka: {auto.matka}")

# Kiihdytetään autoa ja tulostetaan nopeus (speed)
auto.kiihdyta(+30)
print(f"Nopeus: {auto.nopeus}")

# Kiihdytetään autoa ja tulostetaan nopeus (speed)
auto.kiihdyta(+70)
print(f"Nopeus: {auto.nopeus}")

# Kiihdytetään autoa ja tulostetaan nopeus (speed)
auto.kiihdyta(+50)
print(f"Nopeus: {auto.nopeus}")

# Hätäjarrutus ja tulostetaan nopeus (speed)
auto.kiihdyta(-200)
print(f"Nopeus: {auto.nopeus}")
