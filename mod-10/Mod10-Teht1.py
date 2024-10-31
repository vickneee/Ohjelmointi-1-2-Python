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
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    # Kerros ylös metodi
    def kerros_ylos(self):
        if self.kerros <= self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi siirty {self.kerros} kerrokseeen")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    # Kerros alas metodi
    def kerros_alas(self):
        if self.alin_kerros >= 1:
            self.kerros -= 1
            print(f"Hissi siirty {self.kerros} kerrokseeen")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    # Siirry kerrokseen metodi
    def siirry_kerrokseen(self, kohde_kerros):
        self.tulosta_kerros_alku()

        if kohde_kerros < self.alin_kerros:
            print("Valittua kerrosta ei ole olemassa")
            return
        if kohde_kerros > self.ylin_kerros:
            print("Valittua kerrosta ei ole olemassa")
            return

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


# Pääohjelma
# Luodaan Hissi-olio (object) ja siirretään se kerrokseen 5
hissi1 = Hissi(1, 7)
hissi2 = Hissi(1, 3)
hissi1.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(1)
hissi1.siirry_kerrokseen(3)
hissi1.siirry_kerrokseen(9)
print()
hissi2.siirry_kerrokseen(2)
hissi2.siirry_kerrokseen(3)
hissi2.siirry_kerrokseen(1)
