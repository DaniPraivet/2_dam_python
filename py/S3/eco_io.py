# Pedir 3 números
# Mostrar suma, media y mayor
# Adaptación libre

# Programa que pide 3 números, valida la entrada y calcula operaciones básicas

def main():
    # Pedimos los 3 números al usuario
    numeros_str = input("Introduce 3 números separados por espacio: ").strip().split()

    # Comprobar que el usuario introdujo exactamente 3 valores
    if len(numeros_str) != 3:
        print("Debes introducir exactamente 3 números.")
        return  # Termina el programa

    # Verificar que todos los valores sean números
    if not all(num.isdigit() or (num.startswith('-') and num[1:].isdigit()) for num in numeros_str):
        print("Todos los valores deben ser números válidos.")
        return  # Termina el programa

    # Convertir los valores a enteros
    numeros = list(map(int, numeros_str))

    # Calcular suma
    suma = sum(numeros)

    # Calcular media
    media = suma / len(numeros)

    # Calcular el mayor
    mayor = max(numeros)

    # Mostrar resultados
    print(f"\nSuma: {suma}")
    print(f"Media: {media}")
    print(f"Mayor: {mayor}")

    # Extra: ordenar de mayor a menor
    numeros_ordenados = sorted(numeros, reverse=True)

    # Formatear la salida como "a > b > c"
    resultado = " > ".join(map(str, numeros_ordenados))
    print(f"Ordenados de mayor a menor: {resultado}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
