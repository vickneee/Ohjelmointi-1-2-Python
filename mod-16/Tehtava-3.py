class Tyontekija:
    tyont_lkm = 0

    def __init__(self, etunimi, sukunimi):
        Tyontekija.tyont_lkm += 1
        self.tyontekija_nro = Tyontekija.tyont_lkm
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.tyontekija_nro}: {self.etunimi} {self.sukunimi}")


class Rekisteri:

    def __init__(self):
        self.tyontekijat = []

    def tyont_rekisteriin(self, tyontekija):
        self.tyontekijat.append(tyontekija)
        print(f"{tyontekija.nimi} lisätty rekisteriin")

    def tyont_pois_rekisterista(self, tyontekija):
        self.tyontekijat.remove(tyontekija)
        print(f"{tyontekija.nimi} poistettu rekisterista")


class Tuntipalkkainen(Tyontekija):
    def __init__(self, etunimi, sukunimi, tuntipalkka):
        super().__init__(etunimi, sukunimi)
        self.tuntipalkka = tuntipalkka

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"ja tuntipalkka on {self.tuntipalkka}")


class Kuukausipalkkainen(Tyontekija):
    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        super().__init__(etunimi, sukunimi)
        self.kuukausipalkka = kuukausipalkka

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"ja kuukausipalkka on {self.kuukausipalkka}")


tyontekijat = []
tyontekijat.append(Kuukausipalkkainen("Anne", "Liiv", 3000))
tyontekijat.append(Tuntipalkkainen("Leila", "Mere", 30))
tyontekijat.append(Tyontekija("Janica", "Adamson"))
tyontekijat.append(Kuukausipalkkainen("Marek", "Lootus", 3000))

for t in tyontekijat:
    t.tulosta_tiedot()
