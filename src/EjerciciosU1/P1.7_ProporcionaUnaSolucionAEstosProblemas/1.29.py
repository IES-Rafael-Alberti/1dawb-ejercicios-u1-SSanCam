"""Ejercicio 1.29
Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que solicite un nombre y una edad.
Si el nombre está vacío, debes utilizar el valor "Desconocido". 
La edad debe pedirla hasta que introduzca una edad comprendida entre 0 y 125 años.
El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".
El pseudocódigo debes incluirlo como comentarios en el programa de Python."""

"""PSEUDOCÓDIGO
Inicio
    Leer nombre
    Leer edad
    
    anios_por_cumplir = (125 - edad)
    
    Si (nombre = "") entonces
        nombre = "Desconocido."
    
    Mientras (edad not in (0..125)) hacer
        Leer edad
    
    Escribir "Te llamas " + nombre + " y tienes " + edad + ", te quedan aún " + anios_por_cumplir + " años por cumplir."
    
Fin
"""

#Inicio
#Leer nombre
nombre = str(input("Introduce tu nombre: "))
#Leer edad
edad = int(input("Introduce tu edad: "))
#anios_por_cumplir = (125 - edad)
anios_por_cumplir = 125 - edad

#Si (nombre = "") entonces
if (nombre == "") :
    #nombre = "Desconocido."
    nombre = "Desconocido"
    
#Mientras (edad not in (0..125)) hacer
while (edad < 0 or edad > 125):
    print("Error.")
    #Leer edad
    edad = int(input("Introduce tu edad: "))
    
#Escribir "Te llamas " + nombre + " y tienes " + edad + ", te quedan aún " + anios_por_cumplir + " años por cumplir."
print (f"Te llamas {nombre} y tienes {edad} años, te quedan aún {anios_por_cumplir} años por cumplir.")
#Fin