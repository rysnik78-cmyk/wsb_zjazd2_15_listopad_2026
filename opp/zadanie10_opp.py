'''Zadanie 10
Utwórz klasę Zwierze z atrybutem imie oraz metodą daj_glos(), która wyświetla „Nieznany dźwięk”.
Następnie utwórz klasy Pies i Kot, które dziedziczą po Zwierze. W każdej z nich zmień działanie metody daj_glos():
1.
Pies wyświetla „Hau!”.
2.
Kot wyświetla „Miau!”.
Utwórz psa i kota, a następnie wywołaj metodę daj_glos() dla obu obiektów.'''

class Zwierze:
    def __init__(self, imie):
        self.imie = imie

    def daj_glos(self):
        return 'Nieznany dzwięk'

class Pies(Zwierze):
    def daj_glos(self):
        return 'Hau!'

class Kot(Zwierze):
    def daj_glos(self):
        return 'Miau!'

zwierze = Zwierze('smok')
pies = Pies('ruda')
kot = Kot('mruczka')

print(zwierze.imie, zwierze.daj_glos())
print(pies.imie, pies.daj_glos())
print(kot.imie, kot.daj_glos())
