
#pedirle al usuario que ingrese 10 nombres con cc y edad, y en una lista los mayores de edad y en otra los menores
"""
diccionario = {"nombre": "Carlos", "cedula":"1035859376"}
lista = []
lista.append(diccionario)
print(lista)

"""

mayores_de_edad =[]
menores_de_edad = []

# pedir al usuario que ingrese 10 personas
for i in range (10):
    print("ingresa los datos de los usuarios: " )
    nombre = input("ingrese el nombre:")
    apellido = input("ingrese el apellido: " )
    edad = int(input("ingrese su edad: " ))
    cedula = input("ingrese su cedula:" )

    # mirar si es menor o mayor de edad
    if edad >= 18:
        mayores_de_edad.append(nombre)
        print(" mayor de edad"  )
    else:
        menores_de_edad.append(nombre)  
        print(" ""menor de edad")        


    
