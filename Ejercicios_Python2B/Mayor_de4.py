#Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por
#pantalla.

#Pedimos los 4 numero a comparar
num = input("Introduce cuatro numeros: ")

#Definimos los 4 numero usando la duncion .split para separarlos en 4 variables
num1, num2, num3, num4 = num.split(" ")

#Primero comparamos el primer numero con los otros 3 y verificamos si es el mayor
if num1 > num2 and num1 > num3 and num1 > num4:
    print("El numero", num1, "es el mayor")
#Comparamos el segundo numero con los otros 2 y verificamos si es el mayor
elif num2 > num3 and num2 > num4:
    print("El numero", num2, "es el mayor")
#Por ultimo comparamos el 3 con el utimo para verificar cual es el mayor
elif num3 > num4:
    print("El numero", num3, "es el mayor")
#Por decarte si niguno de los anteriores numero es el mayor el cuarto sera
# el mayor de todos
else:
    print("El nuemro", num4, "es el mayor")

if (num1>num2):
    num2 = num1

if (num2>num3):
    num3 = num2

if (num3>num4):
    num4 = num3

print("El mayor de los cautro es", num4)