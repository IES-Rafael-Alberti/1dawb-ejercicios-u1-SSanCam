def grupo(nombre, sexo):
    inicial = (nombre[0]).upper()
    if ((inicial > "M") and (sexo.upper() == "M")) or (inicial < "N") and (sexo.upper() == "H"):
        return "Perteneces al grupo A"
    else:
        return "Perteneces al grupo B"

print(grupo("antonio","h"))