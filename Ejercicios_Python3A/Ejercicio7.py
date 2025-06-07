#7. Crea un script que extraiga los elementos comunes entre dos listas

num_list = [5,4,6,3,7,2,1,10,11,15,13,14,12]
numeros = list(range(1,30))
comunes = []

for num in num_list:
    if num in numeros:
        comunes.append(num)

print(sorted(comunes))