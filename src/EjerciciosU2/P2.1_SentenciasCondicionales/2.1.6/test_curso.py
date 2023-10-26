import pytest 
from curso import grupo

@pytest.mark.parametrize(
    "nombre, sexo, expected",
    [
        ("noelia", "m","Perteneces al grupo A"),
        ("ana", "m", "Perteneces al grupo B"),
        ("antonio", "h", "Perteneces al grupo A"),
        ("paco", "h","Perteneces al grupo B")
    ]
)

def test_curso (nombre, sexo, expected) :
    assert grupo (nombre, sexo) == expected