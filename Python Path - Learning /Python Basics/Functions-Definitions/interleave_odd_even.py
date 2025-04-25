#Zad 5.
#Prześlij przy użyciu **kwargs listę liczb parzystych i nieparzystych. 
# W funkcji dokonaj ich połączenia w jedną listę 
# w następujący sposób: [nieparzysta, parzysta nieparzysta, parzysta ...]

# **kwargs = dict(key : valu, ... , ..., ...)

def combine_even_odd(**kwargs):
    even_numbers = kwargs.get('even', list()) # even_numbers = [2, 4, 6]
    odd_numbers = kwargs.get('odd', list())
    combine_list = list()
    
    for i in range(max(len(even_numbers),len(odd_numbers))): # max(3, 3)  = 3 
        if i < len(odd_numbers):
            combine_list.append(odd_numbers[i])

        if i < len(even_numbers):
            combine_list.append(even_numbers[i])

    print(combine_list)

    
#kwargs = even : even_numbers, odd : odd_number

even_numbers = [2, 4, 6] # type = list() 
odd_numbers = [1, 3, 5] # type = list() 
#key = value
print(combine_even_odd(even=even_numbers, odd=odd_numbers))