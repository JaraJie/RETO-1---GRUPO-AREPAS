from datetime import date
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


# =========================================================
# CATÁLOGO DE EQUIPAMIENTO
# =========================================================
SLOTS = [
    {"id": "arma",     "nombre": "Arma",     "icono": "🗡️"},
    {"id": "casco",    "nombre": "Casco",    "icono": "🪖"},
    {"id": "armadura", "nombre": "Armadura", "icono": "🥋"},
    {"id": "escudo",   "nombre": "Escudo",   "icono": "🛡️"},
    {"id": "anillo",   "nombre": "Anillo",   "icono": "💍"},
    {"id": "botas",    "nombre": "Botas",    "icono": "🥾"},
    {"id": "guantes",  "nombre": "Guantes",  "icono": "🧤"},
    {"id": "amuleto",  "nombre": "Amuleto",  "icono": "📿"},
]


def _item(id, slot, nombre, icono, precio, rareza, **bonus):
    # bonus posibles: ataque, defensa, vida, robo de vida
    return {"id": id, "slot": slot, "nombre": nombre, "icono": icono,
            "precio": precio, "rareza": rareza, "bonus": bonus}


ITEMS = {i["id"]: i for i in [
    # Armas
    _item("madera",     "arma", "Espada de madera",    "🪵", 0,    "comun",      ataque=10),
    _item("hierro",     "arma", "Espada de hierro",    "🗡️", 100,  "comun",      ataque=20),
    _item("acero",      "arma", "Espada de acero",     "⚔️", 300,  "raro",       ataque=35),
    _item("caballero",  "arma", "Espada de caballero", "⚜️", 700,  "epico",      ataque=55),
    _item("legendaria", "arma", "Espada legendaria",   "✨", 1500, "legendario", ataque=90),
    # Cascos
    _item("casco_cuero",  "casco", "Casco de cuero",  "🪖", 60,  "comun", defensa=1, vida=10),
    _item("casco_hierro", "casco", "Casco de hierro", "🪖", 200, "raro",  defensa=3, vida=20),
    _item("casco_acero",  "casco", "Casco de acero",  "🪖", 500, "epico", defensa=6, vida=35),
    # Armaduras
    _item("peto_cuero", "armadura", "Armadura de cuero", "🥋", 100, "comun", defensa=2, vida=20),
    _item("cota_malla", "armadura", "Cota de malla",     "🥋", 350, "raro",  defensa=5, vida=40),
    _item("peto_acero", "armadura", "Armadura de acero", "🥋", 800, "epico", defensa=9, vida=70),
    # Escudos
    _item("escudo_madera", "escudo", "Escudo de madera", "🛡️", 80,  "comun", defensa=2),
    _item("escudo_hierro", "escudo", "Escudo de hierro", "🛡️", 300, "raro",  defensa=5),
    _item("escudo_torre",  "escudo", "Escudo torre",     "🛡️", 900, "epico", defensa=10),
    # Anillos
    _item("anillo_cobre", "anillo", "Anillo de cobre", "💍", 120,  "comun",      robo_vida=5),
    _item("anillo_plata", "anillo", "Anillo de plata", "💍", 400,  "raro",       robo_vida=12),
    _item("anillo_oro",   "anillo", "Anillo de oro",   "💍", 1000, "legendario", robo_vida=25),
    # Botas
    _item("botas_cuero",  "botas", "Botas de cuero",   "🥾", 90,  "comun", defensa=10),
    _item("botas_hierro", "botas", "Botas de hierro",  "🥾", 300, "raro",  defensa=20),
    _item("botas_viento", "botas", "Botas del viento", "🥾", 800, "epico", defensa=35),
    # Guantes
    _item("guantes_cuero",  "guantes", "Guantes de cuero",   "🧤", 80,  "comun", defensa=3),
    _item("guantes_hierro", "guantes", "Guantes de hierro",  "🧤", 300, "raro",  defensa=6,),
    _item("guantes_dragon", "guantes", "Guantes de dragón",  "🧤", 900, "epico", defensa=12,),
    # Amuletos
    _item("amuleto_vida",   "amuleto", "Amuleto de vida",      "📿", 200,  "raro",       vida=30),
    _item("amuleto_vampirico", "amuleto", "Amuleto vampirico", "📿", 500,  "epico",      robo_vida=20),
    _item("amuleto_dragon", "amuleto", "Amuleto del dragón",   "📿", 1200, "legendario", vida=60, robo_vida=10),
]}


