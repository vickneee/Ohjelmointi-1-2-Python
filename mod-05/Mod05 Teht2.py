'''
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
'''

luvut = []
luku = input("Anna luku: (Tyhjä merkkijono lopeta) ")

while luku != "":
    if luku in luvut:
        print("Se luku on jo listalla. Dublikaatti!")
    else:
        luvut.append(int(luku))  # Muutetaan luku kokonaisluvuksi ennen listaan lisämistä
        print(luvut)
    luku = input("Anna luku: (Tyhjä merkkijono lopeta) ")

luvut.sort(reverse=True)
print(f"Viisi suurinta luku suuruusjärjestyksessä suurimmasta alkaen {luvut[0:5]}")
