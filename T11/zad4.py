import re

def funkcja(string):
    patern = r'^[a-z]+[s]+[s]'
    return bool(re.match(patern, string))


print(funkcja("iksss"))