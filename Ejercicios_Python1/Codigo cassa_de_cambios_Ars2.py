pesos = input("Ingresa la cantidad de pesos que desea convertir:  ")

pesos = float(pesos)

dolares = pesos / 1150

comision = dolares * 0.04

cantidadRecibida = dolares - comision

print("Monto ingresado: ", pesos, "$ pesos.", 
      "\nCambio en dolares: ", dolares, "$ dolares.", 
      "\nComision por la gestion: ", comision, "$ dolares.", 
      "\nMonto recibido: ", cantidadRecibida, "$ dolares." )
