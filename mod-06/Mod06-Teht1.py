"""
Kirjoita parametriton funktio,
joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun
silmäluvun.
"""

import random


def satunainen_noppa():
    satunainennop = random.randint(1, 6)
    return satunainennop


luku = satunainen_noppa()
laske = 1
while luku != 6:
    print(luku)
    luku = satunainen_noppa()
    laske += 1

print(f"Ohjelma lopetetaan, koska kierokksella {laske} tuli kuutonen!")
