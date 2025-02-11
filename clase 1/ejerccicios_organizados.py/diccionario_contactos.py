#Crea un diccionario que almacene nombres y números de teléfono.
#o Permite al usuario buscar un contacto ingresando el nombre.
#o Si el contacto no existe, permite agregarlo.

agenda_de_contactos = {
    "lizeth": 3005152109
}

opcion = input("1 para agregar, 2 para buscar ")

if(opcion == "1" ):
    nombre= input("ingresar nombre")
    numero= input("ingresar numero")
    agenda_de_contactos[nombre]=numero


print(agenda_de_contactos)

#terminar ejercicio