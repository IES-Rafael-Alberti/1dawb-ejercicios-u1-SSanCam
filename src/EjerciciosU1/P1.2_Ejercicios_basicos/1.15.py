"""Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final 
de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en 
la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla 
la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

Calcula el interés: capital * (1 + interes)"""

capital = float(input("Introduce tu capital en la cuenta de ahorros: "))
capital_interes = 0

print(f"A lo largo de 3 años, con un capital de {capital} habrás ahorrado: ")

for años in range(1, 4):
    interes = capital * 0.04
    capital_interes += interes
    capital += capital_interes  # Sumar los intereses acumulados al capital para el próximo año
    
    print(f"En el {años}º año, el ahorro es de {interes:.2f}€ y el fondo de ahorros es de: {capital:.2f}€.")
