"""
Jatka edellisen tehtävän ohjelmaa siten,
että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki
hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys."""


# Luodaan Hissi-luokka
class Hissi:
    # Uusi hissi on aina alimmassa kerroksessa
    def __init__(self, alin_kerros, ylin_kerros, hissin_nro):
        self.nykyinen_kerros = alin_kerros
        self.max_kerros = ylin_kerros
        self.hissin_nro = hissin_nro

    # Metodi hissin siirtämiseksi haluttuun kohdekerrokseen (functio)
    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.nykyinen_kerros:
            while kohde_kerros < self.nykyinen_kerros:
                self.kerros_alas()
        elif kohde_kerros > self.nykyinen_kerros:
            while kohde_kerros > self.nykyinen_kerros:
                self.kerros_ylos()

        print(f"# Hissi {self.hissin_nro} on nyt kerroksessa {self.nykyinen_kerros} #")

    # Metodi hissin siirtämiseksi ylöspäin (functio)
    def kerros_ylos(self):
        if self.nykyinen_kerros < self.max_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi {self.hissin_nro} siirtyi kerrokseen {self.nykyinen_kerros}")
        else:
            print(f"Hissi {self.hissin_nro} on jo ylimmässä kerroksessa.")

    # Metodi hissin siirtämiseksi alaspäin (functio)
    def kerros_alas(self):
        if self.nykyinen_kerros > 1:
            self.nykyinen_kerros -= 1
            print(f"Hissi {self.hissin_nro} siirtyi kerrokseen {self.nykyinen_kerros}")
        else:
            print(f"Hissi {self.hissin_nro} on jo alimmassa kerroksessa.")


# Luodaan Talo-luokka
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.nykyinen_kerros = alin_kerros
        self.max_kerros = ylin_kerros
        self.hissien_lkm = hissien_lkm
        # Luodaan tyhjä lista hisseille
        self.hissit = []

        # Luodaan hissit
        for hissi in range(hissien_lkm):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros, hissi + 1))
            # print(f"Luotiin hissi numero {hissi + 1} kerroksiin {alin_kerros} - {ylin_kerros}")

    # Metodi hissin ajamiseksi (functio)
    def kayta_hissia(self, hissi_numero, kohde_kerros):
        if 0 < hissi_numero <= self.hissien_lkm:
            hissi = self.hissit[hissi_numero - 1]  # Hissi-numerot / indexit alkavat nollasta
            hissi.siirry_kerrokseen(kohde_kerros)
        else:
            print(f"Hissi numero {hissi_numero} ei ole olemassa.")

    # Metodi palohälytyksen antamiseksi (functio)
    def palohalytys(self):
        print()
        print("Palohälytys! Kaikki hissit pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(1)


# Pääohjelma
# Luodaan Talo-olio (object)
talo1 = Talo(1, 7, 3)
talo1.kayta_hissia(1, 5)
talo1.kayta_hissia(2, 3)
talo1.kayta_hissia(3, 7)
print()

# Tulostetaan tarkastuksen vuoksi hissien kerrokset
for mika_hissi in talo1.hissit:
    print(f"Hissi {mika_hissi.hissin_nro} on kerroksessa {mika_hissi.nykyinen_kerros}")

# Kutsutaan palohälytystä
talo1.palohalytys()
print()

# Tulostetaan tarkastuksen vuoksi hissien kerrokset
for mika_hissi in talo1.hissit:
    print(f"Hissi {mika_hissi.hissin_nro} on kerroksessa {mika_hissi.nykyinen_kerros}")
