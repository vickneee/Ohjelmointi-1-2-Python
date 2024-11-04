"""Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. Hyödynnä toteutuksessa
aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa:
http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}."""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/alkuluku/<value>')
def is_prime_route(value):
    try:
        number = int(value)
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

    if is_prime(number):
        return {"Number": number, "isPrime": True}
    else:
        return {"Number": number, "isPrime": False}


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
