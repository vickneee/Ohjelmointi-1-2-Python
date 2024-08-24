'''
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen
ja hemoglobiiniarvon (g/l).
Ohjelma ilmoittaa,
onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
'''

sukupuoli = input("Anna biolooginen sukupuoli (Nainen = N tai Mies = M): ")
hemoglobiini = int(input("Anna hemoglobiiniarvo (g/l): "))
if sukupuoli == "N":
    if hemoglobiini >= 117 and hemoglobiini <= 175:
        print("Hemoglobiini on normaali!")
    elif hemoglobiini < 117:
        print("Hemoglobiini on liian alhainen!")
    else:
        print("Hemoglobiini on liian korkea!")
if sukupuoli == "M":
    if hemoglobiini >= 134 and hemoglobiini <= 195:
        print("Hemoglobiini on normaali!")
    elif hemoglobiini < 134:
        print("Hemoglobiini on liian alhainen!")
    else:
        print("Hemoglobiini on liian korkea!")
