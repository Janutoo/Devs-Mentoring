'''
Słowniki - Rozszerzenie

Zad 1. 
Wprowadź poniższy słownik do programu. Program ma działać, tak jak poniżej:
• wyświetla wszystkie klucze na konsoli (tzn. nazwy wszystkich albumów),
• pobiera od użytkownika łańcuch tekstowy i sprawdza czy odpowiada on kluczowi ze słownika. 

Jeśli tak, to wyświetlany jest odpowiedni komunikat, np.: "Wykonawcą albumu "Achtung baby" jest “U2".
W przeciwnym razie wyświetlany jest komunikat: "Brak danych".

{'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza', 'Achtung Baby' : 'U2', 'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}

Zad 2. 
Zmodyfikuj kod z zadania 1 tak, aby możliwe było dodawanie i usuwanie przez użytkownika informacji o nowych albumach do słownika. Program ma zawierać proste menu.

Zad 3. 
Zapisz wszystkie wyrazy z poniższego tekstu do słownika (jako klucze). Wartości przypisane do tych kluczy mają być równe ilości wystąpień słowa w tekście.

"Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this, and nothing more."
 
Zad 4. 
Przekształć poniższy tekst, dopisując w nawiasach do polskich nazw ptaków ich łacińskie odpowiedniki.

Skorzystaj w tym celu ze słownika zawierającego następujące elementy:
{'kos' : 'Turdus merula', 'wilga' : 'Oriolus oriolus', 'rudzik' : 'Erithacus rubecula', 'kukulka' : 'Cuculus canorus', 'pleszka' : 'Phoenicurus phoenicurus', 'bogatka' : 'Parus major', 'drozd' : 'Turdus philomelos', 'zieba' : 'Fringilla coelebs', 'dzwoniec' : 'Chloris chloris', 'szczygiel' : 'Carduelis carduelis', 'szpak' : 'Sturnus vulgaris', 'kopciuszek' : 'Phoenicurus ochruros'}

Tekst:
W polowie maja, juz przed wschodem slonca, o trzeciej zaczyna spiewac drozd, po nim rudzik, a chwile pozniej kos. Pol godziny pozniej odzywa sie kukulka. Zaraz po niej budzi sie bogatka. Wraz ze wschodem slonca, o czwartej godzinie, swoj koncert rozpoczynaja pleszka i zieba. Dwadziescia minut pozniej i wilga akcentuje swoja obecnosc wysoko w koronach drzew. Jeszcze pozniej swoje trzy grosze dodaje szpak, a tuz po nim kopciuszek. Najwiekszymi spiochami w tej ferajnie okazuja sie byc dzwoniec i szczygiel.

Zad 5.
Napisz skrypt, który wygeneruje i wyprintuje słownik zawierający liczby pomiędzy (1 - n; n jest liczbą podawaną przez użytkownika) w formie (x, x*x).
Przykładowy input: n = 5
Oczekiwany wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

Zad 6.
Wyszukaj w zewnętrznych źródłach, jakie obiekty nie mogą być kluczami w słowniku. 

Zad 7.
Napisz program, który scali ze sobą dwa dowolne słowniki.
Mając do dyspozycji następujące słowniki:
lovers = {1: 'Rahima', 2: 'Alishba', 3: 'Fizza'}
friends = {4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}

Otrzymamy:
{1: 'Rahima', 2: 'Alishba', 3: 'Fizza', 4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}

Zwróć uwagę na to, że słowniki mogą być różnej długości.

Zad 8.
Napisz program, który wydrukuje wszystkie unikalne wartości ze słownika.
Dla danych:
{ "V":"S001", "VI": "S002","VIII": "S005", "IX":"S005", "X":"S009", "XI":"S007" }
Oczekujemy wyniku:
“S002”, “S009”, “S007”
'''

data = dict({ "V":"S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX":"S005", "X":"S009", "XI":"S007" })
uniq_value = set(data.values())
print(uniq_value)


list_values = [1, 2, 3, 4 , 3, 3 ,3 ,2 ,2]
uniq_valueV2 = set(list_values) # 0''
# for i in list_values:
#     if i not in uniq_valueV2:
#         uniq_valueV2.append(i) # uniq_value = [1]

print(uniq_valueV2)

# Zad 7.
# Napisz program, który scali ze sobą dwa dowolne słowniki.
# Mając do dyspozycji następujące słowniki:
# lovers = {1: 'Rahima', 2: 'Alishba', 3: 'Fizza'}
# friends = {4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}

# Otrzymamy:
# {1: 'Rahima', 2: 'Alishba', 3: 'Fizza', 4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}

# Zwróć uwagę na to, że słowniki mogą być różnej długości.

lovers = {1: 'Rahima', 2: 'Alishba', 3: 'Fizza'}
friends = {4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}
dict_2 = {}
size_of_lovers = len(lovers)

# for i in range(1, max(len(lovers),len(friends)) + 1 ): # 1: 3
#     #if lovers[i] == lovers.values() # !!! Rahima, Alishba, 
#      if i in lovers:
#         dict_2[i] = lovers[i] # lovers[1] = "Rahima"
#         # 1 = "Rahima" 
#      if i + size_of_lovers in friends:
#          dict_2[i + size_of_lovers] = friends[i+ size_of_lovers]
         
for key, value in lovers.items():
    dict_2[key] = value

for key, value in friends.items():
    dict_2[key] = value

print(dict_2)

   