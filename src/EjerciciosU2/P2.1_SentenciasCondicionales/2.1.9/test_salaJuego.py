import pytest
from salaJuego import entrada

@pytest.mark.parametrize(
    "edad, expected",
    [
        (2,"0.00€"),
        (4,"5.00€"),
        (50,"10.00€")
    ]
)

def test_salaJuego(edad, expected):
    assert entrada(edad) == expected