 calcular_precio_con_decuento(precio_base, porcentaje_descuento)  # Error: calcular_precio_con_descuento noe esta definida como variable
    descuento = precio_base * (porcentaje_descuento / 100)
    precio_final = precio_base- descuento
    retunr precio_final                                      # Error: La funcion return esta mal escrita

precio_base = float("Ingrese el precio base del producto: ")  # Error: precio_base esta mal identado
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
precio_final = calcular_precio_con_descuento(precio_base, porcentaje_descuento)   # Error: Calcular_ precio_con- descuento no esta definida como variable
print(f"El precio final con {porcentaje_descuento}% de descuento es: {precio_final}")


# Correcciones:

def  calcular_precio_con_descuento(precio_base, porcentaje_descuento):  # Correccion: calcular_precio_con_descuento se define como variable
    descuento = precio_base * (porcentaje_descuento / 100)
    precio_final = precio_base- descuento
    return precio_final                                               # Correccion: se escribe correctamente la funcion return

precio_base = float("Ingrese el precio base del producto: ")          # Correccion. Precio_base queda identada
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
precio_final = calcular_precio_con_descuento(precio_base, porcentaje_descuento)  # Correccion: calcular_precio_con_descuento se define como variable
print(f"El precio final con {porcentaje_descuento}% de descuento es: {precio_final}")



