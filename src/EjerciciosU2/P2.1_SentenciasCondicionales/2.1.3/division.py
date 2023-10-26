def op_division (numero1, numero2):
    
    if (numero2 == 0):
        return "Error. No puede dividirse entre 0."
    else:
        division = numero1 / numero2
        division_formateada = "{:.2f}".format(division)
        return division_formateada
        
    