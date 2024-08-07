# ******************
# AREA DE UN TRIANGULO
# ******************

def run(base: float, altura: float) -> float:
    # Calcula el área del triángulo
    area = 0.5 * base * altura
    return area

if __name__ == '__main__':
    base = 5  # Ejemplo de base
    altura = 10  # Ejemplo de altura
    area = run(base, altura)
    print(f"El área del triángulo con base {base} y altura {altura} es: {area}")