'''Zadanie 03: Książki
Masz plik ksiazki.json, który zawiera listę książek. Każda książka ma tytuł, autora oraz liczbę stron. Twoim zadaniem jest napisać skrypt, który:

Wczyta dane z pliku JSON.
Wypisze tytuł każdej książki, autora oraz liczbę stron.'''

import json

with open('E:/github/Devs-Mentoring/Jason/ksiazki.json', 'r', encoding="utf-8") as file:
    ksiazki_data = json.load(file)

for ksiazka in ksiazki_data['ksiazki']:
    print(f"Tytuł: {ksiazka['tytul']}")
    print(f"Autor: {ksiazka['autor']}")
    print(f"Liczba stron: {ksiazka['strony']}")
    print()  
