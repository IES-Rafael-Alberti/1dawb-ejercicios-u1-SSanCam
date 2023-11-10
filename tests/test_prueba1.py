import pytest 
from src.prueba1 import mayor_igual

@pytest.mark.parametrize(
    "numero1, numero2, expected",
    [
        (2,5,5),
        (6,6,0),
        (9,6,9)
    ]
)

def test_prueba1(numero1, numero2, expected):
    assert mayor_igual(numero1, numero2) == expected