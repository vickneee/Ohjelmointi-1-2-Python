"""Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja
ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin
numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi."""


# Luodaan Hissi-luokka
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    # Metodi hissin siirtämiseksi ylöspäin (functio)
    def kerros_ylos(self):
        if self.alin_kerros < self.ylin_kerros:
            self.alin_kerros += 1
            print(f"Hissi on kerroksessa {self.alin_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    # Metodi hissin siirtämiseksi alaspäin (functio)
    def kerros_alas(self):
        if self.alin_kerros > 1:
            self.alin_kerros -= 1
            print(f"Hissi on kerroksessa {self.alin_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    # Metodi hissin siirtämiseksi haluttuun kerrokseen (functio)
    def siirry_kerrokseen(self, kerros):
        if kerros < self.alin_kerros:
            while kerros < self.alin_kerros:
                self.kerros_alas()
        elif kerros > self.alin_kerros:
            while kerros > self.alin_kerros:
                self.kerros_ylos()


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

    # Metodi hissin ajamiseksi (functio)
    def kayta_hissia(self, hissi_by_indeksi, kerros):
        self.hissit[hissi_by_indeksi].siirry_kerrokseen(kerros)


# Pääohjelma
# Luodaan Talo-olio (object) # Ei ole oikea?
talo1 = Talo(1, 7, 3)
print(talo1)
talo1.kayta_hissia(0, 5)
print(talo1)
talo1.kayta_hissia(1, 3)
print(talo1.hissit)
talo1.kayta_hissia(2, 7)
