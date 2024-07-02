word = input("Podaj słowo: ")
letters = len(word)
i = 0
positon = -1
text = ''
while i < letters:
    text = text + word[positon]
    positon -=1
    i+=1
if text == word:
    print("wyraz jest palindromem")
else:
    print("wyraz nie jest palindromem")