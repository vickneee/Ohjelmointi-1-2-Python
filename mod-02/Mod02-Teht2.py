# Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan

import math

sade = float(input("Anna ympyrän säde: "))

pintaala = math.pi * sade ** 2

print(f"Ympyrän pinta-ala on {pintaala:.2f}")
