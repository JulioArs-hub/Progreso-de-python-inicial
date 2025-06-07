#1. Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros:
#[1,2,3,4,5,6,7,8,9,10].
#2. Crea una nueva lista con los números pares de la lista anterior en orden inverso
#3. Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por
#consola.
#4. Intenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método de
#compresión).
#5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla
#6. Haz lo mismo con el número más alto
#7. Suma todos los elementos de la lista con y sin un bucle.
#8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras
#el punto 2

# 1- Hacer una lista de numeros del 1 al 10
list_num = []
ls = list(range(1,11))

for num in range(1,11):
    list_num.append(num)

print("1-",list_num)
print(ls)

# 2- Hacer una nueva lista inversa con los numero pares
num_par_inv = []
for num in range(len(list_num),1,-1):
    if num % 2 == 0:
        print("2-",num)
        num_par_inv.append(num)

# 3- Con un bucle rrecorer todos los numeros e inprimir el cuadrado de cada uno
for num in list_num:
    print("3-",num **2)

# 4- Intentar hacer el ejercicio 2 y 3 con el menor numero de lineas
for num in range(len(list_num),0,-1):
    if num % 2 == 0 :
        print("4-", num ** 2)

# 5- Imprimir el numero mas pequeño
print("5-", min(list_num))

# 6- Imprimir el numero mas alto
print("5-", max(list_num))

# 7- sumar todos los elementos de la lista
print("7-", sum(list_num))

# 8- encontrar el indice de del numero en la posicion 8
# de la lista original y la lista resultante del ejercicio 2
print(num_par_inv)
print("8-", list_num.index(8), "\n", num_par_inv.index(8))