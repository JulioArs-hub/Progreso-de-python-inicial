#Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos
#especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario,
#comprueba si es una contraseña segura e indícalo por pantalla.

contr = input("Ingresa una contraseña: ")
long = len(contr)

if ("a" or "e" or "i" or "o" or "u" in contr) and ("*" in contr) and ("#" in contr):
    print("Tu contraseña es segura")
else:
    print("La contraseña escrita no es segura")



