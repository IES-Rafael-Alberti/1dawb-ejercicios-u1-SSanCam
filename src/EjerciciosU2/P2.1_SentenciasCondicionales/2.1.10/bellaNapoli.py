"""
print("Indica si quieres pizza [V]egetariana o [NV] No Vegetariana.")
print("Introduce el número del ingrediente que desees:\n ·Vegetarianos:\n1.-Pimientos.\n2.-Tofu.")
print("No Vegetarianos:\n1.-Peperoni\n2.-Jamón\n3.-Salmón.")
"""

def pedidoPizza(tipoPizza, ingrediente):

    if (tipoPizza.upper() == "V"):
        tipoPizza = "Vegetariana."
        if (ingrediente == 1):
            ingrediente = "3.-Pimientos"
            return "Has elegido pizza vegetariana con: salsa de tomate, queso y pimiento"
        else:
            ingrediente = "3.-Tofu"
            return "Has elegido pizza vegetariana con: salsa de tomate, queso y tofu"
    else:
        tipoPizza = "No vegetariana."
        if (ingrediente == 1):
            ingrediente = "3.-Peperoni"
            return "Has elegino pizza NO vegetariana con: salsa de tomate, queso y peperoni."
        if (ingrediente == 2):
            ingrediente = "3.-Jamón"
            return "Has elegino pizza NO vegetariana con: salsa de tomate, queso y jamón."
        else:
            return "Has elegino pizza NO vegetariana con: salsa de tomate, queso y salmón."
            
            
"""    
    cabecera1 = "**************************"
    ancho = len(cabecera1)
    
    nombre =("--BELLA NAPOLI--".center(ancho))
    opcion = (f"Has elegido pizza: {tipoPizza}").center(ancho)
    condumio =(f"Los ingredientes son: \n1.-Salsa de tomate\n2.-Queso\n{ingrediente}").center(ancho)
    
    ticket = f"{cabecera1}\n{nombre}\n{cabecera1}\n\n{opcion}\n{condumio}\n\n{cabecera1}"
    
    return ticket

print(pedidoPizza("v",2))
"""
