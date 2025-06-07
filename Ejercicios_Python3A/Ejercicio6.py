#6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto
#que es inferior al número introducido o determinado al inicio del programa.

num_list = [5,4,6,3,7,2,1,10,11,15,13,14,12]
num_user = int(input("Introduce un nuero: "))

for num in sorted(num_list):
    
    if num < num_user:
        num_men = num

print(num_men)