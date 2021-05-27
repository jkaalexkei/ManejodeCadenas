
def ManejodeCadenas():

    correo = input("Ingresa un correo para comprobar: ")

    resul = correo.rfind(".")

    num = 1
    for i in correo:
        if (num == correo.rindex(".")):
            print("se consiguio el punto en la posicion: ",num)
        num = num +1


ManejodeCadenas()

