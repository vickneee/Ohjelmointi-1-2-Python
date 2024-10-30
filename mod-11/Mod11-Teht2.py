"""Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on
ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden
ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman
kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden
polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan
kolmen tunnin verran ja tulosta autojen matkamittarilukemat."""


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus + muutos < 0:
            self.nopeus = 0
        if self.nopeus + muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kuljee(self, tuntimaara):
        self.matka += self.nopeus * tuntimaara
        return self.matka

    def tulosta_matkamittarilukema(self):
        print(f"Matkamittarilukema: ")


class SahkoAuto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)
        pass

    def tulosta_matkamittarilukema(self):
        super().tulosta_matkamittarilukema()
        print(f"Sähköauto: {self.matka}")


class PolttoMoottoriAuto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(rekisteritunnus, huippunopeus)
        pass

    def tulosta_matkamittarilukema(self):
        super().tulosta_matkamittarilukema()
        print(f"Polttomoottoriauto: {self.matka}")


# Pääohjelma
sahkoauto = SahkoAuto("ABC-15", 180, 52.5)
polttomoottoriauto = PolttoMoottoriAuto("ACD-123", 165, 32.3)

# Aseta kummallekin autolle haluamasi nopeus
sahkoauto.nopeus = 90
polttomoottoriauto.nopeus = 95

# Käske autoja ajamaan kolmen tunnin verran
sahkoauto.kuljee(3)
polttomoottoriauto.kuljee(3)

# Tulosta autojen matkamittarilukemat
sahkoauto.tulosta_matkamittarilukema()
polttomoottoriauto.tulosta_matkamittarilukema()
