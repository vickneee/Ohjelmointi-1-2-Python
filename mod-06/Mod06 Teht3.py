'''
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.
'''


def gallonatlitroiksi(gallona):
    litrat = gallona * 3.785
    return litrat


gallon = float(input("Anna bensiinin määrä gallonoina (Negatiivinen luku lopeta ohjelma): "))
while gallon >= 0:
    print(f"{gallon} gallonaa on {gallonatlitroiksi(gallon):.2f} litraa.")
    gallon = float(input("Anna bensiinin määrä gallonoina (Negatiivinen luku lopeta ohjelma): "))
print("Kiitos ohjelman käytöstä.")
