text = input("wprowadz tekst , conajmenij 7 znakow: ")
if len(text) <= 7:
   print("Tekst jest za krótki .")
else:
   print("Wprowadzony tekst: ", text)
   print("Liczba znaków: ", len(text))
   print("Pierwszy znak: ", text[0],"ostatni znak: ",text[-1])
   center = len(text) // 2
   print(" trzy znaki z środka: ", text[center-1:center+2])