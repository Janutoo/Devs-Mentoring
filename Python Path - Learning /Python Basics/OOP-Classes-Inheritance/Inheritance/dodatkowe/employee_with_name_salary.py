# Opis:
# Utwórz klasę Employee z atrybutami name i salary. 
# Następnie stwórz klasę Manager, która dziedziczy po Employee i dodaj atrybut department. 
# Dodaj metodę, która wyświetli wszystkie informacje o menedżerze.
# Przykład:
# >>> emp = Employee("Alice", 5000)
# >>> mgr = Manager("Bob", 7000, "IT")
# >>> print(mgr.name)
# Bob
# >>> print(mgr.department)
# IT


class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
        
class Manager(Employee):
    def __init__(self, name, salary, departament):
        super().__init__(name, salary)
        self.departament = departament
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Departament: {self.departament}")
        