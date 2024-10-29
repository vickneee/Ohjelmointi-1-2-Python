class Koira():
    def __init__(self, nimi, tervehdys="hau, hau"):
        self.nimi = nimi
        self.tervehdys = tervehdys

    def tervehdys(self):
        print(self.tervehdys)


class RotuKoira(Koira):
    def __init__(self, nimi, rotu, tervehdys="hau, hau"):
        super().__init__(self, nimi, tervehdys)
        self.rotu = rotu

