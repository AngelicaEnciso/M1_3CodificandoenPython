def approximate_sqrt(value: float, epsilon: float = 1e-10) -> float:
    # Aproxima la raíz cuadrada usando el método de Newton-Raphson
    guess = value / 2.0
    while abs(guess * guess - value) > epsilon:
        guess = (guess + value / guess) / 2.0
    return guess

def euclidean_distance_2d(point1: tuple, point2: tuple) -> float:
    # Calcula la distancia euclidiana entre dos puntos en 2D sin usar math.sqrt
    sum_of_squares = (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2
    distance = approximate_sqrt(sum_of_squares)
    return distance

if __name__ == '__main__':
    point1 = (1, 2)  # Ejemplo de punto 1
    point2 = (4, 6)  # Ejemplo de punto 2
    distance = euclidean_distance_2d(point1, point2)
    print(f"La distancia euclidiana entre los puntos {point1} y {point2} es: {distance}")


