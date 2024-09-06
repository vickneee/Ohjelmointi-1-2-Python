"""
Kirjoita funktio,
joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat
ja hinnat sekä ilmoittaa,
kumpi pizza antaa paremman vastineen rahalle
(eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
"""


def pizza_hinta(halkaisija, hinta):
    pinta_ala = 3.14 * (halkaisija / 2)**2
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta


pizza1 = float(input("Anna ensimmäisen pizzan halkaisija: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta: "))
pizza2 = float(input("Anna toisen pizzan halkaisija: "))
hinta2 = float(input("Anna toisen pizzan hinta: "))
yksikkohinta1 = pizza_hinta(pizza1, hinta1)
yksikkohinta2 = pizza_hinta(pizza2, hinta2)

if yksikkohinta1 < yksikkohinta2:
    print("Yksikkohinta1:", yksikkohinta1)
    print("Yksikkohinta2:", yksikkohinta2)
    print("Ensimmäine pizza antaa paremman vastineen rahalle.")
else:
    print("Toine pizza antaa paremman vastineen rahalle.")
