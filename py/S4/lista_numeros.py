# Programa que pide una lista de números separados por comas,
# calcula suma, media, máximo y muestra los números duplicados.
# Además, genera una palabra usando letras del abecedario a partir de los números dados.


def main():
    # Pedimos al usuario que introduzca números separados por comas
    entrada = input("Introduce una lista de números separados por comas: ").strip()

    # Comprobamos que no esté vacía la entrada
    if not entrada:
        print("No se ha introducido ningún valor.")
        return  # Se detiene el programa

    # Separamos los números y eliminamos espacios sobrantes
    numeros_str = [n.strip() for n in entrada.split(",")]

    # Intentamos convertir cada valor a número decimal (float)
    try:
        numeros = [float(n) for n in numeros_str]
    except ValueError:
        print("Error: todos los valores deben ser números válidos.")
        return  # Finaliza el programa si hay error de conversión

    # Calculamos la suma total
    suma = sum(numeros)

    # Calculamos la media (promedio)
    media = suma / len(numeros)

    # Calculamos el número más grande
    maximo = max(numeros)

    # Detectamos duplicados:
    # Creamos un diccionario que cuenta cuántas veces aparece cada número
    conteo = {}
    for num in numeros:
        conteo[num] = conteo.get(num, 0) + 1

    # Extraemos los números que aparecen más de una vez
    duplicados = [str(num) for num, veces in conteo.items() if veces > 1]

    # Mostramos resultados generales
    print("\n--- RESULTADOS ---")
    print(f"Suma: {suma}")
    print(f"Media: {media}")
    print(f"Máximo: {maximo}")

    # Mostramos los duplicados, si existen
    if duplicados:
        print(f"Duplicados: {', '.join(duplicados)}")
    else:
        print("Duplicados: Ninguno")

    # Parte adicional: generar una "palabra" a partir de los números
    # Cada número se convierte a una letra según su valor entero
    palabra = ""
    for num in numeros:
        indice = int(abs(num)) % 26   # Nos aseguramos que el valor esté dentro del rango 0-25
        letra = chr(65 + indice)      # Convertimos el índice a letra (A = 65 en ASCII)
        palabra += letra

    # Mostramos la palabra generada
    print(f"Palabra generada: {palabra}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
