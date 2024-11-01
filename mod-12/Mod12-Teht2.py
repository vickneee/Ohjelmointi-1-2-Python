"""Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, joka kysyy
käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy
rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä
tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi."""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

# OpenWeather API.
url = "https://api.openweathermap.org/data/2.5/weather"
# API key
api_key = os.getenv("API_KEY")


def get_weather(city):
    try:
        response = requests.get(url, params={"q": city, "appid": api_key, "units": "metric", "lang": "fi"})
        data = response.json()
        print(f"Sää paikkakunnalla {city}: {data['weather'][0]['description']}")
        print(f"Lämpötila: {data['main']['temp']}°C")
    except requests.exceptions.RequestException as e:
        print(f"Hakua ei voitu suorittaa.\n{e}")


# Pääohjelma
def main():
    city = input("Anna paikkakunnan nimi: ")
    get_weather(city)


if __name__ == "__main__":
    main()
