def es_primo(numero) # Error: faltan los dos puntos en funcion _es primo
    if numero < 2 #Error:Faltan los dos puntos
        return False
    for i in range(2, int(numero**0.5) + 1) #Error:Faltan los dos puntos
        if numero % i == 0  # Error:Faltan los dos puntos
            retrun False    # Error:  funcion return no esta bien escrita y faltan comillas simples
    retunr True      # Error: return no esta bien escrita y faltan comillas simples

limite = int(input("Ingrese el límite superior para encontrar números primos: "))
primos = [num for num in range(2, limite + 1) if es_primo()]
print("Números primos:", primos)


# Correcciones


def es_primo(numero): # Correccion: Se colocan los dos puntos en funcion_es primo
    if numero < 2:    # Correccion: Se colocan  los dos puntos
        return False  
    for i in range(2, int(numero**0.5) + 1): # Correcion: Se agregan los dos puntos 
        if numero % i == 0:  # Correccion:Se agregan los dos puntos
            'return False '   # Correccion: La funcion return se escribe bien y se colocan comillas simples
    'return True'               # Correccion: La funcion return se escribe bien y se colocan comillas simples
limite = int(input("Ingrese el límite superior para encontrar números primos: "))
primos = [num for num in range(2, limite + 1) if es_primo()]
print("Números primos:", primos)




 

 