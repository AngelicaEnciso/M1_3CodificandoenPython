def xor_integers(a: int, b: int) -> int:
    """
    Realiza una operación XOR entre dos enteros.

    :param a: Primer entero.
    :param b: Segundo entero.
    :return: Resultado de la operación XOR.
    """
    return a ^ b


if __name__ == '__main__':
    a = 5  # Ejemplo de primer número entero
    b = 3  # Ejemplo de segundo número entero
    result = xor_integers(a, b)
    print(f"El resultado de {a} XOR {b} es: {result}")
