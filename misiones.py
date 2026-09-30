###############################################
#### PANEL DE SELECCIÓN MISIONES           ####
#### AUTOR: Jara                           ####
###############################################

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
    print('Has ganado 0 oro')