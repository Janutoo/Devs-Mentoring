#Znajdź błąd w poniższym przykładzie realizującym odczyt danych z pliku: przyklad.txt.

plik = open("przyklad.txt", "r")
linie = plik.readlines()
print(linie)

#kod nie zawiera żadnych błędów ale plik się nie zamyka a moze skutkować to problemami z dostępem do pliku 

plik.close()