'''
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
'''

sukupuoli = input("Anna biolooginen sukupuoli (Nainen = N tai Mies = M): ")
hemoglobiini = int(input("Anna hemoglobiiniarvo (g/l): "))
if sukupuoli == "N":
    if hemoglobiini >= 117 and hemoglobiini <= 175:
        print("Naisen hemoglobiini on normaali!")
    elif hemoglobiini < 117:
        print("Naisen hemoglobiini on liian alhainen!")
    else:
        print("Naisen hemoglobiini on liian korkea!")
if sukupuoli == "M":
    if hemoglobiini >= 134 and hemoglobiini <= 195:
        print("Miehen hemoglobiini on normaali!")
    elif hemoglobiini < 134:
        print("Miehen hemoglobiini on liian alhainen!")
    else:
        print("Miehen hemoglobiini on liian lkorkea!")
