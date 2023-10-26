"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""
def edad(anios: int):
    
    if (anios > 0 ):
        
        if (anios >= 18):
            mensaje = "Eres mayor de edad."
        else:
            mensaje = "Eres menor de edad."
            
        if (anios > 100):
            mensaje = "Relája, Nosferatus."
            
        return mensaje

print(edad(-3))


"""def main():
    try:
        anios = int(input("Por favor, ingresa tu edad: "))
        resultado = edad(anios)
        print(resultado)
    except ValueError:
        print("Ingresa una edad válida, por favor.")

if __name__ == "__main__":
    main()"""