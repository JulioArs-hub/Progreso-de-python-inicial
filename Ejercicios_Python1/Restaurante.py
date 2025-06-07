#RESTAURANTE:
#En un restaurante el menú consta de las siguientes opciones:
#Ensalada mixta ———————— 12 EU
#Sopa de pescado ——————— 10 EU
#Dorada al horno ———————— 18 EU
#Arroz al curry ————————— 14 EU
#Lasaña de carne ——————— 15 EU
#Brownie de chocolate ————— 8 EU
#Helado ——————————— 6 EU
#Refrescos —————————— 5,5 EU
#Café ———————————— 3,5 EU
#Escribe un script que lea la cantidad de cada alimento consumido y que calcule e imprima el total
#de la cuenta.

ensaladaMix = input("Total de Ensalada ordenado: ")
sopaPescado = input("Totalde Sopa de Pescado ordando: ")
doradaAlHorno = input("Total de Dorada Al Horno ordenado: ")
ArrosAlCurry = input("Total de Arroz Al Curry ordenado: ")
lasanaCarne = input("Total de Lasaña de Carne ordenado: ")
brownie = input("Total de Brownie de Chocolate ordenado: ")
helado = input("Total de Helado ordenado: ")
refresco = input("Total de Refresco orfenado: ")
cafe = input("Total de Café ordenado: ")

total = float(ensaladaMix) * 12 + \
     float(sopaPescado) * 10 + \
     float(doradaAlHorno) * 18 + \
     float(ArrosAlCurry) * 14 + \
     float(lasanaCarne) * 15 + \
     float(brownie) * 8 + \
     float(helado) * 6 + \
     float(refresco) * 5.5 + \
     float(cafe) * 3.5

print("Total de la cuenta es: ", total, "Euros")