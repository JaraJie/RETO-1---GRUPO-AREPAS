from datetime import date


# =========================================================
# MISIONES DIARIAS
# Para añadir una misión nueva, copia una línea y cambia los datos.
# =========================================================
MISIONES = [
    {"id": "fruta",     "nombre": "Come una pieza de fruta",       "icono": "🍎", "oro": 30},
    {"id": "ejercicio", "nombre": "Haz 30 minutos de ejercicio",   "icono": "🏃", "oro": 100},
    {"id": "mates",     "nombre": "Resuelve 4 problemas de mates", "icono": "🧮", "oro": 80},
    {"id": "lectura",   "nombre": "Lee durante 20 minutos",        "icono": "📖", "oro": 70},
]

# Aquí se guarda qué misiones has hecho hoy
estado_misiones = {"fecha": str(date.today()), "completadas": set()}


def lista_misiones():
    # Las misiones se reinician cada dia
    hoy = str(date.today())
    if estado_misiones["fecha"] != hoy:
        estado_misiones["fecha"] = hoy
        estado_misiones["completadas"].clear()

    return [
        dict(m, completada=m["id"] in estado_misiones["completadas"])
        for m in MISIONES
    ]