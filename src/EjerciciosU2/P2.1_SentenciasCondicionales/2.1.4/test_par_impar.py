import pytest
from par_impar import numero_par 

@pytest.mark.parametrize(
    "numero, expected",
    [
        (2,"Es un número par."),
        (4,"Es un número par."),
        (1,"Es un número impar."),
        (3,"Es un número impar.")
        ]
)

def test_par_impar(numero,expected):
    assert numero_par(numero) == expected