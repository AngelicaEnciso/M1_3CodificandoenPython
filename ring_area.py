import math


def ring_area(outer_radius: float, inner_radius: float) -> float:
    """
    Calcula el área de un anillo (corona circular).

    :param outer_radius: Radio externo del anillo.
    :param inner_radius: Radio interno del anillo.
    :return: Área del anillo.
    """
    if outer_radius <= inner_radius:
        raise ValueError("El radio externo debe ser mayor que el radio interno.")

    area = math.pi * (outer_radius ** 2 - inner_radius ** 2)
    return area


if __name__ == '__main__':
    outer_radius = 10.0  # Ejemplo de radio externo
    inner_radius = 5.0  # Ejemplo de radio interno

    try:
        area = ring_area(outer_radius, inner_radius)
        print(f"El área del anillo con radio externo {outer_radius} y radio interno {inner_radius} es: {area:.2f}")
    except ValueError as e:
        print(e)
