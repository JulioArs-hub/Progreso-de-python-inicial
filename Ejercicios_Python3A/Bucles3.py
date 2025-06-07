#3. Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras
#de la palabra introducida empezando por la última.
import time

word = input("Escribe una palabra: ")

for i in range(len(word)-1,-1,-1):
    print(word[i])
    time.sleep(1)