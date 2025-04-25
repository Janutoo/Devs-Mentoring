dictionary = {'The sensual World':'Kate Bush','Shaday':'Ofra Haza','Achtung Baby':'U2','Aion':'Dead Can Dance','Invisible Touch':'Genesis'}

print(dictionary.keys())

while True:
    try:
        print("1.Dodawanie informajci o albumach ")
        print("2.Usuwanie informacji o albumach  ")
        print("3.Sprawdź czy album jest w słowniku ")
        choice = input(int("Wprowadź numer z menu:"))
        if choice == 1:
            add_key = input("dodaj album: ")
            add_value = input("dodaj wykonawce: ")
            dictionary.update({add_key:add_value})
        if choice == 2:
            pass
        if choice == 3: 
            text = input("Podaj nazwe: ")
            for i in dictionary:
                if i == text: 
                    print(f"Wykonawcą albumu{i}  jest {dictionary[i]}")
                    exit()
            print("Brak danych ")
    except ValueError:
        print("Błedna wartość")
    