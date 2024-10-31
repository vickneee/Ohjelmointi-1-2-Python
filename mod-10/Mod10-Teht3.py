"""
Jatka edellisen tehtävän ohjelmaa siten,
että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki
hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys."""


# Luodaan Hissi-luokka
class Hissi:
    # Uusi hissi on aina alimmassa kerroksessa
    def __init__(self, alin_kerros, ylin_kerros, hissin_nro):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros  # Uusi Hissi on aina alimmassa kerroksessa
        self.hissin_nro = hissin_nro

    # Metodi hissin siirtämiseksi ylöspäin
    def kerros_ylos(self):
        self.kerros += 1
        if self.kerros <= self.ylin_kerros:
            print(f"Hissi nro {self.hissin_nro} siirtyy {self.kerros} kerrokseen")
        else:
            print(f"Hissi nro {self.hissin_nro} on jo ylimmässä kerroksessa.")

    # Metodi hissin siirtämiseksi alaspäin
    def kerros_alas(self):
        self.kerros -= 1
        if self.kerros >= self.alin_kerros:
            print(f"Hissi nro {self.hissin_nro} siirtyy {self.kerros} kerrokseen")
        else:
            print(f"Hissi nro {self.hissin_nro} on jo alimmassa kerroksessa.")

    # Metodi hissin siirtämiseksi haluttuun kohdekerrokseen (functio)
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

    def tulosta_kerros_alku(self):
        print(f"Hissi nro {self.hissin_nro} on siirron alussa {self.kerros} kerroksessa")

    def tulosta_kerros_loppu(self):
        print(f"Hissi nro {self.hissin_nro} on siirron lopussa {self.kerros} kerroksessa")


# Luodaan Talo-luokka
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lkm = hissien_lkm
        # Luodaan tyhjä lista hisseille
        self.hissit = []
        self.luo_hissit()

    # Luodaan hissit
    def luo_hissit(self):
        for hissi in range(self.hissien_lkm):
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros, hissi + 1))
            # print(f"Luotiin hissi numero {hissi + 1} kerroksiin {alin_kerros} - {ylin_kerros}")

    # Metodi hissin ajamiseksi (functio)
    def kayta_hissia(self, hissi_numero, kohde_kerros):
        if 0 < hissi_numero <= self.hissien_lkm:
            hissi = self.hissit[hissi_numero - 1]  # Hissi-numerot / indexit alkavat nollasta
            hissi.siirry_kerrokseen(kohde_kerros)
        else:
            print(f"Hissi numero {hissi_numero} ei ole olemassa.")

    # Metodi hissien tulostamiseksi
    def tulosta_hissit(self):
        for hissi in self.hissit:
            print(f"Hissi {hissi.hissin_nro} on kerroksessa {hissi.kerros}")

    # Metodi palohälytyksen antamiseksi (functio)
    def palohalytys(self):
        print()
        print("Palohälytys! Kaikki hissit pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)


# Pääohjelma
# Luodaan Talo-olio (object)
talo1 = Talo(1, 7, 3)
talo1.kayta_hissia(1, 5)
talo1.kayta_hissia(2, 3)
talo1.kayta_hissia(3, 5)

# Tulostetaan tarkastuksen vuoksi hissien kerrokset
talo1.tulosta_hissit()

# Kutsutaan palohälytystä
talo1.palohalytys()

# Tulostetaan tarkastuksen vuoksi hissien kerrokset
talo1.tulosta_hissit()
