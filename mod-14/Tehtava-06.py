# Henkilö ja työntekijä


class Tyontekija:
    tyontekijoiden_lkm = 0  # staattinen luokkamuuttuja

    def __init__(self, etunimi, sukunimi):
        Tyontekija.tyontekijoiden_lkm += 1  # kasvatetaan luokkamuuttujaa
        self.tyontekijanumero = Tyontekija.tyontekijoiden_lkm  # annetaan työntekijänumeroksi luokkamuuttujan arvo
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):  # tulostetaan työntekijän tiedot
        print(f"{self.tyontekijanumero}: {self.etunimi} {self.sukunimi}")


class Tuntipalkkainen(Tyontekija):
    def __init__(self, etunimi, sukunimi, tuntipalkka):
        super().__init__(etunimi, sukunimi)
        self.tuntipalkka = tuntipalkka

    def tulosta_tiedot(self):  # tulostetaan tuntipalkkaisen työntekijän tiedot
        super().tulosta_tiedot()  # kutsutaan yliluokan metodia
        print(f" Tuntipalkka: {self.tuntipalkka}")


class Kuukausipalkkainen(Tyontekija):
    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        super().__init__(etunimi, sukunimi)  # kutsutaan yliluokan konstruktoria
        self.kuukausipalkka = kuukausipalkka

    def tulosta_tiedot(self):  # tulostetaan kuukausipalkkaisen työntekijän tiedot
        super().tulosta_tiedot()  # kutsutaan yliluokan metodia
        print(f" Kuukausipalkka: {self.kuukausipalkka}")


# Pääohjelma
def kaikki_tyontekijat():
    tyontekijat = []
    tyontekijat.append(Tuntipalkkainen("Viivi", "Virta", 12.35))
    tyontekijat.append(Kuukausipalkkainen("Ahmed", "Habib", 2750))
    tyontekijat.append(Tyontekija("Pekka", "Puro"))
    tyontekijat.append(Tuntipalkkainen("Olga", "Glebova", 14.92))

    for t in tyontekijat:
        t.tulosta_tiedot()


kaikki_tyontekijat()
