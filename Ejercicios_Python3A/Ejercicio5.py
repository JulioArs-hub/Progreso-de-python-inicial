#5. Crea un script dado un número introducido por el usuario o determinado al inicio del
#programa, realice la suma de aquellos números que sean divisibles por este

num_list = [5,4,6,3,7,2,1,10,11,15,13,14,12]

divisor = int(input("Introdusca un divisor: "))
resultado = 0

for num in num_list:
    if num % divisor == 0:
        resultado += num

print(resultado)