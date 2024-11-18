class Ajoneuvo:
    def __init__(self, merkki, huippunopeus, nopeus=0):
        self.merkki = merkki
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus

    def kiihdyta(self, maara):
        self.nopeus = min(self.huippunopeus, self.nopeus + maara)
        print(f"{self.merkki} kiihdyti. Uusi nopeus: {self.nopeus} km/h")

    def jarrutta(self, maara):
        self.nopeus -= maara
        if self.nopeus < 0:
            self.nopeus = 0
            return
        print(f"{self.merkki} jarruti. Uusi nopeus: {self.nopeus} km/h")


class Auto(Ajoneuvo):
    def __init__(self, merkki, huippunopeus, nopeus=0, matkustajat=0):
        super().__init__(merkki, huippunopeus, nopeus)
        self.matkustajat = matkustajat

    def lisaa_matkustaja(self):
        if self.matkustajat < 5:
            self.matkustajat += 1
            print(f"Matkustaja lisätty. Nyt kyydissä: {self.matkustajat}")
        else:
            print(f"Auto on jo täynnä, ei voi lisätä matkustajia")


auto = Auto("Toyota", 200)
auto.kiihdyta(50)
auto.kiihdyta(50)
auto.kiihdyta(50)
auto.kiihdyta(50)
auto.kiihdyta(50)
auto.jarrutta(100)
auto.jarrutta(100)
auto.jarrutta(100)
auto.jarrutta(100)
auto.lisaa_matkustaja()
auto.lisaa_matkustaja()
auto.lisaa_matkustaja()
auto.lisaa_matkustaja()
auto.lisaa_matkustaja()
auto.lisaa_matkustaja()
auto.lisaa_matkustaja()
