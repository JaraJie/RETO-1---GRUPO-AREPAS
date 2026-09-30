###############################################
#### Usuario                               ####
#### Autora: Maitane                       ####
###############################################

#usuario.py se hará cargo de todo lo que tiene que ver con los usuarios, ya sea iniciar sesion, crear cuenta,#
#o ver el perfil#

import os

def crear_cuenta():
    ruta_carpeta = os.path.dirname(__file__)
    ruta_usuarios = os.path.join(ruta_carpeta, "usuarios.txt")

    print("Rellene estos datos para crear su nueva cuenta: ")
    print("Introduzca su nombre")
    nombre_usuario_str = input()
    
    while True:
        print("Introduzca su cuenta de gmail: ")
        correo_usuario_str = input()
        archivo_usuarios = open(ruta_usuarios, "r")
        correos_iguales_bool = False
        for linea in archivo_usuarios:
            lista_datos_usuarios_guardados_str = linea.strip().split(",")
            correo_guardado_str  = lista_datos_usuarios_guardados_str[1]
            if correo_guardado_str == correo_usuario_str:
                correos_iguales_bool = True
                break
        
        archivo_usuarios.close()
        if not correos_iguales_bool:
            break
        print("Ese correo ya esta registrado. Introduzca otro correo no utilizado") 
      
    print("Introduzca su contraseña: ")
    contrasenia_usuario_str = input()
    
    archivo_usuarios = open(ruta_usuarios, "a")
    archivo_usuarios.write(nombre_usuario_str + "," + correo_usuario_str + "," + contrasenia_usuario_str + "\n")
    archivo_usuarios.close()
    
    print("Usuario registrado correctamente")
    
    
def iniciar_sesion():
    ruta_carpeta = os.path.dirname(__file__)
    ruta_usuarios = os.path.join(ruta_carpeta, "usuarios.txt")
    
    while True:
        print("Introduzca su correo electronico: ")
        correo_usuario_str = input()
        archivo_usuarios = open(ruta_usuarios, "r")
        existe_correo_bool = False
        for linea in archivo_usuarios:
            lista_datos_usuarios_guardados_str = linea.strip().split(",")
            correo_guardado_str = lista_datos_usuarios_guardados_str[1]
            if correo_usuario_str == correo_guardado_str:
                existe_correo_bool = True
                break
        archivo_usuarios.close()
        if existe_correo_bool == True:
            break
        else:
            print("No hay ninguna cuenta asociada a ese correo. Introduzca un correo registrado")
    
    while True:
        print("Introduzca la contraseña")
        contrasenia_usuario_str = input()
        if contrasenia_usuario_str == lista_datos_usuarios_guardados_str[2]:
            print("Contraseña correcta")
            break
        print("Contrasña incorrecta. Intentelo de nuevo")  
    print("Iniciando sesion...")