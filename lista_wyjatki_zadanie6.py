'''Zadanie 6
Utwórz listę:
kolory = ["czerwony", "zielony", "niebieski"]
Poproś użytkownika o indeks i wyświetl odpowiedni element listy.
Obsłuż przypadki, w których użytkownik poda tekst zamiast liczby lub indeks spoza zakresu listy.
Wyjątki: ValueError, IndexError.'''

kolory = ["czerwony", "zielony", "niebieski"]


while True:
    index_string = input('podaj index w postaci liczby 0, 1 lub 2')
    try:
        index = int(index_string)
    except ValueError:
        print('to nie liczba całkowita - podaj 0, 1 lub 2')
        continue

    try:
        print(kolory[index])
    except IndexError:
        print('zła wartość - podaj 0, 1 lub 2')
        continue
    break
