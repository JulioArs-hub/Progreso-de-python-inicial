nombre = input("Ingrsa tu Nombre: ")

print ("hola, ", nombre, ", Bienvenido")

pago_por_hora = float(input("Pagos por hora: "))

horasTrabajo = int(input("Ingresa tus horas de trabajo diario: "))

horas_extras = int(input("Horas extras trabajadas: "))

salario_semanal = (pago_por_hora * (horasTrabajo * 5)) + (horas_extras * (pago_por_hora * 0.5))

salario_anual =(pago_por_hora * (horasTrabajo * 5)) * 52

print(nombre.title(), "Tus ingresos semanales son de: ", salario_semanal, "$ pesos.")

print("Y tus ingreso anual (sin contar extras) es de: ", salario_anual, "$ pesos")

gastos_semanales = float(input("Ingresa tus gastos semanales: "))

gasto_anual = gastos_semanales * 52

ahorro = salario_anual - gasto_anual

print("Tu ahorro anual sera de", ahorro, "$ pesos")