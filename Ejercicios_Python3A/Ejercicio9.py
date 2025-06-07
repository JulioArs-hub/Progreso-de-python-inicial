#9. Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo
#números positivos de la lista original

num_list = list(range(-10,10))
num_pstve= []
print(num_list)

for i in num_list:
    if i > 0:
        num_pstve.append(i)

print(num_pstve)