class Koira:

    koirien_lkm = 0

    def __init__(self, nimi, syntymavuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.haukahdus = haukahdus
        Koira.koirien_lkm += 1
        print(f"Koiria luotu: {Koira.koirien_lkm} kpl")

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(f"{self.nimi} haukuu {self.haukahdus}")

    def ika(self):
        return 2024 - self.syntymavuosi


class Hoitola:
    def __init__(self):
        self.koirat = []

    def koira_sisaan(self, koira):
        self.koirat.append(koira)
        print(f"{koira.nimi} kirjattu sisään")

    def koira_ulos(self, koira):
        self.koirat.remove(koira)
        print(f"{koira.nimi} kirjattu ulos")

    def tervehdi_koiria(self):
        for koira in self.koirat:
            koira.hauku(1)


# Pääohjelma
print("-- Koiria luodaan --")
koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

hoitola = Hoitola()
print("-- Koira sisään --")
hoitola.koira_sisaan(koira1)
hoitola.koira_sisaan(koira2)
print("-- Tervehdys --")
hoitola.tervehdi_koiria()
print("-- Koira ulos --")
hoitola.koira_ulos(koira1)
print("-- tervehdys --")
hoitola.tervehdi_koiria()
