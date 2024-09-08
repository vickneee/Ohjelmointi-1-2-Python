"""
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
"""

# Latataan tarvittavat kirjastot
import mysql.connector


# Etsi lentokentät
def etsi_lentokentat(maakoodi):
    sql = f"SELECT type, COUNT(*) FROM airport WHERE iso_country='{maakoodi}' GROUP BY type"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Maassa {maakoodi} on {rivi[1]} kpl {rivi[0]}-tyyppisiä lentokenttiä")

    return tulos


# Yhdistetään tietokantaan
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database="flight_game",
    user='victoria',
    password='Metro',
    autocommit=True
)

# Kysy käyttäjältä maakoodi
syotetty_maakoodi = input("Anna maakoodi: ")
etsi_lentokentat(syotetty_maakoodi)

# Suljetaan yhteys
yhteys.close()
print("Yhteys suljettu")
