#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el
#divisor es cero el programa debe mostrar un error.

num1 = int(input("Introduce un dividendo: "))
num2 = int(input("Introduce un divisor: "))

if num2 != 0:
    print("el resultado de la division es: ", num1 / num2)
else:
    print("Error")