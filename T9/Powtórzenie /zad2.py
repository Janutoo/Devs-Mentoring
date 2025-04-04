# Stwórz klasę bazową Employee (pracownik), która zawiera imię, nazwisko oraz podstawową pensję. Następnie utwórz dwie klasy dziedziczące:
# •	Developer – dodatkowy atrybut: język programowania.
# •	Manager – dodatkowy atrybut: liczba podwładnych.
# Każda klasa potomna ma mieć własną metodę opisującą rolę pracownika.
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, last_name, salary):
        self.name = name 
        self.last_name = last_name
        self.salary = salary
    
    @abstractmethod
    def introduce_yorus_self(self):
        pass



class Developer(Employee):
    def __init__(self, programming_language):
        self.programing_language = programming_language
    
    def introduce_yorus_self(self):
        print("I'm a Developer")

class Manager(Employee):
    def __init__(self, number_of_subordinates):
        self.number_of_subordinates = number_of_subordinates

    def introduce_yorus_self(self):
        print("I'm a Manager!")
        
    

        
    