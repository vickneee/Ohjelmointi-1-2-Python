# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

luoti = 13.3
naula = 32 * luoti
leiviska = 20 * naula

leiviskat = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

massa = luodit * luoti + naulat * naula + leiviskat * leiviska

print(f"Massa nykymittojen mukaan:\n{massa / 1000:.0f} kilogramma ja {massa:.2f} grammaa.")
