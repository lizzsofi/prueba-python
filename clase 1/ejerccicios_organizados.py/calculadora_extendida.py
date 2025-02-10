#Calculadora Extendida
# Crea un programa que solicite dos números al usuario y permita elegir
# entre suma, resta, multiplicación, división y potenciación.
#o Asegura que la división por cero muestre un mensaje de error en lugar
#de fallar.# 

numero1 = input("Introduce el primer número: ")
numero2 = input("Introduce el segundo número: ")
operacion = input("¿Qué operación quieres realizar? (+, -, *, /, ** ): ")

numero1 = float(numero1)
numero2 = float(numero2)


if(operacion == '+'):
    resultado = numero1 + numero2
elif (operacion == '*'):
    resultado = numero1 * numero2
elif (operacion == '/'):
    try:                                              # el bloque try catch ejecuta una operacion y en caso que retorne unan except se pueda capturar y controlarla
        resultado = numero1 / numero2
    except ZeroDivisionError:
        resultado = "no se puede dividir por cero"
elif (operacion == '-'):
    resultado = numero1 - numero2
elif (operacion ==  "**"):
    resultado = numero1 ** numero2 
else:
    resultado = "operacion inesperada"


print(resultado)










