'''W pliku test_funkcje.py napisz testy sprawdzające dodawanie:
1.
Dwóch liczb dodatnich.
2.
Liczby ujemnej i dodatniej.
3.
Zera do dowolnej liczby.



'''
import pytest

from funkcje import dodaj
from parzysta import czy_parzysta
from anna import powitaj
from srednia import srednia
from dzielenie import podziel

def test_dodaj_liczby_dodatnie():
    assert dodaj(2, 3) == 5

def test_dodaj_liczby_znaki_rozne():
    assert dodaj(2, -3) == -1

def test_dodaj_liczby_zero_i_dowolna():
    assert dodaj(0, 3) == 3

'''Zadanie 2
Napisz funkcję czy_parzysta(liczba), która zwraca True dla liczby parzystej, a False dla nieparzystej.
Zaimportuj funkcję do pliku z testami i sprawdź jej działanie dla liczby dodatniej, ujemnej oraz zera.'''

def test_czy_parzysta_parzysta():
    assert czy_parzysta(2) == True
    assert czy_parzysta(3) == False

'''Zadanie 3
Napisz funkcję powitanie(imie), która zwraca tekst, np. dla argumentu "Anna":
Cześć, Anna!
Napisz co najmniej dwa testy dla różnych imion. Sprawdź, czy wynik zawiera odpowiednią interpunkcję.'''



def test_powitaj_imie():
    assert powitaj('Anna') == 'Cześć, Anna!'
    assert powitaj('Jakub') == 'Cześć, Jakub!'

def test_powitaj_interpunkcja():
    assert ',' in powitaj('Anna')

'''Zadanie 4
Napisz funkcję srednia(oceny), która przyjmuje niepustą listę liczb i zwraca ich średnią.
Przygotuj testy dla:
1.
Listy zawierającej kilka liczb.
2.
Listy zawierającej jedną liczbę.
3.
Średniej, która nie jest liczbą całkowitą.
Wskazówka: do porównania liczb zmiennoprzecinkowych możesz użyć pytest.approx:
import pytest assert srednia([1, 2, 2]) == pytest.approx(1.6667, abs=0.0001)'''


def test_srednia_kilka_liczb():
    assert srednia([1, 2, 3]) == 2

def test_srednia_jedna_liczba():
    assert srednia([3]) == 3

def test_srednia_z_niecalkowitych():
    assert srednia([1, 2, 2]) == pytest.approx(1.6667, abs=0.0001)

'''Zadanie 5
Napisz funkcję podziel(a, b), która zwraca wynik dzielenia a przez b. Jeśli b jest zerem, funkcja powinna zgłosić ValueError.
Napisz test poprawnego dzielenia oraz test sprawdzający wyjątek:'''

def test_podziel_poprawne():
    assert podziel(4, 4) == 1

# def test_podziel_przez_zero():
#     with pytest.raises(ValueError):
#         podziel(10, 0)

