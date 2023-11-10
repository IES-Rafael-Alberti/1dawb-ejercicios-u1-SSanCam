"""Formatear la salida de los grados Farenheit a dos posiciones decimales.
Mostrar en pantalla "La temperatura en grados Farenheit es 0.00ºF (0.00ºC)" """

grados_celsius = float(input("Introduce la temperatura en grados Celsius: "))

conversion_fahrenheit = (grados_celsius * (9/5)) + 32

fahrenheit_formateado = "{:.2f}ºF".format(conversion_fahrenheit)
celsius_formateado = "{:.2f}ºC".format(grados_celsius)
print(f"{celsius_formateado} (grados Celsius) convertidos en grados Fahrenheit es: {fahrenheit_formateado}")