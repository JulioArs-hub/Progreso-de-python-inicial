#MATRIZ:
#Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en
#ese caso imprima dos listas correspondientes a:
#1. La fila cuyos elementos suman el máximo
#2. La columna cuyos elementos suman el máximo
#Si no se trata de una matriz devolverá dos listas vacías.


M1= [[2,5,3],[6,1,8],[7,5,4]]

n_columnas = len(M1[0])
n_fila = len(M1)
es_matriz = True

for i in range(0, n_fila):
    if len(M1[i]) != n_columnas:
        es_matriz = False
        break

if es_matriz == True:
    suma_max = 0
    for i in range(0, n_fila):
        fila = M1[i]
        suma_fila = sum(fila)
        print(fila,suma_fila)
        if suma_fila > suma_max:
            suma_max = suma_fila
            num_fila = i

print(f'La fila con la suma de maximo mayor es: {M1[num_fila]} que suma {suma_max}')

if es_matriz == True:
    suma_max = 0
    colum_max = 0
    for j in range(0, n_columnas):
        columna = []
        suma_colum = 0
        for fila in M1:
            suma_colum = suma_colum + fila[j]
            columna.append(fila[j])

        if suma_colum > suma_max:
            suma_max = suma_colum
            colum_max = columna[:]

print(f'La columna con la suma de maxima es: {colum_max} que su suma es {suma_max}')
