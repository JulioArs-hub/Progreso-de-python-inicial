#a. Crea un script en el que el usuario introduzca un número de más de una cifra. El script debe
#imprimir los componentes del número uno a uno por pantalla. Por ejemplo si el número introducido
#es el 4532 por pantalla deberá imprimirse:
#4
#5
#3
#2

num = input("Introduce un nuemero de 4 cifras para reordenar: ")

print(num[0], "\n", 
      num[1], "\n", 
      num[2], "\n", 
      num[3])