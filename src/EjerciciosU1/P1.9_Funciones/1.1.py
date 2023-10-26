"""1.1 => recibe un nombre y retorna una cadena de caracteres con el resultado.

"""
def saludo(nombre) :
    saludo = f"Hola, {nombre}!"
    return saludo

print (saludo(str(input("Introduce tu nombre: "))))