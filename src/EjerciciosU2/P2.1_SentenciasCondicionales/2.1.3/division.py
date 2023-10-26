def op_division (numero1, numero2):
    
    if (numero2 == 0):
        return "Error. No puede dividirse entre 0."
    else:
        division = numero1 / numero2
        return "{:.2f}".format(division)
        
    