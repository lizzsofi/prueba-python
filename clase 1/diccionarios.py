#diccionario es un cajon que tiene varios comparimientos, y cada espacio tiene un nombre etiqueta {} cada uno de los elementos son una pareja
# ejem

diccionario = {"nombre":"carlos",
               "apellido":"zapata",
               "edad":33,
               "celular":"3005152109"
               }

print(len(diccionario))
print(diccionario["nombre"])
print(diccionario)

copia = diccionario.copy()
print(diccionario)
print(copia)
copia["edad"] = 18
print(copia)
print(diccionario)
print(diccionario.get("edad"))
print(diccionario.items())
print(diccionario.keys())
print(diccionario.values())
diccionario.popitem()
print(diccionario)
diccionario.setdefault("cantidadhijos",1)
print(diccionario)
diccionario.update({"salario":10000})
print(diccionario)


