
# Zad 8.
# Stwórz funkcję, która przyjmować będzie dowolny zestaw parametrów reprezentowanych przez **kwargs. 
# Następnie niech taka funkcja utworzy z kwargs słownik, który będzie składał się z takim 
# samych par klucz:wartość co kwargs, ale będą one odwrócone.
# Na przykład:
# Gdy kwargs przyjmie postać {klucz1:wartość1, klucz2:wartość2}, to powstały słownik ma mieć 
# następującą strukturę: {wartość1:klucz1, wartość2:klucz2}. 

# Następnie zapisz tak utworzony słownik do pliku o nazwie output.json.

import json

def save_reversed_kwargs_to_file(**dictionaryWithKeywords):

    # dictionaryWithKeywords = {name: "Karol", age : 26}
    reversed_dict = dict()

    for key, value in dictionaryWithKeywords.items():
        reversed_dict[value] = key 
        
    with open('output.json','w') as data:
        json.dump(reversed_dict, data, ensure_ascii=False, indent=4)

save_reversed_kwargs_to_file(name="Karol", age=26)




