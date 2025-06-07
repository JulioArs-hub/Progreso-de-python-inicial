#ENCRIPTACIÓN ROT13:
#El abecedario latino es un sistema de escritura alfabético más usado del mundo hoy en día. Se
#compone de 26 letras principales, más ciertas modificaciones y letras adicionales según el idioma
#del que se trate (por ejemplo, en castellano y gallego se incluye la ”ñ”, en portugués, francés y
#catalán la ”Ç”, en alemán la ”ß”, etc.).
#Aplicar el cifrado ROT13 a un texto se reduce a examinar sus caracteres alfabéticos y sustituirlos
#por la letra que está 13 posiciones por delante en el alfabeto, volviendo al principio si es necesario
#y conservando las mayúsculas y minúsculas: a se convierte en n, B se convierte en O, y así hasta
#la Z, que se convierte en M. Solo quedan afectadas las 26 letras principales que aparecen en el
#alfabeto latino; los números, símbolos, espacios y otros caracteres se dejan igual

abc = "abcdefghijklmnopqrstuvwxyz"
abc_mayus = abc.upper()

mensaje = "hOlA"
mensaje2 = "uByN"
mensaje_cif = ""

for char in mensaje:
    if char in abc:
        for i in range(len(abc)):
            if char == abc[i]:
                char_ind = i
                if char_ind + 13 >= 26:
                    char_ind = char_ind - 26
                
                ind = char_ind + 13
                letra = abc[ind]
              
        mensaje_cif = mensaje_cif + letra
    elif char in abc_mayus:
        for i in range(len(abc_mayus)):
            if char == abc_mayus[i]:
                char_ind = i
                if char_ind + 13 >= 26:
                    char_ind = char_ind - 26
                
                ind = char_ind + 13
                letra = abc_mayus[ind]
              
        mensaje_cif = mensaje_cif + letra

if mensaje_cif == mensaje2:
    print(f"Los mensajes {mensaje2} y {mensaje_cif} son una encriptacio de uno del otro")
else:
    print(f"Los mensajes {mensaje2} y {mensaje_cif} no son una encriptacion de uno del otro")

            