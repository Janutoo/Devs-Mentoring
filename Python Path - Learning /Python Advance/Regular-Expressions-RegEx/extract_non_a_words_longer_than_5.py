import re

def funkcja(string):
    patern = r'\b[b-zB-Z]{6,}\b'
    return re.findall(patern, string)
    
print(funkcja("wyroby rzeka kotek dom ekrany słowik"))