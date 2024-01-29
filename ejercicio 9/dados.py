import radom  # Error: La funcion random esta mal escrita

 simular_lanzamiento_dados(cantidad_dados, caras_por_dado)  # Error: simular_lanzamiento_dados no esta definida como una variable y faltan dos puntos
    resultados = [random.randint(1, caras_por_dado) for _ in range(cantidad_dados)]  # Error: linea mal identada
    retunr resultados                                                                 # Error: La funcion return esta mal escrita y faltan comillas                                                                  

cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))        # Error: linea mal identada
caras_por_dado = int(input("Ingrese la cantidad de caras por dado: "))
lanzamientos = simular_lanzamiento_dados(, caras_por_dado)                   #  Error :En simular_lanzamiento_dados faltan comillas y sobra una coma
print(f"Resultados del lanzamiento: {lanzamientos}")                         #En la variable caras_por_dado



# Correcciones:

import random  # Correccion: La funcion random se escribe correctamente

def  simular_lanzamiento_dados(cantidad_dados, caras_por_dado):  # Correccion: simular_lanzamiento_dados se define como una variable y se ponen dos puntos
    resultados = [random.randint(1, caras_por_dado) for _ in range(cantidad_dados)]  # Correccion:  linea queda bien identada
    return resultados                                                                 # Correccion: La funcion return queda escrita correctamente                                                                 

cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))         # Correccion:  linea queda bien identada
caras_por_dado = int(input("Ingrese la cantidad de caras por dado: "))
lanzamientos = "simular_lanzamiento_dados"( caras_por_dado)                   #  Correccion :En simular_lanzamiento_dados se colocan comillas
print(f"Resultados del lanzamiento: {lanzamientos}")                           # y se elimina la coma en la variable caras_por_dado





