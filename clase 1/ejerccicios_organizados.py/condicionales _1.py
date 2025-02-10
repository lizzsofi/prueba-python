#EJERCICIO 2
#
# 
# - si la calificacion es 6 o mayor, el estado es "aprobado"
#-si es menor a 6, el estado es "reprobado"
#OBLETIVO:

# crear un nuevo diccionario que  indique el estado de cada estudiante("aprobado" o "reprobado") 
#segun su calificacion

nota = {
    "sofia": 7,
    "lizeth": 5,
    "mauro": 2,
}

calificaciones = {
    "sofia": "aprobado" if nota ["sofia"] >= 6 else "reprobado",
    "lizeth":"aprobado" if nota ["lizeth"] >= 6 else "reprobado",
    "mauro": "aprobado" if nota ["mauro"] >= 6 else "reprobado",
    }
print(calificaciones)
print("felicitaciones para los estudiantes que pasaron")

