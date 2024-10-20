"""Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. Hyödynnä toteutuksessa
aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa:
http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}."""

# Import necessary libraries
from flask import Flask, jsonify
from flask import request

# Create Flask app
app = Flask(__name__)


# Define route for is_prime function
@app.route('/alkuluku/<value>')
# Function to check if number is prime in route /alkuluku/<value>
def is_prime_route(value):
    try:
        n = int(value)
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

    if is_prime(n):
        return {"Number": n, "isPrime": True}
    else:
        return {"Number": n, "isPrime": False}


# Function to check if number is prime
def is_prime(n):
    # Check if input is integer and prime
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Run the app
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
