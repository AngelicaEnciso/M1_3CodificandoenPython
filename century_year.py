def is_century_year(year: int) -> bool:
    # Verifica si un año es un año de siglo
    return year % 100 == 0


def is_leap_year(year: int) -> bool:
    # Verifica si un año es un año bisiesto
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def century_year(year: int) -> str:
    # Determina si el año es un año de siglo y si es bisiesto
    if is_century_year(year):
        if is_leap_year(year):
            return f"{year} es un año de siglo y es bisiesto."
        else:
            return f"{year} es un año de siglo pero no es bisiesto."
    else:
        if is_leap_year(year):
            return f"{year} no es un año de siglo pero es bisiesto."
        else:
            return f"{year} no es un año de siglo y no es bisiesto."


if __name__ == '__main__':
    year = 2000  # Ejemplo de año
    result = century_year(year)
    print(result)

    year = 1900  # Otro ejemplo de año
    result = century_year(year)
    print(result)

    year = 2024  # Otro ejemplo de año no de siglo
    result = century_year(year)
    print(result)

    year = 2100  # Otro ejemplo de año de siglo
    result = century_year(year)
    print(result)
