# funciones

def funcion1():
    print("Hola")

def suma(a,b):        # a,b parametros  
    print("el resultado es: ",a+b)

def suma2(a,b):
    resultado = a + b
    return resultado 

def ensayo():
    a = 5
    print(a) 
    print(saludo)

def ensayo2(*a):
    print(a)  

def ensayo3(a,b):
    print(a+b)
    print(a) 
    print(b)      

funcion1()
suma(5,3)
print(suma2(5,3))       # cuando hago el llamado son argumentos y recibirlos son parametros

saludo = "Hola"
ensayo()

ensayo2(8, 9, 6, 3, 5, 7, 6)
ensayo3(b=18, a=1)








