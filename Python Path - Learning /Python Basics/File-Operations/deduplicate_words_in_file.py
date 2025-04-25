with open("E:\github\Devs-Mentoring\T6\przyklad3.txt", "r",encoding="utf-8") as file:
    text = file.read()

def remove_repeated_words(text):
    words = text.split()
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            result.append(word)
            seen.add(word)
    return ' '.join(result)

cleaned_text = remove_repeated_words(text)


with open('E:\github\Devs-Mentoring\T6\przyklad4.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_text)