class Koira:

    koirien_lkm = 0

    def __init__(self, nimi, syntymavuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.haukahdus = haukahdus
        Koira.koirien_lkm += 1
        print(f"Koiria luotu: {Koira.koirien_lkm} kpl")

    def hauku(self, kertaa):
        print(f"{self.nimi} haukuu {kertaa} kertaa")
        for i in range(kertaa):
            print(f"{self.haukahdus}")


koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

koira1.hauku(2)
koira2.hauku(5)
print(f"Koiria luotu yhteensä: {Koira.koirien_lkm} kpl")
