import requests
import json

hakusana = input("Anna hakusana: ")

try:
    response = requests.get("https://api.tvmaze.com/search/shows?q=" + hakusana)
    data = response.json()
    # print(json.dumps(data, indent=2))
    # print(data)
    for sarja in data:
        print(sarja["show"]["name"])

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
