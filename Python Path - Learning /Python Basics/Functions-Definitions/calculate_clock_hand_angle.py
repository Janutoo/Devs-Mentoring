def tarcza(hour,minutes):
    hour = hour % 12 
    tarcza_minutes = minutes * 6
    tarcza_hour = hour*30 
    return abs(tarcza_hour-tarcza_minutes)

hour = int(input("Podaj godzinę: "))
minutes = int(input("Podaj minuty: "))
print(tarcza(hour,minutes))