"""Analizar las siguientes expresiones:
ancho / alto
ancho // 2
ancho / 2
ancho * 2
ancho * alto
(5 + 1) * 3
(5 + 1) / 3
Después mostrar resultado y tipo por pantalla de cada expresión para comprobar si habéis acertado.
La salida debe ser así:
ancho / alto = 1.4166666666666667 y es de tipo <class 'float'>"""
ancho = 10
alto = 5

operacion1 = ancho / alto
operacion2 = ancho // 2
operacion3 = ancho / 2
operacion4 = ancho * 2
operacion5 = ancho * alto 
operacion6 = (5 + 1) * 3
operacion7 = (5 + 1) / 3

print(f"{ancho} / {alto} = {operacion1} y es de tipo <class '{type(operacion1)}'> ")
print(f"{ancho} / 2 = {operacion2} y es de tipo <class '{type(operacion2)}'> ")
print(f"{ancho} / 2 = {operacion3} y es de tipo <class '{type(operacion3)}'> ")
print(f"{ancho} * 2 = {operacion4} y es de tipo <class '{type(operacion4)}'> ")
print(f"{ancho} / {alto} = {operacion5} y es de tipo <class '{type(operacion5)}'> ")
print(f"{(5 + 1) * 3} = {operacion6} y es de tipo <class '{type(operacion6)}'> ")
print(f"{(5 + 1) / 3} = {operacion7} y es de tipo <class '{type(operacion7)}'> ")

