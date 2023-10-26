"""EJ 2.7
Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma."""
cantidad_numeros = 3
cantidad_total = 0.0

while cantidad_numeros != 0 :
    cantidad_total += float(input("Introduce un numero: "))
    cantidad_numeros -= 1

media_final = cantidad_total / 3

print(f"La suma total es de {cantidad_total:.2f}, y la media es de: {media_final:.2f}")
