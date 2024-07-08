d = (1,[2,4],'tekst',3+5j,'abc')
n = len(d)
i=0

print(d[-1])
print(d[0],d[1])

while i < n:
    if d[i] == 'abc':
        print("abc jest elementem krotki")
        break
    i+=1
else:
    print("abc nie jest elementem krotki")