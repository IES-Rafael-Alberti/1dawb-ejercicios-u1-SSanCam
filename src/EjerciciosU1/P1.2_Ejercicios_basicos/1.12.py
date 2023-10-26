"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales."""

kilogramos = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu estatura: "))
masa_corporal = kilogramos / (altura ** 2)
masa_corporal_formateada = "{:.2f}".format(masa_corporal)

print(f"Para tu peso de {kilogramos} y una altura de {altura} tu masa corporal es de: {masa_corporal_formateada}")