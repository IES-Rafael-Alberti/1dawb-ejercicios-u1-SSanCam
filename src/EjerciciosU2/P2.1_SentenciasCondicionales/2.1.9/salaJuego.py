def entrada(edad):
    
    precioEntrada = 0
    
    if (edad < 4):
        precioEntrada = 0
        print("El precio de tu entrada es de: ")
        precio = ("{:.2f}€".format(precioEntrada))
        return precio
    
    if (edad >=4 and edad < 18):
        precioEntrada = 5
        print("El precio de tu entrada es de: ")
        precio = ("{:.2f}€".format(precioEntrada))
        return precio    
    else :
        precioEntrada = 10
        precio = ("{:.2f}€".format(precioEntrada))
        return precio
    
