# 1. Dekorator liczący czas wykonania funkcji
# Cel: Stworzyć dekorator measure_time, który zmierzy czas wykonania funkcji i wypisze go na ekran.
# Opis: Dekorator powinien korzystać z modułu time do zmierzenia czasu przed i po wykonaniu funkcji,
#  a następnie obliczyć różnicę.

# 2. Dekorator dodający logowanie
# Cel: Stworzyć dekorator log_execution, który loguje rozpoczęcie i zakończenie wykonywania funkcji.
# Opis: Dekorator wypisuje komunikaty przed i po wykonaniu dekorowanej funkcji.

# 3. Dekorator walidujący dane wejściowe
# Cel: Stworzyć dekorator validate_positive, który sprawdzi, czy wszystkie argumenty funkcji są liczbami dodatnimi.
# Opis: Jeśli którykolwiek z argumentów będzie ujemny, dekorator wypisze komunikat o błędzie i nie wywoła funkcji.

# . Użycie @staticmethod i @classmethod
# Cel: Ćwiczenie dekoratorów wbudowanych w Pythonie (@staticmethod, @classmethod).
# Opis: Stworzyć klasę MathUtils z dwiema metodami. @staticmethod nie korzysta z obiektu klasy, 
# a @classmethod operuje na samej klasie.

# 5. Dekorator @property
# Cel: Przećwiczenie dekoratora @property do definiowania właściwości.
# Opis: Stworzyć klasę Rectangle, która pozwala obliczyć pole prostokąta oraz zaktualizować szerokość z walidacją.

# 6. Dekorator przyjmujący argumenty
# Cel: Stworzyć dekorator repeat(n), który wykonuje funkcję n razy.
# Opis: Dekorator musi przyjmować dodatkowe argumenty, dlatego będzie potrzebna funkcja zagnieżdżona.

# 7. Łączenie dekoratorów
# Cel: Stworzyć dwa dekoratory uppercase i exclaim, a następnie użyć ich razem.
# Opis: Dekoratory modyfikują wyniki funkcji, zamieniając tekst na wielkie litery i dodając wykrzyknik.