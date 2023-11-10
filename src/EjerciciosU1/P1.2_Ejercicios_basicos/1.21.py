"""Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida."""

frase = str(input("Introduce una frase: "))

frase_invertida = ""

for caracter in frase[::-1]:
    frase_invertida += caracter
    
print(frase_invertida)