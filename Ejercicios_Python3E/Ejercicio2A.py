# STRING A LISTA:
# Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información:
# nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3 … Por ejemplo:
# David Fernandez 12311267A 43527 2 2.1 4.6 3.4. El script debe crear una lista con esos datos,
# introducirlo en una lista de listas donde se encuentra la información de todos los alumnos e
# imprimir la nota media de los alumnos junto con el DNI.
# Supón ahora que tu input es un string como este:
# ‘’'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n
# Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
# Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ‚’’
# Reescribe el script para que procese ese input adecuadamente e imprima la nota media y el DNI
# de todos los alumnos en ese string.

alumnos = "David Fernandez 12311267A 43527 2 9.1 7.6 2.4"

base_datos = []

datos_alumno = alumnos.split()

base_datos.append(datos_alumno)
print(base_datos)

for alum in base_datos:
    dni = alum[2]
    suma_notas = 0
    n_notas = 0
    for i in range(5,len(alum)):
        suma_notas = suma_notas + float(alum[i])
        n_notas = n_notas + 1

nota_media = suma_notas / n_notas
print(f'El alumno con dni {dni} posee una nota promedio de {nota_media:.2f}')

