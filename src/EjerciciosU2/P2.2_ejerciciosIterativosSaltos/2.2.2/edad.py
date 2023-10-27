def contadorEdad (fecNac):
    
    aniosCumplidos = []
    
    for i in range(1,fecNac + 1):
        aniosCumplidos.append(i)       
    
    return aniosCumplidos 
        
print(contadorEdad(10))