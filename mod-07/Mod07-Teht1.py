"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
että joulukuu on ensimmäinen talvikuukausi.
"""

# Version 1
kuukaudet = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")
numero = int(input("Anna kuukauden numero: "))
vuodenaika = kuukaudet[numero - 1]
print(vuodenaika)

# Version 2
vuodenaika = ("Talvi", "Kevät", "Kesä", "Syksy")
kuukausi = int(input("Anna kuukauden numero: "))

if 3 <= kuukausi <= 5:
    print(vuodenaika[1])
elif 6 <= kuukausi <= 8:
    print(vuodenaika[2])
elif 9 <= kuukausi <= 11:
    print(vuodenaika[3])
elif kuukausi == 12 or kuukausi <= 2:
    print(vuodenaika[0])
else:
    print("Virheellinen kuukauden numero")
