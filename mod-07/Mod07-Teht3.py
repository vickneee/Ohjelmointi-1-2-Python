"""
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
hakea jo syötetyn lentoaseman tiedot vai lopettaa.
Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
Löydät koodeja helposti selaimen avulla.)
"""

valikko = int(input("Haluatko syöttää uuden lentoaseman (Valitse nro 1),"
                    "\nhaluatko hakea lentoaseman tiedot (Valitse nro 2)"
                    "\ntai haluatko lopeta? (Valitse nro 3): "))

eka = 1
toka = 2
kolm = 3
lentoasemat = dict()

while valikko != kolm:
    if valikko == eka:
        print("Syötit nro 1!")
        icao_koodi_syotto = input("Syöttää lentoaseman ICAO-koodi: ")
        lentoaseman_nimi = input("Syöttää lentoaseman nimi: ")
        lentoasemat[icao_koodi_syotto] = lentoaseman_nimi
        print(f"Lisätty lentoasema: {lentoasemat}")
    elif valikko == toka:
        print("Hae lentoaseman ICA-koodi: ")
        icao_koodi_haku = input("Hae ICAO-koodi: ")
        if icao_koodi_haku not in lentoasemat:
            print("Valitettavasti lentoasema puutu sanakirjasta.")
            continue
        elif icao_koodi_haku in lentoasemat:
            lentoaseman_nimi = lentoasemat[icao_koodi_haku]
            print(f"Haettu lentoasema: {icao_koodi_haku} : {lentoaseman_nimi}.")

    valikko = int(input("Haluatko syöttää uuden lentoaseman (Valitse nro 1),\n"
                        "haluatko hakea lentoaseman tiedot (Valitse nro 2)\n"
                        "tai haluatko lopeta? (Valitse nro 3): "))

print("Syötit nro 3! Ohjelma lopetetaan!")
