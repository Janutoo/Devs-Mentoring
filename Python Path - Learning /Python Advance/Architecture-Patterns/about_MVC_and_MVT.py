# MVC - Model- View Controller

# 1. Model (Dane i logika biznesowa) - odpowiada za zarządzanie danym i logiką aplikacji
# 2. View (Widok) - prezentuje dane użytkownikowi
# 3. Controller (Kontroler) - zarządzanie przepływem danych między modelem a widokiem

# +-----------+        +-----------+        +-------------+
# |  Model    | <----> | Controller | <----> |    View     |
# +-----------+        +-----------+        +-------------+
#   - Logika danych     - Obsługa żądań       - Interfejs użytkownika
#   - Obsługa bazy      - Zarządzanie modelami- Wyświetlanie danych
#   - Przetwarzanie     - Przekazywanie danych


class Student:
    def __init__(self, name , surname):
        self.name = name
        self.surname = surname
        


class StudentView:
    def display(self, student):
        print(f"student: {student.name} {student.surname}")


class StudentController:
    def __init__(self, student, view):
        self.student = student
        self.view = view
    
    def update_surname(self, new_surname):
        self.student.surname = new_surname
    
    def display_student(self):
        print(f"student :{self.student.name} {self.student.surname}")

        

student = Student("Jan", "Kowalski")
view = StudentView()
controller = StudentController(student, view)

controller.display_student()
controller.update_surname("Nowak")
controller.display_student()


'''
MVT: Model - View - Template

+-----------+        +-----------+        +-------------+
|  Model    | <----> |    View   | <----> |  Template   |
+-----------+        +-----------+        +-------------+
  - Baza danych      - Logika widoku       - HTML + dynamiczne dane
  - Przetwarzanie    - Pobieranie danych   - Formatowanie treści


Cecha: Kontroler
MVC -Recznie tworzymy
MVT - Obsługiwany przez framework

View
MVC wyświetla dane
MVT Wywołuj szablny Templaye(HTML, CSS)\


'''


# Zaimplementuj aplikację TODO w MVC – Model: zadania, View: lista zadań, 
# Controller: obsługa dodawania/usuwania.











