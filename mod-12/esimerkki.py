import requests


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
