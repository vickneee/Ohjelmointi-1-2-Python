"""
Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
kunnes käyttäjä syöttää tyhjän merkkijonon.
Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi
tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
Käytä joukkotietorakennetta nimien tallentamiseen.
"""


def tyhja_merkkijono():

    # Alustetaan tyhjä joukku
    nimi_joukko = set()

    nimi = input("Anna nimi (Tyhjä merkkijono lopeta): ")

    while nimi != "":
        if nimi in nimi_joukko:
            print("Aiemmin syötetty nimi")
        else:
            print("Ilmeistyi uusi nimi. Lisätään nimi joukkoon.")
        nimi_joukko.add(nimi)  # Joukkotietorakennetta nimien tallentamiseen.
        nimi = input("Anna nimi: (Tyhjä merkkijono lopeta): ")

    for i in nimi_joukko:
        print(i)

    return nimi_joukko


tyhja_merkkijono()
