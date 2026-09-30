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
#### NÚMERO DE MISIÓN: _______             ####
#### NOMBRE DE MISIÓN: ________________    ####
#### AUTOR: _________________              ####
###############################################

if mision_selecionada_int == 6:
    print("╔════════════════════════════╗")
    print("   ★ MISIÓN 6 SELECCIONADA ★")
    print("     ENGLISH QUEST")
    print("╚════════════════════════════╝")
    
    print("El objetivo de este ejercicio es acertar la palabra en ingles mediante el ahorcado")
    print("Para adivinar la palabra secreta tendrás 5 intentos. Cuando queden solo 2 intentos, aparecerá una pista")
    
    intentos_int = 5
    lista_palabras_ingles_str = ["apple", "house", "water", "book", "school", "friend", "bread", "cheese"]
    
    posicion_random_int = random.randint(0, len(lista_palabras_ingles_str) - 1 )
    palabra = lista_palabras_ingles_str[posicion_random_int]

    palabra_ahorcado_str = []
    for i in range(len(palabra)):
        palabra_ahorcado_str.append("_")
        
    letras_int = len(palabra)
    letras_acertadas = 0

    while intentos_int > 0:
        print(palabra_ahorcado_str)
        print("Introduzca una letra: ")
        letra_usuario_str = input().lower()
        aciertos_bool = False
        for i in range(len(palabra)):
            if palabra[i] == letra_usuario_str:
                palabra_ahorcado_str[i] = palabra[i]
                aciertos_bool = True
                letras_acertadas += 1
        if aciertos_bool == False:
            print("La letra '", letra_usuario_str, "' no está en la palabra")
            intentos_int -= 1
        if letras_acertadas == letras_int:
            break
    if letras_acertadas == letras_int:
        print("Felicidades, has acertado la palabra en.")
    else:
        print("No has logrado acertar la palabra.")
        print("La palabra era: ", palabra)
    input()