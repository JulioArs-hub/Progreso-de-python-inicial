#BASE DE DATOS DE UN COLEGIO:
#Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los
#estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
#para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
#También necesitas calcular a nota media de cada estudiante y la nota media de la clase al
#completo.
#Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para
#cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota
#media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la
#clase.

#--Definir Variables para los alumnos, sus promedios y notas--
alumnos = ["alumA","alumB","alumC"]
database = [ ["alumA",[10,9.5,8]]
         ,["alumB",[9.2,10,7]]
         ,["alumC",[7,9,10]]]
sum_media = 0

#--En un bucle calcular el promedio de cada uno de los alumnos--
for datos in database:
    
    nombre = datos[0] #--Definir una variable para los nobmbres de los alumnos
    notas = datos[1] #--Definir una Variable para las notas de los alumnos
    
    #--Sacar el promedio--
    media = sum(notas) / len(notas) #--Definir una variable para los promedios de cada alummno
    
    print(f"El promedio de {nombre} es {media :.2f}")
    
    #--Sumar el promedio de la clase
    sum_media = sum_media + media
    
#--Sacar el promedio de la clase
promedio = sum_media / len(database)
print(f"El promedio de los alumnos es {promedio :.2f}")