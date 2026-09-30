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
###############################################
#### NÚMERO DE MISIÓN: _______             ####
#### NOMBRE DE MISIÓN: ________________    ####
#### AUTOR: _________________              ####
###############################################

#if mision_selecionada_int == NÚMERO DE MISIÓN:#
    #print("╔════════════════════════════╗")#
    #print("   ★ MISIÓN SELECCIONADA ★")#
    #print("     #NOMBRE DE LA MISIÓN#")#
    #print("╚════════════════════════════╝")#




 
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