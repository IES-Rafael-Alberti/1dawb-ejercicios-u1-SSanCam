def repetir(palabra):
    serie = ""
    contador = 0
    
    while (contador != 9):
        serie += palabra + ", "
        contador += 1
        
    serie += palabra
    
    return serie


print (repetir("paco"))