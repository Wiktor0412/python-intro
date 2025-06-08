def calculate_circle_area(radius: float) -> float:
    """
    Oblicza pole kola na podstawie promienia.

    Args:
        radius (float): Promien kola. Musi byc liczba nieujemna.

    Returns:
        float: Pole kola.

    Raises:
        ValueError: Jesli promien jest liczba ujemna.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    pi = 3.14159
    return pi * radius ** 2


def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Oblicza pole prostokata na podstawie dlugosci i szerokosci.

    Args:
        length (float): Dlugosc prostokata. Musi byc nieujemna.
        width (float): Szerokosc prostokata. Musi byc nieujemna.

    Returns:
        float: Pole prostokata.

    Raises:
        ValueError: Jesli dlugosc lub szerokosc jest ujemna.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")
    return length * width


def add_numbers(a: float, b: float) -> float:
    """
    Dodaje dwie liczby.

    Args:
        a (float): Pierwsza liczba.
        b (float): Druga liczba.

    Returns:
        float: Suma dwoch liczb.
    """
    return a + b
