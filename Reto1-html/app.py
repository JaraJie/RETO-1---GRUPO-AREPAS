from flask import Flask, render_template, jsonify

app = Flask(__name__)


# Datos del jugador (el heroe)
jugador = {
    "vida_maxima": 100,
    "daño": 10,
    "defensa": 0,
    "robo_vida": 0,
    "oro": 0,
}


# Pagina principal
@app.route("/")
def index():
    return render_template("paginaWeb.html", jugador=jugador)


# Datos del jugador para el JavaScript de la pagina
@app.route("/api/jugador")
def obtener_jugador():
    return jsonify(jugador)


if __name__ == "__main__":
    app.run(debug=True)

