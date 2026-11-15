'''Zadanie 4
Poproś użytkownika o podanie nazwy pliku tekstowego. Spróbuj otworzyć plik i wyświetlić jego zawartość.
Jeśli plik nie istnieje, wyświetl komunikat „Nie znaleziono pliku”.
Wskazówka: obsłuż wyjątek FileNotFoundError.'''

nazwa_pliku = input('podaj_nazwę pliku:')
try:
    with open(nazwa_pliku, 'r') as f:
        data_read = f.readlines()
        print(data_read)
except FileNotFoundError:
    print('nie znaleziono pliku')

