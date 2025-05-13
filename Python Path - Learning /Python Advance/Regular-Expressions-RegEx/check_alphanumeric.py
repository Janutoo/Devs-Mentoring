import re

def funkcja(string):
    pattern = r'^[a-zA-Z0-9]+$'
    return bool(re.fullmatch(pattern, string))

print(funkcja("witam42313"))

