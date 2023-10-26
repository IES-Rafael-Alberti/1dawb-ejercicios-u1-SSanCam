def tramoRenta (renta) :
    
    impositivo = 0
    
    if (renta < 10000):
        impositivo = "5%"
        
    if (renta >= 10000):
        impositivo = "15%"
        
    if (renta >= 20000):
        impositivo = "20%"
        
    if (renta >= 35000):
        impositivo = "30%"
        
    if (renta >= 60000):
        impositivo = "45%"
    
    impositivo_correspondiente = impositivo
    
    return impositivo_correspondiente

