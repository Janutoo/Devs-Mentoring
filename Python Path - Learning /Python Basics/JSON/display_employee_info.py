'''Zadanie 04: Pracownicy
Masz plik pracownicy.json, który przechowuje listę pracowników w firmie. Każdy pracownik ma imię, stanowisko oraz miesięczne wynagrodzenie. Twoim zadaniem jest napisać skrypt, który:

Wczyta dane z pliku JSON.
Wypisze imię, stanowisko oraz wynagrodzenie każdego pracownika.'''


import json

with open('E:\github\Devs-Mentoring\Jason\\pracownicy.json', 'r') as file:
    pracownicy_data = json.load(file)


for pracownik in pracownicy_data['pracownicy']:
    print(f"Imię: {pracownik['imie']}")
    print(f"Stanowisko: {pracownik['stanowisko']}")
    print(f"Wynagrodzenie: {pracownik['wynagrodzenie']} PLN")
    print()  
