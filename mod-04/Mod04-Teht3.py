'''
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
'''

lukustr = input("Anna luku (Tyhjä merkkijono lopeta): ")

suurin = int(lukustr)
pienin = int(lukustr)

while lukustr != "":
    if int(lukustr) > suurin:
        suurin = int(lukustr)
    if int(lukustr) < pienin:
        pienin = int(lukustr)
    lukustr = input("Anna luku (Tyhjä merkkijono lopeta): ")

print(f"Suurin luku on {suurin}. Pienin luku on {pienin}. Kiitos!")

# Tyhjä merkkijonon lisääminen
