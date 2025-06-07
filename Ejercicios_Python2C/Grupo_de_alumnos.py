#En uno de los cursos se ha dividido a una clase en dos grupos A y B. Para mezclar a los alumnos
#lo mejor posible se ha asignado a todas las chicas con nombres empezando por la letra E hasta la
# M en el grupo A y el resto en el B. A los chicos con nombres empezando por la letra A hasta la H y
# R hasta la Z se les ha asignado al grupo A también, el resto están en el B.
#Crea un script que pregunte al usuario si es chica o chico y el nombre. El script debe mostrar por
#pantalla el grupo que le corresponde a ese alumno.

nom = input("Introduce tu nombre: ")
gen = input("¿Eres chico/chica? ")

GruP_A_fem = "EFGHIJKLM"
GruP_A_hom = "ABCDFGHRSTUBWXYZ"

if gen.lower() == "chica":
    if nom[0].upper() in GruP_A_fem:
        print("Tu grupo correspondiente es el A")
    else:
        print("Tu grupo correspondiente es el B")
elif gen.lower() == "chico":
    if nom[0].upper() == GruP_A_hom:
        print("Tu grupo correspondiente es el A")
    else:
        print("Tu grupo correspondiente es el B")
else:
    print("Hubo un error reinicie el programa")