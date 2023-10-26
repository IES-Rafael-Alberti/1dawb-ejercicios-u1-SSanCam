"""Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo."""

precio_articulo = float(input("Cuanto cuesta el articulo?: "))
iva = float(input("Que porcentaje de IVA debe aplicarse?: "))
iva_aplicar = (iva / 100) * precio_articulo
importe_total = precio_articulo + iva_aplicar

print(f"Precio de articulo: {precio_articulo}\nIVA a aplicar: {iva_aplicar}")
print(f"El precio final es de: {importe_total} €.")