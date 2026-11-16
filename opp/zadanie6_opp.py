'''Zadanie 6
Utwórz klasę Licznik. Nowy licznik powinien mieć wartość 0. Dodaj metody:
1.
zwieksz() — zwiększa wartość o 1.
2.
resetuj() — ustawia wartość na 0.
Wywołaj metody i sprawdź, jak zmienia się wartość licznika.'''

class Licznik():
    def __init__(self):
        self.wartosc = 0

    def zwieksz(self):
        self.wartosc += 1

    def zmniejsz(self):
        self.wartosc -= 1

    def resetuj(self):
        self.wartosc = 0

moj_licznik = Licznik()
moj_licznik.zwieksz()
moj_licznik.zwieksz()
moj_licznik.zwieksz()
moj_licznik.zwieksz()
moj_licznik.zwieksz()
print(moj_licznik.wartosc)

moj_licznik.zmniejsz()
print(moj_licznik.wartosc)

moj_licznik.resetuj()
print(moj_licznik.wartosc)