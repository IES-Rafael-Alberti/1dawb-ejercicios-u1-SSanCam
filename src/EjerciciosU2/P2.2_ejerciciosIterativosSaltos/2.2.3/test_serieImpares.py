import pytest 
from serieImpares import serieImpares

@pytest.mark.parametrize(
    "numero, expected",
    [
        (43, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43]),
        (6, [1, 3, 5])
    ]
)

def test_serieImpares(numero, expected):
    assert serieImpares(numero) == expected