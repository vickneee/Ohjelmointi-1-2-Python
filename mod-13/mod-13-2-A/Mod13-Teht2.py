"""Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin
JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava
GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa: {"ICAO":"EFHK",
"Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}."""

from flask import Flask, jsonify
from db_functions import db_query

app = Flask(__name__)


@app.route('/kentta/<icao_koodi>')
def lentokentta(icao_koodi):
    try:
        sql = f"""  
            SELECT * FROM airport
            WHERE ident = %s
        """

        result = db_query(sql, (icao_koodi,))

        if not result:
            return jsonify({"error": "No such airport"}), 404

        airport = result[0]
        answer = jsonify({"ICAO": airport["ident"], "Name": airport["name"], "Municipality": airport["municipality"]})

        return answer

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
