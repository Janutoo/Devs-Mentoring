class InvalidUserDataException(Exception):
    pass


class User:
    

    def __init__(self, username, age):
        if age <= 0:
            raise InvalidUserDataException("Wiek musi być większy niż 0.")
        if len(username) <= 3:
            raise InvalidUserDataException("Nazwa użytkownika musi mieć więcej niż 3 znaki.")

        self.username = username
        self.age = age


# Przykłady użycia
try:
    user1 = User("Jan", 25)
    print(f"Użytkownik: {user1.username}, Wiek: {user1.age}")

    user2 = User("An", 0) 
except InvalidUserDataException as e:
    print(f"Błąd: {e}")

try:
    user3 = User("Anna", 28)
    print(f"Użytkownik: {user3.username}, Wiek: {user3.age}")
except InvalidUserDataException as e:
    print(f"Błąd: {e}")

try:
    user4 = User("Piotr", -5)
    print(f"Użytkownik: {user4.username}, Wiek: {user4.age}")
except InvalidUserDataException as e:
    print(f"Błąd: {e}")

try:
    user5 = User("Ja", 22)
    print(f"Użytkownik: {user5.username}, Wiek: {user5.age}")
except InvalidUserDataException as e:
    print(f"Błąd: {e}")