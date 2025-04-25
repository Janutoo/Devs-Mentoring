# Zadanie 5 – Metody statyczne i klasowe
# Stwórz klasę TemperatureConverter do przeliczania temperatury między Celsiuszem i Fahrenheitem:
# •	Metody statyczne: celsius_to_fahrenheit(c) i fahrenheit_to_celsius(f).
# •	Metoda klasowa: description() – zwracająca opis działania klasy.




class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

    @classmethod
    def description(cls):
        return "Klasa TemperatureConverter służy do przeliczania temperatur między stopniami Celsjusza i Fahrenheita."

celsius = 25
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C to {fahrenheit}°F")

fahrenheit = 77
celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F to {celsius}°C")

print(TemperatureConverter.description())