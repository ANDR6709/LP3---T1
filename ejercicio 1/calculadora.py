def calculadora():
    num1 = float("Ingrese el primer número: ")
    num2 = float("Ingrese el segundo número: ")
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == '+':
        resultado = num + num2 # error: num no esta definida como variable num 1
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num / num2  # error: num no esta definida como variable num 1
    else:
        resultado = "Operación no válida"

    print("Resultado: "resultado)  # error: falta una coma despues de cerrar comillas

calculdora()                       #error: falta definir calculadora como funcion y faltan los dos puntos



# correcciones


def calculadora():
    num1 = float("Ingrese el primer número: ")
    num2 = float("Ingrese el segundo número: ")
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == '+':
        resultado = num1 + num2 # correccion: se define num como variable num 1
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2  # correccion: se define num como variable num 1
    elif operacion == '-':
        resultado = "Operación no válida"

    print("Resultado: ",resultado)  # correccion: se coloca la coma despues de cerrar comillas

def calculdora():                       #correccion: se define calculadora como funcion y se ponen los dos puntos


