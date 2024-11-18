class Opiskelija:
    def __init__(self, nimi, kurssit):
        self.nimi = nimi
        self.kurssit = kurssit  # sanakirja

    def laske_keskiarvo(self):
        if len(self.kurssit) == 0:
            return 0
        return sum(self.kurssit.values()) / len(self.kurssit)

    def print(self):
        for i in self.kurssit.values():
            # i = self.kurssit.values()
            print(i)
        for j in self.kurssit.keys():
            print(j)

    def tuplataan_arvosanat(self):
        for kurssi in self.kurssit:
            self.kurssit[kurssi] *= 2


# Luodaan opiskelija-oliot
opiskelija1 = Opiskelija("Anna", {"Matematiikka": 5, "Ohjelmointi": 4, "Fysiikka": 3})
opiskelija2 = Opiskelija("Mikko", {"Biologia": 6, "Kemia": 7})

# Tulostetaan alkuperäiset keskiarvot
print(f"{opiskelija1.nimi} keskiarvo: {opiskelija1.laske_keskiarvo():.2f}")
print(f"{opiskelija2.nimi} keskiarvo: {opiskelija2.laske_keskiarvo():.2f}")

# Tuplataan arvosanat ja tulostetaan uudet keskiarvot
opiskelija1.tuplataan_arvosanat()
opiskelija2.tuplataan_arvosanat()

opiskelija1.print()
opiskelija2.print()

print(f"{opiskelija1.nimi} tuplatut keskiarvo: {opiskelija1.laske_keskiarvo():.2f}")
print(f"{opiskelija2.nimi} tuplatut keskiarvo: {opiskelija2.laske_keskiarvo():.2f}")