from flask import Flask, render_template, request
from db_functions import db_query
import folium

app = Flask(__name__)

ICAO_CODES = ['----', 'EFHK', 'ENGM', 'EGLL', 'LFPG',
              'LEMD', 'EDDB', 'LIRF', 'LPPT', 'EIDW',
              'LOWW', 'LGAV', 'EBBR', 'ESSA', 'EPWA',
              'LHBP', 'LROP', 'LKPR', 'LYBE', 'BIKF', 'LBSF', 'UKBB']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        icao_koodi = request.form['icao_code']
        return lentokentta(icao_koodi)
    return render_template('result.html', airport=None, icao_codes=ICAO_CODES)


@app.route('/all_airports', methods=['GET'])
def all_airports():
    m = folium.Map(location=[54.5260, 15.2551], zoom_start=4)  # Centered in Europe
    m.fit_bounds([[38.0, -7.0], [65.0, 35.0]])

    for icao in ICAO_CODES:
        sql = "SELECT * FROM airport WHERE ident = %s"
        result = db_query(sql, (icao,))
        if result:
            airport = result[0]
            folium.Marker(location=[airport["latitude_deg"], airport["longitude_deg"]], popup=airport["name"]).add_to(m)

    map_html = m._repr_html_()
    return render_template('all_airports.html', map_html=map_html)


def lentokentta(icao_koodi):
    try:
        sql = "SELECT * FROM airport WHERE ident = %s"
        result = db_query(sql, (icao_koodi,))

        if not result:
            return render_template('result.html', error="Lentokenttää ei löytynyt", airport=None, icao_codes=ICAO_CODES)

        airport = result[0]

        m = folium.Map(location=[airport["latitude_deg"], airport["longitude_deg"]], zoom_start=10, max_bounds=True)
        m.fit_bounds([[34.5, -10.5], [71.0, 40.0]])

        folium.Marker([airport["latitude_deg"], airport["longitude_deg"]], popup=airport["name"]).add_to(m)

        map_html = m._repr_html_()

        airport_data = {"ICAO": airport["ident"], "Name": airport["name"], "Municipality": airport["municipality"],
                        "Latitude": airport["latitude_deg"], "Longitude": airport["longitude_deg"], "Map": map_html}

        return render_template('result.html', airport=airport_data, icao_codes=ICAO_CODES)

    except Exception as e:
        return render_template('result.html', error=str(e), airport=None, icao_codes=ICAO_CODES)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5001, debug=True)
