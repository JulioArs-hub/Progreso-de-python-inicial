#ANALISIS DE VENTAS:
#Supongamos que eres el propietario de una tienda en línea y tienes una lista de ventas de los
#últimos 30 días. Quieres analizar las ventas por día de la semana para identificar los días de mayor
#venta

#--Esto es para ahorrarme tiempo en la lista de ventas y no tener que dfinir 30 variables una por una--
import random

#--Definir una lasita con los dias de la semana--
dia_semana = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']

#--Lista de ventas por dia de la semana--
datos_venta = []
#--Lista de los dias de cada semana con mayor ventas--
mayor_venta = []
#--Variable para usr en el bucle while
dias = 0

#--En este bcle se recorrera los treinta dias y se esxtreran las ventas por dia y los dias con myor venta--
while dias <= 30: 
    top_ventas = 0 #Variable para enlistar la venta mayor de la semana
    for dia in dia_semana: #Se leen los dias de la semana
        ventas = random.randint(1,100) #Esta variable definira la cantidad de ventas de forma aleatoria
        if top_ventas < ventas: #Si la venta definida actual es menor a la anterior la actual tora el lugar de venta mayor
            top_ventas = ventas #Se define la Venta mayor
            dia_top = dia #Se define el dia de la venta mayor
        #Se suma el dia y las ventas del mismo
        datos_venta.append([dia,ventas])
        #Se le suma 1 al dia hasta llegar a 30
        dias += 1
    mayor_venta.append([dia, ventas]) #Suma el dato de venta mayor y el dia que le corresponde

#--Se muestra por consola la lista de ventas por dia y la lista de los dias con mayor venta de cada semana--
print(f'Ventas de los ultimos 30 dias: {datos_venta} \nDias de mayor venta: {mayor_venta}')
