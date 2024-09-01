'''
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
'''

import random


def satunnainennoppa():
    arvottu = random.randint(1, 6)
    return arvottu


nopan_silmaluku = int(input("Anna nopan silmäluku: "))
luku = satunnainennoppa()
laske = luku
while laske <= nopan_silmaluku:
    print(luku)
    laske += luku
    luku = satunnainennoppa()
print(f"Kokonaissumma on {laske}! Nopan silmaluku oli {nopan_silmaluku}. Ohjelma lopetetaan.")
