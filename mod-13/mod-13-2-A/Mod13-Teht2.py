"""Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin
JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava
GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa: {"ICAO":"EFHK",
"Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}."""

# Import necessary libraries
from flask import Flask, jsonify

from db_functions import db_query

# Create Flask app
app = Flask(__name__)


# Define route for lentokentta function
@app.route('/kentta/<icao_koodi>')
# Function to get airport information in route /kentta/<icao_koodi>
def lentokentta(icao_koodi):
    # Get airport information from database
    try:
        # Query to get airport information
        sql = f"""  
            SELECT * FROM airport
            WHERE ident = %s
        """

        result = db_query(sql, (icao_koodi,))
        # print(result)

        if not result:
            return jsonify({"error": "No such airport"}), 404

        # Airport information
        airport = result[0]
        answer = jsonify({"ICAO": airport["ident"], "Name": airport["name"], "Municipality": airport["municipality"]})

        # Return airport information
        return answer

    # Handle exceptions
    except ValueError as e:
        # Return error message
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Return error message
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
