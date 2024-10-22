"""Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit
siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h
esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta
kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai
alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin
ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen."""


# Luodaan Hissi-luokka
class Hissi:
    # Uusi hissi on aina alimmassa kerroksessa
    def __init__(self, alin_kerros, ylin_kerros):
        self.nykyinen_kerros = alin_kerros
        self.max_kerros = ylin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.max_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > 1:
            self.nykyinen_kerros -= 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.nykyinen_kerros:
            while kohde_kerros < self.nykyinen_kerros:
                self.kerros_alas()
        elif kohde_kerros > self.nykyinen_kerros:
            while kohde_kerros > self.nykyinen_kerros:
                self.kerros_ylos()


# Pääohjelma
# Luodaan Hissi-olio (object) ja siirretään se kerrokseen 5
hissi1 = Hissi(1, 7)
hissi2 = Hissi(1, 3)
print(hissi1.nykyinen_kerros)
hissi1.siirry_kerrokseen(5)
print(hissi1.nykyinen_kerros)
hissi1.siirry_kerrokseen(1)
print(hissi1.nykyinen_kerros)
hissi1.siirry_kerrokseen(7)
print(hissi1.nykyinen_kerros)
hissi1.siirry_kerrokseen(4)
