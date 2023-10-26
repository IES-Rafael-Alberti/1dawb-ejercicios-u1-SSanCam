"""Escribir un programa que pregunte por consola por los productos de una cesta de la compra, 
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta."""

lista = str(input("Introduce los productos de tu cesta de la compra, separados por una \",\": "))
lista_formateada = lista.split(",")

for articulo in lista_formateada:
    print(articulo)

    """
    lista_compra = "tomate, lechuga, huevos"
    listaProd = lista_compra.replace(" "," ").replace(',','\n')
    """