class Tili:

    lkm = 0

    def __init__(self, omistaja, saldo=0):
        self.omistaja = omistaja
        self.saldo = saldo
        Tili.lkm += 1
        print(f"Tilejä luotu: {Tili.lkm}")

    def maksa(self, summa):
        if self.saldo >= summa:
            self.saldo -= summa
            print("Maksu onnistui")
        else:
            print("Ei tarpeeksi rahaa")

    def tulostus(self):
        print(f"Omistaja: {self.omistaja}, tilillä rahaa {self.saldo}")


# Pääohjelma
print("--- tilien luonti ---")
t1 = Tili("Jorma")
t2 = Tili("Anne", 100)

print("--- maksut ---")
t1.maksa(25)
t2.maksa(25)

print("--- tilien saldot ---")
t1.tulostus()
t2.tulostus()
