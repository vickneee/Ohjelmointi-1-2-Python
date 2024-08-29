'''
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
'''

tuumat = float(input("Anna tuumamäärä: "))

while tuumat > 0:
    sentit = tuumat * 2.54
    print(f"{tuumat} tuumia on {sentit:.2f} sentimetriä.")
    tuumat = float(input("Anna tuumamäärä: "))
print("Kiitos ohjelman käytöstä!")
