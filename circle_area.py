# ******************
# AREA DE UN CIRCULO
# ******************


def run(radius: float) -> float:
    # TU CÓDIGO AQUÍ
    PI = 3.14
    volume = PI * (radius ** 2)

    return volume


if __name__ == '__main__':
    run(4)