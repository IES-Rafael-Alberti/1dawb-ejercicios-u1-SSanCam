def evaluacion(puntaje):
        
    if (puntaje == 0.0):
        bonificacion = 0.0 * 2400
        print(f"Con una puntuación de 0.0, tu nivel ha sido inaceptable.\nTu bonificación es de:")
        return "{:.2f}€".format(bonificacion)
    
    if (puntaje == 0.4):
        bonificacion = 0.4 * 2400
        print (f"Con una puntuación de 0.4, tu nivel ha sido aceptable.\nTu bonificación es de:" )
        return "{:.2f}€".format(bonificacion)
    
    if (puntaje == 0.6):
        bonificacion = 0.6 * 2400
        print(f"Con una puntuación de 0.6, tu nivel ha sido meritorio.\nTu bonificación es de:")
        return "{:.2f}€".format(bonificacion) 
