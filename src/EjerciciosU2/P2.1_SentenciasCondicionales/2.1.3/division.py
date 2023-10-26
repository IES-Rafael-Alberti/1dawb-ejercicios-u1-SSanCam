"""Escribir un programa que pida al usuario dos números y muestre por pantalla su 
división. Si el divisor es cero el programa debe mostrar un error."""

def operacion_div ():
    
    try:
        
        print("Vamos a realizar una división.")
        num1 = float(input("Introduce un número: "))
        num2 = float(input("Introduce otro número: "))
                
        if (num2 != 0):
            return f"La división de {num1}/{num2} da como resultado: {num1/num2:.2f}"
        
    except(ZeroDivisionError):
        return "ERROR.\nNo puede dividirse entre 0."
    
