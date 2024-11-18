# Zadanie 3: Klasy Person i Student
# Opis:
# Stwórz klasę Person z atrybutami name (imię) i age (wiek).
# Następnie utwórz klasę Student, która dziedziczy po Person, i dodaj atrybut student_id. 
# Dodaj metodę, która wyświetli wszystkie informacje o studencie.
# Przykład:
# >>> person = Person("John", 30)
# >>> student = Student("Anna", 20, "S1234")
# >>> print(student.name)
# Anna
# >>> print(student.student_id)
# S1234

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    

class Student(Person):
    def __init__(self, name,age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"student ID: {self.student_id}")