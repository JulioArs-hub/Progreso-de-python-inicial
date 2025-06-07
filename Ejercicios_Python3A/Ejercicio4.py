#4. Crea un script que cuente el número de elementos más grandes que un determinado número
#dado por el usuario (supón una lista numérica).

numeros = list(range(1,30))
num = int(input("Contar numeros mayores de: "))
contador = 0

for num1 in numeros:
    if num1 > num:
        contador += 1

print(contador)