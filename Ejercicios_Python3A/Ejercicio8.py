#8. Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista
#(P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2

num_list = [5,4,6,3,7,2,1,10,11,15,13,14,12,3,7,2,1,10,11,15,13,5,4,6,3,7,2,1,10,11,15,13,14,12,3,7,2,1,10,11,15,13]
elegido = int(input("Elige un numero para contar: "))
conteo = 0

print(num_list.count(elegido))

for num in num_list:
    if num == elegido:
        conteo += 1

print("La cantidad de veces que aparece el numero es", elegido," de:",conteo)