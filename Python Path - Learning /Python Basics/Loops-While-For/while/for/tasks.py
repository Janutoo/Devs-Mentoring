# A)
print('*' * 10)
# B)
for i in range(5):
    print('*'*i)
# C)
i = 0
while i <3:
    print('*'*3)
    i+=1
# D)
i= 0
a=1
while i <= 5:
    text = ('*'*a)
    text = text.center(20)
    print(text)
    a=a+2
    i+=1
