import pytest
from cadenaCaracteres import cadena

@pytest.mark.parametrize(
    "contrasenia, expected",
    [
        "AYtortilla", "La contraseña es correcta.",
        "tortillasincebolla", "Contraseña incorrecta.",
        "sintortilla", "Contraseña incorrecta.",
        "ahytortilla", "Contraseña incorrecta."
    ]
  )
  
def cadena(contrasenia, expected):
  contrasenia.lower()
  assert cadena(contrasenia) == expected
    