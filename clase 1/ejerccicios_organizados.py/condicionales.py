
"""
edad = int(input("ingrese la edad: "))

if edad >= 0 and edad < 6:
    print("primera infancia")
elif edad  >= 6 and edad < 13:
    print("niñez")

elif edad >= 13 and edad < 18:
    print("Adolescente")

else:
    print("adulto")

"""
# EJERCIOCI 1

#Supon que tienes un diccionario con las edades de varias personas. 
# tu tarea es crear un nuevo diccionario que indique
#si cada persona es mayor de edad o menor.

#edades
#- mayor de edad : 18 o mas
#menor de edad :17 o menos


edades = {
    "sofia": 4,
    "lizeth": 33,
    "mauro": 30
}

mayoria_edad = {
    "sofia": "Mayor de edad" if edades ["sofia"] >= 18 else "menor de edad",
    "lizeth":"Mayor de edad" if edades ["lizeth"] >= 18 else "menor de edad",
    "mauro": "Mayor de edad" if edades ["mauro"] >= 18 else "menor de edad",
    }
print(mayoria_edad)


















