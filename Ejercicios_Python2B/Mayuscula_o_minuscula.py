#Permite que el usuario introduzca una letra (del alfabeto latino) como input. Comprueba si esta es
#una mayúscula o una minúscula.

letra = input("Escribe una letra: ")

if letra == letra.lower():
    print("La letra elegida esta en minuscula")
elif letra == letra.upper():
    print("La letra elegida esta en mayuscula")