# Podstawowe elementy wyrażeń regularnych
# 1. Znak kropki .
# Opis: Dopasowuje dowolny pojedynczy znak z wyjątkiem znaku nowej linii.
# Przykład: Wzorzec a.b dopasuje „a*b”, „a b”, ale nie „ab” ani „a\nb”.
# 2. Klasy znaków
# Klasy znaków pozwalają grupować określone typy znaków:

# \d - dowolna cyfra ([0-9]).
# \D - dowolny znak, który nie jest cyfrą.
# \s - dowolny biały znak (np. spacja, tabulator).
# \S - dowolny znak niebędący białym znakiem.
# \w - dowolny znak alfanumeryczny lub podkreślenie (litery, cyfry, _).
# \W - dowolny znak, który nie jest znakiem alfanumerycznym ani podkreśleniem.]

#Wzorzec \d\d-\d\d\d dopasuje np. „12-345”, czyli strukturę, w której występują dwie cyfry, myślnik i trzy cyfry.

# Flagi w wyrażeniach regularnych
# Flagi wpływają na sposób interpretacji wyrażenia:
# g (global): Znajduje wszystkie wystąpienia wzorca. Bez tej flagi zostanie dopasowane tylko pierwsze wystąpienie.
# m (multi-line): Sprawdza początek i koniec każdej linii oddzielnie.
# i (insensitive): Ignoruje wielkość liter – nie dopasuje Nie, NIE, itd.
# x (extended): Pozwala na dodanie białych znaków w celu poprawy czytelności wyrażenia (spacje, tabulatory).
# u (unicode): Rozszerza dopasowanie na znaki Unicode (np. polskie znaki).


# \nie\i - 


# ^ – Dopasowuje początek tekstu lub linii. ^Ala
# $ – Dopasowuje koniec tekstu lub linii.  xyz$
# . – Dopasowuje dowolny pojedynczy znak (z wyjątkiem nowej linii, chyba że użyta jest flaga s).

# * - dopasowuje 0 lub więcej powtórzeń danego znaku lub grupy.
# + - dopasowuje 1 lub więcej powtórzeń.
# ? - dopasowuje 0 lub 1 powtórzenie (element opcjonalny).
# {n} - dopasowuje dokładnie n powtórzeń.
# {n,m} - dopasowuje od n do m powtórzeń.


# \d{2,4}


# Grupy przechwytujące: Nawiasy () umożliwiają wyodrębnienie części wzorca. Można odwoływać się do nich po numerze.
# Grupy nieprzechwytujące: Zapis (?: ...) umożliwia tworzenie grup tylko dla czytelności, bez przypisania numeru.
# Grupy nazwane: Używane jako (?P<nazwa> ...) ułatwiają nawigację w skomplikowanych


# (\d{3})-(\d{2})-(\d{4}) lll-ll-llll
 
#  (?P<DAY>\d{2})-(?P<MONTH>\d{2})-(?P<YEAR>\d{4})

#  pattern = r"(?P<DAY>\d{2})-(?P<MONTH>\d{2})-(?P<YEAR>\d{4})"

# Day: 31
# Moint : 12
# Year : 2024
  
# clou?r color colour

# Karil|Kamil|Bartosz

# if(name == "Karol ") || (name == "Kamil") || (name == "Bartosz)
                                              
# \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}

# ^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$ - sprawdzenie adresu e mail

# [abc] - a, b, cdll Creates 
# [a-z] 
# ^[0-9]

# [A-Za-z]
# [a-zA-Z0-9_]

# <.*?> - <html>

# import re

# patern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]"

# re.match(patern)
# # re.search(patern)
# # re.sub(patern)
# # re.split(patern)


#ABC 12345

import re

patern = r"^[A-Z]{3} \d{5}$"
registrations = ["KRK 12345", "WWA 54321", "INVALID 123"]


for reg in registrations:
    result = re.match(patern, reg)

    if result:
        print(f"Numer rejestarcyny {reg} jest poprawny")

    else:
        print(f"Numer rejestarcyny {reg} jest nie poprawny")

# Zadanie: Sprawdź, czy w tekście e-maila znajduje się wzmianka o rabacie (np. słowa „rabat” lub „zniżka”).
# email_text = """
# Cześć! Chcielibyśmy poinformować, że na naszej stronie trwa promocja. 
# Skorzystaj z 10% rabatu na wszystkie produkty! 
# Pozdrawiamy, Zespół Promocji
# """

# Zadanie: W tekście dokumentu zamień wszystkie numery telefonów na „[UKRYTY]” dla zachowania prywatności.
# document_text = """
# Kontakt: 123-456-789 lub 987-654-321. Zadzwoń, aby uzyskać więcej informacji!
# """

# Zadanie: Podziel tekst zawierający listę zakupów, gdzie poszczególne pozycje są oddzielone przecinkiem lub średnikiem, na pojedyncze elementy.
# shopping_list = "chleb, masło; mleko, jajka; owoce, warzywa"


# Zadanie: Sprawdź poprawność adresu e-mail. Dodatkowo, jeśli jest poprawny, zmień wszystkie litery
# w adresie e-mail na małe litery.


emails = ["Test@Example.COM", "wrong-email@.com", "valid.email@domain.pl"]
patern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

'''

if match 
    lower
    pl != com 
'''
