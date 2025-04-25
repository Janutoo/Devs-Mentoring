class Author:
   
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author  
        self.price = price

    def get_description(self):
        return f"Tytuł: {self.title}, Autor: {self.author}, Cena: {self.price} zł"


author1 = Author("Adam", "Mickiewicz")
book1 = Book("Pan Tadeusz", author1, 35.99)

print(book1.get_description())

author2 = Author("Henryk", "Sienkiewicz")
book2 = Book("Quo Vadis", author2, 42.50)

print(book2.get_description())