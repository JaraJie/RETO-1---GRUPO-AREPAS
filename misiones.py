import random

###############################################
#### PANEL DE SELECCIÓN MISIONES           ####
#### AUTOR: Jara                           ####
###############################################

#Jara: esta parte es simplemente el menú visual para que el usuario pueda ver las opciones disponibles#
print("★ MISIONES DISPONIBLES ★")
print("^_^ Elige tu próxima misión y prepárate para el desafío!")
print("[01] (๑•̀ㅂ•́)و FRUTI-QUEST")
print("[02] (>_<) EL RETO MATEMÁTICO")
print("[03] (ง'̀-'́)ง MODO ESTUDIO")
print("[04] (^_^)b MAESTRO DEL SABER")
print("[05] (ง •̀_•́)ง OPERACIÓN: CASA LIMPIA")
print("[06] (^_^)/ ENGLISH QUEST")
print("[07] ★ (¬‿¬) SPECIAL QUEST: NÚMERO MISTERIOSO ★")

#Jara: esta parte la he hecho para que el usuario introduzca un numero valido del menú y si no es valido entre un bucle con el siguiente mensaje#
while True:
    
    mision_selecionada_int = int(input())
    
    if 1 <= mision_selecionada_int <= 7:
        break
    else:
        
        print(">>> ERROR_404 <<<")
        print("(×_×) ¡MISIÓN NO ENCONTRADA!")
        print("La misión que buscas no existe...")
        print("(^_^) Prueba con otro número.")

#Jara: hice una plantilla para cuando selecciones la misión aparezca lo siguiente#
#if mision_selecionada_int == NÚMERO DE MISIÓN:#
    #print("╔════════════════════════════╗")#
    #print("   ★ MISIÓN SELECCIONADA ★")#
    #print("     #NOMBRE DE LA MISIÓN#")#
    #print("╚════════════════════════════╝")#




#AQUÍ HAY QUE MERGEAR#


###############################################
#### NÚMERO DE MISIÓN: __1_____             ####
#### NOMBRE DE MISIÓN: ___FRUTI-QUEST   ####
#### AUTOR: ___Mikel______________              ####
###############################################

if mision_selecionada_int == 1:
    print("╔════════════════════════════╗")
    print("   ★ MISIÓN SELECCIONADA ★")
    print("  [01] (๑•̀ㅂ•́)و FRUTI-QUEST")
    print("╚════════════════════════════╝")
    
    print('Come 5 frutas al día para conseguir monedas hasta 50 monedas!')
    frutas_int = int(input('¿Cuántas frutas has comido hoy?: '))
    
    #He usado los if, junto con las demás condiciones elif y else, para conectar cada cantidad de fruta con su premio de oro correspondiente

if frutas_int >= 5:
    print('Has ganado 50 oro')
elif frutas_int == 4:
    print('Has ganado 40 oro')
elif frutas_int == 3:
    print('Has ganado 30 oro')
elif frutas_int == 2:
    print('Has ganado 20 oro')
elif frutas_int == 1:
    print('Has ganado 10 oro')                         
else:
    print('Has ganado 0 oro')  #Este código utiliza la entrada de datos para recoger la cantidad, estructuras 
# condicionales para evaluar el valor y comandos de salida para mostrar la recompensa.


#MERGEAR#



###############################################
#### NÚMERO DE MISIÓN: 2                   ####
#### NOMBRE DE MISIÓN: EL RETO MATEMÁTICO  ####
#### AUTOR: Jara                           ####
###############################################

