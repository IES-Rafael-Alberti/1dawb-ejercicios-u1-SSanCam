def serieImpares (numero: int):
    serieImpar = []   
    
    for num in range(1,numero+1):
        
        serieImpar.append(num)
            
    return serieImpar[::2]

print (serieImpares(43))
            