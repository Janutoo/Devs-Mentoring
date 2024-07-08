weight = float(input("Podaj wagę: "))
height = float(input("Podaj wzrost: "))

bmi = weight / (height * height)
bmi = bmi * 10000

if bmi < 18.5:
    print("Masz niedowagę")
elif 18.5 <= bmi < 24:
    print("Waga normalna")
elif 24 <= bmi < 26.5:
    print("Lekka nadwaga")
elif 26.5 <= bmi < 30:
    print("Nadwaga")
elif 30 <= bmi < 35:
    print("Nadwaga i Otyłość I stopnia")
elif 35 <= bmi < 40:
    print("Nadwaga i Otyłość II stopnia")
elif bmi >= 40:
    print("Nadwaga i Otyłość III stopnia")