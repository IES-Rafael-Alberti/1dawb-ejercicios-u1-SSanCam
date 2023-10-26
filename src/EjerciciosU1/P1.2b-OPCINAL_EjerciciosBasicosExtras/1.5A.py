"""Ejercicios 1.5 al 1.10
Usar tipos de datos float y mostrar con 2 posiciones decimales."""

"""EJ 2.5
Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo."""

precio_articulo = float(input("Cuanto cuesta el articulo?: "))
iva = float(input("Que porcentaje de IVA debe aplicarse?: "))
iva_aplicar = (iva / 100) * precio_articulo
importe_total = precio_articulo + iva_aplicar
importe_total_formateado = "{:.2f}€".format(importe_total)

print(f"El precio final es de: {importe_total_formateado}.")
