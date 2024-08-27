'''
Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
'''

import random

koneluku = random.randint(1, 10)
# print(koneluku) # Testi
arvaus = 0
while arvaus !=koneluku:
    arvaus = int(input("Arvaa luku väliltä 1-10: "))
    if arvaus < koneluku:
        print("Liian pieni arvaus!")
    elif arvaus > koneluku:
        print("Liian suuri arvaus!")
    else:
        print("Oikein!!!")
        break
