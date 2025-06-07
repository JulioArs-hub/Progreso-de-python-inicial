#Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma
#de los otros dos.
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
num3 = float(input("Introduce el tercer numero: "))

if (num1==num2+num3):
    print(num1, "es igual a la suam de", num2, "y", num3)
elif (num2 == num1 + num3):
    print(num2, "es igual a la suma de", num1, "y", num3)
elif (num3 == num1 + num2):
    print(num3, "es igual a la suma de", num1, "y", num3)
else:
    print("ningun numero el la suma de uno con el otro")