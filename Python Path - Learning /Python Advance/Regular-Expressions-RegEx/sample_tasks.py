# Zadanie: Sprawdź, czy w tekście e-maila znajduje się wzmianka o rabacie (np. słowa „rabat” lub „zniżka”).
# email_text = """



import re

email_text = """Cześć! Chcielibyśmy poinformować, że na naszej stronie trwa promocja. 
Skorzystaj z 10% rabatu na wszystkie produkty! 
Pozdrawiamy, Zespół Promocji
"""
paterrn = r"(rabat[a-z]*|zniżk[a-z]*)" # żnika, żniki itp itd

has_discount = bool(re.search(paterrn, email_text))
print(has_discount)

matches = re.findall(paterrn, email_text)
print(matches)
# pattern_defutl = r"\b(rabat|zniżka)" # rabat, zniżka 



# with open ("T11/teskt") as file: 
#     text = file.read()
#     words = text.split()
#     seen = set()
#     result = []
#     for word in words:
#         if word not in seen:
#             result.append(word)
#             seen.add(word)
#     print(result)
#     for i in result:
#         wynik = re.match(patern, i)

#         if i == patern:
#             print(i)
    

