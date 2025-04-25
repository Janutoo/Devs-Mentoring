# # Zasada 1: Dobre nazewnictwo zmiennych i funckji

# p = '123456' # user's password
# y = datetime.date.today().year # Year

# user_password = '1235' # Klarowane nazwa zmiennych
# current_year = datetime.date.today().year 

# # Zasada 2: Unikaj komentarzy tam, gdzie nazwa funkcji mówi wszytkoL

# # Donwnload  list of active users
# def get_users():
#     ... 
# # BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD BAD

# def get_active_users():
#     ...

# # Zasada 3: Organizacja kodu w projekcie
# '''''
# project / 
#     main.py
#     utilis.py 

# Bad exampple !! 


# project/
#     src/ 
#         __init__.py
#         models.py
#         views.py
#         controller.py
#     test/
#         test_models.py
#         test_view.py
        
#     run.py
    
# ../ ../project

# python run.py
# '''

# # ZApytać o kolejemn zasady- mini test! 

# # S O L I D

# #S - Single Responsibility Principle (SRP)
# # "Jedna klasa powinna mieć tylko jedną odpowiedzialność."'


# class Raport:
#     def generate(self):
#         print("Generring raports .. ")
        
#     def send_email(self):
#         print("Sent email .. ")
        
# # Bad exaple 

# class ReportGenerator:
#     def generate(self):
#         return "Generating report"
    
# class EmailSender:
#     def send_email(self, report):
#         print(f"Sent email with {report}")

# # O - Open/Closed Principle (OCP)
# # "Kod powinien być otwarty na rozszerzenia, ale zamknięty na modyfikacje."


# class Payment:
#     def pay(self, method):
#         if method == "PayPal":
#             print("Payment wiht Paypal")
#         elif method == "Card":
#             print("Payment with Card")
#         elif method == "CreditCard":
#             print("payment with Credit Card")
#         elif method == "BitCoins":
#             ......
#             .
#             .
#             .
#             ..
#             .
#             .
#             .
            
            
# class Payment:
#     def pay(self):
#         raise NotImplementedError

# class PayPal(Payment):
#     def pay(self):
#         print("payment with Paypal")
        
# class CreditCard(Payment):
#     def pay(self):
#         print("Payment with Credit Card")
        
        
# #L – Liskov Substitution Principle (LSP)
# #"Obiekty klasy bazowej powinny być zastępowalne przez obiekty klas dziedziczących."


# class Rectangle:
#     def set_height(self, height):
#         self.height = height
    
#     def set_width(self, width):
#         self.widt = width


# class Square(Rectangle):
#     def set_width(self, width):
#         self.widt = width 

# # I – Interface Segregation Principle (ISP)
# # "Nie zmuszaj klas do implementowania metod, których nie używają."


# class Printer:
#     def print(self):
#         pass
    
#     def scan(self):
#         pass
    
#     def fax(self):
#         pass
    

# from abc import ABC, abstractmethod

# class Printer(ABC):
#     @abstractmethod
#     def print(self):
#         pass

# class Scanner(ABC):
#     @abstractmethod
#     def scan(self):
#         pass

# class SimplePrinter(Printer):
#     def print_document(self):
#         print("Printing sommting...")
        
# class MultiFuncPrinter(Printer, Scanner):
#     def print_document(self):
#         print("Printing sommting ...")
    
#     def scan(self):  
#         print("Scanning...")
        
# printer = SimplePrinter()
# multiFuncPrinter= MultiFuncPrinter()


# printer.print_document()


# #  D – Dependency Inversion Principle (DIP)
# # "Moduły wysokopoziomowe nie powinny zależeć od modułów niskopoziomowych."


# # class PostGreSQL:
# #     def get_data(self):
# #         return "Some data"

# # class MySQLDatabase:
# #     def get_data(self):
# #         return "Dane z SQL"
    
# # class DataFetcher:
# #     def __init__(self):
# #         self.db = MySQLDatabase()
        
        

