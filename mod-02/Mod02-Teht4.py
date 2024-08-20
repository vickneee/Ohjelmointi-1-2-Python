# Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

eka = int(input("Anna ensimmäinen luku: "))
toka = int(input("Anna toinen luku: "))
kolmas = int(input("Anna kolmas luku: "))

summa = eka + toka + kolmas
tulo = eka * toka * kolmas
keskiarvo = summa / 3

print(f"Lukujen summa on {summa}, tulo on {tulo} ja keskiarvo on {keskiarvo:.2f}.")
