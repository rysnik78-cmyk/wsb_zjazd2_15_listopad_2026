'''Zadanie 1
Poproś użytkownika o podanie liczby całkowitej. Wyświetl jej kwadrat.
Jeśli wpisana wartość nie jest liczbą całkowitą, wyświetl komunikat „To nie jest poprawna liczba”.
Wskazówka: obsłuż wyjątek ValueError.'''

liczba_str = input('podaj liczbę całkowitą: ')
try:
    n = int(liczba_str)
    print(n * n)
except ValueError:
    print('to nie jest poprawna liczba')