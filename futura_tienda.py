#Jara: de momento la cantidad de monedas será la siguiente para que el código funcione.#
#En un futuro planeamos implementar esta opción a las monedas que tiene cada usuario.#
#Para ello, hace falta conectarla a la main, pero como es una branch con un plan futuro,#
#aún no esta hecho#
monedas_usuario_int = 1500

#Jara: variables para que el estado de la compra de las siguientes mascotas sea falso#
dragon_comprado_bool = False
gatomagico_comprado_bool = False
 
while True: #Jara: bucle para que una vuelva al menú de compra constantemente#
    
    #Jara: menú visual de las opciones disponibles#
    print()
    print("              ⚜ MERCADO DE AVENTUREROS ⚜")
    print()
    print("        ✦ Los objetos de hoy ✦")
    print()
    print("    > 01 🧪  Poción de Vida")
    print("        « Una pequeña ayuda para seguir luchando »")
    print("        🪙 20 monedas")
    print()
    print("    > 02 ⚔️  Espada del Guerrero")
    print("        « El acero habla por quien sabe usarlo »")
    print("        🪙 200 monedas")
    print()
    print("    > 03 🛡️  Escudo del Guardián")
    print("        « Ningún golpe atravesará esta defensa »")
    print("        🪙 150 monedas")
    print()
    print("    > 04 🥾  Botas del Explorador")
    print("        « El camino no tendrá secretos »")
    print("        🪙 100 monedas")
    print()
    print()
    print("              ✦ ✧ ✦ MASCOTAS FANTASÍA ✦ ✧ ✦")
    print("        ✦ 💡 Las mascotas pueden acompañarte durante tus aventuras. ✦")
    print()
    print("    > 05 🐉  Dragón Bebé")
    print("        « Una criatura de poder legendario »")
    print("        🪙 500 monedas")
    print()
    print("    > 06 🦄  Unicornio")
    print("        « Una criatura mágica nacida de las estrellas »")
    print("        🪙 450 monedas")
    print()
    print("    > 07 🐈‍⬛✨  Gato Mágico")
    print("        « Una criatura misteriosa que trae buena fortuna »")
    print("        🪙 400 monedas")
    print()
    print("    > 00 🚪  Salir de la tienda")
    print("        « Volverás cuando necesites algo »")
    print()
    print("        💰 Monedas Totales: ", monedas_usuario_int)
    print("        ❯ ¿Qué deseas comprar?")

    while True: #Jara: un bucle para que que se repita lo siguiente#
       
        compra_seleccionada_int = int(input())
        
        if 0 <= compra_seleccionada_int <= 7: #Jara: si el usuario selecciona un número valido en el menú, el bucle se rompe#
            break
        else: #Jara: si la opción no es valida te aparecera el siguiente mensaje hasta que introduzcas un número valido#
            print()
            print("              ⚠ OPCIÓN NO DISPONIBLE ⚠")
            print()
            print("        ❯ Pulsa cualquier tecla para volver a la tienda...")
            print()
            input()

    #TIENDA DE OBJETOS#

    if compra_seleccionada_int in (1, 3, 4): #Jara: en caso de seleccionar 1, 3, 4 aparezca un mensaje diciendo que aún no esta disponible#
        print()
        print("                 ✦ ¡AVISO! ✦")
        print()
        print("        « El objeto seleccionado aún")
        print("          no está disponible. »")
        print()
        print("        🔒 Este objeto permanece bloqueado")
        print("           hasta nuevo aviso...")
        print()
        print("                 ✧ ✧ ✧")
        print("        ❯ Regresa cuando esté disponible.")
        print()
        input()


    elif compra_seleccionada_int == 2:
        
        if monedas_usuario_int >= 200: #Jara: en caso de que el usuario tenga monedas suficientes para la compra#

            monedas_usuario_int = monedas_usuario_int - 200 #Jara: se le restará 200 monedas y le aparecerá el siguiente mensaje#
        
            print()
            print("              ⚜ COMPRA REALIZADA ⚜")
            print()
            print("        ✦ El objeto ha sido adquirido ✦")
            print()
            print("        ⚔️  Espada del Guerrero")
            print("        « El acero habla por quien sabe usarlo »")
            print()
            print("        💰 Monedas restantes:", monedas_usuario_int)
            print()
            print("              ⚔ ¡Buena suerte, aventurero! ⚔")
            print()
            print()
            print("""
                                        /
                                *//////{<>==================-
                                        \\
            """)
            print("             ⚔ ¡OBJETO ADQUIRIDO! ⚔")
            print()
            input()
            
        else: #Jara: en caso de que no tengas suficientes monedas#
            print()
            print("        ❌ No tienes suficientes monedas.")
            print("             ⚔ ¡OBJETO NO ADQUIRIDO! ⚔")           
            print()
            input()
    
    #TIENDA DE MASCOTAS#
      
    elif compra_seleccionada_int == 5:
        
        if dragon_comprado_bool == False: #Jara: en caso de que aún no hayas comprado el dragón#
            
            if monedas_usuario_int >= 500: #Jara: para comprobar si el usuario tiene monedas suficientes#

                monedas_usuario_int = monedas_usuario_int - 500 #Jara: se le restan 500 y aparecerá lo siguiente#
            
                print()
                print("              ⚜ COMPRA REALIZADA ⚜")
                print()
                print("        ✦ La mascota ha sido adquirida ✦")
                print()
                print("        🐉  Dragón Bebé")
                print("        « Una criatura de poder legendario »")
                print()
                print("        💰 Monedas restantes:", monedas_usuario_int)
                print()
                print("              ⚔ ¡Buena suerte, aventurero! ⚔")
                print()
                print()
                print("""
                                            ∩   ∩
                                          ⊂・・つ)
                                        ～(●●)～ |)
                                         V些V_ノ |)
                                          ⊂|ー| |つ
                                            |ー| |)  ﾂ
                                            |ー| ヽ_ノl
                                            ヽ_ヽ＿_ノ
                """)
                print("             ⚔ ¡MASCOTA ADQUIRIDA! ⚔")
                print()
                dragon_comprado_bool = True #Jara: como la compra se ha realizado dragon_comprado_bool se volvera cierto#
                input()
                
            else: #Jara: en caso de no tener suficientes monedas#
                print()
                print("        ❌ No tienes suficientes monedas.")
                print("             ⚔ ¡MASCOTA NO ADQUIRIDA! ⚔")
                print()
                input()
        else: #Jara: si ya has comprado el dragón anteriormente no te dejará comprarlo de nuevo y aparecerá lo siguiente#
            print()
            print("          ✦ ✧ ✦ MASCOTA YA ADQUIRIDA ✦ ✧ ✦")
            print()
            print("        🐉 « Esta criatura ya forma parte")
            print("             de tu aventura. »")
            print()
            print("        🔒 No puedes comprarla de nuevo.")
            print()
            print("             ✧ Tu compañero te espera ✧")
            print()
            input()
    
    #Jara: en caso de seleccionar la opción 6 que aparezca que aún no esta disponible.#
    #El mensaje es diferente a la de objetos#        
    elif compra_seleccionada_int == 6:
            print()
            print("                 ✦ ¡AVISO! ✦")
            print()
            print("        « La mascota seleccionado aún")
            print("          no está disponible. »")
            print()
            print("        🔒 Este mascota permanece bloqueada")
            print("           hasta nuevo aviso...")
            print()
            print("                 ✧ ✧ ✧")
            print("        ❯ Regresa cuando esté disponible.")
            print()
            input()
            
    elif compra_seleccionada_int == 7:
        
        if gatomagico_comprado_bool == False: #Jara: si aún no has comprado el gato#
            
            if monedas_usuario_int >= 400: #Jara: para comprobar si tienes monedas suficientes para hacer la compra#
                
                monedas_usuario_int = monedas_usuario_int - 400 #Jara: si es así te restará 400 y aparecerá lo siguiente#
                
                print()
                print("              ⚜ COMPRA REALIZADA ⚜")
                print()
                print("        ✦ La mascota ha sido adquirida ✦")
                print()
                print("        🐈‍⬛✨  Gato Mágico")
                print("        « Una criatura misteriosa que trae buena fortuna »")
                print()
                print("        💰 Monedas restantes:", monedas_usuario_int)
                print()
                print("              ⚔ ¡Buena suerte, aventurero! ⚔")
                print()
                print()
                print("""
                                             ╱|、  MEOW
                                           (˚ˎ 。7
                                            |、˜〵
                                            じしˍ,)ノ
                """)
                print("             ⚔ ¡MASCOTA ADQUIRIDA! ⚔")
                print()
                gatomagico_comprado_bool = True #Jara: al acabar la compra gatomagico_comprado_bool se guardará como verdadero#
                input()
            
            else: #Jara: en caso de no tener monedas#
                print()
                print("        ❌ No tienes suficientes monedas.")
                print("             ⚔ ¡MASCOTA NO ADQUIRIDA! ⚔")
                print()
                input()
        else: #Jara: en caso de ya haber realizado la compra del gato anteriormente#
            print()
            print("          ✦ ✧ ✦ MASCOTA YA ADQUIRIDA ✦ ✧ ✦")
            print()
            print("        🐈‍⬛✨ « Esta criatura ya forma parte")
            print("             de tu aventura. »")
            print()
            print("        🔒 No puedes comprarla de nuevo.")
            print()
            print("             ✧ Tu compañero te espera ✧")
            print()
            input()

    elif compra_seleccionada_int == 0: #Jara: si selecciona el 0 para que salga del programa#
        print()
        print("        ⚜ HAS SALIDO DE LA TIENDA ⚜")
        print("        Gracias por visitar el Mercado de Aventureros.")
        print()
        break #Jara: para romper el bucle inicial#

input("Saliendo de la tienda...")