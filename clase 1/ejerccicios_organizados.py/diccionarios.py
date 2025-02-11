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
"""

#ejercicio clase 1
#supon que tienes un diccionario con los nombres de algunos estudiantes 
# y sus respectivas caliifcaciones de una materia. Tu tarea es crear un
#diccionario nuevo que contenga los nombres de los estudiantes y sus
#calificaciones aumentadas en un 10 %

"""
notas = {"lizet":5,
         "mauro":3,
         "sofia":4 
         }



calificaciones_aumentadas =dict(map(lambda item: (item[0], round(item[1] * 1.10, 2)), notas.items()))
print(calificaciones_aumentadas)


#ejercicio2#

# tienes un diccionario con los nombres de algunas ciudades y sus respectivas 
# temperaturas en grados celsius. Tu tarea es crear un diccionario nuevo con los nombres de las 
# ciudades y sus temperaturas convertidas a grados fahrenheit.

ciudades ={
    "Madrid": 15,
    "Londres": 10,
    "Paris": 18,
    "Berlin": 5,
}

temperatura_fahrenheit = dict([
    ("Madrid"), round(temperaturas_celsius["Madrid"] * 9/5 + 32, 2)),
    ("Londres"), round(temperaturas_celsius["Londres"] * 9/5 + 32, 2),
    ("Paris"), round(temperaturas_celsius["Londres"] * 9/5 + 32, 2)

])
 

