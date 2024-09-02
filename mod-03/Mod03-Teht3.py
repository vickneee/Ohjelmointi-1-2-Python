"""
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen
ja hemoglobiiniarvon (g/l).
Ohjelma ilmoittaa,
onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
"""

sukupuoli = input("Anna biolooginen sukupuoli (Nainen = N tai n or Mies = M tai n): ")
sukupuoli = sukupuoli.upper()

hemoglobiini = int(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "N":
    if 117 <= hemoglobiini <= 175:
        print("Hemoglobiini on normaali!")
    elif hemoglobiini < 117:
        print("Hemoglobiini on liian alhainen!")
    else:
        print("Hemoglobiini on liian korkea!")

if sukupuoli == "M":
    if 134 <= hemoglobiini <= 195:
        print("Hemoglobiini on normaali!")
    elif hemoglobiini < 134:
        print("Hemoglobiini on liian alhainen!")
    else:
        print("Hemoglobiini on liian korkea!")
