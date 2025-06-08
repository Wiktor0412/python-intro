def is_palindrome(text: str) -> bool:
    """
    Sprawdza, czy podany tekst jest palindromem,
    ignorujac wielkosc liter i znaki niealfanumeryczne.

    Args:
        text (str): Tekst do sprawdzenia.

    Returns:
        bool: True, jesli tekst jest palindromem, False w przeciwnym razie.
    """

    cleaned_chars = []
    for char in text:
        if char.isalnum():
            cleaned_chars.append(char.lower())

    cleaned = "".join(cleaned_chars)

    return cleaned == cleaned[::-1]


def count_words(text: str) -> int:
    """
    Zlicza liczbe slow w podanym tekscie.
    Slowa sa oddzielone spacjami. Puste slowa sa ignorowane.

    Args:
        text (str): Tekst do analizy.

    Returns:
        int: Liczba slow w tekscie.
    """
    words = text.split()
    return len(words)
