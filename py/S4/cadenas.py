# Programa que analiza una cadena de texto
# Cuenta las vocales, consonantes y mayúsculas (solo letras)
# Además, calcula un valor según las vocales (+4) y las consonantes (-1)

def main():
    try:
        # Pedimos al usuario una cadena de texto
        texto = input("Introduce una cadena de texto: ").strip()

        # Comprobamos que el usuario haya introducido algo
        if not texto:
            print("No se ha introducido ningún texto.")
            return  # Terminamos el programa

        # Definimos las vocales para comparar fácilmente
        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

        # Inicializamos los contadores
        contador_vocales = 0
        contador_consonantes = 0
        contador_mayusculas = 0
        contador_letras = 0  # Solo letras (sin números, signos ni espacios)

        # Recorremos cada carácter del texto
        for caracter in texto:
            # Verificamos si el carácter es una letra (ignoramos todo lo demás)
            if caracter.isalpha():
                contador_letras += 1  # Sumamos al total de letras

                # Comprobamos si es vocal o consonante
                if caracter in vocales:
                    contador_vocales += 1
                else:
                    contador_consonantes += 1

                # Contamos las mayúsculas
                if caracter.isupper():
                    contador_mayusculas += 1

        # Calculamos el valor final del texto
        # Regla: cada vocal suma +4, cada consonante resta -1
        valor_texto = (contador_vocales * 4) - contador_consonantes

        # Mostramos los resultados
        print("\n--- RESULTADOS ---")
        print(f"Letras totales: {contador_letras}")
        print(f"Vocales: {contador_vocales}")
        print(f"Consonantes: {contador_consonantes}")
        print(f"Mayúsculas: {contador_mayusculas}")
        print(f"Valor del texto: {valor_texto}")

    except Exception as e:
        # Capturamos cualquier error inesperado
        print(f"Ocurrió un error: {e}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
