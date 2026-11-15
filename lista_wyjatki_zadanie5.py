'''Zadanie 5
Poproś użytkownika o podanie wieku jako liczby całkowitej.
Jeśli wpisze niepoprawną wartość, wyświetl komunikat i poproś go o ponowne podanie wieku.
Powtarzaj pytanie aż do wpisania poprawnej liczby.
Wskazówka: połącz pętlę while z obsługą wyjątku ValueError.'''


while True:
    wiek_string = input('podaj_wiek_jako_liczba_całkowita:')
    try:
        wiek = int(wiek_string)
        break
    except ValueError:
        print('nie podałeś liczby całkowitej')
print('twój wiek to:',wiek)





