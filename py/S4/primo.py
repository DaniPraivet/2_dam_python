# Programa que determina si un número es primo
# y muestra el siguiente número primo después de él

def es_primo(numero: int) -> bool:
    """Devuelve True si el número es primo, False si no lo es."""
    if numero < 2:
        return False  # Los números menores que 2 no son primos
    for i in range(2, int(numero ** 0.5) + 1):  # Solo comprobamos hasta la raíz cuadrada
        if numero % i == 0:  # Si es divisible por otro número, no es primo
            return False
    return True  # Si no tiene divisores, es primo

def siguiente_primo(numero: int) -> int:
    """Encuentra el siguiente número primo después del número dado."""
    siguiente = numero + 1
    while not es_primo(siguiente):  # Buscamos hasta encontrar el siguiente primo
        siguiente += 1
    return siguiente

def main():
    try:
        # Pedimos al usuario que introduzca un número
        entrada = input("Introduce un número: ").strip()

        # Comprobamos que no esté vacío
        if not entrada:
            print("No se ha introducido ningún valor.")
            return

        # Intentamos convertirlo a entero
        numero = int(entrada)

        # Comprobamos si es primo
        if es_primo(numero):
            print(f"\n✅ {numero} es un número primo.")
        else:
            print(f"\n❌ {numero} no es un número primo.")

        # Calculamos y mostramos el siguiente número primo
        siguiente = siguiente_primo(numero)
        print(f"El siguiente número primo es: {siguiente}")

    except ValueError:
        # Error si el valor no es un número entero
        print("Error: Debes introducir un número entero válido.")
    except Exception as e:
        # Cualquier otro error inesperado
        print(f"Ocurrió un error inesperado: {e}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
