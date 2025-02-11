'''1. Adivina el número (if, elif, else, while)
Un clásico juego donde tienes que adivinar un número secreto.
'''

import random

numero_secreto = random.randint(1, 10)
intentos = 0

print("🎯 ¡Adivina el número entre 1 y 10!")

while True:
    intento = int(input("Tu intento: "))
    intentos += 1

    if intento < numero_secreto:
        print("🔼 Es más alto. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("🔽 Es más bajo. Intenta de nuevo.")
    else:
        print(f"🎉 ¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break