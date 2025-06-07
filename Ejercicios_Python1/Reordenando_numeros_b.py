#b. Crea un script que dado un numero entero de cuatro cifras calcula e imprima el número que
#resulta de leer el número introducido de derecha a izquierda. Por ejemplo si el número introducido
#es 4532, el output deberá ser 2354

num = input("Introduce un numero de 4 cifras para reordenar: ")

print(num[3], num[2], num[1], num[0])