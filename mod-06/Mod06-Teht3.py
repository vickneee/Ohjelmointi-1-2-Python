"""
Kirjoita funktio,
joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
ja palauttaa paluuarvonaan vastaavan litramäärän.
Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä
ja muuntaa sen litroiksi.
Muunnos on tehtävä aliohjelmaa hyödyntäen.
Muuntamista jatketaan siihen saakka,
kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.
"""


def gal_litroiksi(gallon):
    return gallon * 3.785


luku = float(input("Anna gallonit: "))

while luku > 0:
    litrat = gal_litroiksi(luku)
    print(f"{luku} gallonia litroina {litrat:.2f}")
    luku = float(input("Anna gallonit: "))

print("Ohjelma lopetettiin, koska syötit negatiivisen arvon!")

