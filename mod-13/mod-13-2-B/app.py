from flask import Flask, jsonify, render_template, request
from db_functions import db_query
import folium

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        icao_koodi = request.form['icao_code']
        return lentokentta(icao_koodi)
    return render_template('result.html', airport=None if request.method == 'GET' else {})


def lentokentta(icao_koodi):
    try:
        sql = """  
            SELECT * FROM airport
            WHERE ident = %s
        """

        result = db_query(sql, (icao_koodi,))

        if not result:
            return render_template('result.html', error="Lentokenttää ei löytynyt", airport=None)

        airport = result[0]

        # Create a map centered at the airport with bounds set to the EU region
        m = folium.Map(location=[airport["latitude_deg"], airport["longitude_deg"]], zoom_start=10, max_bounds=True)

        m.fit_bounds([[34.5, -10.5], [71.0, 40.0]])  # Approximate bounds for the EU region

        folium.Marker(
            [airport["latitude_deg"], airport["longitude_deg"]],
            popup=airport["name"]
        ).add_to(m)

        # Generate the map HTML
        map_html = m._repr_html_()

        # Prepare data for the template
        airport_data = {
            "ICAO": airport["ident"],
            "Name": airport["name"],
            "Municipality": airport["municipality"],
            "Latitude": airport["latitude_deg"],
            "Longitude": airport["longitude_deg"],
            "Map": map_html
        }

        return render_template('result.html', airport=airport_data)

    except Exception as e:
        return render_template('result.html', error=str(e))


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5001, debug=True)
