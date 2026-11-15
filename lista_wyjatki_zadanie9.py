'''Zadanie 9
Przygotuj plik liczby.txt, w którym każda linia zawiera jedną wartość. Niektóre linie mogą zawierać tekst, np.:
10 5 abc 15
Napisz program, który:
1.
Odczyta plik i spróbuje zamienić każdą linię na liczbę.
2.
Pominie niepoprawne linie i wyświetli ich numery.
3.
Obliczy średnią poprawnych liczb. Jeśli nie ma żadnych poprawnych liczb, wyświetli odpowiedni komunikat zamiast wykonywać dzielenie.
4.
Obsłuży sytuację, w której plik nie istnieje.
Wyjątki: ValueError, FileNotFoundError.'''

nazwa_pliku = 'liczby.txt'

with open(nazwa_pliku, 'r') as f:
    data_read = f.readlines()
liczba_linii = len(data_read)
suma_liczb = 0
niepoprawne = []
for i in range(liczba_linii):
    try:
        suma_liczb += int(data_read[i])

    except ValueError:
        niepoprawne.append(i)

print(niepoprawne)
if liczba_linii == len(niepoprawne):
    print('wszystkie niepoprawne')

else:
    print(suma_liczb/(liczba_linii-len(niepoprawne)))