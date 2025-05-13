dictionary = {'The sensual World':'Kate Bush','Shaday':'Ofra Haza','Achtung Baby':'U2','Aion':'Dead Can Dance','Invisible Touch':'Genesis'}

print(dictionary.keys())

while True:
    text = input("Podaj nazwe: ")
    for i in dictionary:
        if i == text: 
            print(f"Wykonawcą albumu{i}  jest {dictionary[i]}")
            exit()
    print("Brak danych ")
    