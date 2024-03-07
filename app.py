# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

# Solicitar los valores al usuario
base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

# Llamar a la función y mostrar el resultado
area_rectangulo = calcular_area_rectangulo(base, altura)
print(f"El área del rectángulo es: {area_rectangulo}")