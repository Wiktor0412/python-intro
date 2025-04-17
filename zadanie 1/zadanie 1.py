# Zadanie 1 – zip(), random i obsługa wyjątków
#
#   Funkcje wbudowane:
#       1.len() – Zwraca długość obiektu, np. liczby elementów w liście.
#       https://docs.python.org/3/library/functions.html#len
#       Przykład: len([1, 2, 3]) → zwróci 3
#
#       2.max() – Zwraca największą wartość z podanych elementów.
#       https://docs.python.org/3/library/functions.html#max
#       Przykład: max(4, 10, 2) → zwróci 10
#
#       3.str() – Konwertuje dowolną wartość na tekst.
#       https://docs.python.org/3/library/functions.html#str
#       Przykład: str(123) → zwróci "123"
#
#   Moduły z biblioteki standardowej:
#       1.datetime – Służy do pracy z datą i czasem.
#       https://docs.python.org/3/library/datetime.html
#       Przykład: datetime.datetime.now() zwraca aktualny czas
#
#       2.random – Umożliwia losowanie wartości, np. liczb.
#       https://docs.python.org/3/library/random.html
#       Przykład: random.choice(["tak", "nie"]) losuje jeden z elementów
#
#       3.math – Zawiera funkcje matematyczne, np. pierwiastkowanie.
#       https://docs.python.org/3/library/math.html
#       Przykład: math.sqrt(16) → 4.0
#
#   Wyjątki:
#       1.ValueError – Błąd, gdy np. konwertujemy tekst na liczbę, ale tekst nie wygląda jak liczba.
#       https://docs.python.org/3/library/exceptions.html#ValueError
#       Przykład: int("abc") → ValueError
#
#       2.ZeroDivisionError – Próba dzielenia przez zero.
#       https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
#       Przykład: 5 / 0 → ZeroDivisionError
#
#       3.IndexError – Odwołanie się do nieistniejącego indeksu listy.
#       https://docs.python.org/3/library/exceptions.html#IndexError
#       Przykład: lista[10], gdy lista ma tylko 3 elementy
#
#
#
#
import random

# 1. Tworzenie dwóch list
imiona = ["Ala", "Bartek", "Celina"]  # Lista imion
punkty = [random.randint(1, 100) for _ in imiona]  # Losowanie punktów dla każdego imienia (zakres 1-100)

# 2. Łączenie list imion i punktów za pomocą funkcji zip()
wyniki = list(zip(imiona, punkty))
# Funkcja zip() łączy dwie listy, tworząc listę krotek (par) z elementów z obu list -> https://docs.python.org/3/library/functions.html#zip
print("Połączona lista:", wyniki)

# 3. Moduł random z biblioteki standardowej
# Losowanie liczby 0 lub 1 w celu wywołania wyjątku ZeroDivisionError
liczba = random.randint(0, 1)  # Funkcja random.randint() losuje liczbę całkowitą z zadanego zakresu -> https://docs.python.org/3/library/random.html#random.randint
print("Wylosowana liczba:", liczba)

# 4. Obsługa wyjątku ZeroDivisionError
try:
    wynik = 10 / liczba  # Próba dzielenia przez wylosowaną liczbę
    print("10 podzielone przez", liczba, "to", wynik)
except ZeroDivisionError:  # Obsługuje błąd dzielenia przez zero
    print("Ups! Dzielenie przez zero.")
# Wyjątek ZeroDivisionError pojawia się, gdy próbujemy podzielić przez zero -> https://docs.python.org/3/library/exceptions.html#ZeroDivisionError


