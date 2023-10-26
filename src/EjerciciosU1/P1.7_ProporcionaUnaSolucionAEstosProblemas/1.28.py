"""Ejercicio 1.28
Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que :
lea dos números enteros, muestre cuál es el menor de los dos y cuantos números existen entre ellos dos.
El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
Si los números son diferentes, por ejemplo 5 y 12 debe mostrar la frase "El número menor es el 5 y entre ellos existen 7 números enteros".
El pseudocódigo debes incluirlo como comentarios en el programa de Python."""

"""PSEUDOCÓDIGO:
Inicio

    Lee numero1
    Lee numero2 
    
    Si (numero1 == numero2) entonces
        Escribe "Los números no pueden ser iguales" 
        
    cantidad_numeros = numero1 - numero2    

    Si (numero1 != numero2) entonces
        Si (numero1 > numero2) entonces
            Escribe numero1 + " es mayor que " + numero2 + " y entre ellos existen " + contador + " números enteros."
        Sino
            Escribe numero1 + " es menor que " + numero2 + " y entre ellos existen " + contador + " números enteros."
            
Fin
"""
#Código con el Pseudocódigo comentado:

#Inicio
#Lee numero1
numero1 = int(input("Introduce un número entero: "))
#Lee numero2 
numero2 = int(input("Introduce otro número entero: "))

#cantidad_numeros = numero1 - numero2 
cantidad_numeros = abs(numero1 - numero2)

#Si (numero1 != numero2) entonces
if (numero1 == numero2) :
    #Escribe "Los números no pueden ser iguales" 
    print("Los números no pueden ser iguales.")

#Si (numero1 != numero2) entonces
if (numero1 != numero2):
    #Si (numero1 > numero2) entonces
    if (numero1 > numero2):
        #Escribe numero1 + " es mayor que " + numero2 + " y entre ellos existen " + contador + " números enteros."
        print(f"{numero1} es mayor que {numero2} y entre ellos existen {cantidad_numeros} números entre ellos.")
    #Sino
    else:
        #Escribe numero1 + " es menor que " + numero2 + " y entre ellos existen " + contador + " números enteros."
        print(f"{numero1} es menor que {numero2} y entre ellos existen {cantidad_numeros} números entre ellos.")
#Fin