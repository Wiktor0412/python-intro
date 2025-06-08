from datetime import datetime


def convert_date_format(date_str: str) -> str:
    """
    Konwertuje date z formatu 'DD-MM-RRRR' na 'RRRR/MM/DD'.

    Args:
        date_str (str): Data jako ciag znakow w formacie
        'DD-MM-RRRR' (np. "01-01-2024").

    Returns:
        str: Skonwertowana data jako ciag znakow w
        formacie 'RRRR/MM/DD' (np. "2024/01/01").

    Raises:
        ValueError: Jesli format wejsciowej daty jest nieprawidlowy.
    """
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    return date_obj.strftime("%Y/%m/%d")


def filter_even_numbers(numbers: list) -> list:
    """
    Filtruje liste liczb, zwracajac tylko liczby calkowite i parzyste.

    Args:
        numbers (list): Lista zawierajaca rozne typy danych.

    Returns:
        list: Nowa lista zawierajaca tylko liczby calkowite i
        parzyste z oryginalnej listy.
    """
    return [n for n in numbers if isinstance(n, int) and n % 2 == 0]


def reverse_list(input_list: list) -> list:
    """
    Odwraca kolejnosc elementow w podanej liscie.

    Args:
        input_list (list): Lista do odwrocenia.

    Returns:
        list: Nowa lista z odwrocona kolejnoscie elementow.
    """
    return input_list[::-1]
