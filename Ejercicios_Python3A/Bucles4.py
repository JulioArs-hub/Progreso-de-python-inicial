#4. Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
#pantalla el número de veces que aparece la letra en la frase

frase = input("Ingrese una frase: ")
Letra = input("Ingrese la letra que quierer detectar: ")
cant = 0

for i in range(0, len(frase)):
    if Letra == frase[i]:
        cant = cant + 1

print("La letra", Letra, "aparece", cant, "veces")