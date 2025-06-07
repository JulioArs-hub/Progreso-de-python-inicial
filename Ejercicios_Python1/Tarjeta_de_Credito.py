#TARJETA DE CRÉDITO:
#Crea un script que reciba como input un número de tarjeta de crédito e imprima por pantalla todos
#los caracteres en forma de asterisco salvo los últimos cuatro. Si por ejemplo el número de tarjeta
#es 1234 2345 3456 5678, el output deberá ser **** **** **** 5678

#Pedir los numeros de la tarjeta.

tarjeta = input("Ingresa Tu numero de Tarjeta: ")

#Mostramos por consola los ultimos 4 numero indicando con asteriscos los primero 12
# e indicando las posicion de los ultimos 4 numeros de la tarjeta.

print("**** **** ****", tarjeta[12:16])

#Mediante el comando "len (Longitud)" se puede realizar otra forma el mismo algoritmo

longitud = len(tarjeta)

#Con este metodo podemos usar la Longitud para usar "loongitud-4" para marcar el desde donde
# se quiere que se identifique el numero a mostrar hasta "longitud" que es el total de numeros que se han esecrito
"El * y otros numero del mismo tipo se pueden multiplicar por numeros enteros y segun el numero indicado"
"se va a mostrar el total en cantidad de caracteres"

print("*" * (longitud-4), tarjeta[longitud-4:longitud])