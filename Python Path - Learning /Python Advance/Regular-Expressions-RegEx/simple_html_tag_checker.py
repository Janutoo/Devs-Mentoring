import re

def html_element(html):
   
    pattern = r'^<([a-zA-Z][a-zA-Z0-9]*)>\s*.*?\s*</\1>$'
    return bool(re.match(pattern, html))

print(html_element("<p>Twój tekst</p>"))  
print(html_element("<h1>Twój tekst</h1>"))  
print(html_element("<div>Coś tam <span>innego</span></div>")) 