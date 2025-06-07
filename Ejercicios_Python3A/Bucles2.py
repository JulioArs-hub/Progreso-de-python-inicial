#2. Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


# 1- Definir la Contraseña
passw = "contraseña"
# 2- Realizar una variable de verificacion
verificacion = False

# 3- En un bucle "while" mientras la verificacion se mantenga en falso
# se le seguira pidiendo la cpntraseña al ususario
while verificacion == False:
    # 4- Solicitamos la contraseña
    contr = input("Contraseña: ")
    # 5- Con un condicional Verificamos si la contraseña es la correcta
    if contr == passw:
        # 6- Si la contraseña es correcta camviamos el valor de la variable de verificacion
        # para finalizar el bucle
        print("¡Bienvenido!")
        verificacion = True
    else:
        # 7- Si la contraseña ingrsada es incorrecta inprimimos por consola el mensaje de contraseña incorrecta
        # y comenzamos el bucle desde el princio, solicitando un nuevo ingreso de contraseña
        print("Incorrecto, Vuelva a introducir la contraseña")
