#Zad. 6
'''Zrób system, który obsługiwał będzie określone zamówienia. W programie istnieć będą 2 klasy: Manager oraz Order. W Managerze ma się znajdować słownik zamówień, w którym kluczem będzie obiekt zamówienia, a wartością jego ilość na stanie. W klasie Order natomiast mają znajdować się takie pola jak: id, nazwa, cena. 

Funkcjonalność programu to:
- dodawanie nowego zamówienia do słownika (jeżeli dodawać będziemy obiekt, którego id znajduje się już w słowniku, to nie będziemy dodawali nowej pary do dicta, ale zwiększali ilość danego obiektu w słowniku (zwiększali odpowiednią wartość w słowniku)).
- usuwanie o 1 zamówienia ze słownika o określonym id

Podpowiedź:
Pseudokod slownika:
self.orders = {obiekt1 : jego_ilosc}
Sprzedawanie produktu:

def sell(self, id_to_sell):
    for order in self.orders:
        if order.id == id_to_sell:
           self.orders[order] -= 1
'''

class Order:
    def __init__(self, order_id, nazwa, cena):
        self.id = order_id
        self.nazwa = nazwa
        self.cena = cena
    def __eq__(self, other):
        return self.id == other.id
    def __hash__(self):
        return hash(self.id)
    def __str__(self):
        return f"Order(id = {self.id}, name = {self.nazwa}, price = {self.cena})"

class Manager:
    def __init__(self):
        self.orders = {}
    
    def add_item(self, order):
        if order in self.orders:
            self.orders[order] += 1 
        else:
            self.orders[order] = 1

    def remove_item(self, order_id):
        for order in self.orders.keys():
            if order_id == order:
                if self.orders[order_id] > 1:
                    self.orders[order_id] -= 1
                else:
                    del self.orders[order_id]
                    break
    def display(self):
        for order,quantity in self.orders.items():
            print(f"ID : {order}, Quantity : {quantity}")
    
    


    
order1 = Order(1,"kutas",2.00)
order2 = Order(2,"janusz",1.50)

manager = Manager()

manager.add_item(order1)
manager.add_item(order2)
manager.display()

manager.add_item(order1)
manager.display()
print("________________")
manager.remove_item(order1)
manager.remove_item(order1)
manager.display()
    
