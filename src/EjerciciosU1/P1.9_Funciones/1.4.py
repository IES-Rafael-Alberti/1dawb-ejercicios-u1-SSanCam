"""1.4 => NO recibe parámetros y retorna la temperatura convertida en grados Celsius. 
Dentro de la función se pedirá al usuario los grados Farenheit.
"""
def conversor_temperatura ():
    
    temperatura_celcius = float(input("¿Que temperatura, en grados Celsius, hace?: "))
    conversion_fahrenheit = (temperatura_celcius * 1.8) + 32

    return print(f"{temperatura_celcius}º Celsius es en grados Fahrenheit: {conversion_fahrenheit:.1f}º")

print(conversor_temperatura())