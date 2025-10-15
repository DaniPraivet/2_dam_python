# analisis_notas.py
# Programa que analiza un conjunto de notas y muestra un resumen estadístico.

# Lista fija de asignaturas en el orden indicado
asignaturas = [
    "Programación multimedia y dispositivos móviles",
    "Acceso a datos",
    "Desarrollo de interfaces",
    "Sistemas de gestión empresarial",
    "Proyecto Intermodular",
    "Programación de servicios y procesos",
    "Itinerario personal para la empleabilidad II",
    "Optativa Grado Superior",
    "Inglés Profesional Grado Superior"
]

def main():
    try:
        # Pedimos las notas separadas por comas
        entrada = input("Introduce las notas separadas por comas: ")

        # Separamos las notas en una lista y eliminamos espacios
        notas_str = [n.strip() for n in entrada.split(",")]

        # Comprobamos que haya exactamente 9 notas (una por asignatura)
        if len(notas_str) != len(asignaturas):
            print(f"❌ Debes introducir exactamente {len(asignaturas)} notas, una por cada asignatura.")
            return  # Termina el programa

        # Convertimos las notas a enteros y validamos que sean numéricas
        notas = []
        for n in notas_str:
            notas.append(int(n))  # Si hay un valor no numérico, lanzará ValueError

    except ValueError:
        # Si alguna nota no es numérica, mostramos un error
        print("❌ Error: todas las notas deben ser números enteros.")
        return

    # Calculamos estadísticas básicas
    total_notas = len(notas)
    media = round(sum(notas) / total_notas, 2)  # Redondeamos a 2 decimales
    nota_minima = min(notas)
    nota_maxima = max(notas)

    # Calculamos porcentajes
    aprobados = len([n for n in notas if n >= 5])
    sobresalientes = len([n for n in notas if n >= 9])
    porcentaje_aprobados = (aprobados / total_notas) * 100
    porcentaje_sobresalientes = (sobresalientes / total_notas) * 100

    # Determinamos el nivel según la media
    if media >= 8:
        nivel = "Nivel excelente"
    elif media >= 5:
        nivel = "Nivel medio"
    else:
        nivel = "Necesita esfuerzo"

    # Determinamos mejor y peor asignatura
    mejor_asig = asignaturas[notas.index(nota_maxima)]
    peor_asig = asignaturas[notas.index(nota_minima)]

    # Mostramos los resultados
    print("\n📊 RESUMEN DE NOTAS 📊")
    print(f"Número total de notas: {total_notas}")
    print(f"Media: {media}")
    print(f"Nota mínima: {nota_minima}")
    print(f"Nota máxima: {nota_maxima}")
    print(f"Porcentaje de aprobados: {porcentaje_aprobados:.2f}%")
    print(f"Porcentaje de sobresalientes: {porcentaje_sobresalientes:.2f}%")
    print(f"Evaluación general: {nivel}")
    print(f"\n🏆 Mejor asignatura: {mejor_asig} ({nota_maxima})")
    print(f"📉 Peor asignatura: {peor_asig} ({nota_minima})")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
