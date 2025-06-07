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


#--Definir variables, nombre de los alumnos--
alumnos = ["alumA","alumB","alumC"]

#--Definir la variable con las notas y nombres de los alumnos
database = [ ["alumA",[10,9.5,8]]
         ,["alumB",[9.2,10,7]]
         ,["alumC",[7,9,10]]]

#--Con un bucle sacar el priomedio de cada alumno

for datos in database:
    nombre = datos[0] #--Variable que separa los nombres de los alumnos
    notas = datos[1] #--Variable que separa las notas de los alumnos
    suma_notas = 0
    
#metodo 3   
    for j in range(0,len(notas)):
        suma_notas = suma_notas + notas[j] #--Variable que suma las notas de un estudiante
        print(suma_notas) #Probando que este funcionando
    #--Calcular el promedio de los alumnos
    media3 = suma_notas / (j + 1) # Hay que sumar 1 a j por que en el buecle solo llega hasta el 2

#metodo 2    
    i = 0 #-Variable para sacar lo promedios
    for nota in notas:
        suma_notas = suma_notas + nota #--Variable que suma las notas de un estudienate
        i = i + 1 #--Se suma la cantidad de veces que se suman las notas

media1 = suma_notas / len(notas) # Metodo 1: sin nececidad de un bucle
media2 = suma_notas / i # Metodo 2: utilizando la variable i
print(media1)
print(media2)
print(media3)

#--Con un bucle sacar el promedio de la clase--
total_notas = 0 #--Variable para la suma de todas las notas
num_notas = 0 #--Variable para contar el total de las notas

for data in database:
    notas = data[1] #--Variable que muestra las notas de cada estudiante
    total_notas = total_notas + sum(notas) # Sumando las notas de cada estudiante 
    
    num_notas = num_notas + len(notas) # Contando el total de notas de cada estudiante

media_clase = total_notas / num_notas # Calculando el promedio de la clase
print(media_clase)