if mision_selecionada_int == 2:
    
    print()
    
    print("╔════════════════════════════╗")
    print("   ★ MISIÓN SELECCIONADA ★")
    print("  (>_<) EL RETO MATEMÁTICO")
    print("╚════════════════════════════╝")
    
    print()
    
    #Jara: Breve explicación de en que consiste la misión para el usuario#
    print('◆ Misión:')
    print('   Resuelve 5 operaciones.')
    print('◆ Puntuación:')
    print('   ✓ Cada acierto = +1 punto')
    print('   🪙 Cada punto = +10 oro')
    print('◆ Máximo:')
    print('   ★ 5 puntos = 50 🪙 oro')
    print()
    print('⚠ ¡Cuidado! Tienes un número limitado de intentos.')
    
    print()
    
    #aquí empieza el primer ejercicio#
    #variables#
    contador_int = 0
    respuesta1_bool = False
    
    while contador_int < 3: #Jara: esta parte sirve para que el usuario tenga hasta 3 posibles intentos#
        
        respuesta1_int = int(input('6 x 7 = '))
        
        if respuesta1_int == 42: #Jara: si la respuesta que da es 42, la respuesta será correcta y se guardara como 1)
            respuesta1_bool = True
            print("★ (^_^) ¡CORRECTO! +10 🪙 ★")
            break
        
        else: #Jara: si la respuesta no es correcta, al contador se le suma 1#
            contador_int = contador_int + 1
            print("✗ (╥﹏╥) ¡INCORRECTO! ★")
            
        if contador_int == 3: #Jara: Esta parte es para que cuando se quede sin intentos aparezca el siguiente mensaje#
            print("(×_×) ¡OH, NO! No has conseguido 🪙 monedas en este ejercicio.")
            
    
    #aquí empieza el seguundo ejercicio#
    print()
    contador_int = 0
    respuesta2_bool = False
    
    while contador_int < 3:
        
        respuesta2_int = int(input('64 / 8 = '))
        
        if respuesta2_int == 8:
            respuesta2_bool = True
            print("★ (^_^) ¡CORRECTO! +10 🪙 ★")
            break
        
        else:
            contador_int = contador_int + 1
            print("✗ (╥﹏╥) ¡INCORRECTO! ★")
            
        if contador_int == 3:
            print("(×_×) ¡OH, NO! No has conseguido 🪙 monedas en este ejercicio.")
    
     #aquí empieza el tercer ejercicio#
    print()
    contador_int = 0
    respuesta3_bool = False
    
    while contador_int < 3:
        
        respuesta3_int = int(input('7 x 8 = '))
        
        if respuesta3_int == 56:
            respuesta3_bool = True
            print("★ (^_^) ¡CORRECTO! +10 🪙 ★")
            break
        
        else:
            contador_int = contador_int + 1
            print("✗ (╥﹏╥) ¡INCORRECTO! ★")
            
        if contador_int == 3:
            print("(×_×) ¡OH, NO! No has conseguido 🪙 monedas en este ejercicio.")
    
    #aquí empieza el cuarto ejercicio#
    print()
    contador_int = 0
    respuesta4_bool = False
    
    while contador_int < 3:
        
        respuesta4_int = int(input('6 + 7 = '))
        
        if respuesta4_int == 13:
            respuesta4_bool = True
            print("★ (^_^) ¡CORRECTO! +10 🪙 ★")
            break
        
        else:
            contador_int = contador_int + 1
            print("✗ (╥﹏╥) ¡INCORRECTO! ★")
            
        if contador_int == 3:
            print("(×_×) ¡OH, NO! No has conseguido 🪙 monedas en este ejercicio.")
    
    #aquí empieza el quinto ejercicio#
    print()
    contador_int = 0
    respuesta5_bool = False
    
    while contador_int < 3:
        
        respuesta5_int = int(input('63 - 42 = '))
        
        if respuesta5_int == 21:
            respuesta5_bool = True
            print("★ (^_^) ¡CORRECTO! +10 🪙 ★")
            break
        
        else:
            contador_int = contador_int + 1
            print("✗ (╥﹏╥) ¡INCORRECTO! ★")
            
        if contador_int == 3:
            print("(×_×) ¡OH, NO! No has conseguido 🪙 monedas en este ejercicio.")
    
    print() #Jara: en esta parte he sumado los puntos totales que el usuario ha ganado e hice una multiplicación porque 1 moneda equivale a 10 monedas#
    monedas_totales_int = (respuesta1_bool + respuesta2_bool + respuesta3_bool + respuesta4_bool + respuesta5_bool) * 10
    
    if monedas_totales_int == 0: #Jara: en caso de que consigas 0 monedas que salga el siguiente mensaje#
        print("╭──────────────────────────────╮")
        print("      (×_×) MISIÓN FALLIDA")
        print("╰──────────────────────────────╯")
        print("🪙 Oro conseguido: ", monedas_totales_int)
        print("(^_^) ¡No te rindas!")
        print("¡La próxima misión te espera!")
    else: #Jara: si has conseguido monedas que salga el siguiente mensaje#
        print("╭──────────────────────────────╮")
        print("     (ﾉ◕ヮ◕)ﾉ ¡ENHORABUENA!")
        print("╰──────────────────────────────╯")
        print("🪙 Oro conseguido: ", monedas_totales_int)
        print("¡La próxima misión te espera!")

#Fin de la mision 2#


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
#Fin mision 6


#Input final para que no se cierre el programa
input()
