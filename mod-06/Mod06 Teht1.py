"""
Kirjoita parametriton funktio,
joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun
silmäluvun.
"""

import random


def satunnainennoppa():
    arvottu = random.randint(1, 6)
    return arvottu


def main():
    luku = satunnainennoppa()
    while luku != 6:
        print(luku)
        luku = satunnainennoppa()
    print(f"Nyt tuli kuutonen! {luku} Ohjelma lopetetaan.")


main()
