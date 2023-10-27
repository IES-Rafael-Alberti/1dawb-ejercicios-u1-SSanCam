import pytest
from edad import contadorEdad

@pytest.mark.parametrize(
    "fecNac, expected",
    [
        (5, [1, 2, 3, 4, 5]),
        (10,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ]
)

def test_edad (fecNac, expected):
    assert contadorEdad(fecNac) == expected