import pytest
from cadena import contrasenia

@pytest.mark.parametrize(
    "cadena, expected",
    [
        ("AYtortilla", "Contraseña correcta."),
        ("ayTORTILLA", "Contraseña correcta."),
        ("nohaytortilla", "Contraseña incorrecta.")
    ]
)
def test_contrasenia(cadena, expected):
    assert contrasenia(cadena) == expected