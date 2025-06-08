from my_awesome_lib.math_tools import calculate_circle_area, add_numbers, \
    calculate_rectangle_area
from my_awesome_lib.data_utils import filter_even_numbers, \
    convert_date_format, reverse_list
from my_awesome_lib.text_processing import is_palindrome, count_words

# Uzycie funkcji matematycznych
promien = 5.0
pole_kola = calculate_circle_area(promien)
print(f"Pole kola o promieniu {promien}: {pole_kola}")

dlugosc = 4.0
szerokosc = 6.0
pole_prostokata = calculate_rectangle_area(dlugosc, szerokosc)
print(f"Pole prostokata {dlugosc}x{szerokosc}: {pole_prostokata}")

wynik_dodawania = add_numbers(10, 20)
print(f"Suma 10 i 20: {wynik_dodawania}")

# Uzycie funkcji do obrobki danych
liczby = [1, 2, 3, 4, 5, 6, 'a', 8.5]
parzyste = filter_even_numbers(liczby)
print(f"Liczby parzyste z {liczby}: {parzyste}")

data_do_konwersji = "15-08-2023"
skonwertowana_data = convert_date_format(data_do_konwersji)
print(f"Data {data_do_konwersji} po konwersji: {skonwertowana_data}")

moja_lista = [1, 2, 3, 4, 5]
odwrocona_lista = reverse_list(moja_lista)
print(f"Lista {moja_lista} odwrocona: {odwrocona_lista}")

# Uzycie funkcji do przetwarzania tekstu
tekst_palindrom = "Kajak"
tekst_nie_palindrom = "Ziemniak"
print(f"'{tekst_palindrom}' to palindrom? {is_palindrome(tekst_palindrom)}")
print(f"'{tekst_nie_palindrom}' to palindrom? "
      f"{is_palindrome(tekst_nie_palindrom)}")

moj_tekst = "To jest przykladowy tekst do zliczenia slow."
liczba_slow = count_words(moj_tekst)
print(f"Liczba slow w tekscie '{moj_tekst}': {liczba_slow}")
