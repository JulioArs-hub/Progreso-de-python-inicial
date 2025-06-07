#Crea un script que acepte un string de 5 caracteres y devuelva otro string con todos los caracteres
#duplicados. Si el input es ‘sbc56’, el output deberá ser ‘ssbbcc5566’

duplicado = input("introduca una serie de 5 caracteres: ")

#una forma de realizarlo es dulplicando la posicion de cada caracter uno por uno

print(duplicado[0] + duplicado[0] + duplicado[1] + duplicado[1] + duplicado[2] + duplicado[2] + duplicado[3] + 
      duplicado[3] + duplicado[4] + duplicado[4])

#algo ma sensillo seria usar la multiplicacion para no tenre que repetir caracter por cararcter

print(duplicado[0] * 2 + duplicado[1]*2 + duplicado[2]*2 + duplicado[3]*2 + duplicado[4]*2)