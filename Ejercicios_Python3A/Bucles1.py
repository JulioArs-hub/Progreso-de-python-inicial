#1. Escribe un programa que pida al usuario un número entero y muestre por pantalla una
#estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el
#centro de la estructura.
#*
#**
#***
#****
#*****
#****
#***
#**
#*

# 1- Pedir un numero que indique el tamaño de la estrucura

cant = int(input("Introduce  un numero: "))

# 2- Definir en un bucle "for" un conteo hasta la el numero indicado por terminal

for i in range(1, cant + 1):
    # 3- Con la variable i multilplicamos en el comando print la cantidad de asteriscos a mostra
    print("*" * i)
    # 4- Cuando alcance el maximo del numero indicado, realisamos un condicional con un nuevo bucle
    # que realize los paso al reverso de lo que indicamos anteriormente
    if i == cant:
        for i in range(cant - 1, 1,-1):
            print("*"*i)