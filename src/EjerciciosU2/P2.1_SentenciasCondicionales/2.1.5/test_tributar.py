import pytest 
from tributar import tributar 

@pytest.mark.parametrize(
    "edad, ingresos, expected",
    [
        (17,1000,"Te toca tributar."),
        (4,300000,"Aún tienes que pasar la edad del pavo, no tributas."),
        (25,500,"Estás un poco tieso, no tributes.")
    ]
)

def test_tributar(edad, ingresos, expected):
    assert tributar(edad, ingresos) == expected