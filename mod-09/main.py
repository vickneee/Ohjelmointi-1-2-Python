from auto import Auto

import random

# auto1 = Auto("ABC-123", 142)
# auto2 = Auto("ABC-999", 122)
# auto1.tulosta_auton_tiedot()

# auto1.kiihdyta(30)
# print(auto1.nopeus)
# auto2.kiihdyta(90)
# print(auto2.nopeus)
# print(auto2.kulje(2))
# auto1.kiihdyta(-20)
# print(auto1.nopeus)
# auto2.kiihdyta(-60)
# print(auto2.kulje(1))
# print(f"Nopeus: {auto2.nopeus}")


def luo_kilpailu_autot():
    autot = []
    for i in range(10):
        maxnopeus = (random.randint(100, 200))
        autot.append(Auto(f"ABC-{i + 1}", maxnopeus))
        print(f"Auto: {autot[i].rekisteritunnus} | Huippunopeus {autot[i].huippunopeus} km/h")
    return autot


def kilpailu():
    autot = luo_kilpailu_autot()
    kilpailu_kaynissa = True

    while kilpailu_kaynissa:
        for auto in autot:  # 10 kierrosta
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)
            if auto.matka >= 10000:
                print(f"Voittaja: {auto.rekisteritunnus} ja se on kulkenut {auto.matka} km.")
                kilpailu_kaynissa = False
                break
    return autot


def tulosta_kilpailu_tulokset():
    autot = kilpailu()
    print("Kilpailun tulokset:")
    print("Rek-tunnus | Huippunopeus | Nopeus | Matka")
    for auto in autot:
        print(f"{auto.rekisteritunnus:>10} | {auto.huippunopeus:>12} | {auto.nopeus:>6} | {auto.matka}.")


tulosta_kilpailu_tulokset()
