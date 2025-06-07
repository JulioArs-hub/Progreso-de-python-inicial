#1. Escribe un programa en Python para encontrar los elementos duplicados de una lista,
#añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los
#elementos únicos.

elementos = ['uno','uno','dos','tres', 'tres','cuatro', 'cinco','cinco']
print("Lista principal: ", elementos)
eliminados = []

for i in elementos:
    if elementos.count(i) > 1:
        if i not in eliminados:
         eliminados.append(i)
         elementos.remove(i)
    



print("Lista principal sin duplicados \n",elementos)

print("Lista de duplicados: \n",eliminados)