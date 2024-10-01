### Zadanie 3: Klasy `Task` i `TaskManager`
'''
**Opis**:
Utwórz klasę `Task`, która przechowuje opis zadania, datę rozpoczęcia i status (np. "do zrobienia", "w trakcie", "zakończone"). 
Klasa `TaskManager` zarządza listą zadań, umożliwiając dodawanie zadań, aktualizację statusu, 
wyświetlanie wszystkich zadań i usuwanie zakończonych zadań.
**Przykład:**   
```python
>>> task1 = Task("Zrobić zakupy", "2024-09-26", "do zrobienia")
>>> task2 = Task("Umyć auto", "2024-09-27", "w trakcie")
>>> manager = TaskManager()
>>> manager.dodaj_zadanie(task1)
>>> manager.dodaj_zadanie(task2)
>>> manager.wyswietl_zadania()
Masz takie zadania:
"Zrobić zakupy" - Data: 2024-09-26, Status: do zrobienia
"Umyć auto" - Data: 2024-09-27, Status: w trakcie
>>> manager.aktualizuj_status(task1, "zakończone")
>>> manager.usun_zakonczone()
>>> manager.wyswietl_zadania()
Masz takie zadania:
"Umyć auto" - Data: 2024-09-27, Status: w trakcie
'''
class Task:
    def __init__(self, opis, data, status):
        self.opis = opis 
        self.data = data
        self.status = status
    def __repr__(self):
        return f"{self.opis} - Data: {self.data}, Status: {self.status}"
    

class TaskManager:
    def __init__(self):
        self.listazadan = []
    def dodaj_zadanie(self, zadanie):
        self.listazadan.append(zadanie)
    def wyswietl_zadania(self):
        for i in self.listazadan:
            print(i)
    def usun_zakonczone(self):
        for i in self.listazadan:
            if i.status == "zakończone":
                self.listazadan.remove(i)
    def aktualizuj_status(self, _task, aktualizacja):
        _task.status = aktualizacja

        

        
task1 = Task("Zrobić zakupy", "2024-09-26", "do zrobienia")
task2 = Task("Umyć auto", "2024-09-27", "w trakcie")
manager = TaskManager()
manager.dodaj_zadanie(task1)
manager.dodaj_zadanie(task2)
manager.wyswietl_zadania()
manager.aktualizuj_status(task1, "zakończone")
manager.usun_zakonczone()
manager.wyswietl_zadania()
