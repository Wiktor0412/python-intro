import re
from datetime import datetime

def is_valid_email(email: str) -> bool:
    """
    Sprawdza, czy podany ciag znakow jest poprawnym adresem e-mail.
    """
    pattern = r"^[a-zA-Z0-9]+(?:[._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*(?:\.[a-zA-Z]{2,6})+$"
    return re.match(pattern, email) is not None

def calculate_circle_area(radius: float) -> float:
    """
    Oblicza pole kola na podstawie promienia.
    Zglasza ValueError, jesli promien jest ujemny.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    pi = 3.141592653589793
    return pi * radius ** 2

def filter_even_numbers(numbers: list) -> list:
    """
    Filtruje liste, zwracajac tylko liczby parzyste bedace liczbami calkowitymi.
    Ignoruje wartosci boolowskie.
    """
    return [n for n in numbers if isinstance(n, int) and not isinstance(n, bool) and n % 2 == 0]

def convert_date_format(date_str: str) -> str:
    """
    Konwertuje date z formatu "DD-MM-YYYY" na "RRRR/MM/DD".
    Zglasza ValueError w przypadku nieprawidlowego formatu daty.
    """
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        return date_obj.strftime("%Y/%m/%d")
    except ValueError:
        raise ValueError(f"Incorrect date format: {date_str}. Expected 'DD-MM-YYYY'")

def is_palindrome(text: str) -> bool:
    """
    Sprawdza, czy dany tekst jest palindromem (ignorujac wielkosc liter i znaki niealfanumeryczne).
    """
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

