class Student:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.grades = []

    def add_grades(self, grades):
        self.grades.append(grades)
    
    def average(self, numbers):
        return sum(numbers)/len(numbers)
    
    def __repr__(self):
        return f"{self.name} {self.last_name}, Oceny: {self.grades}, SREDNIA: {self.average(self.grades)}"
    

student1 = Student("Kamil","Janusz")
data = [1,2,3,4,5,6,7,8]
value = student1.average(data)  
print("some value: ", value)
