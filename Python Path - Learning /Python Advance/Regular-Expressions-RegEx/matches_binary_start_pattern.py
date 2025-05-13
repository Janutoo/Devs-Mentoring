import re 

def funkcja(string):
    patern = r'^[0b]'
    return bool(re.match(patern, string))

print(funkcja("bitam1234"))
print(funkcja("witam1234"))
print(funkcja("0itam1234"))