# =========================================================
# DATOS INICIALES DEL JUEGO
# =========================================================
jugador = {
    "vida": 100,
    "vida_maxima": 100,
    "daño": 10,
    "defensa": 0,
    "robo_vida": 0,
    "oro": 0,
    "oleada": 1,
    "record": 1,
    "arma": "Espada de madera",
    "game_over": False,
    "inventario": ["madera"],
    "equipado": {s["id"]: None for s in SLOTS},
}
jugador["equipado"]["arma"] = "madera"

VIDA_BASE = 100


def recalcular():
    """Calcula las estadísticas a partir del equipamiento puesto."""
    total = {"ataque": 0, "defensa": 0, "vida": 0, "robo_vida": 0}

    for item_id in jugador["equipado"].values():
        if item_id:
            for clave, valor in ITEMS[item_id]["bonus"].items():
                total[clave] += valor

    jugador["daño"] = total["ataque"]
    jugador["defensa"] = total["defensa"]
    jugador["robo_vida"] = total["robo_vida"]
    jugador["vida_maxima"] = VIDA_BASE + total["vida"]
    jugador["vida"] = min(jugador["vida"], jugador["vida_maxima"])

    arma = jugador["equipado"]["arma"]
    jugador["arma"] = ITEMS[arma]["nombre"] if arma else "Sin arma"


recalcular()


def estado_tienda(mensaje=None):
    items = [
        dict(
            it,
            comprado=it["id"] in jugador["inventario"],
            equipado=jugador["equipado"].get(it["slot"]) == it["id"],
        )
        for it in ITEMS.values()
    ]
    datos = {"slots": SLOTS, "items": items, "jugador": jugador}
    if mensaje:
        datos["mensaje"] = mensaje
    return datos


# PÁGINA PRINCIPAL
@app.route("/")
def index():
    # Cada vez que se abre la página empieza una partida nueva
    # (el oro, el récord y el equipamiento se conservan).
    jugador["vida"] = jugador["vida_maxima"]
    jugador["oleada"] = 1
    jugador["game_over"] = False
    return render_template("paginaWeb.html", jugador=jugador)


# OBTENER LOS DATOS DEL JUGADOR
@app.route("/api/jugador")
def obtener_jugador():
    return jsonify(jugador)


# REINICIAR LA PARTIDA
@app.route("/api/reiniciar", methods=["POST"])
def reiniciar():
    jugador["vida"] = jugador["vida_maxima"]
    jugador["oleada"] = 1
    jugador["game_over"] = False

    return jsonify({
        "mensaje": "Partida reiniciada",
        "jugador": jugador
    })


# SUBIR DE OLEADA
@app.route("/api/siguiente_oleada", methods=["POST"])
def siguiente_oleada():
    if jugador["game_over"]:
        return jsonify({"error": "La partida ha terminado"}), 400

    jugador["oleada"] += 1

    if jugador["oleada"] > jugador["record"]:
        jugador["record"] = jugador["oleada"]

    return jsonify(jugador)


# RECIBIR ORO
@app.route("/api/recompensa", methods=["POST"])
def recompensa():
    datos = request.get_json(silent=True) or {}
    try:
        oro = max(0, int(datos.get("oro", 0)))
    except (TypeError, ValueError):
        return jsonify({"error": "Datos no válidos"}), 400

    jugador["oro"] += oro

    return jsonify({
        "mensaje": "Recompensa recibida",
        "jugador": jugador
    })


