"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan,
joka on muuten samanlainen kuin parametrina saatu lista
paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan,
kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
"""


def poista_parittomat(lista):
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista


alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
uusilista = poista_parittomat(alkuperainen_lista)
print("Alkuperäinen lista:", alkuperainen_lista)
print("Karsittu lista:", uusilista)
