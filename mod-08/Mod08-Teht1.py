"""
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen
ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
"""

# Lataa tarvittavat kirjastot
import mysql.connector


# Etsi lentoasema
def etsi_lentoasema(icao):
    sql = f"SELECT name, municipality FROM airport where ident='{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentoasema {icao} on {rivi[0]} ja sijaitsee {rivi[1]}-ssa")
    return tulos


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database="flight_game",
    user='victoria',
    password='Metro',
    autocommit=True
)

# Kysy käyttäjältä ICAO-koodi
syotetty_icao = input("Anna lentoaseman ICAO-koodi: ")
etsi_lentoasema(syotetty_icao)


# Suljetaan yhteys
yhteys.close()
print("Yhteys suljettu")
