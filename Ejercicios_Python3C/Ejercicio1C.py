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

#--Definir una lista con los nombres de los alumnos
alumnos = ["alumA","alumB","alumC"]

#--Definir una lista donde se integraran todos los datos de la clase
datos = []


#--Con un bucle vamos a tomar las notas de cada alumno y luego lo agregamos a la lista de datos
for estudent in alumnos:
    notas = [] # lista de notas, se iran ingresando mediante un input

    print(f"Ingrese las notas del estudiante {estudent}") #--Solicitud de Ingreso de notas
    tarea = float(input("Notas de tareas: ")) #--Se solicita la nota de la tarea
    notas.append(tarea) # Se agregan las notas de la tarea a la lista notas
    preoyectos = float(input("Notas de proyecto: "))#--Se solicita la nota del proyecto
    notas.append(preoyectos) # Se agrega la nota del proyecto a la lista de notas
    examenes = float(input("Notas de examen: ")) #--Se solicita la nota del examen
    notas.append(examenes) # Se agrega la nota del examen a la lista de notas
    
    #-- En la lista de datos se grega al estudiante y sus notas
    datos.append([estudent, notas])

#--En un bucle calculamos el promedio de cadad alumno
sum_media = 0
for i in datos:
    nombre = i[0] # Iniciamos una variable para los nombres de los estudiantes
    notas = i[1] # Iniciamos una variable para las notas de los estudiantes

    media = sum(notas) / len(notas) #Se calcula el promedio
    
    print(f"El promedio de {nombre} es {media :.2f}") # Se muestra en consola el promedio de cada alumno

    sum_media = sum_media + media # Se suma el promedio de cada alumno
    

promedio = sum_media / len(datos) # Se calcula el promedio de la clase
print(f"El promedio de la clase es: {promedio}")