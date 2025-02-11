#haga un programa que llene una lista de datos numericos
#hasta que el usuario digite el numero 0. recorra la lista 
# e imprima la suma de los numeros mayores que 5,
#si no hay numeros >5, imprimir la suma y un mensaje indicandolo.
#evaluar la condicion y hacerlo con print

lista =[]
suma = 0
while True:
    num = int(input("ingrese un umero "))
    if(num == 0):
        break
    else:
        lista.append(num)
        
for i in lista:
    if (i > 5):
        suma += i

if suma==0:
   print("no hay numeros mayores que 5 ") 
else:
    print("la suma de numeros mayores que 5, es : ", suma)   
    
