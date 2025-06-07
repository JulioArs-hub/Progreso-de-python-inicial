#El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media.
#Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. Crea un script que
#pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no.
#*Los ejercicios bonus no se resolverán directamente en clase si no que están pensados para que
#los alumnos los discutan por el chat de Discord y compartan sus soluciones. Las soluciones
#compartidas de los alumnos se subirán en un archivo a la academia.

nom_alum = input("Introduzca El nombre del Alumno: ")
edad_alum = int(input("Indique la edad del alumno: "))
promedio = float(input("¿Cual es el promedio del alumno? "))

if promedio >= 8 and edad_alum >= 17 and edad_alum <= 21:
    print("El alumno", nom_alum, "cumple los requisitos para aplicar por la beca")
else:
    print("El alumno", nom_alum, "no cumple con los requisitos para aplcar por la beca")