# class Database:
#     def get_data(self):
#         raise NotImplementedError

# class MySQLDatabase(Database):
#     def get_data(self):
#         return "Dane z SQL"

# class PostgreSQLDatabase(Database):
#     def get_data(self):
#         return "Dane z PostgreSQL"
    
# class DataFetcher:
#     def __init__(self, db: Database):
#         self.db = db
    
#     def fetch(self):
#         print(self.db.get_data())
        

# mysql_fetcher = DataFetcher(MySQLDatabase())
# postgres_fetcher = DataFetcher(PostgreSQLDatabase())

# mysql_fetcher.fetch()
# postgres_fetcher.fetch()


# # 1. Która zasada Clean Code mówi o tym, że kod powinien być łatwy do czytania i rozumienia?

#  #A) Zasada jednej odpowiedzialności (Single Responsibility Principle - SRP)
# B) Czytelność i prostota
# # C) Hermetyzacja kodu


# # 2. Która zasada mówi o tym, że nazwy zmiennych powinny być znaczące i opisowe?
#  A) Nazewnictwo powinno być znaczące
# # B) Minimalizacja liczby komentarzy
# # C) Formatowanie kodu



# # 3. Jak najlepiej podzielić kod na moduły?
#  A) Według zależności biznesowych i funkcjonalności
# # B) Tak, aby każdy plik miał podobną ilość kodu
# # C) Tak, aby w jednym pliku znajdowało się jak najwięcej funkcji

# # 4. Co oznacza zasada Open/Closed Principle (OCP)?
# # A) Klasy powinny być zamknięte na modyfikacje, ale otwarte na rozszerzanie
#  B) Klasy powinny być otwarte na modyfikacje i rozszerzanie
# # C) Klasy powinny implementować wszystkie możliwe metody interfejsu


# # 5. Które z poniższych są częścią SOLID?
# # A) Single Responsibility Principle (SRP)
# # B) Open/Closed Principle (OCP)
#  C) Obie odpowiedzi są poprawne
 
# # 6. Jak poprawnie organizować bloki kodu?
# # A) Najpierw zmienne, potem funkcje, na końcu klasy
#  B) Najpierw najważniejsze funkcje, potem szczegóły implementacyjne
# # C) Nie ma znaczenia, ważne są tylko komentarze



# # KONIEC TEORII

# # 1. Popraw nazewnictwo zmiennych zgodnie z Clean Code

# # first_number = 100
# # second_number = 50
# # result = first_number * second_number
# # print(result)

# # width = 100
# # heihgt = 50
# # area  = width * heihgt
# # print(area)


# # 2. Popraw strukturę kodu zgodnie z zasadą S R P'

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def send_email(self, message):
#         print(f"Wysyłanie e-maila do {self.email}: {message}")

# ##### BAD #### 

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

# class EmailService:
#     def send_email(self, user, message):
#         print(f"Wysyłanie e-maila do {user.email}: {message}")


# user = User("karol", "karol@gmail.com")
# gmail = EmailService(user, "Hello")


#3.  Popraw kod zgodnie z zasadą Open/Closed Principle (OCP)


# class Payment:
#     def process_payment(self, method):
#         if method == "PayPal":
#             print("Płatność przez PayPal")
#         elif method == "CreditCard":
#             print("Płatność kartą")


class Payment:
    def procces_payment(self):
        raise NotImplementedError
    
class PayPal(Payment):
    def process_payment(self):
        print("Płatność przez PayPal")

class CreditCard(Payment):
    def process_payment(self):
        print("Płatność kartą")
        
        
payments = [PayPal(), CreditCard(), ]
for payment in payments:
    payment.process_payment()
    
    
#  4. Popraw kod zgodnie z Liskov Substitution Principle (LSP)

class Rectangle:
    def set_width(self, w):
        self.width = w
    
    def set_height(self, h):
        self.height = h

class Square(Rectangle):
    def set_width(self):
       pass