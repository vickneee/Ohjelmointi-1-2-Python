"""Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. Käytä seuravalla sivulla
esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti."""

# Importoidaan tarvittavat kirjastot.
import requests


# import json
def get_joke(url):

    try:
        response = requests.get(url)
        data = response.json()
        print(data["value"])

    except requests.exceptions.RequestException as e:
        print(f"Hakua ei voitu suorittaa.\n{e}")


def main():
    url = "https://api.chucknorris.io/jokes/random"
    get_joke(url)


if __name__ == "__main__":
    main()
