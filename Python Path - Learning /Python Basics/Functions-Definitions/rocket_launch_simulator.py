def get_fuel_amount():
    while True:
        try:
            fuel = int(input("Podaj ilość paliwa: "))
            if 5000 <= fuel <= 30000:
                return fuel
            else:
                print("Podaj poprawną wartość 5000-30000")
        except ValueError:
            print("Podaj poprawną wartość")

def get_members_amount():
    while True:
        try:
            members = int(input("Podaj ilość członków: "))
            if 0 < members <= 7:
                return members
            else:
                print("Podaj poprawną wartość od 1-7")
        except ValueError:
            print("Podaj poprawną wartość")

def calculate_distance(fuel, members):
    distance = 0
    for i in range(0, fuel, 100):
        fuel -= (300 + 100 * members)
        print("Przebyto:", i)
        distance = i
        print("Pozostało paliwa:", fuel)
        if fuel <= 0:
            break
    return distance

def check_orbit_reach(distance):
    if distance > 2000:
        print("Statek dotarł na orbitę")
    else:
        print("Statek kosmiczny nie dotarł na orbitę")

def space_journey():
    fuel = get_fuel_amount()
    members = get_members_amount()
    distance = calculate_distance(fuel, members)
    check_orbit_reach(distance)

space_journey()