### Zadanie 5: Klasy `Product` i `ShoppingCart`
'''**Opis**:
Utwórz klasę `Product`, która przechowuje nazwę, cenę i ilość produktu. Klasa `ShoppingCart` zarządza listą produktów w koszyku,
 umożliwia dodawanie produktów, usuwanie produktów, obliczanie łącznej wartości koszyka oraz wyświetlanie wszystkich produktów.
**Przykład:**
```python
>>> p1 = Product("Chleb", 3.5, 2)
>>> p2 = Product("Mleko", 2.0, 1)
>>> cart = ShoppingCart()
>>> cart.dodaj_produkt(p1)
>>> cart.dodaj_produkt(p2)
>>> cart.wyswietl_produkty()
Produkty w koszyku:
"Chleb" - Cena: 3.5 zł, Ilość: 2
"Mleko" - Cena: 2.0 zł, Ilość: 1
>>> print(f"Łączna wartość koszyka: {cart.oblicz_wartosc()} zł")
Łączna wartość koszyka: 9.0 zł
>>> cart.usun_produkt("Chleb")
>>> cart.wyswietl_produkty()
Produkty w koszyku:
"Mleko" - Cena: 2.0 zł, Ilość: 1
```
'''

class Product:
    def __init__(self, nazwa, cena, ilosc):
        self.nazwa = nazwa
        self.cena = cena 
        self.ilosc = ilosc
    def __repr__(self):
        return f"{self.nazwa} - Cena: {self.cena}, Ilość: {self.ilosc}"

class ShoppingCart:
    def __init__(self):
        self.listaproduktow = []
    def dodaj_produkt(self, produkt):
        self.listaproduktow.append(produkt)
    def usun_produkt(self, produkt):
        for i in self.listaproduktow:
            if i.nazwa == produkt:
                self.listaproduktow.remove(i)

    def wyswietl_produkty(self):
        for i in self.listaproduktow:
            print(i)
    def oblicz_wartosc(self):
        cena = 0
        for i in self.listaproduktow:
            cena += (i.cena * i.ilosc)
        return cena    

p1 = Product("Chleb", 3.5, 2)
p2 = Product("Mleko", 2.0, 1)
cart = ShoppingCart()
cart.dodaj_produkt(p1)
cart.dodaj_produkt(p2)
cart.wyswietl_produkty()
print(f"Łączna wartość koszyka: {cart.oblicz_wartosc()} zł")
cart.usun_produkt("Chleb")
cart.wyswietl_produkty()