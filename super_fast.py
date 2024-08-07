def super_fast_primes(n: int) -> list:
    """
    Encuentra todos los números primos menores o iguales a n usando la Criba de Eratóstenes.

    :param n: El límite superior del rango (inclusive).
    :return: Una lista de números primos menores o iguales a n.
    """
    # Inicializa una lista de booleanos para marcar los números primos
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 y 1 no son números primos

    for start in range(2, int(n ** 0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, n + 1, start):
                is_prime[multiple] = False

    # Devuelve la lista de números primos
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes


if __name__ == '__main__':
    limit = 100  # Ejemplo de límite superior
    primes = super_fast_primes(limit)
    print(f"Números primos menores o iguales a {limit}: {primes}")
