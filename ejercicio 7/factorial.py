def factorial(n) # Error: faltan los dos puntos en la funcion factorial
    if n == 0 or n == 1 # Error: Falta completar el operador de igualdad y faltan los dos puntos
        retunr 1      # Error: La funcion return esta mal escrita
    else:
        retunr n * factorial(n - 1)   # Error: La funcion return esta mal escrita

numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es {factorial()}")



# Correcciones:


def factorial(n): #Correccion: Se colocan los dos puntos en la funcion factorial
    if n == 0 or n == 1: # Correccion: Se agrega el operador de igualdad y se colocan los dos puntos
        return 1      # Correccion: La funcion return se escribe correctamente
    else:
        return n * factorial(n - 1)  # Correccion: La funcion return se escribe correctamente

numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es {factorial()}")



