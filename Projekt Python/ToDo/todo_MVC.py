# Zaimplementuj aplikację TODO w MVC – Model: zadania, View: lista zadań, 
# Controller: obsługa dodawania/usuwania.

# MODEL

class Task:
    def __init__(self, text, done=False):
        self.text = text
        self.done = done

    def __str__(self):
        return f"{int(self.done)}|{self.text}"

    @staticmethod
    def from_line(line):
        parts = line.strip().split("|", 1)
        return Task(parts[1], bool(int(parts[0])))

# VIEW
class View:
    def show(self, tasks):
        if not tasks:
            print("Brak zadań.")
        for i, task in enumerate(tasks):
            status = "[x]" if task.done else "[ ]"
            print(f"{i + 1}. {status} {task.text}")

# CONTROLLER
class Controller:
    def __init__(self):
        self.tasks = self.load_tasks()
        self.view = View()

    def add(self, text):
        self.tasks.append(Task(text))

    def remove(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def toggle(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = not self.tasks[index].done

    def run(self):
        while True:
            print("\n1. Dodaj  2. Usuń  3. Zmień status  4. Pokaż  5. Wyjdź")
            choice = input("Wybierz: ")

            if choice == "1":
                self.add(input("Zadanie: "))
            elif choice == "2":
                self.remove(int(input("Numer zadania: ")) - 1)
            elif choice == "3":
                self.toggle(int(input("Numer zadania: ")) - 1)
            elif choice == "4":
                self.view.show(self.tasks)
            elif choice == "5":
                self.save_tasks()
                print("Zapisano zadania. Do zobaczenia!")
                break
            else:
                print("Nieznana opcja.")

    def save_tasks(self):
        with open("todo.txt", "w", encoding="utf-8") as f:
            for task in self.tasks:
                f.write(str(task) + "\n")

    def load_tasks(self):
        try:
            with open("todo.txt", "r", encoding="utf-8") as f:
                return [Task.from_line(line) for line in f]
        except FileNotFoundError:
            return []

# URUCHOMIENIE
Controller().run()
