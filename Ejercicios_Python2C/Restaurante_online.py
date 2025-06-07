# En una hamburguesería han abierto la posibilidad de hacer pedidos online. Ofrecen básicamente
# dos productos de fama mundial: su hamburguesa clásica y la hamburguesa vegana.
# Los ingredientes extra de la hamburguesa clásica son:
# - Queso Idiazabal
# - Bacon
# - Huevo
# Los ingredientes extra de la hamburguesa vegana son:
# - Tofu
# - Cebolla caramelizada
# Crea un script que le pregunte al usuario que tipo de hamburguesa quiere. En función de la
# respuesta debe enseñarle los ingredientes extra disponibles y permitirle escoger uno de ellos.
# Finalmente debe imprimir por pantalla que tipo de hamburguesa se ha elegido y cuales son sus
# ingrediente

burger = input("Que hamburguesa dea pedir 'clasica'/'vegana' ")

if burger.lower() == "vegana":
    extra = input("Quiere agregar un ingrediente extra \n" \
    "Tofu\n" \
    "cebolla (Cebolla Caramelizada)\n")
    if extra.lower() == "tofu":
        print("Hamburguesa Vegana Con Tofu")
    elif extra.lower() == "Cebolla":
        print("Hamburguesa Vegana con Cebolla Caramelizada")
    else:
        print("El ingrediete elegido no esta disponible")
elif burger.lower() == "clasica":
    extra = input("Quiere agregar un ingrediente extra\n" \
    "Queso (Queso Idiazabal)\n" \
    "Bacon\n" \
    "Huevo\n")
    if extra.lower() == "queso":
        print("Hamburguesa Clasica con Queso Idiazabal")
    elif extra.lower() == "bacon":
        print("Hamburguesa Clasica con Bacon")
    elif extra.lower() == "huevo":
        print("Hamburguesa Clasica con Huevo")
    else:
        print("El ingrediente no esta disponible")
else:
    print("La hamburguesa elegida no esta diponible" \
    "Vuelava a iniciar su orden.")