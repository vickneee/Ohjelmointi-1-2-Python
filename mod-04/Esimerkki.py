"""
Tehtävä:
Tulosta lukujen 3, 4 ... 7 kertotaulu.
Kunkin kertotaulun alussa kerrotaan
minkä luvun kertotaulu esitetään.
Kertojana on luvut 1, 2, 3, 4 ja 5
"""

# * Tästä alkaa ns. ulompi toistorakenne
luku = 3  # minkä luvun kertotaulu tulostetaan

while luku <= 7:
    print(f"Luvun {luku} kertotaulu:")

    # * Tästä alkaa ns. sisempi toistorakenne
    # tähän väliin tulostetaan ko. luvun kertotaulu
    kertoja = 1

    while kertoja <= 5:
        tulo = kertoja * luku
        print(f"  {kertoja} * {luku} = {tulo}")
        kertoja += 1  # kertoja arvoa lisätään yhdellä

    # lisätään ns. ulomman toistorakenteen muuttujaa
    luku += 1  # sama kuin luku = luku +1

'''
# Harjoittelu 1:
luku = 3    # minkä luvun kertotaulu tulostetaan
while luku <= 7:
    print(f"Luvun {luku} kertotaulu:")
    luku += 1   # sama kuin luku = luku +1

# Harjoittelu 2:
# tulostan luvun 3 kertotaulun
luku = 3
kertoja = 1

while kertoja <= 5:
    tulo = kertoja * luku
    print(f"  {kertoja} * {luku} = {tulo}")
    kertoja += 1  # kertoja arvoa lisätään yhdellä
'''
