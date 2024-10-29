import requests
# import json

hakusana = input("Anna hakusana: ")

try:
    response = requests.get("https://api.tvmaze.com/search/shows?q=" + hakusana)

    if response.status_code == 200:
        data = response.json()
        # print(json.dumps(data, indent=2))
        # print(data)

        for sarja in data:
            print(f"Name: {sarja["show"]["name"]}")
            # print(f"Language: {sarja["show"]["language"]}")
    else:
        print("Hakusanalla ei löytynyt sarjoja.")

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
