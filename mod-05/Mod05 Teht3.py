'''
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. Tässä tehtävässä alkulukuja
ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
'''

# negatiiviset numerot, 0 ja 1 eivat ole alkulukuja
numero = int(input("Anna numero: "))

if numero > 1:
    # Silmukka annetun numeron asti jaottuna kahdella ja lisätty yksi
    for i in range(2, (numero // 2) + 1):
        if (numero % i) == 0:
            print(numero, "ei ole alkuluku!")
            break
    else:
        print(numero, "on alkuluku!")
else:
    print(numero, "ei ole alkuluku!")
