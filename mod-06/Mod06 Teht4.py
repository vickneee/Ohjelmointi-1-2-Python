'''
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
'''


def summalista(parameterlista):
    return sum(parameterlista)


lista = [1, 2, 9, 8, 3, 4, 5]
print(f"Lista tulostetuna on: {lista}. Listassa olevien lukujen summa on: {summalista(lista)}.")
