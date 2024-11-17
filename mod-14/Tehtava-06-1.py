class Tyontekija:

    tyontekijoiden_lkm = 0

    def __init__(self, etunimi, sukunimi):
        Tyontekija.tyontekijoiden_lkm += 1
        self.tyontekija_nro = Tyontekija.tyontekijoiden_lkm
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.tyontekija_nro}: {self.etunimi} {self.sukunimi}")


class Tuntipalkkainen(Tyontekija):
    def __init__(self, etunimi, sukunimi, tuntipalkka):
        super().__init__(etunimi, sukunimi)
        self.tuntipalkka = tuntipalkka

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Tuntipalkka: {self.tuntipalkka} €/h")


class Kuukausipalkkainen(Tyontekija):
    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        super().__init__(etunimi, sukunimi)
        self.kuukausipalkka = kuukausipalkka

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kuukausipalkka: {self.kuukausipalkka} kk")


tyontekijat = []
tyontekijat.append(Tuntipalkkainen("Hanna", "Haitov", 12))
tyontekijat.append(Kuukausipalkkainen("Viivi", "Virta", 2000))
tyontekijat.append(Tyontekija("Kaija", "Koo"))
tyontekijat.append(Tuntipalkkainen("Tene", "Laul", 20))

for t in tyontekijat:
    t.tulosta_tiedot()
