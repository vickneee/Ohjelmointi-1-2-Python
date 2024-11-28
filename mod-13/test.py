from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/summa')
def summa():
    try:
        args = request.args
        luku1 = float(args.get("luku1"))
        luku2 = float(args.get("luku2"))
        loppu_summa = luku1 + luku2

        vastaus = {
            "luku1": luku1,
            "luku2": luku2,
            "summa": loppu_summa
        }

        return jsonify(vastaus)
    except ValueError:
        return jsonify({"error": "Virheellinen yhteenlaskettava"}), 400


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
