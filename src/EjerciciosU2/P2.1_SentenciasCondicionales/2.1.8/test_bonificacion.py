import pytest
from bonificacion import evaluacion

@pytest.mark.parametrize(
    "puntaje, expected",
    [
        (0.0, "0.00€"),
        (0.4, "960.00€"),
        (0.6, "1440.00€")
    ]
)

def test_bonificacion (puntaje, expected):
    assert evaluacion(puntaje) == expected
    