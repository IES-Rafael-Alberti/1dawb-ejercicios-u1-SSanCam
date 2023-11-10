"""Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), 
el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas."""

barra_pan = 3.49
descuento = barra_pan * 0.6


pan_vendido = float(input("Cuantas barras de pan se han vendido que no son de hoy?: "))
total_vendido = pan_vendido * barra_pan
total_descuento = total_vendido - (total_vendido * 0.6)

nombre_tienda = "***********PANADERIA PEPI***********"
longitud_nombre_tienda = len(nombre_tienda)

print("____________________________________")
print(nombre_tienda)
print("____________________________________")
print(f"Se ha vendido {pan_vendido} unidades.".center(longitud_nombre_tienda))
print(f"Total: {total_vendido:.2f}".center(longitud_nombre_tienda))
print(f"Descuento del 60%: {descuento:.2f}€".center(longitud_nombre_tienda))
print(f"Total con descuento: {total_descuento:.2f}€".center(longitud_nombre_tienda))
print("____________________________________")

