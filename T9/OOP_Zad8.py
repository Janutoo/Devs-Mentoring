# # ; Zad. 8
# # ; Rozważ klasę Case, która będzie inicjalizowana wraz z poniższymi danymi:

# # ; first_case = {
# # ;     ‘name’: ‘first_case’,
# # ;     ‘created_task’: ‘2021-10-26T19:48:12+00:00’,
# # ;     ‘end_task’: None
# # ; }

# # ; second_case = {
# # ;     ‘name’: ‘second_case’,
# # ;     ‘created_task’: ‘2021-09-26T19:48:12+00:00’,
# # ;     ‘end_task’: ‘2021-10-26T19:48:12+00:00’
# # ; }

# # ; Klasa Case ma zawierać metodę retrieve_seconds, która zwracać będzie różnicę czasową między end_task a created_task podaną w sekundach.

# # ; UWAGA
# # ; Wartość None przypisana do klucza end_task oznacza, że task jeszcze trwa. 
# # ; Zwróć uwagę na to, iż retrieve_seconds możemy wywoływać wielokrotnie 

# from datetime import datetime, timezone

# # datatime.now(timezone.utc) 

# class Case:
#     def __init__(self, data):
#         self.name = data['name']
#         self.created_task = self.to_data_time(data['created_task'])      
#         self.end_task = self.to_data_time(data['end_task'])
    
#     def to_data_time(self, data_str):
#         if data_str is None:
#             return None
#         return datetime.fromisoformat(data_str)
        
#     def print_values(self):
#         print(self.name)
#         print(self.created_task)
#         print(self.end_task)
        
        
#     def retrive_seconds(self):
#         if self.end_task is None:
#             end_time = datetime.now(timezone.utc)
#         else:
#             end_time = self.end_task
       
#         delta = end_time - self.created_task
#         return int(delta.total_seconds())
      
    
    
# first_case = {
#     'name': 'first_case',
#     'created_task': '2021-10-26T19:48:12+00:00',
#     'end_task': None
# }

# second_case = {
#     'name': 'second_case',
#     'created_task': '2021-09-26T19:48:12+00:00',
#     'end_task': '2021-10-26T19:48:12+00:00'
# }

# '2021-10-26T19:48:12+00:00'


# case1 = Case(first_case)
# # case1.print_values()
# seconds = case1.retrive_seconds()
# print(seconds)

# case2 = Case(second_case)
# # case2.print_values()
# seconds2 = case2.retrive_seconds()
# print(seconds2)



# Utwórz klasę bazową Vehicle (Pojazd) oraz dwie klasy pochodne Car (Samochód) i Bicycle (Rower).

# Klasa Vehicle powinna mieć atrybut:

# brand (marka pojazdu)
# oraz metodę:

# move(), która zwraca tekst "Pojazd się porusza...".
# Klasy Car oraz Bicycle dziedziczą po klasie Vehicle. Każda z nich powinna nadpisać metodę move():

# Metoda klasy Car powinna zwracać "Samochód jedzie drogą."
# Metoda klasy Bicycle powinna zwracać "Rower jedzie ścieżką rowerową."

from abc import ABC, abstractmethod
class Vehicle: 
    def __init__(self, brand):
        self.brand = brand


    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    
    def move(self):
        return("Samochód jedzie drogą")
    


class Bicycle(Vehicle):
    def move(self):
        return ("Rower jedzie ścieżką")

vehicle = Vehicle("Generic")
car = Car("Toyota")
bike = Bicycle("Kross")

print(vehicle.move())
print(car.move())
print(bike.move())