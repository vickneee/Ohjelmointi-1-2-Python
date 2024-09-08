"""
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
Laske etäisyys geopy-kirjaston avulla:
"""

# Lataa tarvittavat kirjastot
import mysql.connector
from geopy.distance import geodesic


# Etsi lentoasema
def etsi_lentoasema(icao):
    sql = f"SELECT name, latitude_deg, longitude_deg FROM airport where ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentoasema {icao} on {rivi[0]} ja sijaitsee koordinaateissa {rivi[1]} {rivi[2]}")
    return tulos


# Kysy käyttäjältä ICAO-koodi
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database="flight_game",
    user='victoria',
    password='Metro',
    autocommit=True
)

icao1 = input("Anna ensimmäisen lentoaseman ICAO-koodi: ")
icao2 = input("Anna toisen lentoaseman ICAO-koodi: ")

lentoasema1 = etsi_lentoasema(icao1)
lentoasema2 = etsi_lentoasema(icao2)

if len(lentoasema1) > 0 and len(lentoasema2) > 0:
    koord1 = (lentoasema1[0][1], lentoasema1[0][2])
    koord2 = (lentoasema2[0][1], lentoasema2[0][2])
    etaisyys = geodesic(koord1, koord2).kilometers
    print(f"Lentoasemien {icao1} ja {icao2} etäisyys on {etaisyys} km")

# Suljetaan yhteys
yhteys.close()
print("Yhteys suljettu")
