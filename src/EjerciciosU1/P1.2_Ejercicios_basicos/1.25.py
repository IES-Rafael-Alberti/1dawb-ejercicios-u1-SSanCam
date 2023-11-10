"""Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, 
el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter."""

fecha_nacimiento = str(input("Introduce tu fecha de nacimiento con el fomato: DD/MM/AAAA: "))
fecha_nacimiento = fecha_nacimiento.split("/")

dia = fecha_nacimiento[0].zfill(2)
mes = fecha_nacimiento[1].zfill(2)
anio = fecha_nacimiento[2]

print("Fecha de nacimiento: ")
print(f"Dia: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")
