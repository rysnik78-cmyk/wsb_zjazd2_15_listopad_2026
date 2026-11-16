'''Zadanie 7
Utwórz klasę Konto z atrybutami wlasciciel i saldo. Nowe konto powinno mieć saldo równe 0. Dodaj metody:
1.
wplac(kwota) — zwiększa saldo o podaną dodatnią kwotę; dla pozostałych wartości wyświetla komunikat o błędzie.
2.
wyplac(kwota) — zmniejsza saldo, jeśli kwota jest dodatnia i nie przekracza salda. W przeciwnym razie wyświetla komunikat o błędzie.
Sprawdź poprawną wypłatę oraz próbę wypłacenia zbyt dużej kwoty.'''

class Konto:
    def __init__(self, wlasciciel = 'nobody', saldo = 0):
        self.wlasciciel = wlasciciel
        self.saldo = 0

    def wplac(self, kwota):
        self.saldo += kwota


    def wyplac(self, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
        else:
            print('bład - nie masz tyle na koncie')

moje_konto = Konto()
print('saldo:', moje_konto.saldo)
moje_konto.wplac(5)
print('saldo:', moje_konto.saldo)
moje_konto.wplac(6)
print('saldo:', moje_konto.saldo)
moje_konto.wplac(7)
print('saldo:', moje_konto.saldo)
moje_konto.wplac(80)
print('saldo:', moje_konto.saldo)
moje_konto.wyplac(90)
print('saldo:', moje_konto.saldo)
moje_konto.wyplac(90)
print('saldo:', moje_konto.saldo)




