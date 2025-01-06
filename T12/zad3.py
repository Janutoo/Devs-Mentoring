# 3. Dekorator walidujący dane wejściowe
# Cel: Stworzyć dekorator validate_positive, który sprawdzi, czy wszystkie argumenty funkcji są liczbami dodatnimi.
# Opis: Jeśli którykolwiek z argumentów będzie ujemny, dekorator wypisze komunikat o błędzie i nie wywoła funkcji.

def validate_positive(func):
    def wrapper(*args):
        
        pass


@validate_positive
def check_additional(a, b):
    pass
    