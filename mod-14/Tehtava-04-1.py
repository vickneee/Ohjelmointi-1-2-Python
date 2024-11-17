class Koira:

    koirien_lkm = 0

    def __init__(self, nimi, syntymavuosi, haukahdus="Viuh-viuh"):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.haukahdus = haukahdus

    def haukuu(self, kertaa):
        for i in range(kertaa):
            print(f"{self.nimi} haukuu {self.haukahdus}")


class Hoitola:

    def __init__(self):
        self.koirat = []

    def koira_sisään(self, koira):
        self.koirat.append(koira)
        print(f"{koira.nimi} kirjattu sisään")
        return

    def koira_ulos(self, koira):
        self.koirat.remove(koira)
        print(f"{koira.nimi} kirjattu ulos")
        return

    def tervehdi_koiria(self):
        for koira in self.koirat:
            koira.haukuu(1)


koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

hoitola = Hoitola()

hoitola.koira_sisään(koira1)
hoitola.koira_sisään(koira2)
hoitola.tervehdi_koiria()

hoitola.koira_ulos(koira1)
hoitola.tervehdi_koiria()

