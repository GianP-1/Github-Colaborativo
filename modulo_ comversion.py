convertir = float(input("Introduce el número a convertir: "))

km_m = convertir * 1000

print(f"La convercion de {convertir} kilometros a Metros es: {km_m} Metros")

def cm_a_metros():
    convertir_cm = float(input("Introduce el número a convertir (centímetros): "))
    cm_m = convertir_cm / 100
    print(f"La conversión de {convertir_cm} centímetros a Metros es: {cm_m} Metros")

    # Conversor de libras a kilogramos

libras = float(input("Ingrese el peso en libras: "))

kilogramos = libras * 0.453592

print("El peso en kilogramos es:", kilogramos)