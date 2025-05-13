with open("E:\github\Devs-Mentoring\T6\przyklad.txt",encoding="utf-8") as file:
    lines = file.readlines()
    numberOfLines = len(lines)
    for i in range(1, numberOfLines, 2):
        print(lines[i])
    file.close()

