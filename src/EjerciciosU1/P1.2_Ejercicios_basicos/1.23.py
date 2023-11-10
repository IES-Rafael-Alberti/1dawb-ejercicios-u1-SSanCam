"""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla 
otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es."""
correo_electronico = str(input("Introduce tu correo electronico: "))

posicion_arroba = correo_electronico.find("@")
nombre_usuario = correo_electronico[:posicion_arroba]
nueva_extension = nombre_usuario + "@ceu.es"

print(f"Tu nuevo correo electrónico es: {nueva_extension}")

"""
division = correo.split('@')
print (f"{division} + @ceu.es")

////////////

print(correo[correo.find("@")] + "@ceu.es")
//
mail = correo.find("@")
print (mail[:pos+1]+"@ceu.es")
"""
