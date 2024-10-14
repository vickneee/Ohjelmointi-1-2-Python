"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma,
jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
"""


def summalista(alkulista):
    return sum(alkulista)

    # summa = 0
    # for luku in alkulista:
    #     summa += luku
    # return summa


luku = int(input("Kuinka monta lukua haluat listalle? "))
lista = []
for i in range(luku):
    lista.append(int(input(f"Anna luku {i + 1}: ")))

print(f"Lista tulostetuna on: {lista}. Listassa olevien lukujen summa on: {summalista(lista)}.")
