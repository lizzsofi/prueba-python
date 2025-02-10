#Pide al usuario que ingrese una frase.
#Devuelve la frase en mayúsculas, minúsculas, con la primera letra de
#cada palabra en mayúscula y al revés.

frase = input("Ingrese una frase: ")           
mayusculas = frase.upper()                      #  upper convertir a mayusculas

minusculas = frase.lower()                       # convertir a minusculas

#Primera letra de cada palabra en mayúscula 

titulo = frase.title()

# Invertir la frase- [::-1] → Invierte el texto.
reversa = frase[::-1]

# Mostrar resultados
print("Mayúsculas:", mayusculas)
print("Minúsculas:", minusculas)
print("Título:", titulo)
print("Al revés:", reversa)


