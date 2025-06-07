#Crea un script que dado un número y una potencia compruebe si ese numero elevado a esa
#potencia es par o impar. (Pista: los números pares tiene resto = 0 al dividirlos por 2)

num = int(input("Introduce un numero: "))

if num % 2 != 0:
    print("El numero", num, "es impar")
else:
    print("El numero", num, "es par")