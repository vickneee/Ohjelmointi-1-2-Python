"""Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
Talon alustajaparametreina annetaan alimman ja
ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin
numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi."""


# Luodaan Hissi-luokka
class Hissi:
    # Uusi hissi on aina alimmassa kerroksessa
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    # Kerros ylös metodi
    def kerros_ylos(self):
        self.kerros += 1
        if self.kerros <= self.ylin_kerros:
            print(f"Hissi siirtyy {self.kerros} kerrokseeen")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    # Kerros alas metodi
    def kerros_alas(self):
        self.kerros -= 1
        if self.alin_kerros >= 1:
            print(f"Hissi siirtyy {self.kerros} kerrokseeen")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    # Siirry kerrokseen metodi
    def siirry_kerrokseen(self, kohde_kerros):
        self.tulosta_kerros_alku()
        if kohde_kerros < self.alin_kerros:
            print("Valittua kerrosta ei ole olemassa")
            return  # Poistutaan metodista
        if kohde_kerros > self.ylin_kerros:
            print("Valittua kerrosta ei ole olemassa")
            return  # Poistutaan metodista

        while self.kerros > kohde_kerros:
            self.kerros_alas()
        while self.kerros < kohde_kerros:
            self.kerros_ylos()

        self.tulosta_kerros_loppu()

    # Tulosta kerros metodi
    def tulosta_kerros_alku(self):
        print(f"Hissi on siirron alussa {self.kerros} kerroksessa")

    # Tulosta kerros metodi
    def tulosta_kerros_loppu(self):
        print(f"Hissi on siirron lopussa {self.kerros} kerroksessa")


# Luodaan Talo-luokka
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lkm = hissien_lkm
        # Luodaan tyhjä lista hisseille
        self.hissit = []
        self.luo_hissit()

    # Metodi hissien luomiseksi
    def luo_hissit(self):  # Luodaan hissit
        for hissi in range(self.hissien_lkm):
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros))
            # print(f"Luotiin hissi numero {i + 1} kerroksiin {alin_kerros} - {ylin_kerros}")

    # Metodi hissin ajamiseksi
    def kayta_hissia(self, hissi_numero, kohde_kerros):
        if 0 < hissi_numero <= self.hissien_lkm:
            hissi = self.hissit[hissi_numero - 1]  # Hissi-numerot / indexit alkavat nollasta
            hissi.siirry_kerrokseen(kohde_kerros)
        else:
            print(f"Hissi numero {hissi_numero} ei ole olemassa.")


# Pääohjelma
# Luodaan Talo-olio (object)
talo1 = Talo(1, 7, 3)
talo1.kayta_hissia(1, 5)
talo1.kayta_hissia(2, 3)
talo1.kayta_hissia(3, 7)
talo1.kayta_hissia(5, 7)
