import pytest 
from repeticionPalabra import repetir 

@pytest.mark.parametrize(
    "palabra, expected",
    [
        ("sara", "sara, sara, sara, sara, sara, sara, sara, sara, sara, sara"),
        ("paco", "paco, paco, paco, paco, paco, paco, paco, paco, paco, paco")
    ]
)

def test_repeticionPAlabra(palabra, expected):
    assert repetir(palabra) == expected