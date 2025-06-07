#10. Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de
#los strings de la lista original.

lista1 = ['julio','tomas','denise','ana','nerina','rita','carlos','pozzo','gonzalo','luz','rolon']
list_long = []

for string in lista1:
    list_long.append(string,len(string))

print(list_long)