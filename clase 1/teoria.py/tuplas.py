#es inmutable, incambiable, puedo tener elementos repetidos o de diferentes tipos  solo coutn, index. tupla = tuple
""""
lista = [5,68, "Hola"]
tupla = (5,68, "Hola")
"""

frutas = tuple(("fresa" , "manzana" , "papaya" , "manzana"))
print(frutas)

frutas2 = (("fresa" , "manzana" , "papaya" , "manzana"))
print(frutas2)
print(frutas.count("manzana"))
print(frutas.index("manzana"))

#ingresar a alguien a la lista

temporal =list(frutas)         # se convierte a listas con temporal
print(temporal)
temporal.append("mango")       #aca se ingresa lo nuevo que en este caso es mango
print(temporal)
frutas = tuple(temporal)       # se convierte nuevaente a tuple con temporal
print(frutas)

