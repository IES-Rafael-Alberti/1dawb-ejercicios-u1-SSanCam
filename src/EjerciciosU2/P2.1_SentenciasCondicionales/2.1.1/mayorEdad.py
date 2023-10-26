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