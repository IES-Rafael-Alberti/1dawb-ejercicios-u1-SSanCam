"""1.5 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, 
sino que se imprime desde dentro de la función."""

def precio_final(importe: float, iva: int) :
    
    if (iva < 0 or iva > 100):
        iva =20
        iva_aplicar = (iva / 100) * importe
        print ("ERROR.")
        
    else:
        iva_aplicar = (iva / 100) * importe
        importe_total = importe + iva_aplicar
        resultado = (f"Precio de articulo: {importe}\nIVA a aplicar: {iva}%\nEl precio final es de: {importe_total:.2f} €.") 
        return resultado

importe = float(input("Cuanto cuesta el articulo?: "))
iva = int(input("Que porcentaje de IVA debe aplicarse?: "))

print(precio_final(importe,iva))