import pytest
from cadenaCaracteres import cadena

def cadena():
    assert cadena("AYtortilla") == "La contraseña es correcta."
    assert cadena("ayTORTILLA") == "La contraseña es correcta."
    assert cadena("tortillasincebolla") == "Contraseña incorrecta."
    assert cadena("sintortilla") == "Contraseña incorrecta."
    assert cadena("ahytortilla") == "Contraseña incorrecta."