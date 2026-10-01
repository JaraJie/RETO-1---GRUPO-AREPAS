import random
import os

###############################################
#### PANEL DE SELECCIÓN MISIONES           ####
#### AUTOR: Jara                           ####
###############################################
def cargar_misiones(linea_usuario_int):
    #Jara: variables para saber si el estado de la misión (completa o incompleta)#
    mision1_completada_bool = False
    mision2_completada_bool = False
    mision6_completada_bool = False

    while True: #Jara: bucle para que vuelva al menú de misiones#

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
        print("[00] <(•_•)> EXIT")

        #Jara: esta parte la he hecho para que el usuario introduzca un número valido del menú y si no es valido entre un bucle con el siguiente mensaje#
        while True:
            
            mision_selecionada_int = int(input())
            
            if 0 <= mision_selecionada_int <= 7:
                break
            else:
                
                print(">>> ERROR_404 <<<")
                print("(×_×) ¡MISIÓN NO ENCONTRADA!")
                print("La misión que buscas no existe...")
                print("(^_^) Prueba con otro número.")


    #PLANTILLA MISIONES#
        #Jara: hice una plantilla para cuando selecciones la misión aparezca lo siguiente#
        #if mision_selecionada_int == NÚMERO DE MISIÓN:#
            #print("╔════════════════════════════╗")#
            #print("   ★ MISIÓN SELECCIONADA ★")#
            #print("     #NOMBRE DE LA MISIÓN#")#
            #print("╚════════════════════════════╝")#



        ###############################################
        #### NÚMERO DE MISIÓN: 1                   ####
        #### NOMBRE DE MISIÓN: FRUTI-QUEST         ####
        #### AUTOR: Mikel                          ####
        ###############################################

        if mision_selecionada_int == 1:
            
            if mision1_completada_bool == False: #Jara: he añadido una condicion de que si la misión no esta completada, se ejecute la misión)
                
                print()
                
                print("╔════════════════════════════╗")
                print("   ★ MISIÓN SELECCIONADA ★")
                print("  [01] (๑•̀ㅂ•́)و FRUTI-QUEST")
                print("╚════════════════════════════╝")
                
                print()
                
                #Jara: He añadido un menú con la explicación más visual#
                print("(๑•̀ㅂ•́)و ¡Es hora de cuidar tu salud!")
                print("🎯 OBJETIVO")
                print("   Come 5 frutas para completar la misión.")
                print("💰 RECOMPENSA")
                print("   🪙 Consigue hasta 50 monedas de oro.")
                print("════════════════════════════════════")
                frutas_int = int(input("🍎 ¿Cuántas frutas has comido hoy? → "))
                
                print()
            
                #añadir condiciones para que te de una cantidad de monedas diferentes dependiendo de la cantidad de fruta que has comido#
                if frutas_int >= 5:
                    print("╔══════════════════════════════╗")
                    print("    (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ¡PERFECTO!")
                    print("╚══════════════════════════════╝")
                    print("🍎 ¡Has alcanzado el objetivo!")
                    print("★ Recompensa obtenida: +50 🪙 ORO")
                    monedas_conseguidas_int = 50 #Maitane: variable en la que se guardara las monedas obtenidas
                elif frutas_int == 4:
                    print("★ ¡CASI LO CONSIGUES! ★")
                    print("🍎 Has comido 4 de 5 frutas.")
                    print("🪙 Recompensa: +40 ORO")
                    monedas_conseguidas_int = 40
                elif frutas_int == 3:
                    print("(^_^) ¡BUEN TRABAJO!")
                    print("🍎 Has comido 3 de 5 frutas.")
                    print("🪙 Recompensa: +30 ORO")
                    monedas_conseguidas_int = 30
                elif frutas_int == 2:
                    print("(•̀ᴗ•́)و ¡VAS POR BUEN CAMINO!")
                    print("🍎 Has comido 2 de 5 frutas.")
                    print("🪙 Recompensa: +20 ORO")
                    monedas_conseguidas_int = 20
                elif frutas_int == 1:
                    print("(^_^) ¡TODO SUMA!")
                    print("🍎 Has comido 1 de 5 frutas.")
                    print("🪙 Recompensa: +10 ORO")
                    monedas_conseguidas_int = 10
                else:
                    print("(╥﹏╥) ¡OH, NO!")
                    print("🍎 No has comido ninguna fruta.")
                    print("🪙 Recompensa: +0 ORO")
                mision1_completada_bool = True #Jara: para que la misión este completada y la variante se vuelva True#
                print(">>> Pulsa una tecla para volver al menú de misiones <<<")
            else: #Jara: en caso de que la misión este completada, aparezca el siguiente mensaje#
                print("╔══════════════════════════════╗")
                print("    ★ MISIÓN YA COMPLETADA ★")
                print("╚══════════════════════════════╝")
                print(">>> Pulsa una tecla para volver al menú de misiones <<<")
        
        #FIN MISIÓN 1#


        ###############################################
        #### NÚMERO DE MISIÓN: 2                   ####
        #### NOMBRE DE MISIÓN: EL RETO MATEMÁTICO  ####
        #### AUTOR: Jara                           ####
        ###############################################

        elif mision_selecionada_int == 2:

            if mision2_completada_bool == False: #Jara: si la misión no esta completa para que puedas hacerla#
            
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
                    print("🪙 Oro conseguido en esta misión: ", monedas_totales_int)
                    print("(^_^) ¡No te rindas!")
                    print("¡La próxima misión te espera!")
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                else: #Jara: si has conseguido monedas que salga el siguiente mensaje#
                    print("╭──────────────────────────────╮")
                    print("     (ﾉ◕ヮ◕)ﾉ ¡ENHORABUENA!")
                    print("╰──────────────────────────────╯")
                    print("🪙 Oro conseguido: ", monedas_totales_int)
                    print("¡La próxima misión te espera!")
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")
        
                mision2_completada_bool = True #Jara: como se ha terminado la misión 2. quiero que ahora se guarde como completada#
            
            else: #Jara: si en el menu eliges el 2 y ya completaste la misión para que te salga que ya se completó#
                print("╔══════════════════════════════╗")
                print("    ★ MISIÓN YA COMPLETADA ★")
                print("╚══════════════════════════════╝")
                print(">>> Pulsa una tecla para volver al menú de misiones <<<")
        #FIN MISIÓN 2#


        ###############################################
        #### NÚMERO DE MISIÓN: 6                   ####
        #### NOMBRE DE MISIÓN: ENGLISH QUEST       ####
        #### AUTORA: Maitane                        ####
        ###############################################

        elif mision_selecionada_int == 6:
            
            if mision6_completada_bool == False:
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
                
                mision6_completada_bool = True
                print(">>> Pulsa una tecla para volver al menú de misiones <<<")
            else:
                print("╔══════════════════════════════╗")
                print("    ★ MISIÓN YA COMPLETADA ★")
                print("╚══════════════════════════════╝")
                print(">>> Pulsa una tecla para volver al menú de misiones <<<")
        #FIN MISIÓN 6#
        
        elif mision_selecionada_int == 0:
            print("(^-^) ¡Has salido del menú de misiones!")
            print("★ ¡Hasta la próxima, aventurero! ★")
            break

        if monedas_conseguidas_int > 0:
            #AÑADIR MONEDAS AQUI#
            ruta_carpeta = os.path.dirname(__file__)
            ruta_usuarios = os.path.join(ruta_carpeta, "usuarios.txt")
            #Abrimos el archivo txt con lectura y escritura a la vez (r+)
            archivo_usuarios = open(ruta_usuarios, "r+")
            lineas_archivo = archivo_usuarios.readlines()
            lista_datos_usuario_str = lineas_archivo[linea_usuario_int].strip().split(",")
            valor_nuevo_monedas_int = int(lista_datos_usuario_str[3]) + monedas_conseguidas_int
            linea_nueva_usuario_str = lista_datos_usuario_str[0] + "," + lista_datos_usuario_str[1] + "," + lista_datos_usuario_str[2] + "," + str(valor_nuevo_monedas_int) + "," + lista_datos_usuario_str[4] + "\n"
            lineas_archivo[linea_usuario_int] = linea_nueva_usuario_str
            archivo_usuarios.seek(0)
            archivo_usuarios.writelines(lineas_archivo)
            archivo_usuarios.close()
        
        #Input final para que no se cierre el programa
        input()