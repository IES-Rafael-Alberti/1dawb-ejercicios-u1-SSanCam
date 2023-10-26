import pytest 
from impositivo import tramoRenta

@pytest.mark.parametrize(
    "renta, expected",
    [
        (5000, "5%"),
        (10000, "15%"),
        (15000, "15%"),
        (21000, "20%"),
        (36000, "30%"),
        (128736234, "45%")
    ]
)

def test_impositivo (renta, expected):
    assert tramoRenta(renta) == expected