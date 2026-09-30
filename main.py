###############################################
#### MAIN                                  ####
#### Autora: Maitane                       ####
###############################################

# Explicación de que va a consistir main.py #
# En el main.py vamos a desarrollar el menu principal y dependiendo de que elección elija el usuario el main.py va #
# a llamar a los demás programas. Primero cargará la primera pantalla donde se podrá Iniciar Sesion o crear una #
# cuenta. Tras ello, se abrirá el menu, y el usuario podrá elegir entre: Ver misiones, Ver Progreso, Ver Personaje #
# o salir del programa. Al elegir cualquier opcion de las primeras, menos la de salir, en principio el programa #
# abrirá otro archivo python, donde estará el codigo de dicha acción #

from usuario import crear_cuenta, iniciar_sesion

print("Bienvenido a Skillia")
while True:
    print("Elija una opción: ")
    print("1) Crear Cuenta")
    print("2) Iniciar Sesion")
    numero_seleccion_int = int(input())
    if numero_seleccion_int == 1 or numero_seleccion_int == 2:
        break
    print("Opcion no valida. Intentelo de nuevo")

if numero_seleccion_int == 1:
    crear_cuenta()
else:
    iniciar_sesion()
    
input()
