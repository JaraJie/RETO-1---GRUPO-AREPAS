#Maitane: random se utiliza para generar valores aleatorios en algunas misiones
import random

#Maitane: os se utiliza para obtener la ruta de usuarios.txt y limpiar la consola
import os

###############################################
#### PANEL DE SELECCIÓN MISIONES           ####
#### AUTOR: Jara                           ####
###############################################

# Maitane: Función principal del menú de misiones.
# Recibe la línea del usuario que ha iniciado sesión para poder actualizar
# sus monedas en usuarios.txt después de completar una misión.
def cargar_misiones(linea_usuario_int):
    #Jara: variables para saber si el estado de la misión (completa o incompleta)#
    mision1_completada_bool = False
    mision2_completada_bool = False
    mision3_completada_bool = False
    mision4_completada_bool = False
    mision5_completada_bool = False
    mision6_completada_bool = False
    mision7_completada_bool = False

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
            #print("      #NOMBRE DE LA MISIÓN#")#
            #print("╚════════════════════════════╝")#


        #Reiniciamos por si acaso la variable para que en un inicio no tenga monedas nuevas de las misiones
        monedas_conseguidas_int = 0

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
                print("     (๑•̀ㅂ•́)و FRUTI-QUEST")
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
            
                # Dependiendo de la cantidad de frutas introducida,
                # asignamos una recompensa diferente al usuario
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
                print("◆ Misión:")
                print("   Resuelve 5 operaciones.")
                print("◆ Puntuación:")
                print("   ✓ Cada acierto = +1 punto")
                print("   🪙 Cada punto = +10 oro")
                print("◆ Máximo:")
                print("   ★ 5 puntos = 50 🪙 oro")
                print()
                print("⚠ ¡Cuidado! Tienes un número limitado de intentos.")
                
                print()
                
                #aquí empieza el primer ejercicio#
                # El contador controla los intentos disponibles y el booleano
                # guarda si el usuario ha acertado el ejercicio
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
                monedas_conseguidas_int = monedas_totales_int
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
        #### NÚMERO DE MISIÓN: 3                   ####
        #### NOMBRE DE MISIÓN: MODO ESTUDIO        ####
        #### AUTOR: Uhaitz                         ####
        ###############################################

        elif mision_selecionada_int ==3:
            if mision3_completada_bool == False: #Jara: en caso de que sea la primera vez que hagas la misión, puedas completarla#
                print()
                
                print("╔════════════════════════════╗")
                print("   ★ MISIÓN SELECCIONADA ★")
                print("     (ง'̀-'́)ง MODO ESTUDIO")
                print("╚════════════════════════════╝")
                
                print()
                
                #Jara: Breve explicación de en que consiste la misión para el usuario#
                print("◆ Misión:")
                print("   Estudia y demuestra tu concentración.")
                print("◆ Objetivo:")
                print("   ✓ Estudia durante un máximo de 60 minutos.")
                print("◆ Recompensa:")
                print("   🪙 Cuanto más estudies, más oro ganarás.")
                print("◆ Máximo:")
                print("   ★ 60 minutos = 100 🪙 oro")
                print()
                print("⚠️ ¡No superes el límite de 60 minutos!")
                print("💤 ¡Recuerda hacer descansos para recuperar energía!")
                print("(ง •̀_•́)ง ¡CONCENTRACIÓN AL MÁXIMO!")
                
                print()

                print("⏱️ ¿Cuántos minutos has estudiado?")
                print("➤ Escribe el tiempo en minutos.")# Aqui pedimos en numero en minutos para que no haya confusiones
                tiempomisionestudio_int = int(input())

                print()
                print("━━━━━━━━━━━━ 📖 ━━━━━━━━━━━━")

                # Dependiendo del tiempo que haya estudiado el usuario,
                # asignamos una cantidad diferente de monedas como recompensa
                if tiempomisionestudio_int <= 14:
                    print("(×_×) ¡OH, NO!")
                    print("📚 Has estudiado muy poco.")
                    print("🪙 RECOMPENSA: +0 ORO")
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                    monedas_conseguidas_int = 0
                elif 31 > tiempomisionestudio_int > 14:
                    print("(^_^) ¡BIEN HECHO!")
                    print("📚 ¡Has conseguido estudiar!")
                    print("🪙 RECOMPENSA: +50 ORO")
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                    monedas_conseguidas_int = 50
                elif 46 > tiempomisionestudio_int > 30:
                    print("(ง •̀_•́)ง ¡MUY BIEN!")
                    print("📚 ¡Buen esfuerzo de estudio!")
                    print("🪙 RECOMPENSA: +75 ORO")
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                    monedas_conseguidas_int = 75
                elif 61 > tiempomisionestudio_int > 45:
                    print("★ (^▽^) ¡EXCELENTE! ★")
                    print("📚 ¡Has dado lo mejor de ti!")
                    print("🪙 RECOMPENSA: +100 ORO")
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                    monedas_conseguidas_int = 100
                else:
                    print("★ (^▽^) ¡EXCELENTE! ★")
                    print("💤 ¡Pero recuerda hacer descansos")
                    print("🪙 RECOMPENSA: +100 ORO")
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                    monedas_conseguidas_int = 100
                mision3_completada_bool = True

            else: #Jara: si en el menu eliges el 3 y ya completaste la misión para que te salga que ya se completó#
                print("╔══════════════════════════════╗")
                print("    ★ MISIÓN YA COMPLETADA ★")
                print("╚══════════════════════════════╝")
                print(">>> Pulsa una tecla para volver al menú de misiones <<<")
        #FIN MISIÓN 3#



        ###############################################
        #### NÚMERO DE MISIÓN: 4                   ####
        #### NOMBRE DE MISIÓN: MAESTRO DEL SABER   ####
        #### AUTOR: Jara                           ####
        ###############################################

        elif mision_selecionada_int == 4:
            
            if mision4_completada_bool == False: #Jara: si la misión no esta completa para que puedas completarla#
                
                print()

                print("╔════════════════════════════╗")
                print("   ★ MISIÓN SELECCIONADA ★")
                print("  (^_^)b MAESTRO DEL SABER")
                print("╚════════════════════════════╝")

                print()

                #Jara: Breve explicación de en que consiste la misión para el usuario#
                print("🧠 ¡PON A PRUEBA TU CONOCIMIENTO!")
                print("◆ Misión:")
                print("   Responder 5 preguntas.")
                print("◆ Puntuación:")
                print("   ✓ Cada acierto = +1 punto")
                print("   🪙 Cada punto = +10 oro")
                print("◆ Máximo:")
                print("   ★ 5 puntos = 50 🪙 oro")
                print("⚠️ Elige entre A, B, C o D.")
                print("(ง •̀_•́)ง ¡QUE COMIENCE EL DESAFÍO!")

                print()

                #pregunta 1#
                print("╭────────── ✦ PREGUNTA 1 ✦ ──────────╮")
                print("🧠 ¿Cuál es el planeta más cercano al Sol?")
                print("   A) Venus")
                print("   B) Mercurio")
                print("   C) Marte")
                print("   D) Júpiter")
                respuesta1_str = input()
                respuesta1_bool = respuesta1_str == 'b' or respuesta1_str == 'B' #Jara: en caso de que el usuario responda b o B para que la variable sea correcta#

                if respuesta1_bool == 1: #Jara: como la variable es correcta será igual a 1#
                    print("★ (^_^) ¡CORRECTO! +10 🪙 ★")
                else: #Jara: en caso de ser incorrecta printeará lo siguiente#
                    print("✗ (╥﹏╥) ¡INCORRECTO! ★")

                print()

                #pregunta 2#
                print("╭────────── ✦ PREGUNTA 2 ✦ ──────────╮")
                print("🧠 ¿En qué año llegó Cristóbal Colón a América?")
                print("   A) 1512")
                print("   B) 1492")
                print("   C) 1808")
                print("   D) 1402")
                respuesta2_str = input()
                respuesta2_bool = respuesta2_str == 'b' or respuesta2_str == 'B'

                if respuesta2_bool == 1:
                    print("★ (^_^) ¡CORRECTO! +10 🪙 ★")
                else:
                    print("✗ (╥﹏╥) ¡INCORRECTO! ★")

                print()

                #pregunta 3#
                print("╭────────── ✦ PREGUNTA 3 ✦ ──────────╮")
                print("🧠 ¿Cuál es la capital de España?")
                print("   A) Barcelona")
                print("   B) Sevilla")
                print("   C) Madrid")
                print("   D) Valencia")
                respuesta3_str = input()
                respuesta3_bool = respuesta3_str == 'c' or respuesta3_str == 'C'

                if respuesta3_bool == 1:
                    print("★ (^_^) ¡CORRECTO! +10 🪙 ★")
                else:
                    print("✗ (╥﹏╥) ¡INCORRECTO! ★")

                print()

                #pregunta 4#
                print("╭────────── ✦ PREGUNTA 4 ✦ ──────────╮")
                print("🧠 ¿Cómo se llama el proceso por el cual las plantas producen su propio alimento?")
                print("   A) Respiración")
                print("   B) Digestión")
                print("   C) Fotosíntesis")
                print("   D) Germinación")
                respuesta4_str = input()
                respuesta4_bool = respuesta4_str == 'c' or respuesta4_str == 'C'

                if respuesta4_bool == 1:
                    print("★ (^_^) ¡CORRECTO! +10 🪙 ★")
                else:
                    print("✗ (╥﹏╥) ¡INCORRECTO! ★")

                print()

                #pregunta 5#
                print("╭────────── ✦ PREGUNTA 5 ✦ ──────────╮")
                print("🧠 ¿Quién pintó la Mona Lisa o Gioconda?")
                print("   A) Leonardo da Vinci")
                print("   B) Vincent van Gogh")
                print("   C) Karlos Arguiñano")
                print("   D) Lamine Yamal")
                respuesta5_str = input()
                respuesta5_bool = respuesta5_str == 'a' or respuesta5_str == 'A'

                if respuesta5_bool == 1:
                    print("★ (^_^) ¡CORRECTO! +10 🪙 ★")
                else:
                    print("✗ (╥﹏╥) ¡INCORRECTO! ★")

                # En Python, True equivale a 1 y False a 0 al realizar operaciones.
                # Sumamos los booleanos para obtener el número de respuestas correctas
                # y multiplicamos por 10 porque cada acierto recompensa con 10 monedas.
                monedas_totales_int = (respuesta1_bool + respuesta2_bool + respuesta3_bool + respuesta4_bool + respuesta5_bool) * 10 #Jara: para que sume la cantidad de respuestas correctas. La multipicación se debe a que una respuesta correcta equivale a 10 monedas#
                monedas_conseguidas_int = monedas_totales_int
                print()
                
                if monedas_totales_int == 0: #Jara: en caso de que no aciertes ninguna pregunta y no consigas monedas que aparezca lo siguiente#
                    print("╭──────────────────────────────╮")
                    print("      (×_×) MISIÓN FALLIDA")
                    print("╰──────────────────────────────╯")
                    print("🪙 Oro conseguido en esta misión: ", monedas_totales_int)
                    print("(^_^) ¡No te rindas!")
                    print("¡La próxima misión te espera!")
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                else: #Jara: en caso de conseguir monedas que aparezca lo siguiente#
                    print("╭──────────────────────────────╮")
                    print("     (ﾉ◕ヮ◕)ﾉ ¡ENHORABUENA!")
                    print("╰──────────────────────────────╯")
                    print("🪙 Oro conseguido: ", monedas_totales_int)
                    print("¡La próxima misión te espera!")
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")

                mision4_completada_bool = True #Jara: al finalizar la misión para que la variable de mision completada se vuelva verdadera#
            
            else: #Jara: si en el menu eliges el 4 y ya completaste la misión para que te salga que ya se completó#
                print("╔══════════════════════════════╗")
                print("    ★ MISIÓN YA COMPLETADA ★")
                print("╚══════════════════════════════╝")
                print(">>> Pulsa una tecla para volver al menú de misiones <<<")
        #FIN MISIÓN 4#


        ###############################################
        #### NÚMERO DE MISIÓN: 5                   ####
        #### NOMBRE DE MISIÓN: CASA LIMPIA         ####
        #### AUTOR: Erik                           ####
        ###############################################
    
        elif mision_selecionada_int == 5:
            
            if mision5_completada_bool == False: #Jara: para poder completar la misión si aún no esta completada#
                #Explicacion visual de la misión
                print("╔════════════════════════════╗")
                print("   ★ MISIÓN 5 SELECCIONADA ★")
                print("(ง •̀_•́)ง OPERACIÓN: CASA LIMPIA")
                print("╚════════════════════════════╝")

                print()

                print("◆ Misión:")
                print("   Completar tareas del hogar.")
                print("◆ Objetivo:")
                print("   ✓ Responde SÍ o NO en cada tarea.")
                print("   ★ Cada tarea completada = +1 punto")
                print("◆ Recompensa:")
                print("   🪙 ¡Gana oro por cada tarea realizada!")
                print("⚠️ ¡Sé sincero con tus respuestas!")
                print("(ง •̀_•́)ง ¡QUE COMIENCE LA MISIÓN!")
                
                print()

                print("◆ TAREA [01] 🧽")
                #Pregunta si hiciste cada tarea
                respuesta1_str= input("   ¿Has recogido la habitación? (sí/no): ")
                #Si la respuesta es si, la variable se vuelve True y se guarda como 1
                respuesta1_bool = respuesta1_str == "si" or respuesta1_str == "sí"

                print()
                print("◆ TAREA [02] 🧽")
                respuesta2_str= input("   ¿Has hecho la cama? (sí/no): ")             
                respuesta2_bool = respuesta2_str == "si" or respuesta2_str == "sí"

                print()
                print("◆ TAREA [03] 🧽")
                respuesta3_str= input("   ¿Has recogido la mesa? (sí/no): ")                           
                respuesta3_bool = respuesta3_str == "si" or respuesta3_str == "sí"

                print()
                print("◆ TAREA [04] 🧽")
                respuesta4_str= input("   ¿Has sacado la basura? (sí/no): ")                            
                respuesta4_bool = respuesta4_str == "si" or respuesta4_str == "sí"

                print()
                print("◆ TAREA [05] 🧽")
                respuesta5_str= input("   ¿Has barrido el suelo? (sí/no): ")                       
                respuesta5_bool = respuesta5_str == "si" or respuesta5_str == "sí"

                #Suma de todas las respuestas correctas
                resultado_int = respuesta1_bool + respuesta2_bool + respuesta3_bool + respuesta4_bool + respuesta5_bool

                print()

                #Dependiendo del resultado, se dan mas o menos monedas
                if resultado_int == 1:
                    print("╭────────── ✦ RESULTADOS ✦ ──────────╮")
                    print("       🧹 PROGRESO DE LA MISIÓN")
                    print("          ★ 1 / 5 TAREAS ★")
                    print("       🟩⬜⬜⬜⬜ 20%")
                    print("       🪙 RECOMPENSA: +10 ORO")
                    print("╰───────────────────────────────────╯")
                    print()
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                    monedas_conseguidas_int = 10
                elif resultado_int == 2:
                    print("╭────────── ✦ RESULTADOS ✦ ──────────╮")
                    print("       🧹 PROGRESO DE LA MISIÓN")
                    print("          ★ 2 / 5 TAREAS ★")
                    print("       🟩🟩⬜⬜⬜ 40%")
                    print("       🪙 RECOMPENSA: +20 ORO")
                    print("╰───────────────────────────────────╯")
                    print()
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                    monedas_conseguidas_int = 20
                elif resultado_int == 3:
                    print("╭────────── ✦ RESULTADOS ✦ ──────────╮")
                    print("       🧹 PROGRESO DE LA MISIÓN")
                    print("          ★ 3 / 5 TAREAS ★")
                    print("       🟩🟩🟩⬜⬜ 60%")
                    print("       🪙 RECOMPENSA: +30 ORO")
                    print("╰───────────────────────────────────╯")
                    print()
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                    monedas_conseguidas_int = 30
                elif resultado_int == 4:
                    print("╭────────── ✦ RESULTADOS ✦ ──────────╮")
                    print("       🧹 PROGRESO DE LA MISIÓN")
                    print("          ★ 4 / 5 TAREAS ★")
                    print("       🟩🟩🟩🟩⬜ 80%")
                    print("       🪙 RECOMPENSA: +40 ORO")
                    print("╰───────────────────────────────────╯")
                    print()
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                    monedas_conseguidas_int = 40
                elif resultado_int == 5:
                    print("╭────────── ✦ RESULTADOS ✦ ──────────╮")
                    print("       🧹 PROGRESO DE LA MISIÓN")
                    print("          ★ 4 / 5 TAREAS ★")
                    print("       🟩🟩🟩🟩🟩 100%")
                    print("       🪙 RECOMPENSA: +50 ORO")
                    print("╰───────────────────────────────────╯")
                    print()
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                    monedas_conseguidas_int = 50
                else:
                    print("╔══════════════════════════════════╗")
                    print("       ⚠️ MISIÓN FALLIDA")
                    print("╚══════════════════════════════════╝")
                    print("          (×_×) ¡OH, NO!")
                    print("       📜 RESULTADOS")
                    print("       ☆ 0 / 5 TAREAS ☆")
                    print("       ⬜⬜⬜⬜⬜ 0%")
                    print("       🪙 ORO OBTENIDO: 0")
                    print("   (ง •̀_•́)ง ¡No te rindas!")
                    print()
                    print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                    monedas_conseguidas_int = 0
                mision5_completada_bool = True #Jara: para que la misión se guarde como completada una vez hecha#
            else: #Jara: para que si vuelves a seleccionar una misión ya hecha aparezca lo siguiente#
                print("╔══════════════════════════════╗")
                print("    ★ MISIÓN YA COMPLETADA ★")
                print("╚══════════════════════════════╝")
                print(">>> Pulsa una tecla para volver al menú de misiones <<<")


        ###############################################
        #### NÚMERO DE MISIÓN: 6                   ####
        #### NOMBRE DE MISIÓN: ENGLISH QUEST       ####
        #### AUTORA: Maitane                       ####
        ###############################################

        elif mision_selecionada_int == 6:
            
            if mision6_completada_bool == False:
                #Visual misión
                print()
                print("╔════════════════════════════╗")
                print("   ★ MISIÓN 6 SELECCIONADA ★")
                print("         ENGLISH QUEST")
                print("╚════════════════════════════╝")
                
                #Explicación de en que consiste la misión
                print("¡PON A PRUEBA TU INGLÉS!")
                print("◆ Misión:")
                print(" Adivinar la palabra secreta.")
                print("◆ Objetivo:")
                print(" ✓ Descubre la palabra en inglés.")
                print("◆ Modalidad:")
                print(" ✓ Juego basado en el ahorcado.")
                print()
                print("⚠️ ¡Cuidado! Dispones de 5 intentos.")
                print("(ง •̀_•́)ง ¡QUE COMIENCE EL DESAFÍO!")
                
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
                    print()
                    print("🔎 ¡DESCUBRE LA PALABRA!")
                    print("📖 La palabra en español es: ", palabra_castellano_str)

                    #Printeamos como va la palabra a adivinar, si se ha acertado alguna letra saldra en esa posicion, sino saldra _
                    print(palabra_ahorcado_str)
                    
                    #Bucle para pedir que el usuario introduzca una nueva letra
                    while True:
                        
                        print("◆ Tu turno:")
                        print("   ➤ Introduce una letra.")
                        letra_usuario_str = input().lower()
                        
                        #En el caso de que esa letra aparezca en la lista letras_usadas (es decir, ya se haya dicho esa letra), 
                        #el programa nos imprime que ya hemos dicho esa letra y continua en el bucle
                        if letra_usuario_str in letras_usadas_str:
                            print("⚠️ ¡LETRA REPETIDA!")
                            print(" ✖ Ya has introducido esa letra.")
                            print("💡 ¡Prueba con otra!")
                        
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
                        print("✖ ¡LETRA INCORRECTA!")
                        print("➤ La letra ",letra_usuario_str, " no está en la palabra.")
                        print("⚠️ ¡Cuidado! Has perdido un intento.")
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
                    print()
                    print("🎉 ¡MISIÓN COMPLETADA!")
                    print("◆ Resultado:") 
                    print(" ✓ ¡Has acertado la palabra!") 
                    print("◆ Recompensa:") 
                    print(" 🪙 +50 monedas de oro") 
                    print("(ง •̀_•́)ง ¡ENHORABUENA!")
                    monedas_conseguidas_int = 50
                #En el caso contrario, se ha salido al quedarse sin intentos. Por lo que nos imprime un mensaje de que no se ha logrado acertar la palabra. Y nos enseña cual era la palabra
                else:
                    print()
                    print("💀 ¡MISIÓN FALLIDA!")
                    print("◆ Resultado:")
                    print(" ✖ No has logrado adivinar la palabra.")
                    print("◆ Solución:")
                    print("📖 La palabra era: ", palabra_ingles_str)
                    print("💡 ¡No te rindas! La próxima vez lo conseguirás.")
                    monedas_conseguidas_int = 0
                
                mision6_completada_bool = True
                print(">>> Pulsa una tecla para volver al menú de misiones <<<")
            else:
                print("╔══════════════════════════════╗")
                print("    ★ MISIÓN YA COMPLETADA ★")
                print("╚══════════════════════════════╝")
                print(">>> Pulsa una tecla para volver al menú de misiones <<<")
        #FIN MISIÓN 6#
        

        ###############################################
        #### NÚMERO DE MISIÓN: 7                   ####
        #### NOMBRE DE MISIÓN: MISIÓN ESPECIAL     ####
        #### AUTOR: Jara                           ####
        ###############################################

        elif mision_selecionada_int == 7:

            if mision7_completada_bool == False: #Jara: en caso de no tener la misión completa para poder hacerla#
                
                print()

                print("★━━━━━━━━━━━━━━━━━━━━━━━━━━━━★")
                print("   ☆ SPECIAL QUEST ☆")
                print("   (¬‿¬) NÚMERO MISTERIOSO")
                print("★━━━━━━━━━━━━━━━━━━━━━━━━━━━━★")

                print()
                
                #explicación objetivo de la misión y recomensas#
                print("◆ Misión:")
                print("   Acierta el número secreto (entre 1-30).")
                print("◆ Recompensa:")
                print("   ★ Si aciertas → +100 🪙 oro")
                print()
                print("(¬‿¬) ¿Serás capaz de descubrirlo?")
                print()
                print("⚠ ¡Cuidado! Tienes 5 intentos.")

                numero_secreto_int = random.randint(1, 31) #Jara: para que el el número secreto sea un número aleatorio entre el 1 y 30 (30 incluido)#

                contador_int = 0
                
                print()
                print("🔮 Escribe el número secreto: ")

                while contador_int < 5: #Jara: para entrar en un bucle y salir trás 5 intentos#
                    numero_int = int(input())
                    contador_int = contador_int + 1 #Jara: para que el contador vaya sumando por intento usado#

                    if numero_int != numero_secreto_int: #Jara: en caso de que el número secreto no sea igual aparezca lo siguiente#
                        if numero_int < numero_secreto_int: #Jara: si el número secreto es mayor que lo indique#
                            print("✗ (╥﹏╥) ¡INCORRECTO! ★")
                            print("⬆️ ¡El número secreto es MAYOR!")
                        else: #Jara: si el número secreto es menor que lo indique#
                            print("✗ (╥﹏╥) ¡INCORRECTO! ★")
                            print("⬇️ ¡El número secreto es MENOR!")
                        if contador_int == 5: #Jara: en caso de no acertar el número secreto y haber usado los 5 intentos que aparezca el siguiente mensaje#
                            print("(×_×) ¡OH, NO! No has conseguido 🪙 monedas en este ejercicio.")
                            print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                            monedas_conseguidas_int = 0
                            break #Jara: como no has acertado y ya usaste todos los intentos para que salga del bucle#
                    else: #Jara: en caso de acertar el número secreto aparezca lo siguiente#
                        print("★ (^_^) ¡CORRECTO! ★")
                        print("🎉 ¡Has descubierto el número secreto!")
                        print("🪙 +100 oro")
                        print(">>> Pulsa una tecla para volver al menú de misiones <<<")
                        monedas_conseguidas_int = 100
                        break #Jara: como acertaste el número para que salga del bucle#
                    mision7_completada_bool = True #Jara: como ya completaste la misión el valor se volvera cierto#
                
            else: #Jara: si en el menu eliges el 7 y ya completaste la misión para que te salga que ya se completó#
                print("╔══════════════════════════════╗")
                print("    ★ MISIÓN YA COMPLETADA ★")
                print("╚══════════════════════════════╝")
                print(">>> Pulsa una tecla para volver al menú de misiones <<<")
            #FIN MISIÓN ESPECIAL#


        elif mision_selecionada_int == 0:
            print("(^-^) ¡Has salido del menú de misiones!")
            print("★ ¡Hasta la próxima, aventurero! ★")
            input("Pulsa cualquier tecla para volver al menu principal")
            os.system("cls")
            break

        #Añadir monedas a la base de datos del usuario en el txt
        #Solo entra a modificar las monedas si se han conseguido monedas, sino, lo ignora
        if monedas_conseguidas_int > 0:
            #Buscamos y abrimos el txt
            ruta_carpeta = os.path.dirname(__file__)
            ruta_usuarios = os.path.join(ruta_carpeta, "usuarios.txt")
            #Abrimos el archivo txt con lectura y escritura a la vez (r+)
            archivo_usuarios = open(ruta_usuarios, "r+")
            #Cargamos en lineas_archivo todas las lineas del txt
            lineas_archivo = archivo_usuarios.readlines()
            #Separamos las lineas, en una lista
            lista_datos_usuario_str = lineas_archivo[linea_usuario_int].strip().split(",")
            #Cogemos las linea que contiene la informacion del usuario actual y leemos su cantidad
            #de monedas y le sumamos las conseguidas
            valor_nuevo_monedas_int = int(lista_datos_usuario_str[3]) + monedas_conseguidas_int
            #Creamos una linea nueva, con las mismas variables que la anterior
            #A excepcion de las monedas, que ponemos las calculadas en la variable de arriba
            linea_nueva_usuario_str = lista_datos_usuario_str[0] + "," + lista_datos_usuario_str[1] + "," + lista_datos_usuario_str[2] + "," + str(valor_nuevo_monedas_int) + "," + lista_datos_usuario_str[4] + "\n"
            #Entramos a la lista de lineas, y en la posicion donde hemos hecho un cambio, le damos
            #la nueva linea creada en la variable de arriba
            lineas_archivo[linea_usuario_int] = linea_nueva_usuario_str
            #volvemos a poner el cursor del txt al inicio con seek(0)
            archivo_usuarios.seek(0)
            #reescribimos todo el archivo. Todo se mantiene igual a excepcion de las monedas del
            #usuario actual
            archivo_usuarios.writelines(lineas_archivo)
            #cerramos el archivo
            archivo_usuarios.close()


        # Esperamos a que el usuario pulse una tecla antes de volver al menú de misiones
        input()

        # Limpiamos la consola antes de mostrar nuevamente el menú
        os.system("cls")