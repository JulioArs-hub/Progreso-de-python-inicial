long1 = float(input("Introduce la longitud uno: "))
long2 = float(input("Introduce la longitud dos: "))
long3 = float(input("Introduce la longitud tres: "))

if long1 + long2 > long3 and long2 + long3 > long1 and long1 + long3 > long2:
    print("Es poseible construir la estructura")
else:
    print("No es posible construir la estructura")