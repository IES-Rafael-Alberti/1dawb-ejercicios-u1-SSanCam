import pytest 
from prueba1 import numero_mayor_igual

@pytest.mark.parametrize(
    "numero1, numero2, expected",
    [
        (2,5,5),
        (6,6,0),
        (9,6,9)
    ]
)

def numero_mayor_igual(numero1, numero2, expected):
    assert numero_mayor_igual(numero1, numero2) == expected