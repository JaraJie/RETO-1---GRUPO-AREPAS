MONEDAS USUARIO_INT = 1500

 
while True:
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

    while True:

        compra_seleccionada_int = int(input())
        
        if 0 <= compra_seleccionada_int <= 7:
            break
        else:
            print()
            print("              ⚠ OPCIÓN NO DISPONIBLE ⚠")
            print()
            print("        ❯ Pulsa cualquier tecla para volver a la tienda...")
            print()
            input()

    #TIENDA DE OBJETOS#

    if compra_seleccionada_int in (1, 3, 4):
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
        
        if monedas_usuario_int >= 200:

            monedas_usuario_int = monedas_usuario_int - 200
        
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
            
        else:
            print()
            print("        ❌ No tienes suficientes monedas.")
            print()
            input()
    
    #TIENDA DE MASCOTAS#
      
    elif compra_seleccionada_int == 5:
        
        if dragon_comprado_bool == False:
            
            if monedas_usuario_int >= 500:

                monedas_usuario_int = monedas_usuario_int - 500
            
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
                dragon_comprado_bool = True
                input()
                
            else:
                print()
                print("        ❌ No tienes suficientes monedas.")
                print()
                input()
        else:
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
        
        if gatomagico_comprado_bool == False:
            
            if monedas_usuario_int >= 400:
                
                monedas_usuario_int = monedas_usuario_int - 400
                
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
                gatomagico_comprado_bool = True
                input()
            
            else:
                print()
                print("        ❌ No tienes suficientes monedas.")
                print()
                input()
        else:
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