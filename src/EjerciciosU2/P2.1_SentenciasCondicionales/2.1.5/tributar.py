def tributar (edad: int, ingresos: float):
    
    if (edad > 16) and (ingresos >= 1000):
        return "Te toca tributar."
    
    if (edad < 16):
        return "Aún tienes que pasar la edad del pavo, no tributas."
    
    if (ingresos < 1000):
        return ("Estás un poco tieso, no tributes.")
    
"""    
edad = int(input("Introduce tu edad: "))
ingresos = float(input("Introduce tus ingresos mensuales: "))

print (tributar(edad,ingresos))"""