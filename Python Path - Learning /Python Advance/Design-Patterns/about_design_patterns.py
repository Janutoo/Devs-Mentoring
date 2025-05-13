# Factory Method

# import random
# from abc import ABC 

# class Message(ABC):
#     counter = 0
    
#     def __init__(self):
#         self.id = Message.counter
#         Message.counter  += 1 

#     def show(self):
#         raise NotImplemented
            
# class HardwareMessage(Message):
#     def __init__(self):
#         super().__init__()
#         self.show()
        
#     def show(self):
#         print(f"Problem z komponentem sprzętowym! ID: {self.id}")
            
# class SoftwareMessage(Message):
#     def __init__(self):
#         super().__init__()
#         self.show()
    
#     def show(self):
#         print(f"Problem z systemem operacyjnym! ID: {self.id}") 

# # Factory Methods
# def error_factory():
#     error_types = {b"0xf": HardwareMessage, b"0x0": SoftwareMessage}
#     rand_error = random.choice(list(error_types))
#     error_types[rand_error]()
        

# def main():
#     for _ in range(5):
#         error_factory()


# if __name__ == "__main__":
#     main()
    
#  Zadanie 1: Implementacja Factory Method dla kont bankowych
# Instrukcja:
# Napisz kod, który będzie tworzył trzy typy kont bankowych:

# PersonalAccount
# BusinessAccount
# SavingsAccount
# Zaimplementuj metodę fabrykującą (create_account()), która na podstawie typu konta zwróci odpowiedni obiekt.


# Abstract factory

from abc import ABC

class Button(ABC):
    def render(self):
        raise NotImplementedError

    
class WindowsButton(Button):
    def render(self):
        print("Renderowanie przycisku dla Windows...")


class GUIFactory(ABC):
    def create_button(self):
        raise NotImplemented
        
    
class UnixButton(Button):
    def render(self):
        print("Renderowanie przycisku dla Unix...")


    
class UnixFactory(GUIFactory):
    def create_button(self) -> UnixButton:
        return UnixButton()

    
def get_factory(systen: str) -> GUIFactory:
    factories = {"Windows" : WindowsFactory, "Unix" : UnixFactory}
    return factories[systen]()


class WindowsFactory(GUIFactory):
    def create_button(self) -> WindowsButton:
        return WindowsButton()



def main():
    system_name = "Windows"
    factory = get_factory(system_name)
    button = factory.create_button()
    button.render()
    
    system_name = "Unix"
    factory = get_factory(system_name)
    button = factory.create_button()
    button.render()
    
if __name__ == "__main__":
    main()
    
# Zadanie 2: Implementacja Abstract Factory dla bazy danych
# Instrukcja:
# Napisz kod, który będzie tworzył połączenie z bazą danych w zależności od jej typu:

# MySQLDatabase
# PostgreSQLDatabase
# Za pomocą Abstract Factory utwórz fabryki:

# MySQLFactory
# PostgreSQLFactory
# Każda baza danych powinna posiadać metodę connect().

    