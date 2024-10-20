"""Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. Käytä seuravalla sivulla
esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti."""

import requests
import json

url = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(url)
    data = response.json()
    # print(json.dumps(data, indent=2))
    # print(data["id"])
    print(data["value"])
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
