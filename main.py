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
import subprocess, sys

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
    numero_linea_usuarios_int = crear_cuenta()
#Segunda Opcion: Inicio de sesion
else:
    #llama a la funcion de usuario.py y le ejecuta
    numero_linea_usuarios_int = iniciar_sesion()



#Tras iniciar sesion/crear cuenta, accedemos al menu principal de la app
numero_seleccion_int = -1

#El menu inicial se muestra hasta que el usuario inserte la opcion de Apagar la applicacion
while numero_seleccion_int != 0:
    
    #En el siguiente while, comprobamos que la opcion que elija el usuario sea valida
    numero_no_valido_bool = True
    while numero_no_valido_bool:
        #Opciones que hay por el momento. Añadir más si tenemos tiempo
        print("Elija una opción: ")
        print("0) Apagar app")
        print("1) Acceder a misiones ")
        print("2) Ver personaje")
    
        numero_seleccion_int = int(input())
        OPCION_MINIMA = 0
        OPCION_MAXIMA = 2
        #Comprobamos si la opcion es valida, si lo es cambia el booleano a false para poder salir del bucle
        if numero_seleccion_int >= OPCION_MINIMA and numero_seleccion_int <= OPCION_MAXIMA:
            numero_no_valido_bool = False
        else:
            print("Opcion no valida. Intentalo de nuevo")
    
    #Realizar la opcion elegida:
    if numero_seleccion_int == 0:
        print("Apagar aplicación seleccionado")
        continue
    elif numero_seleccion_int == 1:
        #Llamar a misiones.py (por hacer)
        subprocess.run([sys.executable, "misiones.py"])
    elif numero_seleccion_int == 2:
        #Llamar a usuario.py para ver el personaje (por hacer)
        continue
        
        
input("FIN")