# =========================================================
# MISIONES DIARIAS (el oro se consigue aquí, no matando enemigos)
# =========================================================
MISIONES = [
    {"id": "fruta",     "nombre": "Come una pieza de fruta",       "icono": "🍎", "oro": 30},
    {"id": "ejercicio", "nombre": "Haz 30 minutos de ejercicio",   "icono": "🏃", "oro": 100},
    {"id": "mates",     "nombre": "Resuelve 4 problemas de mates", "icono": "🧮", "oro": 80},
    {"id": "lectura",   "nombre": "Lee durante 20 minutos",        "icono": "📖", "oro": 70},
]

estado_misiones = {"fecha": str(date.today()), "completadas": set()}


def lista_misiones():
    # Las misiones se reinician cada día
    hoy = str(date.today())
    if estado_misiones["fecha"] != hoy:
        estado_misiones["fecha"] = hoy
        estado_misiones["completadas"].clear()

    return [
        dict(m, completada=m["id"] in estado_misiones["completadas"])
        for m in MISIONES
    ]


@app.route("/api/misiones")
def obtener_misiones():
    return jsonify(lista_misiones())


@app.route("/api/misiones/<mision_id>/completar", methods=["POST"])
def completar_mision(mision_id):
    lista_misiones()  # comprueba si hay que reiniciar el día

    mision = next((m for m in MISIONES if m["id"] == mision_id), None)

    if mision is None:
        return jsonify({"error": "Misión no encontrada"}), 404

    if mision_id in estado_misiones["completadas"]:
        return jsonify({"error": "Ya completaste esta misión hoy"}), 400

    estado_misiones["completadas"].add(mision_id)
    jugador["oro"] += mision["oro"]

    return jsonify({
        "mensaje": "¡Misión completada!",
        "mision": mision,
        "jugador": jugador,
        "misiones": lista_misiones()
    })


# =========================================================
# TIENDA Y EQUIPAMIENTO
# =========================================================
@app.route("/api/tienda")
def obtener_tienda():
    return jsonify(estado_tienda())


@app.route("/api/comprar/<item_id>", methods=["POST"])
def comprar(item_id):
    item = ITEMS.get(item_id)

    if item is None:
        return jsonify({"error": "Objeto no encontrado"}), 404

    if item_id in jugador["inventario"]:
        return jsonify({"error": "Ya tienes este objeto"}), 400

    if jugador["oro"] < item["precio"]:
        return jsonify({"error": "No tienes suficiente oro"}), 400

    jugador["oro"] -= item["precio"]
    jugador["inventario"].append(item_id)

    # Se equipa solo si el hueco está vacío o es mejor que lo que llevas
    actual = jugador["equipado"][item["slot"]]
    if actual is None or item["precio"] > ITEMS[actual]["precio"]:
        jugador["equipado"][item["slot"]] = item_id

    recalcular()
    return jsonify(estado_tienda("¡Has comprado: " + item["nombre"] + "!"))


@app.route("/api/equipar/<item_id>", methods=["POST"])
def equipar(item_id):
    item = ITEMS.get(item_id)

    if item is None:
        return jsonify({"error": "Objeto no encontrado"}), 404

    if item_id not in jugador["inventario"]:
        return jsonify({"error": "Aún no tienes este objeto"}), 400

    jugador["equipado"][item["slot"]] = item_id
    recalcular()
    return jsonify(estado_tienda("Equipado: " + item["nombre"]))


@app.route("/api/desequipar/<slot>", methods=["POST"])
def desequipar(slot):
    if slot not in jugador["equipado"]:
        return jsonify({"error": "Hueco no válido"}), 404

    if slot == "arma":
        return jsonify({"error": "Siempre necesitas un arma equipada"}), 400

    jugador["equipado"][slot] = None
    recalcular()
    return jsonify(estado_tienda("Objeto guardado en la mochila"))


if __name__ == "__main__":
    app.run(debug=True)
