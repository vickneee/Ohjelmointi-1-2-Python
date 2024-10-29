"""Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman
alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan
100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään
kutsumalla kiihdytä-metodia. Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla
kulje-metodia. Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan
kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna."""


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 2000

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus + muutos < 0:
            self.nopeus = 0
        elif self.nopeus + muutos >= self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kuljee(self, tuntimaara):
        self.matka = self.nopeus * tuntimaara + self.matka
        return self.matka


auto = Auto("ABC-123", 142)
print(f"Rekisteritunnus: {auto.rekisteritunnus}\n"
      f"Huippunopeus: {auto.huippunopeus}\n"
      f"Alkunopeus: {auto.nopeus}\n"
      f"Matka: {auto.matka}")

auto.kiihdyta(+60)
print(f"Auton hetken nopeus: {auto.nopeus}")
auto.kiihdyta(-20)
print(f"Auton hetken nopeus: {auto.nopeus}")

auto.kuljee(1.5)
print(f"Auto matka {auto.matka:.0f} km")
