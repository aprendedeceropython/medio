# inicialmente funciona 

from datetime import datetime

def calcular_biorritmo(fecha_nacimiento, fecha_evaluacion):
    # Convertir las fechas a objetos datetime
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
    fecha_evaluacion = datetime.strptime(fecha_evaluacion, "%d-%m-%Y")

    # Calcular la edad en días
    edad_en_dias = (fecha_evaluacion - fecha_nacimiento).days

    # Calcular los tres componentes del biorritmo
    fisico = round(100 * (edad_en_dias % 23) / 23, 2)
    emocional = round(100 * (edad_en_dias % 28) / 28, 2)
    intelectual = round(100 * (edad_en_dias % 33) / 33, 2)

    return fisico, emocional, intelectual

def obtener_fecha_input():
    fecha_input = input("Ingresa la fecha en formato DD-MM-YYYY: ")
    try:
        datetime.strptime(fecha_input, "%d-%m-%Y")
        return fecha_input
    except ValueError:
        print("Formato de fecha incorrecto. Por favor, inténtalo de nuevo.")
        return obtener_fecha_input()

def imprimir_biorritmo():
    print("Por favor, ingresa las fechas de nacimiento y evaluación:")
    fecha_nacimiento = obtener_fecha_input()
    fecha_evaluacion = obtener_fecha_input()

    fisico, emocional, intelectual = calcular_biorritmo(fecha_nacimiento, fecha_evaluacion)
    print("Biorritmo:")
    print(f" - Físico: {fisico}%")
    print(f" - Emocional: {emocional}%")
    print(f" - Intelectual: {intelectual}%")

imprimir_biorritmo()
