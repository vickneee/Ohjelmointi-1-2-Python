"""Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, joka kysyy
käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy
rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä
tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi."""

import os
# Importoidaan tarvittavat kirjastot.
import requests
from dotenv import load_dotenv
# import json

# Ladataan ympäristömuuttujat.
load_dotenv()

# OpenWeather API.
url = "https://api.openweathermap.org/data/2.5/weather"
# API key
api_key = os.getenv("API_KEY")

# Kysytään käyttäjältä paikkakunnan nimi.
city = input("Anna paikkakunnan nimi: ")

# Kokeillaan hakea säätila paikkakunnalta.
try:
    # https://openweathermap.org/api/geocoding-api  # q=London,uk, appid=api_key
    # https://openweathermap.org/current#data  # units=metric
    # Kyselyparametrit: q (query), appid (API key), units (yksiköt to metric, tämä on valinnainen)
    response = requests.get(url, params={"q": city, "appid": api_key, "units": "metric"})

    # Tiedot saadaan JSON-muodossa.
    data = response.json()

    # Tulostetaan JSON-muotoiset tiedot.
    # print(json.dumps(data, indent=2))

    # Tulostetaan säätila paikkakunnalla.
    print(f"Sää paikkakunnalla {city}: {data['weather'][0]['description']}")
    # Tulostetaan lämpötila Celsius-asteina.
    print(f"Lämpötila: {data['main']['temp']}°C")

    # Lisätehtävä: Tulosta myös paikkakunnan koordinaatit (latitude ja longitude).
    print(f"latitude: {data['coord']['lat']}")
    print(f"longitude: {data['coord']['lon']}")

# Virheenkäsittely.
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
