import re

def funkcja(string):
    patern = r'^[a-z]+[_]+[a-z]+$'
    return bool(re.match(patern, string))

print(funkcja("DdsaSdalollll9"))
print(funkcja("poprawny_dobry"))