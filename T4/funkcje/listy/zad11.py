print("Prostokąt 7 x 6:")
for i in range(6):
    print("*******")

print("\nKwadrat 5 x 5 bez wypełnionego środka:")
for i in range(5):
    if i == 0 or i == 4:
        print("*****")
    else:
        print("* *")

print("\nChoinka o wysokości 5:")
i= 0
a=1
while i < 5:
    text = ('*'*a)
    text = text.center(20)
    print(text)
    a=a+2
    i+=1  