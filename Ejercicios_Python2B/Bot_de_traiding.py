#Un bot de trading está programado para realizar ciertas acciones con respecto a un producto
#financiero. Crea un script de manera que dado un precio introducido por el usuario, si el precio del
#producto está por debajo de 100 dólares, el bot imprima por pantalla la orden de comprar. Si está
#entre 100 y 150 dolores (ambos incluidos) el bot deberá imprimir la orden de hold. Si el precio está
#estrictamente por encima de 150 el bot deberá imprimir la orden de vender.

precio = float(input("Introduce el precio del producto: "))

if precio < 100:
    print("Ordenden compra realizada")
elif precio >= 100 and precio < 150:
    print("Orden de holding realizada")
else:
    print("Orden de venta realizada")