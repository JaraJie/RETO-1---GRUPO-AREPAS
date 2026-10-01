###############################################
#### Usuario                               ####
#### Autora: Maitane                       ####
###############################################

#usuario.py se hará cargo de todo lo que tiene que ver con los usuarios, ya sea iniciar sesion, crear cuenta,#
#o ver el perfil (proximamente)#

#os es un modulo de Python, que permite trabajar con el Sistema Operativo (rutas, carpetas y archivos)
#En nuestro caso, lo usamos para encontrar la ruta de usuarios.txt para poder trabajar correctamente con el archivo
import os

#Aqui, definimos que hacen las funciones llamadas en main.py
def crear_cuenta():
    
    # __file__ contiene la ruta donde se encuentra usuario.py.
    # os.path.dirname() elimina el nombre del archivo y se queda solo con la carpeta.
    # De esta forma obtenemos automáticamente la carpeta del proyecto,
    # sin tener que escribir manualmente una ruta diferente para cada ordenador.
    ruta_carpeta = os.path.dirname(__file__)
    
    # Unimos la ruta de la carpeta con "usuarios.txt" para obtener la ruta completa del archivo
    ruta_usuarios = os.path.join(ruta_carpeta, "usuarios.txt")

    #Aqui ya comenzamos a trabajar con los datos para crear la cuenta
    print("Rellene estos datos para crear su nueva cuenta: ")
    print("Introduzca su nombre")
    nombre_usuario_str = input()
    
    #En este while, nos encargamos de que el correo no exista ya en otra cuenta
    while True:
        
        print("Introduzca su cuenta de gmail: ")
        correo_usuario_str = input()
        
        # Abrimos el archivo usuarios.txt en modo lectura (r) y lo guardamos en archivo_usuarios, para poder acceder al texto del archivo
        archivo_usuarios = open(ruta_usuarios, "r")
        correos_iguales_bool = False
        
        #en este for, recorremos todo el archivo linea por linea para comprobar si el correo ya esta asociado a una cuenta
        for linea in archivo_usuarios:
            # Eliminamos el salto de línea con strip() y separamos los datos por cada coma con split(","), guardamos esa linea modificada en formato lista
            #para acceder facilmente a los datos
            lista_datos_usuarios_guardados_str = linea.strip().split(",")
            
            #accedemos a la posicion donde esta guardado el correo y lo guardamos en una variable para compararlo en el siguiente if
            correo_guardado_str  = lista_datos_usuarios_guardados_str[1]
            
            #Si el correo existe, cambiamos de valor al booleano y salimos del bucle for, ya que no hay que buscar mas
            #En caso de que no haya sido encontrado, seguimos en el bucle for hasta que terminemos de comprobar todas las lineas
            if correo_guardado_str == correo_usuario_str:
                correos_iguales_bool = True
                break
                
        #Al trabajar con archivos en python, es muy importante cerrar el archivo de texto tras su uso. Para ello usamos el .close()
        archivo_usuarios.close()
        
        #Si no hemos encontrado el correo en todo el for, salimos del bucle while, ya que es un correo valido
        if not correos_iguales_bool:
            break
        
        #En este caso, como no es un correo valido, volvemos al inicio del while
        print("Ese correo ya esta registrado. Introduzca otro correo no utilizado") 
    
    #continuamos pidiendole al usuario que introduzca la contraseña nueva que va a crear en su cuenta
    print("Introduzca su contraseña nueva: ")
    contrasenia_usuario_str = input()
    
    #Una vez tenemos ya todos los datos validos, vamos a calcular en que linea se va a guardar el nuevo usuario
    #Para ello, volvemos a abrir usuarios.txt en modo lectura "r"
    archivo_usuarios = open(ruta_usuarios, "r")
    #Guardamos en una variable, la cantidad de lineas que hay en usuarios.txt
    lineas_archivo_int = archivo_usuarios.readlines()
    #Y como siempre que tratamos con archivos, cerramos al terminar
    archivo_usuarios.close()
    #Guardamos en una nueva variable, en que linea se va a escribir el nuevo usuario, para devolverla al main
    #De esta forma, nos será más facil acceder a los datos del usuario.
    linea_usuario_int = len(lineas_archivo_int)
    
    #Una vez tenemos ya todos los datos, podemos escribir los datos en el archivo de texto
    #Abrimos usuarios.txt en modo añadir ("a") para agregar un nuevo usuario al final del fichero (sin borrar los anteriores)
    archivo_usuarios = open(ruta_usuarios, "a")
    
    # Escribimos los datos del nuevo usuario separados por comas y añadimos un salto de línea al final
    archivo_usuarios.write(nombre_usuario_str + "," + correo_usuario_str + "," + contrasenia_usuario_str + "\n")
    
    # Cerramos el archivo una vez terminamos de escribir en él
    archivo_usuarios.close()

    print("Usuario registrado correctamente")
    #Devolvemos a main el dato de la linea donde se ha guardado usuario en el txt
    return linea_usuario_int
#Fin de la funcion crear usuario
    
 

#Funcion Iniciar Sesion 
def iniciar_sesion():
    
    #Como esta explicado en crear cuenta, usamos estas 2 primeras lineas para buscar la ruta del archivo para poder acceder a usuarios.txt
    ruta_carpeta = os.path.dirname(__file__)
    ruta_usuarios = os.path.join(ruta_carpeta, "usuarios.txt")
    
    #Comprobamos en el while si el correo ya existe en usuarios.txt para poder iniciar sesion
    while True:
        
        print("Introduzca su correo electronico: ")
        correo_usuario_str = input()
        
        #Abrimos el archivo de texto en modo lectura (r)
        archivo_usuarios = open(ruta_usuarios, "r")
        existe_correo_bool = False

        linea_usuario_int = 0
        #En el for, miramos linea por linea en el archivo si el correo ya existe. Similar a como hemos hecho en crear cuenta
        for linea in archivo_usuarios:
            lista_datos_usuarios_guardados_str = linea.strip().split(",")
            correo_guardado_str = lista_datos_usuarios_guardados_str[1]
            if correo_usuario_str == correo_guardado_str:
                existe_correo_bool = True
                break
            linea_usuario_int += 1
        
        #Cerramos el archivo de texto tras la lectura
        archivo_usuarios.close()
        
        #Si el correo ya esta asociado a una cuenta, salimos del while
        if existe_correo_bool == True:
            break
        #Si el correo no existe, volvemos al inicio del bucle while para pedir que introduzca un correo valido qu eya exista
        print("No hay ninguna cuenta asociada a ese correo. Introduzca un correo registrado")
    
    #Tras tener el correo, comprobamos si la contraseña que nos dice el usuario es la correcta
    while True:
        
        print("Introduzca la contraseña")
        contrasenia_usuario_str = input()
        
        #Comprobamos si ambas contraseñas son iguale, la que el usuario nos acaba de decir con la que esta guardada en usuarios.txt
        #Como ya tenemos la lista de datos correcta del while y for anterior, podemos acceder a ella mediante la variable lista_datos_usuarios_guardados_str
        #en la posicion 2, que es la que guarda la contraseña
        if contrasenia_usuario_str == lista_datos_usuarios_guardados_str[2]:
            print("Contraseña correcta")
            break
        
        #En caso de fallar la contraseña, se vuelve al inicio del bucle while
        print("Contrasña incorrecta. Intentelo de nuevo")

    #Hemos comprobado que el inicio de sesion ha sido correcto, por lo que ya hemos terminado la funcion iniciar sesion
    print("Iniciando sesion...")
    return linea_usuario_int
    
#Fin de la funcion inciar sesion