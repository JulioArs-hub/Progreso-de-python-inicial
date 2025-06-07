
cadena_alumnos = "David Fernandez 12311267A 43527 2 9.1 7.6 2.4\
    \nMaria Garcia 12316487A 43527 2 7.1 8.6 5.4 \
\nJuan Perez 647829236A 43527 2 8.1 8.5 8.4"

alumnos = cadena_alumnos.split('\n')

print(cadena_alumnos)

base_datos = []

for alumno in alumnos:
    datos_alumno = alumno.split()
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