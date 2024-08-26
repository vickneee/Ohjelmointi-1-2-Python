'''
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
'''

luku = input("Anna luku: ")
suurin = luku
pienin = luku
while luku != "":
    luku = input("Anna luku: ")
    if luku == "":
        break
    if luku > suurin:
        suurin = luku
    if luku < pienin:
        pienin = luku
print(f"Suurin luku on {suurin}. Pienin luku on {pienin}. Kiitos!")
