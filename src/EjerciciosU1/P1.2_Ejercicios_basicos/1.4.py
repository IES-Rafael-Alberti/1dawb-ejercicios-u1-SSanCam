"""Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida."""
temperatura_celcius = float(input("que temperatura, en grados Celsius, hace?: "))
conversion_fahrenheit = (temperatura_celcius * (9/5)) + 32

print(f"{temperatura_celcius} grados Celsius es en grados Fahrenheit: {conversion_fahrenheit}")
