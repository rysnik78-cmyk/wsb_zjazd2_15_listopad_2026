'''Zadanie 8
Utwórz klasę ListaZakupow, która przechowuje listę produktów. Dodaj metody:
1.
dodaj_produkt(nazwa) — dodaje produkt do listy.
2.
pokaz_produkty() — wyświetla wszystkie produkty.
Utwórz dwie listy zakupów i sprawdź, czy każda przechowuje własne produkty.'''

class ListaZakupow:
    def __init__(self):
        self.lista_zakupow = []

    def dodaj_produkt(self, nazwa):
        self.lista_zakupow.append(nazwa)

    def pokaz_produkty(self):
        return '\n'.join(self.lista_zakupow)

moja_lista_zakupow = ListaZakupow()

moja_lista_zakupow.dodaj_produkt('chleb')
moja_lista_zakupow.dodaj_produkt('maslo')
moja_lista_zakupow.dodaj_produkt('kielbasa')
print(moja_lista_zakupow.pokaz_produkty())

