def contrasenia(cadena: str):
    password = "aytortilla"
    
    if cadena.lower() == password:
        return "Contraseña correcta."
    else:
        return "Contraseña incorrecta."