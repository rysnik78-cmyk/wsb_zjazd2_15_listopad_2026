'''Zadanie 3
Utwórz listę:
owoce = ["jabłko", "banan", "gruszka"]
Poproś użytkownika o podanie indeksu i wyświetl owoc znajdujący się pod tym indeksem.
Jeśli indeks jest nieprawidłowy, wyświetl odpowiedni komunikat.
Wskazówka: obsłuż wyjątek IndexError.'''


owoce = ["jabłko", "banan", "gruszka"]
index = int(input('podaj index: '))

try:
    print(owoce[index])
except IndexError:
    print('indeks jest nieprawidłowy')