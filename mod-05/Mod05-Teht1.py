"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
Ohjelma heittää kerran kaikkia arpakuutioita 
ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
"""

import random

# Versio 1
print("Versio 1")
lukumaara = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

for i in range(lukumaara):
    j = random.randint(1, 6)  # Arvotaan luku
    # print(j)
    summa += j

print(f"Summa on {summa}")  # Summan tulostus

# Versio 2
print("Versio 2")
lukumaara = int(input("Anna arpakuutioiden lukumäärä: "))
lista = []

for i in range(lukumaara):
    lista.append(random.randint(1, 6))  # Arvotaan luku ja lisätään listaan
    print(lista)  # Lista tulostetuna

print(f"Summa on {sum(lista)}")  # Listan summa tulostus
