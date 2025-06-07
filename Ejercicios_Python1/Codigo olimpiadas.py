#OLIMPIADAS:
#En la competición de skeleton de las olimpiadas de invierno hay tres finalistas. El cronómetro mide
#los siguientes tiempos:
#Hannah Neise: 8 minutos 3 segundos y 10 centésimas
#Jackie Narracott: 12 minutos 7 segundos y 8 centésimas
#Kimberley Bos: 9 minutos 14 segundos y 3 centésimas
#1. Crea un script que pida los tiempos por pantalla para cada uno de los finalistas
#2. Convierte los tiempos de minutos-segundos-centésimas a segundos
#3. Sabiendo que la pista es de 100 metros calcula la velocidad media de cada uno de ellos en
#metros por segundo.
#4. Imprime los resultados por pantalla

Hanna = (input("Total de minutos en el que Hanna hizo los 100m (min seg cen): "))
Jakie = input("Total de minutos en el que Jakie hizo los 100m (min seg cen): ")
Kimberley = input("Total de minutos en el que Kimberley hizo los 100m (min seg cen): ")

min_hanna, seg_hanna, cen_hanna = Hanna.split(" ")
min_jakie, seg_jakie, cen_jakie = Jakie.split(" ")
min_kimberley, seg_kimberley, cen_kimberley = Kimberley.split(" ")

Hanna = float(min_hanna) * 60 + float(seg_hanna) + float(cen_hanna) * 0.01
Jakie = float(min_jakie) * 60 + float(seg_jakie) + float(cen_jakie) * 0.01
Kimberley = float(min_kimberley) * 60 + float(seg_kimberley) + float(cen_kimberley) * 0.01

vel_hanna = 100.0 / Hanna
vel_jakie = 100.0 / Jakie
vel_kimberley = 100.0 / Kimberley

print("Velocidad de los Participante: \n", 
      vel_hanna, "Metros por segundo", "\n", 
      vel_jakie, "Metros por segundo", "\n", 
      vel_kimberley, "Metros por segundo" )