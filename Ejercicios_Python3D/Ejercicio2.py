
#VALIDAR ACCESO A UN SITIO WEB:
#Supongamos que eres un administrador de sistemas y necesitas validar el acceso de los usuarios
#a un sitio web. Crea un script que verifique si el nombre de usuario y la contraseña ingresados son
#correctos y permita el acceso solo si ambos son correctos


#--Definir una lista anidada con los usuarios y sus contrasenhas
user_paswd = [['user1','usr321'],['user2','usr231'],['user3','usr123']]

#Variables que se utilizan para confirmar el acceso
acceso = False
acceso_con = False

#--En este Bucle se solicitara y confirmaran el usuario y contrasenha--
while acceso == False: #Mientras permanesca en "False" el bucle no terminara
    ingreso_user = input('Ingresa el nombre de usuario: \n') #Se solicita que se ingrese un usuario
    #--Se recorrera cada usuario de la lista
    for user in user_paswd:
        if ingreso_user == user[0]: #Si el usuario ingresado coincide con uno de le lista se procedera a solicitar la contrasenha
            while acceso_con == False: #El buche se Mantendra hasta que se ingrese la contrasenha correcta
                ingreso_pasw = input('Inrgresa la contrasenha: \n') #Se solicita que se ingrese la contrasenha
                #--Se verifica si la contrasenha ingrasada coincide con la del usuario
                if ingreso_pasw == user[1]:
                    #Si la contrasenha ingresada es correcta se avisara que es la correcta con unmmesaje y dara fin al bucle
                    print('Contrasenha correcta \nAcceso Concedido')
                    acceso = True
                    acceso_con = True
                else:
                    #En caso de no ser la correcta se pedira que vuelva a ingresar la contrasenha
                    print('Contrasenha incorrecta \nVuelva a intentarlo')


