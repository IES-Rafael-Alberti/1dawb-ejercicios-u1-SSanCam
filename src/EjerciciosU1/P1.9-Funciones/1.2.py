"""1.2 => recibe horas y coste y retorna el importe total."""
def total(horas: int , coste: float) :
    return (horas * coste)

horas = int(input("Horas de trabajo: "))
coste = float(input("Coste por hora: "))

print(f"Importe total: {total(horas,coste):.2f}€.")