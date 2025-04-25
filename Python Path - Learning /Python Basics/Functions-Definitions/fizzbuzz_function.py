def fizz_buzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return"FizzBuzz"
    if number % 3 == 0:
        return"Fizz"    
    if number % 5 == 0: 
        return"Buzz"
number = int(input("Podaj liczbe"))
print(fizz_buzz(number))




