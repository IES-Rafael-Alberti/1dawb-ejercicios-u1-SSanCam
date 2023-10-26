"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""

def cadena():
    password = "aytortilla"
    contrasenia = str(input("Introduce la contraseña: "))
    
    if (contrasenia.lower() == password):
        return "La contraseña es correcta."
    else:
        return "Contraseña incorrecta."
    
print(cadena())