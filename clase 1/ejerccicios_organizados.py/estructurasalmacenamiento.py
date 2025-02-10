#longitud para contar cuanto hay en la lista

edadd = 52
lista1 =["Hola", 58 , True , 3.1416]
print(len(lista1))


frutas = ["papaya" , "fresa" , "mango"]
print(frutas)
print(frutas[1])


frutas =["papaya" , "fresa" , "mango"]
frutas.append("naranja")                                #agregar naranja al final
print(frutas)
frutas.insert(2, "uva")                                  #agregar una en la posicion que se indica 
print(frutas)

frutas [2]="mandarina"                                  # reemplaza el lemento
print(frutas)
verduras =["espinaca" , "tomate" , "lecguha"]           #extiende la lista
frutas.extend(verduras)
print(frutas)
copia = frutas.copy()                            #hace copia
copia.append("perro")  
print(copia)
print(frutas)   


verduras =["espinaca" , "tomate" , "lechuga" , "tomate"]
print(verduras.count("tomate"))                              #count  cuenta los elementos
print(verduras.index("lechuga"))             #devuelve la posicion del primero elemnto, si hay dos elementos iguales devuelve solo el primero
verduras.pop()                               # elimina el ultimo elemento
verduras.pop(1)                              #elimina el elemento que se `pone dentro del parentesis
print(verduras)
verduras.remove("lechuga")                   # remueve el elemento y si hay repetidos elimina solo el primero 
print(verduras)    


verduras = ["espinaca" , "tomate" , " lechuga" , "tomate"]
verduras.reverse()                             #reversa la lista. cambiando el orden del ultimo al primero
print(verduras)
verduras.sort()                                #ordena en orden alfabetico y solo si son del mismo tipo
print (verduras)
#ejemplo git





