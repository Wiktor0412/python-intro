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

# tworzymy dwie listy
imiona = ["Ala", "Bartek", "Celina"]
punkty = [random.randint(1, 100) for _ in imiona]  # losowe liczby dla każdego imienia

# łączymy imiona z punktami
wyniki = list(zip(imiona, punkty))
print("Lista wyników:", wyniki)

# sprawdzamy dzielenie z możliwym wyjątkiem
try:
    liczba = random.randint(0, 1)  # może być 0 albo 1
    wynik = 10 / liczba
    print("10 podzielone przez", liczba, "to", wynik)
except ZeroDivisionError:
    print("Ups! Dzielenie przez zero.")

