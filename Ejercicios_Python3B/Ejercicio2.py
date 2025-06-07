#UMEROS PRIMOS 2:
#Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con
#los números primos de la lista original. Además, el script debe devolver el número total de
#números primos encontrados y la suma de los números primos encontrados

num = list(range(1,30))
num_primos = []

for numero in num:
    primo = True
    for i in range(2,numero):
        if numero % i == 0:
            primo = False
    if primo == True:
        num_primos.append(numero)

print("Numeros primos: \n ", num_primos, "\nTotal de numeros primos: \n", len(num_primos), "\nSuma de nuemeros primos: \n", sum(num_primos))