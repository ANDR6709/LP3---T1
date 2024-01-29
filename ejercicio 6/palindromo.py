def es_palindromo(texto) #Error: faltan los dos puntos
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
    return texto == texto[::-1]

palabra_frase = input("Ingrese una palabra o frase: ")
if es_palindromo():
    print(f"{palabra_frase} es un palíndromo.")
else:
    print(f"{palabra_frase} no es un palíndromo.")


    # Correccion:

    def es_palindromo(texto): # Correccion: Se agregan  los dos puntos
        texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
        return texto == texto[::-1]

palabra_frase = input("Ingrese una palabra o frase: ")
if es_palindromo():
    print(f"{palabra_frase} es un palíndromo.")
else:
    print(f"{palabra_frase} no es un palíndromo.")



    