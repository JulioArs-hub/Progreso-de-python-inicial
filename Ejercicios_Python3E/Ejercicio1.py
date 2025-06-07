#MATRIZ:
#Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en
#ese caso imprima dos listas correspondientes a:
#1. La fila cuyos elementos suman el máximo
#2. La columna cuyos elementos suman el máximo
#Si no se trata de una matriz devolverá dos listas vacías.

m1 = [[3.5,6.5,10],
      [4.6,7.1,9.3],
      [5.6,7.5,3.9]]

m2 = [[3.4,5.7],[3.4,5.9,10],[5,5,0.5]]

fila = []
col = []

sum_maxF = 0
sum_maxC = 0

for m in m1:
    if sum_maxF < sum(m):
        sum_maxF = sum(m)
        fila = m
    for j in range(0, len(m1[0])):
        columna = []
        for num in m1:
          columna.append(num[j])
        if sum_maxC < sum(columna):
            sum_maxC = sum(columna)
            col = columna

print(f'La suma mayor de las filas es: {sum_maxF} de la fila {fila}')
    
print(f'La suma mayor de las columnas es: {sum_maxC} de la columna {col}')    