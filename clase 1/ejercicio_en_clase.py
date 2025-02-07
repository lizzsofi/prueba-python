#crea una lista con 5 numeros
#usa la funcion sorted() para obtener una lista ordenada de menor a mayor
#usa la funcion sum() para obtener la suma de todos los elementos de la lista
#usa la funcion min() para obtener el valor minimo de la lista
#usa la funcion max () para obtener el valor maximo de la lista

"""numeros = []

for i in range (5):
 
    num = int(input(f"Ingrese cinco numeros {i + 1}:  "))
 #agrgarlo a la lista
    numeros.append(num)    

 #mostrar la lista
print("Lista de numeros ingresados:", numeros)   
"""

num1 =  int(input("ingrese el numero 1: "))
num2 =  int(input("ingrese el numero 2: "))
num3 =  int(input("ingrese el numero 3: "))
num4 =  int(input("ingrese el numero 4: "))
num5 =  int(input("ingrese el numero 5: "))


numeros = [num1, num2, num3, num4, num5,]

lista_ordenada = sorted(numeros)
suma = sum(numeros)
minimo = min(numeros)
maximo = max(numeros)

print("lista: ",numeros)
print("lista ordenada: ", lista_ordenada)
print("suma total: ", suma)
print("lista valor minimo: ", minimo)
print("lista valor ,aximo: ", maximo)




