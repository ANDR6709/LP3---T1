import rando  # error: La funcion random esta mal escrita ,falta la letra m
import string

generar_contraseña(longitud=8):    # error:generar contraseña no se a definido como funcion
    caracteres = string.ascii_letters + string.digits + string.punctuation   # Error: La variable caracteres esta mal identada
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))  # Error: Al parametro longitud le faltan commillas simples
    retunr contraseña     # Error:  Return esta mal escrita y faltan comillas simples en return y contraseña

print(generar_contrasena())   # Error :En generar contraseña faltan comillas simples y sobran parentesis internos




# Correcciones:

import random  # correcccion: Se corrige la funcion random poniendo letra m
import string

def generar_contraseña(longitud=8):    # correccion: Se define generar contraseña como funcion
    caracteres = string.ascii_letters + string.digits + string.punctuation   #  correcccion: La variable caracteres queda identada
    contraseña = ''.join(random.choice(caracteres) for _ in range('longitud'))  # corrrecion: Al parametro longitud se le ponen commillas simples
    'return contraseña'     # correccion:  Se escribe bien la palabra return y se colocan comillas simples

print('generar_contrasena')  # correccion :En generar contraseña  se colocan comillas simples y se eliminan parentesis internos



