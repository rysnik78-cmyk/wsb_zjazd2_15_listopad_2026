'''Zadanie 7
Poproś użytkownika o podanie liczby całkowitej.
Jeśli wpisze niepoprawną wartość, wyświetl komunikat i ponów pytanie.
Gdy poda poprawną liczbę, wyświetl ją i zakończ program.
Wskazówka: użyj pętli while, instrukcji try i except oraz break.'''



while True:
    number_string = input('podaj liczbę całkowitą: ')
    try:
        number_int = int(number_string)
        break
    except ValueError:
        print('to nie liczba całkowita - podaj liczbę całkowitą')
        continue

print('ok. podałeś w końcu dobrą liczbę całkowitą: ', number_int)