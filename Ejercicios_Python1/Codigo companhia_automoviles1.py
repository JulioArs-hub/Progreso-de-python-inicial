Kangoo_precio = 32.28 * 10**6
Kwid_precio = 19.12 * 10**6
Sandero_precio = 25.62 * 10**6

comision = 0.04

cantVen_Kangoo = int(input("Cantidad del Modelo Kangoo vendidas: "))
cantVen_Kwid = int(input("Cantidad del modelo Kwid vendidas: "))
cantVen_Sandero = int(input("Cantidad del modelo Sandero Vendidas: "))

totalEnCom = (cantVen_Kangoo * Kangoo_precio + cantVen_Kwid * Kwid_precio + cantVen_Sandero * Sandero_precio) * comision

print("Total de ganancia en comisiones en el mes es de: ", totalEnCom, "$ pesos")