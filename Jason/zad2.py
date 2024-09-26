import json


with open('E:/github/Devs-Mentoring/Jason/filmy.json', 'r') as file:
    filmy_data = json.load(file)

for film in filmy_data['filmy']:
    print(f"Tytuł: {film['tytul']}")
    print(f"Rok produkcji: {film['rok']}")
    print(f"Gatunki: {', '.join(film['gatunki'])}")
    print()  
