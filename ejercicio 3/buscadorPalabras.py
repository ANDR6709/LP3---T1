def contar_palabra(texto, palabra)
    return texto.lower().split().count(palabra.lower())

texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
palabra_buscada = "texto"

print(f"La palabra '{palabra_buscada aparece contar_palabra(texto, palabra_buscada)} veces.")  
                  # Error: en la variable palabra_buscada falta cerrar el  corchete
                  # Error: en el string aparece faltan comillas simples 
                  # Error: En la funcion contar palabra falta abrir el corchete


# Correcciones:


def contar_palabra(texto, palabra)
    return texto.lower().split().count(palabra.lower())

texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
palabra_buscada = "texto"

print(f"La palabra '{palabra_buscada} 'aparece' {contar_palabra(texto, palabra_buscada)} veces.")  
                                                                                        
# Correccion: En la variable palabra_buscada se cierra el corchete
# Correccion: En el string aparece se colocan comillas simples
# Correccion: En la funcion contar palabra se abre el corchete