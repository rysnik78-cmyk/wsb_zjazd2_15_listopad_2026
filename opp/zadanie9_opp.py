'''Zadanie 9
Utwórz klasę Student z imieniem oraz listą ocen. Dodaj metody:
1.
dodaj_ocene(ocena) — dodaje ocenę do listy.
2.
srednia() — zwraca średnią ocen. Jeśli lista jest pusta, metoda zwraca None.
Utwórz studenta, dodaj kilka ocen i wyświetl jego średnią.'''

class Student:
    def __init__(self, imie):
        self.imie = imie
        self.lista_ocen = []

    def dodaj_ocen(self, ocena):
        self.lista_ocen.append(float(ocena))

    def srednia(self):
        if self.lista_ocen:
            return sum(self.lista_ocen) / len(self.lista_ocen)
        else:
            return None

student_pierwszy = Student('pierwszy')
student_pierwszy.dodaj_ocen(5)
student_pierwszy.dodaj_ocen(6)
student_pierwszy.dodaj_ocen(7)
student_pierwszy.dodaj_ocen(8)
student_pierwszy.dodaj_ocen(9)
print(student_pierwszy.srednia())
