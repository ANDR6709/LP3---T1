def contar_palabras_en_archivo(nombre_archivo) #Error: Faltan los dos puntos en la funcion contar_palabras_en_archivo
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            return len(palabras)
    except FileNotFoundError:
        retunr f"El archivo {nombre_archivo} no fue encontrado."  # Error: Falta abrir y cerrar el parentesis despues de la funcion return
                                                                  # Error: La funcion return esta mal escrita
archivo_nombre = input("Ingrese el nombre del archivo de texto: ")
print(f"El archivo contiene {contar_palabras_en_archivo(archivo_nombre)} palabras.")



# Correcciones:


def contar_palabras_en_archivo(nombre_archivo): # Correccion: Se agregan los dos puntos en la funcion contar_palabras_en_archivo
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            return len(palabras)
    except FileNotFoundError:
        return (f"El archivo {nombre_archivo} no fue encontrado.")  # Correccion: Se abre y cierra el parentesis despues de la funcion return
                                                                  # Correccion: La funcion return se escribe correctamente
archivo_nombre = input("Ingrese el nombre del archivo de texto: ")
print(f"El archivo contiene {contar_palabras_en_archivo(archivo_nombre)} palabras.")






