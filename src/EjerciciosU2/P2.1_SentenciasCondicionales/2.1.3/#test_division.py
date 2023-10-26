import pytest
from division import operacion_div

@pytest.mark.parametrize(
    "num1, num2, expected",
    [
      (10, 5, f"La división de {10}/{5} da como resultado: {10/5:.2f}"),
      (20, "Eres mayor de edad."),
      (16, "Eres menor de edad."),
      (200, "Relája, Nosferatus.")
    ]
  )

def test_operacion_div():
    assert operacion_div() == 2.00
    assert operacion_div() == ZeroDivisionError