numbersofCats = int(input("Ile kotów ma Ala?: "))
print(f"Dzisiaj Ala znalazła jeszcze 3 koty w parku.")
numbersofCats += 3
zdanie = f"Teraz Ala ma już {numbersofCats} kotów"
print(zdanie)
print(','.join(zdanie.split()))
print('\n'.join(zdanie.split()))
zdanie = zdanie.lower()
print(zdanie)
zdanie = zdanie.capitalize()
print(zdanie)