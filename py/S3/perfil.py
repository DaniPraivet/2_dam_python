# Pedir nombre + año nacimiento
# Calcular edad
# Clasificar por tramo (<18, 18-65, >65)
# Manejo de error si no mete número
# Comentarios

import datetime
import random

# Método para calcular la edad a partir del año de nacimiento
def calcular_edad(anio_nacimiento: int) -> int:
    """Calcula la edad de una persona dado su año de nacimiento."""
    anio_actual = datetime.datetime.now().year
    return anio_actual - anio_nacimiento

# Método para clasificar la edad en categorías
def clasificar_edad(edad: int) -> str:
    """Clasifica la edad en categorías."""
    if edad < 18:
        return "Menor de edad"
    elif 18 <= edad <= 65:
        return "Mayor de edad"
    else:
        return "Persona mayor"

# Método para generar un nivel de felicidad aleatorio
def nivel_felicidad() -> int:
    """Genera un número entre 0 y 5 que indica el nivel de felicidad."""
    return random.randint(0, 5)

def main():
    try:
        # Pedir nombre
        nombre = input("Introduce tu nombre: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")

        # Pedir año de nacimiento
        anio_str = input("Introduce tu año de nacimiento: ").strip()
        if not anio_str:
            raise ValueError("El año de nacimiento no puede estar vacío.")

        # Comprobar que el año es un número
        if not anio_str.isdigit():
            raise ValueError("El año de nacimiento debe ser un número.")

        anio_nacimiento = int(anio_str)

        # Calcular edad
        edad = calcular_edad(anio_nacimiento)

        # Clasificar edad
        clasificacion = clasificar_edad(edad)

        # Mostrar resultados
        print(f"\nHola {nombre}, tienes {edad} años.")
        print(f"Clasificación: {clasificacion}")

        # Extra: felicidad
        felicidad = nivel_felicidad()
        estados = {
            0: "Muy feliz 😄",
            1: "Feliz 🙂",
            2: "Normal 😐",
            3: "Un poco molesto 😕",
            4: "Molesto 😡",
            5: "Muy enfadado 🤬"
        }
        print(f"Hoy estás: {estados[felicidad]}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
