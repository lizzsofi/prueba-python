#Entrada de datos
numero1 = input("Introduce el primer número: ")
numero2 = input("Introduce el segundo número: ")
operacion = input("¿Qué operación quieres realizar? (+, -, *, /): ")

# casteo de datos de texto a float
numero1 = float(numero1)
numero2 = float(numero2)

# operamos 
if(operacion == '+'):
    resultado = numero1 + numero2
elif (operacion == '*'):
    resultado = numero1 * numero2
elif (operacion == '/'):
    resultado = numero1 / numero2
elif (operacion == '-'):
    resultado = numero1 - numero2
else:
    resultado = 'Operacion no esperada'


# mostramos el resultado
print(resultado)