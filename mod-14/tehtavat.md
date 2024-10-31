```python
# Pysyvä assisiaatio 
# Koira ja hoitola

class Koira:
    koirien_lkm = 0  # staattinen luokkamuuttuja
    def __init__(self, nimi, syntymavuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.haukahdus = haukahdus
        Koira.koirien_lkm += 1  # kasvatetaan luokkamuuttujaa
        print(f"Koiria luotu: {Koira.koirien_lkm} kpl")  # tulostetaan koirien lkm

    def hauku(self, kerrat):
        for i in range(kerrat):  # toistetaan kerrat kertaa
            print(f"{self.nimi} haukuu {self.haukahdus}")

class Hoitola:
    def __init__(self):
        self.koirat = []  # luodaan lista koirille pysyvä assosiaatio

    def koira_sisaan(self, koira):
        self.koirat.append(koira)  # lisätään koira listaan
        print(f"{koira.nimi} kirjattu sisään")

    def koira_ulos(self, koira):
        self.koirat.remove(koira)  # poistetaan koira listasta
        print(f"{koira.nimi} kirjattu ulos")

    def tervehdi_koiria(self):
        for koira in self.koirat:  # käydään kaikki koirat läpi
            koira.hauku(1)

# Pääohjelma
print("-- Koiria luodaan --")
koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")
hoitola = Hoitola()
hoitola.koira_sisaan(koira1)
hoitola.koira_sisaan(koira2)
hoitola.tervehdi_koiria()
hoitola.koira_ulos(koira1)
hoitola.tervehdi_koiria()
```

```python
# Tilapäinen assosiaatio
# Auto ja maalaamo

class Auto:
    def __init__(self, rekisteritunnus, väri):
        self.rekisteritunnus = rekisteritunnus
        self.väri = väri
        
class Maalaamo:
    def maalaa(self, auto, väri):  
        # metodi muuttaa auton väriä
        auto.väri = väri  # muutetaan auton väriä

# Pääohjelma
maalaamo = Maalaamo()
auto = Auto("ABC-123", "sininen")
print("Auto on " + auto.väri)
maalaamo.maalaa(auto, "punainen")
print("Auto on nyt " + auto.väri)
```

```python
# Tilapäinen assosiaatio 
# Asiakas ja tuote sekä tilaus

class Asiakas:
    def __init__(self, nimi):
        self.nimi = nimi

    def tee_tilaus(self, tuote):
        print(f"{self.nimi} teki tilauksen tuotteelle {tuote.nimi}.")
         
class Tuote:
    def __init__(self, nimi, hinta):
        self.nimi = nimi
        self.hinta = hinta

# Luodaan asiakas ja tuote
asiakas1 = Asiakas("Matti")
tuote1 = Tuote("Kahvikuppi", 4.5)

# Asiakas tekee tilauksen tuotteesta
asiakas1.tee_tilaus(tuote1)
```

```python
# Staattinen luokkamuuttuja
# Tili ja maksu sekä saldo

class Tili:
    lkm = 0  # staattinen luokkamuuttuja
    def __init__(self, omistaja, saldo=0):  # oletussaldo on 0
        self.omistaja = omistaja
        self.saldo = saldo
        Tili.lkm += 1  # kasvatetaan luokkamuuttujaa
        print(f"Tilejä luotu: {Tili.lkm}")  
        # tulostetaan luokkamuuttuja

    def maksa(self, amount):
        if self.saldo >= amount:  # jos rahaa on tarpeeksi
            self.saldo -= amount  # vähennetään saldosta
            print("Maksu onnistui")
        else:
            print("Ei tarpeeksi rahaa")
        return

    def tulostus(self):
        print(f"Omistaja: {self.omistaja}, tilillä rahaa {self.saldo}")

# Pääohjelma
print("--- tilien luonti ---")
t1 = Tili("Jorma")
t2 = Tili("Anne", 100)

print("--- maksut ---")
t1.maksa(25)
t2.maksa(25)

print("--- tilien saldot ---")
t1.tulostus()
t2.tulostus()
```

```python
# Periytyminen
# Henkilö ja opiskelija

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def plot(self):  # metodi tulostaa nimen
        print(f"-- My name is {self.firstname} {self.lastname}")  
        # tulostetaan nimi

class Student(Person):  # Student perii Person-luokan
    def __init__(self, firstname, lastname, student_nr):
        super().__init__(firstname, lastname)  
        # kutsutaan yliluokan konstruktoria
        self.student_nr = student_nr  # lisätään opiskelijanumero

    def plot(self):  # metodi tulostaa nimen ja opiskelijanumeron
        super().plot()  # kutsutaan yliluokan metodia
        print(f"and my student number is {self.student_nr}")  
        # tulostetaan lisäksi opiskelijanumero

# Pääohjelma
p1 = Person("James", "Bond")
s1 = Student("Johnny", "English", 321)
p1.plot()
s1.plot()
```

