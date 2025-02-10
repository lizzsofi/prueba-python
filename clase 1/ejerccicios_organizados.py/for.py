#paso 1 : Usar for con if para filtrar elementos

numbers = [1, 4, 6, 7, 2, 8, 3]

#complete el codigo, para que se haga lo sgte
#1. Sume los numeros mayores que 5 y muestre el resultado
#2. Multiplique los numeros menores de 5 y muestre el resutado
#3. Cuente y muestre la cantidad de datos del arreglo
#4. Modifique el programa para que analice cualquier numero

#for para recorrer lista y if para filtrar

lista = [1,2,5,6,7,8,9,3,8,]

suma = 0 
multiplicacion = 1 

condicion = int (input("Ingrese un numero: "))

for num in lista :
    if num > condicion:
       suma += num
    elif num < condicion:
        multiplicacion *= num

    else:
        print("Numero no esta en la lista")

print("la suma de los numeros menores a, " + str(condicion)+ "es", suma)  
print("La multiplicacion de los numeros menores que "+ str(condicion), multiplicacion)
print("La longitud de la lista es: ",len(lista))


       

    