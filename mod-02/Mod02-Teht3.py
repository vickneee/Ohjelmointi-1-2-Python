# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan. Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.
# pinta-ala = kanta * korkeus
# piiri = 2 * (kanta + korkeus)

kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))
pintaala = kanta * korkeus
piiri = 2 * (kanta + korkeus)

print(f"Suorakulmion pinta-ala on {pintaala:.2f}")
print(f"Suorakulmion piiri on {piiri:.2f}")
