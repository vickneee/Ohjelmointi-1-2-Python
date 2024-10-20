"""Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. Käytä seuravalla sivulla
esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti."""

# Importoidaan tarvittavat kirjastot.
import requests
# import json

# Chuck Norris API.
url = "https://api.chucknorris.io/jokes/random"

# Kokeillaan hakea Chuck Norris -vitsi.
try:
    # Kysely, jolla haetaan satunnainen vitsi. Parametrit: ei ole.
    response = requests.get(url)
    # Tiedot saadaan JSON-muodossa.
    data = response.json()

    # Tulostetaan JSON-muotoiset tiedot.
    # print(json.dumps(data, indent=2))

    # Tulostetaan vitsi.
    print(data["value"])

# Virheenkäsittely
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
