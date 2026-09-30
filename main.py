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

#comando para importar las funciones de crear_cuenta y iniciar_sesion de usuario.py
from usuario import crear_cuenta, iniciar_sesion

#Menu inicial donde Iniciaremos sesion o Crearemos una cuenta
print("Bienvenido a Skillia")

#usamos un bucle para que el usuario elija si o si una de las 2 opciones
while True:
    print("Elija una opción: ")
    print("1) Crear Cuenta")
    print("2) Iniciar Sesion")
    numero_seleccion_int = int(input())
    #si el numero introducido por el usuario esta asociado a una opcion, salimos del bucle. 
    #En caso contrario, permanecemos en el bucle hasta que el usuario de una opcion valida
    if numero_seleccion_int == 1 or numero_seleccion_int == 2:
        break
    print("Opcion no valida. Intentelo de nuevo")

#Primera Opcion: Crear una cuenta.
if numero_seleccion_int == 1:
    #llama y ejecuta la funcion definida en usuario.py
    crear_cuenta()
#Segunda Opcion: Inicio de sesion
else:
    #llama a la funcion de usuario.py y le ejecuta
    iniciar_sesion()
    
input()
