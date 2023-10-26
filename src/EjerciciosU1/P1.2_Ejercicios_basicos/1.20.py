"""Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, 
y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 

Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión."""

numero_telefono = str(input("Introduce tu número de teléfono, incluyendo el prefijo y su extension: "))
numero = numero_telefono[4:13]

print(f"Tu numero sin prefijo ni extensión es: {numero}")

"""
numero = input("introduce un numero con el formato +34-913724710-56")
contador = numero.split('-')
if len(numero) == 16 and numero[0] == '+' :
    if len(contador[1]) == 9 :
        print(contador[1])
"""