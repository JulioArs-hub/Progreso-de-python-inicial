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

#--Definir Variables--

#Varible de tipo lista con los nombres de los alumnos y una lista anidada en cada uno con sus notas
datos = [ ["alumA",[10,9.5,8]],["alumB",[9.2,10,7]],["alumC",[7,9,10]],["alumD",[6.2,7,8]],["alumE",[8,7.6,9]],["alumF",[7,5.4,4]]]
#Variable para el promedio de la clase
promedioTotal = 0

#Bucle para sacar el promedio de cada uno de los alumnos
for nom in datos:
    nombre = nom[0] #Variable para el nombre del estudiante
    notas = nom[1] #Variable para Las notas del estudiante
    promedio = sum(notas)/3 # Calcular promedio del estudiante
    print(nombre, notas, "Promedio: ", sum(notas)/3) #Mostrar por consola el promedio de cada estudiante
    promedioTotal = promedioTotal+promedio # Se suma el promedio de los estudiantes

print(f"El promedio de la clesse es de: {promedioTotal / 6}")  # Se calcula el promedio de notas de la clase y luego se imprime