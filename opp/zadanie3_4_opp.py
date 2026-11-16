'''Zadanie 3
Utwórz klasę Osoba, której konstruktor przyjmuje imię i wiek.
Zapisz je jako atrybuty obiektu. Utwórz dwie osoby i wyświetl ich imiona oraz wiek.
Wskazówka: użyj metody __init__.'''

'''Zadanie 4
Rozbuduj klasę Osoba o metodę przedstaw_sie(), która wyświetli komunikat, np.:
Mam na imię Anna i mam 20 lat.
Wywołaj metodę dla dwóch różnych osób.'''

class Osoba():
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        return f'Mam na imię {self.imie} i mam {self.wiek} lat.'

osoba_pierwsza = Osoba('Kuba', 47)
print(f'{osoba_pierwsza.imie} ma {osoba_pierwsza.wiek} lat')
osoba_druga = Osoba('Druga', 54)
print(f'{osoba_druga.imie} ma {osoba_druga.wiek} lat')

print(osoba_pierwsza.przedstaw_sie())
print(osoba_druga.przedstaw_sie())