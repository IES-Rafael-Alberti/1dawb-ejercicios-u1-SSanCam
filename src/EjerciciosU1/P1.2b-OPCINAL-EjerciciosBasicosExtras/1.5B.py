"""EJ 2.6
Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%)."""

importe_bruto = float(input("Cual es el precio final del articulo?: "))
importe_siniva = importe_bruto - (importe_bruto * 0.1)
print(f"El articulo tiene un precio final de {importe_bruto:.2f}€ y tiene aplicado un IVA del 10%, su precio sin IVA es de: {importe_siniva:.2f}€.")
