###############################################
#### PANEL DE SELECCIÓN MISIONES           ####
#### AUTOR: Jara                           ####
###############################################

import random

print("★ MISIONES DISPONIBLES ★")
print("^_^ Elige tu próxima misión y prepárate para el desafío!")
print("[01] (๑•̀ㅂ•́)و FRUTI-QUEST")
print("[02] (>_<) EL RETO MATEMÁTICO")
print("[03] (ง'̀-'́)ง MODO ESTUDIO")
print("[04] (^_^)b MAESTRO DEL SABER")
print("[05] (ง •̀_•́)ง OPERACIÓN: CASA LIMPIA")
print("[06] (^_^)/ ENGLISH QUEST")
print("[07] ★ (¬‿¬) SPECIAL QUEST: NÚMERO MISTERIOSO ★")

while True:
    
    mision_selecionada_int = int(input())
    
    if 1 <= mision_selecionada_int <= 7:
        break
    else:
        
        print(">>> ERROR_404 <<<")
        print("(×_×) ¡MISIÓN NO ENCONTRADA!")
        print("La misión que buscas no existe...")
        print("(^_^) Prueba con otro número.")


###############################################
#### NÚMERO DE MISIÓN: 6                   ####
#### NOMBRE DE MISIÓN: ENGLISH QUEST       ####
#### AUTORA: Maitane                        ####
###############################################


if mision_selecionada_int == 6:
    
    #Visual misión
    print("╔════════════════════════════╗")
    print("   ★ MISIÓN 6 SELECCIONADA ★")
    print("     ENGLISH QUEST")
    print("╚════════════════════════════╝")
    
    #Explicación de en que consiste la misión
    print("El objetivo de este ejercicio es acertar la palabra en ingles mediante el ahorcado")
    print("Para adivinar la palabra secreta tendrás 5 intentos")
    
    #Variable principal y 2 listas con las palabras de la misión
    intentos_int = 5
    lista_palabras_ingles_str = ["apple", "house", "water", "book", "school", "friend", "bread", "cheese"]
    lista_palabras_castellano_str = ["manzana", "casa", "agua", "libro", "escuela", "amigo", "pan", "queso"]
    
    #Con el random.randint() creamos un numero aleatorio entre 0 y la longitud de la lista de palabras - 1
    #De esa forma, el programa elige una posicion al azar, la cual apunta a una palabra que guardamos en una variable tanto en español como en ingles
    posicion_random_int = random.randint(0, len(lista_palabras_ingles_str) - 1 )
    palabra_ingles_str = lista_palabras_ingles_str[posicion_random_int]
    palabra_castellano_str = lista_palabras_castellano_str[posicion_random_int]

    #creamos una lista con la misma cantidad de _ que letras tiene la palabra a 
    letras_palabra_int = len(palabra_ingles_str)
    palabra_ahorcado_str = []
    for i in range(letras_palabra_int):
        palabra_ahorcado_str.append("_")
    
    #creamos las ultimas variables guardando cuantas letras hemos acertado, y una lista con las letras que ya hemos mencionado (vacio por el momento)
    letras_acertadas_int = 0
    letras_usadas_str = []

    #Comienza el juego del Ahorcado
    #Mientras que se siga teniendo intentos, seguimos en el juego
    #Nota, hay otra condición para salir del bucle más adelante con un break
    while intentos_int > 0:
        
        #Printeamos la palabra a adivinar en español
        print("La palabra en español es: ", palabra_castellano_str)

        #Printeamos como va la palabra a adivinar, si se ha acertado alguna letra saldra en esa posicion, sino saldra _
        print(palabra_ahorcado_str)
        
        #Bucle para pedir que el usuario introduzca una nueva letra
        while True:
            
            print("Introduzca una letra: ")
            letra_usuario_str = input().lower()
            
            #En el caso de que esa letra aparezca en la lista letras_usadas (es decir, ya se haya dicho esa letra), 
            #el programa nos imprime que ya hemos dicho esa letra y continua en el bucle
            if letra_usuario_str in letras_usadas_str:
                print("Ya has dicho esa letra")
            
            #En el caso contrario (la letra no se ha dicho antes), salimos del bucle while
            else:
                break
        
        #Ahora necesitamos comprobar si esa letra esta en la palabra.
        #Para ello, creamos un boolean para poder comprobar si la letra aparece o no
        aciertos_bool = False
        
        #Por cada elemento de la lista, comprobamos si es la misma que ha introducido el usuario
        for i in range(letras_palabra_int):
            
            if palabra_ingles_str[i] == letra_usuario_str:
                #En el caso de que la letra aparezca, esa posicion en nuestra lista de ahorcado, se reemplaza la _ por dicha letra en la posicion correcta
                palabra_ahorcado_str[i] = palabra_ingles_str[i]
                #Marcamos que se ha encontrado minimo una vez esa letra en la palabra
                aciertos_bool = True
                #Y a la vez se suma una por cada letra que haya en la palabra oculta
                letras_acertadas_int += 1
        
        #Si no se ha encontrado esa letra en la palabra, nos muestra por pantalla que no esta, y nos resta un intento. En el caso contrario no pasa nada
        if aciertos_bool == False:
            print("La letra '", letra_usuario_str, "' no está en la palabra")
            intentos_int -= 1
        
        #En el caso de que se hayan acertado la misma cantidad de letras que hay en la palabra, salimos del While (del juego)
        if letras_acertadas_int == letras_palabra_int:
            break
            
        #Añadimos la letra usada a la lista de letras usadas
        letras_usadas_str.append(letra_usuario_str)
        #Volvemos al inicio del while
    
    #Fin del while principal (el juego del ahorcado como tal)
    
    #Si se ha salido del while, por haber acertado la palabra, nos enseña un mensaje de felicidades
    if letras_acertadas_int == letras_palabra_int:
        print("Felicidades, has acertado la palabra.")
    #En el caso contrario, se ha salido al quedarse sin intentos. Por lo que nos imprime un mensaje de que no se ha logrado acertar la palabra. Y nos enseña cual era la palabra
    else:
        print("No has logrado acertar la palabra.")
        print("La palabra era: ", palabra_ingles_str)

#Input final para que no se cierre el programa
input()