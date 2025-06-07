#1 Pedir nombre de usuario
nombre = input("Ingresar nombre de usuario: ")

nombre = nombre.replace(".", "")

lenguaje = 'python'
mensaje = '¡Hola, ' + nombre.title() + ", estas usando " + lenguaje.title() + "!"

print(mensaje)