```python
# Periytyminen 
# Työntekijä ja tuntipalkkainen sekä kuukausipalkkainen

class Tyontekija:
    tyontekijoiden_lkm = 0  # staattinen luokkamuuttuja
    def __init__(self, etunimi, sukunimi):
        Tyontekija.tyontekijoiden_lkm += 1  # kasvatetaan luokkamuuttujaa
        self.tyontekijanumero = Tyontekija.tyontekijoiden_lkm  
        # annetaan työntekijänumeroksi luokkamuuttujan arvo
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):  # tulostetaan työntekijän tiedot
        print(f"{self.tyontekijanumero}: {self.etunimi} {self.sukunimi}")

class Tuntipalkkainen(Tyontekija):
    def __init__(self, etunimi, sukunimi, tuntipalkka):
        super().__init__(etunimi, sukunimi) # kutsutaan yliluokan konstruktoria 
        self.tuntipalkka = tuntipalkka

    def tulosta_tiedot(self): 
        super().tulosta_tiedot()  # kutsutaan yliluokan metodia. 
        print(f" Tuntipalkka: {self.tuntipalkka}")  # lisätään tuntipalkka

class Kuukausipalkkainen(Tyontekija):
    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        super().__init__(etunimi, sukunimi)  # kutsutaan yliluokan konstruktoria 
        self.kuukausipalkka = kuukausipalkka  # lisätään kuukausipalkka

    def tulosta_tiedot(self):  
        super().tulosta_tiedot()  # kutsutaan yliluokan metodia. 
        print(f" Kuukausipalkka: {self.kuukausipalkka}")  # lisätään kuukausipalkka

# Pääohjelma
def kaikki_tyontekijat():
    tyontekijat = []
    tyontekijat.append(Tuntipalkkainen("Viivi", "Virta", 12.35))
    tyontekijat.append(Kuukausipalkkainen("Ahmed", "Habib", 2750))
    tyontekijat.append(Tyontekija("Pekka", "Puro"))
    tyontekijat.append(Tuntipalkkainen("Olga", "Glebova", 14.92))

    for t in tyontekijat:
        t.tulosta_tiedot()

kaikki_tyontekijat()
```

```python
## Moniperintä
# Kulkuneuvo ja urheiluväline sekä polkupyörä

class Kulkuneuvo:  # luokka Kulkuneuvo
    def __init__(self, nopeus):
        self.nopeus = nopeus

class Urheiluväline:  # luokka Urheiluväline
    def __init__(self, paino):
        self.paino = paino

class Polkupyörä(Kulkuneuvo, Urheiluväline):  
    # luokka Polkupyörä perii Kulkuneuvo ja Urheiluväline -luokat
    def __init__(self, nopeus, paino, vaihteet):  
        # konstruktori
        Kulkuneuvo.__init__(self, nopeus)  
        # kutsutaan yliluokkien konstruktoreita
        Urheiluväline.__init__(self, paino)  
        # kutsutaan yliluokkien konstruktoreita
        self.vaihteet = vaihteet  # lisätään vaihteet

# Pääohjelma
pp = Polkupyörä(45, 18.7, 3)
print (pp.vaihteet)
print (pp.nopeus)
print (pp.paino)
```

```python
# Rajapinta ja Flask

import json
import requests

hakusana = input("Anna hakusana: ")  # kysytään hakusana

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana  
# luodaan pyyntö

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:  # jos vastaus onnistui
        json_vastaus = vastaus.json()  
        # muutetaan vastaus json-muotoon
        print(json.dumps(json_vastaus, indent=2))  
        # tulostetaan vastaus json-muodossa
        for a in json_vastaus:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:  
    # virheenkäsittely jos pyyntö ei onnistu
    print ("Hakua ei voitu suorittaa.")
```

```python
# Rajapinta ja Flask

import requests
import json

hakusana = input("Anna hakusana: ")  # kysytään hakusana

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyynto = "https://api.tvmaze.com/search/shows?q=" + hakusana  
vastaus = requests.get(pyynto).json()  
# tehdään pyyntö ja muutetaan vastaus json-muotoon
print(vastaus)  # tulostetaan vastaus json-muodossa


hakusana = input("Anna hakusana: ")  # kysytään hakusana

respond = requests.get(f"https://api.tvmaze.com/search/shows?q={hakusana}")  
# tehdään pyyntö
respond = respond.json()  # muutetaan vastaus json-muotoon
print(respond)

# Tulostetaan vastauksen rakenne
print(json.dumps(vastaus, indent=2))  
# tulostetaan vastaus json-muodossa

# Tulostetaan vastauksen sisältö
for a in vastaus:
    print(a["show"]["name"])  # tulostetaan ohjelman nimi
```

```python
# Päätepiste (Endpoint) ja Flask

from flask import Flask, Response
import json

app = Flask(__name__)  # luodaan Flask-olio

@app.route('/summa/<luku1>/<luku2>')  
# määritellään reitti
def summa(luku1, luku2):
        luku1 = float(luku1)
        luku2 = float(luku2)
        summa = luku1 + luku2
        # summa = int(luku1) + int(luku2)

        vastaus = {
            "luku1": luku1,
            "luku2": luku2,
            "summa": summa
        }
        return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
```

```python
# Päätepiste (Endpoint) ja Flask 

from flask import Flask, request

app = Flask(__name__)  # luodaan Flask-olio

# 127.0.0.1:3000/summa?luku1=3&luku2=4  
# esimerkki pyynnöstä &-merkillä erotetut parametrit

@app.route('/summa')  
# määritellään reitti
def summa():
    args = request.args  
    # pyyntö parametrit args -sanakirjassa
    luku1 = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    summa = luku1 + luku2

    vastaus = {  # luodaan sanakirja vastaus
        "luku1" : luku1,
        "luku2" : luku2,
        "summa" : summa
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
```
