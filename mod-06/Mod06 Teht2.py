"""
Muokkaa edellistä funktiota siten,
että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa
kunnes saadaan nopan maksimisilmäluku,
joka kysytään käyttäjältä ohjelman suorituksen alussa.
"""

import random


def satunnainennoppa(tahkoja):
    satunainnen = random.randint(1, tahkoja)
    return satunainnen


nopan_silmaluku = int(input("Anna nopan silmäluku: "))
while True:
    arvottu = satunnainennoppa(nopan_silmaluku)
    print(arvottu)

    if arvottu == nopan_silmaluku:
        break

print(f"Kokonaissumma on {arvottu}! Nopan silmaluku oli {nopan_silmaluku}. Ohjelma lopetetaan.")
