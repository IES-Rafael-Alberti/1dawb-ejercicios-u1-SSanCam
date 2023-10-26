import pytest 
from bellaNapoli import pedidoPizza

@pytest.mark.parametrize(
    "tipoPizza, ingrediente, expected",
    [
        ("V", 1, "Has elegido pizza vegetariana con: salsa de tomate, queso y pimiento"),
        ("v", 2, "Has elegido pizza vegetariana con: salsa de tomate, queso y tofu"),
        ("W", 1, "Has elegino pizza NO vegetariana con: salsa de tomate, queso y peperoni."),
        ("NV", 2, "Has elegino pizza NO vegetariana con: salsa de tomate, queso y jamón."),
        ("NV", 6, "Has elegino pizza NO vegetariana con: salsa de tomate, queso y salmón.")
    ]
)

def test_bellaNapoli(tipoPizza, ingrediente, expected):
    assert pedidoPizza(tipoPizza, ingrediente) == expected
    