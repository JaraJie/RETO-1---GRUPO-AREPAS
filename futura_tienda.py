import os

def cargar_tienda(linea_usuario_int)

    #Buscamos la dirección donde se encuentra usuarios.txt
    ruta_carpeta = os.path.dirname(__file__)
    ruta_usuarios = os.path.join(ruta_carpeta, "usuarios.txt")
    #Abrimos el archivo en modo lectura
    archivo_usuarios = open(ruta_usuarios, "r")
    #Guardamos todas las lineas en una lista de lineas usuarios
    lineas_usuarios = archivo_usuarios.readlines()
    #Tras leer y guardar todas las lineas, cerramos el archivo
    archivo_usuarios.close()
    #Guardamos solo la informacion de la linea donde se encuentra el usuario
    datos_usuario = lineas_usuarios[linea_usuario_int].strip().split(",")
    #Guardamos solo el dato de las monedas que tiene el usuario
    monedas_usuario_str = datos_usuario[3]

    print()
    print("              ⚜ MERCADO DE AVENTUREROS ⚜")
    print()
    print("        ✦ Los objetos de hoy ✦")
    print()
    print("    > 01 🧪  Poción de Vida")
    print("        « Una pequeña ayuda para seguir luchando »")
    print("        🪙 20 monedas")
    print()
    print("    > 02 ⚔️  Espada del Guerrero")
    print("        « El acero habla por quien sabe usarlo »")
    print("        🪙 200 monedas")
    print()
    print("    > 03 🛡️  Escudo del Guardián")
    print("        « Ningún golpe atravesará esta defensa »")
    print("        🪙 150 monedas")
    print()
    print("    > 04 🥾  Botas del Explorador")
    print("        « El camino no tendrá secretos »")
    print("        🪙 100 monedas")
    print()
    print()
    print("              ✦ ✧ ✦ MASCOTAS FANTASÍA ✦ ✧ ✦")
    print("        ✦ 💡 Las mascotas pueden acompañarte durante tus aventuras. ✦")
    print()
    print("    > 05 🐉  Dragón Bebé")
    print("        « Una criatura de poder legendario »")
    print("        🪙 500 monedas")
    print()
    print("    > 06 🦄  Unicornio")
    print("        « Una criatura mágica nacida de las estrellas »")
    print("        🪙 450 monedas")
    print()
    print("    > 07 🐈‍⬛✨  Gato Mágico")
    print("        « Una criatura misteriosa que trae buena fortuna »")
    print("        🪙 400 monedas")
    print()
    print()
    print("        💰 Monedas Totales: ", monedas_usuario_str)
    print("        ❯ ¿Qué deseas comprar?")