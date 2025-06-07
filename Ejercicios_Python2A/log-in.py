#Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta).
#Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe
#indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la
#contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
#Cambia el script para que no distinga entre mayúsculas y minúsculas.
#(Pista: Necesitarás in If Statement anidado)

pasw = "user123"

contr = input("Introduce la contraseña: ")

if contr.lower() == pasw:
    print("Bienvenido Usuario")
else:
    print("Contraseña incorrecta")
    contr = input("Introduce la contraseña: ")
    if contr.lower() == pasw:
        print("Bienvenido Usuario")
    else:
        print("Contraseña incorrecta")