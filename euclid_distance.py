def run(point1: tuple, point2: tuple, epsilon: float = 1e-10) -> float:
    # Aproxima la raíz cuadrada usando el método de Newton-Raphson
    def run(value: float) -> float:
        guess = value / 2.0
        while abs(guess * guess - value) > epsilon:
            guess = (guess + value / guess) / 2.0
        return guess

    # Calcula la suma de los cuadrados de las diferencias
    sum_of_squares = (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2

    # Calcula la distancia usando la aproximación de la raíz cuadrada
    distance = run(sum_of_squares)
    return distance

