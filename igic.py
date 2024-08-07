def calculate_igic(price: float, igic_rate: float) -> float:
    """
    Calcula el IGIC sobre un precio dado.

    :param price: Precio antes de impuestos.
    :param igic_rate: Tasa de IGIC aplicable (en porcentaje, por ejemplo 7%).
    :return: Cantidad de IGIC.
    """
    igic = price * (igic_rate / 100)
    return igic


def calculate_total_price(price: float, igic_rate: float) -> float:
    """
    Calcula el precio total incluyendo el IGIC.

    :param price: Precio antes de impuestos.
    :param igic_rate: Tasa de IGIC aplicable (en porcentaje, por ejemplo 7%).
    :return: Precio total incluyendo el IGIC.
    """
    igic = calculate_igic(price, igic_rate)
    total_price = price + igic
    return total_price


if __name__ == '__main__':
    price = 100.0  # Precio antes de impuestos
    igic_rate = 7.0  # Tasa de IGIC en porcentaje

    igic = calculate_igic(price, igic_rate)
    total_price = calculate_total_price(price, igic_rate)

    print(f"Precio antes de impuestos: {price:.2f} €")
    print(f"IGIC ({igic_rate}%): {igic:.2f} €")
    print(f"Precio total incluyendo IGIC: {total_price:.2f} €")
