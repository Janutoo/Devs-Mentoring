_range = int(input("podaj ilość liczb: "))
number = 0
prev_number = 1
i = 0
while i < _range: 
    prev_number,number = number,prev_number + number
    i+=1
    print(number)



    