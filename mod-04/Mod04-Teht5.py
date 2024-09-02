"""
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein
tai väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
(Oikea käyttäjätunnus on python ja salasana rules).
"""

kayttajatunnus = "python"
salasana = "rules"
yritykset = 0

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salas = input("Anna salasana: ")
    yritykset += 1
    if tunnus != kayttajatunnus or salas != salasana:
        print(f"Yrittä uudeleen! Olet yrittänyt {yritykset} kertaa!")
    elif tunnus == kayttajatunnus and salas == salasana:
        print("Pääsy hyväksytty!")
else:
    print(f"Pääsy evätty! Olet yrittänyt {yritykset} kertaa!")


