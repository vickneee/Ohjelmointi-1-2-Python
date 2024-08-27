nimet = []

etunimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while etunimi != "":
    nimet.append(etunimi)
    etunimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

for nimi in nimet:
    print(f"Moi, {nimi}!")

for i in range(0, len(nimet)):
    print(f"Moi, {nimet[i]}!")
