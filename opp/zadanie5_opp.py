'''Zadanie 5
Utwórz klasę Prostokat z atrybutami szerokosc i wysokosc.
Dodaj metodę pole(), która zwraca pole prostokąta. Utwórz obiekt i wyświetl wynik metody.'''

class Prostokat:
    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc

    def pole(self):
        return self.szerokosc * self.wysokosc

prostokat_pierwszy = Prostokat(4, 6)

print(prostokat_pierwszy.pole())