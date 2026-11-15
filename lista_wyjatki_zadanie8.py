'''Zadanie 8
Poproś użytkownika o nazwę pliku tekstowego. Otwórz plik z kodowaniem UTF-8 i wyświetl jego zawartość.
Jeśli plik nie istnieje, poinformuj o tym użytkownika.
Dodaj blok finally, który zawsze wyświetli komunikat „Zakończono próbę odczytu”.
Wyjątek: FileNotFoundError.'''

nazwa_pliku = input('podaj_nazwę pliku:')
try:
    with open(nazwa_pliku, 'r', encoding='utf-8') as f:
        data_read = f.readlines()
        print(data_read)
except FileNotFoundError:
    print('nie znaleziono pliku')

print('zakończono próbę odczytu')