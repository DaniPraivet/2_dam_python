# Programa que convierte una temperatura en grados Celsius
# a Kelvin o Fahrenheit, según la elección del usuario.
# Además, indica cómo se siente la temperatura en palabras.

def main():
    # Pedimos al usuario la temperatura en grados Celsius
    entrada_temp = input("Introduce la temperatura en grados Celsius: ").strip()

    # Comprobamos que el usuario haya introducido un valor
    if not entrada_temp:
        print("No se ha introducido ninguna temperatura.")
        return  # Terminamos el programa

    # Intentamos convertir la entrada a número (float)
    try:
        celsius = float(entrada_temp)
    except ValueError:
        print("Error: la temperatura debe ser un número.")
        return  # Terminamos el programa si no es numérico

    # Pedimos al usuario el tipo de conversión que desea hacer
    tipo = input("¿A qué unidad quieres convertir? (K para Kelvin / F para Fahrenheit): ").strip().upper()

    # Verificamos que haya introducido una opción válida
    if tipo not in ("K", "F"):
        print("Opción no válida. Debes escribir 'K' o 'F'.")
        return  # Finaliza el programa si la opción no es correcta

    # Realizamos la conversión según la opción elegida
    if tipo == "K":
        # Conversión a Kelvin
        resultado = celsius + 273.15
        unidad = "K"
    else:
        # Conversión a Fahrenheit
        resultado = (celsius * 9/5) + 32
        unidad = "°F"

    # Mostramos el resultado de la conversión
    print(f"\n{celsius}°C equivalen a {resultado:.2f}{unidad}")

    # Analizamos la sensación térmica según la temperatura en Celsius
    if celsius < 0:
        mensaje = "Me congelo 🥶"
    elif celsius < 15:
        mensaje = "Hace fresquito ❄️"
    elif celsius < 25:
        mensaje = "Se está bien 🙂"
    elif celsius < 35:
        mensaje = "Hace calor ☀️"
    elif celsius < 50:
        mensaje = "Hace mucho calor 🔥"
    else:
        mensaje = "¡Temperatura extrema! 🌋"

    # Mostramos el mensaje correspondiente
    print(mensaje)

# Punto de entrada del programa
if __name__ == "__main__":
    main()
