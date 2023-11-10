"""Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y 
muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos 
enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales."""

nombre_producto = str(input("Introduce el nombre del articulo: "))
precio = float(input("Introduce su precio: "))
unidades = int(input("Cuantas unidades necesitas?: "))
unidades_formateadas = "{:03d}".format(unidades)
precio_formateado = "{:06.2f}€".format(precio)
coste_total = "{:08.2f}€".format(precio * unidades)

print(f"Ticket:\n Nombre del producto: {nombre_producto}, precio unitario: {precio_formateado}, unidades: {unidades_formateadas}, coste total: {coste_total}")