'''Masz plik JSON o nazwie uczniowie.json, który przechowuje informacje o uczniach w szkole. Każdy uczeń ma swoje imię, wiek i listę przedmiotów, na które uczęszcza. Twoim zadaniem jest napisać skrypt, który:
1.Wczyta dane z pliku JSON.
2.Wypisze imię i wiek każdego ucznia.
3.Wypisze wszystkie przedmioty, na które uczęszcza każdy uczeń.'''

import json

with open('E:/github/Devs-Mentoring/Jason/uczniowie.json', 'r') as file:
    uczniowie_data = json.load(file)

for uczen in uczniowie_data['uczniowie']:
    print(f"Imię: {uczen['imie']}, Wiek: {uczen['wiek']}")

    print("Przedmioty:", ", ".join(uczen['przedmioty']))
    print() 
