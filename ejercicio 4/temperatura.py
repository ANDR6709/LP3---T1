def celsius_a_fahrenheit(celsius)
    return (celsius * 9/5)   32     # Error: falta el signo + despues del parentesis que se cierra

temperatura_celsius = float("Ingrese la temperatura en Celsius: ")
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")


# Correccion:

def celsius_a_fahrenheit(celsius)
    return (celsius * 9/5)  + 32     # Correccion: Se agrega el signo + despues del parentesis que se cierra

temperatura_celsius = float("Ingrese la temperatura en Celsius: ")
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")



