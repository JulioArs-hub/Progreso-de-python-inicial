#1. Crea una lista llamada frutas que contengan los siguientes nombres de frutas como cadenas
#de caracteres: manzana, plátano, cereza, pera, higo, frambuesa y fresa.
#2. Usa la función len() para imprimir la longitud de la lista frutas.
#3. Accede al objeto numero 3 de la lista e imprímelo or consola.
#4. Modifica el segundo objeto de la lista y cambiado a mora.
#5. Añade el string mango al final de la lista.
#6. Usa el método insert() y añade el string “uva“ año comienzo de la lista.
#7. Usa un bucle para recorrer la lista e imprimir cada fruta por la consola
#8. Usa el método pop() para eliminar el último elemento de la lista y guárdalo en una variable
#llamada “ultima_fruta“.
#9. Realiza un bucle que recorra la lista e imprima cada una de las frutas por consola
#10. Modifica el script para que imprima también la longitud de cada nombre de fruta por consola
#11. Modifica el script para que recorra la lista de frutas y solo imprima aquellos nombres que
#tengan más de 5 caracteres
#12. Usa el método remove() para borrar el string “cereza“ de la lista.
#13. Usa el método clear() para vaciar la lista.
#Recomendación: En cada paso comprueba que el código hace aquello que quieres

frutas = ['manzana','platáno', 'cereza', 'pera','higo','frambuesa','frutilla']

# 2- Utilizar funcion len() para imprimir la longitud de la lista
print("2", len(frutas))

# 3- Acceder al objeto 3 de la lista
print("3",frutas[2])

# 4- Cambiar el segundo objeto de la lista a mora
frutas[1] = 'mora'
print("4",frutas)

# 5- Añadir mango al final de la lista
frutas.append('mango')
print("5",frutas)

# 6- Con el comando 'insert' añadir a la lista el string 'uva'
frutas.insert(0,'uva')
print("6",frutas)

# 7- Utilizar un bucle para imprimir en consola cada una de las frutas de la lista
for nuF in range(0,len(frutas)):
    print("7",frutas[nuF])

# 8- Eliminar el ultimo objeto de la lista y agregarlo en una nueva variable llamda
# ultima_fruta con el comando pop()
ultima_fruta = frutas.pop()

print("8",frutas)
print("8",ultima_fruta)

# 9- Realizan un bucle que recorra toda la lista de frutas
for fruta in frutas:
    print("9",fruta)

# 10- Imprimir la longitud de cada objeto de la lista
for fruta in frutas:
    print(f"10- fruta {fruta}. longitud {len(fruta)}")

# 11- Recorrer la lista de frutas e imprimir los que tienen 5 o mas caracteres
for fruta in frutas:
    if len(fruta) >= 5:
        print("11-",fruta)

# 12- Utilizar el metodo remove() para borrar de la lista el string cereza
frutas.remove('cereza')
print("12-",frutas)

# 13- Utilizar el metodo clear para vaciar la lista
frutas.clear()
print("13-",frutas)