# Connect to the database

import mysql.connector


# Versio 1, tarvespesifi aliohjelma
def maakoodi(nimi):
    sql = f"SELECT iso_country, continent FROM country where name='{nimi}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Maan {nimi} iso_koodi on {rivi[0]} ja maa sijaitsee {rivi[1]}-ssa")
    return


# Versio 2, geneerinen aliohjelma
def tietokantahaku(sql):
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database="flight_game",
    user='victoria',
    password='Metro',
    autocommit=True
)

# Versio 1, jossa jokaista maata haetaan erikseen alihojelmalla
maa = input("Anna maa nimi: ")
maakoodi(maa)

# Versio 2, jossa käytetään genereetista aliohjelmaa
sql = f"SELECT iso_country, continent FROM country where name='{maa}'"
tulos = tietokantahaku(sql)
for rivi in tulos:
    print(f"Maan {maa} iso_koodi on {rivi[0]} ja maa sijaitsee {rivi[1]}-ssa")

# Suljetaan yhteys
yhteys.close()
print("Yhteys suljettu")
