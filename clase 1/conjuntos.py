# se colocan llaves {} no puede contener elementos repetidos, interseccion, unio, diferencia entre dos conjuntos

""""
conjunto = {"carro" , "casa" , "beca" , "empresa"}
conjunto2 = set(("carro" , "casa" , "beca" , "empresa"))
print(conjunto)
print(conjunto2)
"""

frutas = {"manzana" , "piña" , "naranja" , "mandarina" , "ferrary"}
carros = {"toyota" , "fiat" , "ferrary" , "fiat" , "piña"}
print(frutas)
print(carros)
frutas.add("guanabana")                       # add sirve para agregar en cualquier parte
print(frutas)
#frutas.clear()                          #sirve para limpiar
copia = frutas.copy()                    #  copy sirve para copiar
print(copia)
print(frutas.difference(carros))                #diferencia entre conjuntos
frutas.discard("guanabana")              #saca elementos del conjunto si  ya existe--- remove si no existe saca error y saca errorno sigue ejecutando
print(frutas)
#frutas.discard("piña")
print(frutas.intersection(carros))                   #intercepcion es el elemento que tiene en ambos conjuntos

conjunto1 = {1,2,3,4,5,6,}
conjunto2 = {3,5}
print(conjunto2.issubset(conjunto1))
print(conjunto1.issuperset(conjunto2) )          





