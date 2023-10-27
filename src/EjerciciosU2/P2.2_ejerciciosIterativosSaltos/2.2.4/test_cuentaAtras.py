import pytest 
from cuentaAtras import retroceso

@pytest.mark.parametrize(
    "numero, expected",
    [
        (9,[9, 8, 7, 6, 5, 4, 3, 2, 1]),
        (-5, []),
        (5, [5, 4, 3, 2, 1])
    ]
)

def test_cuentaAtras(numero, expected):
    assert retroceso(numero) == expected