"""Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja
ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin
numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi."""


# Luodaan Hissi-luokka
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    # Metodi hissin siirtämiseksi haluttuun kerrokseen (functio)
    def siirry_kerrokseen(self, kerros):
        if kerros < self.alin_kerros:
            while kerros < self.alin_kerros:
                self.kerros_alas()
        elif kerros > self.alin_kerros:
            while kerros > self.alin_kerros:
                self.kerros_ylos()

        print(f"# Hissi on kerroksessa {self.alin_kerros} #")

    # Metodi hissin siirtämiseksi ylöspäin (functio)
    def kerros_ylos(self):
        if self.alin_kerros < self.ylin_kerros:
            self.alin_kerros += 1
            print(f"Hissi on kerroksessa {self.alin_kerros}")
        else:
            print(f"Hissi on jo ylimmässä kerroksessa.")

    # Metodi hissin siirtämiseksi alaspäin (functio)
    def kerros_alas(self):
        if self.alin_kerros > 1:
            self.alin_kerros -= 1
            print(f"Hissi on kerroksessa {self.alin_kerros}")
        else:
            print(f"Hissi on jo alimmassa kerroksessa.")


# Luodaan Talo-luokka
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lkm = hissien_lkm
        # Luodaan tyhjä lista hisseille
        self.hissit = []

        # Luodaan hissit
        for i in range(hissien_lkm):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))
            # print(f"Luotiin hissi numero {i + 1} kerroksiin {alin_kerros} - {ylin_kerros}")

    # Metodi hissin ajamiseksi (functio)
    def kayta_hissia(self, hissi_numero, kohdekerros):
        if 0 < hissi_numero <= self.hissien_lkm:
            hissi = self.hissit[hissi_numero - 1]  # Hissi-numerot / indexit alkavat nollasta
            hissi.siirry_kerrokseen(kohdekerros)
        else:
            print(f"Hissi numero {hissi_numero} ei ole olemassa.")


# Pääohjelma
# Luodaan Talo-olio (object)
talo1 = Talo(1, 7, 3)
talo1.kayta_hissia(1, 5)
print()
talo1.kayta_hissia(2, 3)
print()
talo1.kayta_hissia(3, 7)
print()

for mika_hissi in talo1.hissit:
    print(f"Hissi on kerroksessa {mika_hissi.alin_kerros}")
