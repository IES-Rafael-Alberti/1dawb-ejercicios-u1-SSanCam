"""Escribir un programa que pregunte por consola el precio de un producto en euros 
con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido."""

precio_total = float(input("Introduce el precio del articulo: "))

precio_formateado = "{:.2f}".format(precio_total)
decimales = precio_formateado.find(".")
euros = precio_formateado[:decimales]
centimos = precio_formateado[decimales + 1:]

print(f"El precio fraccionado es de: {euros} euros y {centimos} centimos.")

"""
precio = str(precio).split(".")    
precio[0] -> euros
precio[1] -> centimos
#EL PRECIO SE CONVIERTE EN UNA LISTA, LA IMPRIMIRLA SALDRA EN TERMINAL DE LA SIGUIENTE FORMA:
["Euros", "Centimos"]
"""