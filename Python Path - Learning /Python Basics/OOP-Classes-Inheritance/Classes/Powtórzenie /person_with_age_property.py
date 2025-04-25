class InvalidAgeException(Exception):
    pass


class Person:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 0 <= value <= 130:
            self._age = value
        else:
            raise InvalidAgeException("Wiek musi być w zakresie 0-130.")



try:
    person1 = Person(25)
    print(f"Wiek: {person1.age}")

    person1.age = 30
    print(f"Nowy wiek: {person1.age}")

    person1.age = 150
except InvalidAgeException as e:
    print(f"Błąd: {e}")

try:
    person2 = Person(15)
    print(f"Wiek: {person2.age}")
except InvalidAgeException as e:
    print(f"Błąd: {e}")

try:
    person3 = Person(-5)
    print(f"Wiek: {person3.age}")
except InvalidAgeException as e:
    print(f"Błąd: {e}")