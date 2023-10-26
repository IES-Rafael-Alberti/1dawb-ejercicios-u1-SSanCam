import pytest
from division import op_division

@pytest.mark.parametrize(
    "numero1, numero2, expected",
    [
        (10,0,"Error. No puede dividirse entre 0."),
        (10,5,"2.00"),
        (456,11,"41.45"),
        (-58,12,"-4.83")
    ]
)
def test_division(numero1, numero2, expected):
    assert op_division(numero1, numero2) == expected