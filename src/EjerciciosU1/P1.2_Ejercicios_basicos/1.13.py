"""Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: 
"la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, 
y c y r son el cociente y el resto de la división entera respectivamente."""

n = int(input("Introduce un dividendo: "))
m = int(input("Introduce un vidisor, distinto de 0: "))

c = n // m 
r = n % m

print(f"La division de {n} entre {m} da como resultado un cociente de {c} y un resto de {r}")