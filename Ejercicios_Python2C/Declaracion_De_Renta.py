# Para tributar en un determinado país es necesario ser mayor de edad y cobrar más de 1000 euros
# al mes. Además los tramos impositivos de la renta anual son los siguientes:
# RENTA TIPO IMPOSITIVO
# Menos de 15.000 eu 5%
# Entre 15.000 y 25.000 eu 15%
# Entre 25.000 y 35.000 eu 20%
# Entre 35.000 y 60.000 eu 30%
# Más de 60.000 eu 45%
# Escribe un script que primero compruebe si eres susceptible de que se te aplique algún tipo
# impositivo y en caso afirmativo imprima por pantalla cuál te tocaría.

edad = int(input("Introdusca se edad: "))
ingr = float(input("Introduce el total de tus ingresos: "))

ingr_anual = ingr * 12

if edad >= 18 and ingr >= 1000:
    if ingr_anual < 15000:
        print("La renta correspondiente es del 5%: ", ingr * 0.05, "Euros")
    elif ingr_anual < 25000:
        print("La renta correspondiente es del 15%: ", ingr * 0.15, "Euros")
    elif ingr_anual < 35000:
        print("La renta correspondiente es del 20%: ", ingr * 0.20, "Euros")
    elif ingr_anual < 60000:
        print("La renta correspondiente es del 30%: ", ingr * 0.30, "Euros")
    else:
        print("La renta correspondiente es del 45%: ", ingr * 0.45, "Euros")
else:
    print("No eres suseptible de tributar")