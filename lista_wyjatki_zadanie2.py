'''Zadanie 2
Poproś użytkownika o podanie dwóch liczb i wyświetl wynik dzielenia pierwszej przez drugą.
Jeśli druga liczba wynosi zero, wyświetl komunikat „Nie można dzielić przez zero”.
Wskazówka: obsłuż wyjątek ZeroDivisionError.'''

first_number = input('podaj liczbę a: ')
second_number = input('podaj liczbę b: ')
try:
    division = int(first_number) / int(second_number)
except ZeroDivisionError:
    print('Nie można dzielić przez zero')

