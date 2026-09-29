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
#### NÚMERO DE MISIÓN: _______             ####
#### NOMBRE DE MISIÓN: ________________    ####
#### AUTOR: _________________              ####
###############################################

if mision_selecionada_int == #NÚMERO DE MISIÓN#:
    print("╔════════════════════════════╗")
    print("   ★ MISIÓN SELECCIONADA ★")
    print("     #NOMBRE DE LA MISIÓN#")
    print("╚════════════════════════════╝")