# Cel: Stworzymy system zarządzania inteligentnym domem.

# System ma obsługiwać:
# Światło w korytarzu
# Drzwi główne
# Drzwi garażowe
# Użytkownik steruje całym systemem przez klasę RemoteControl, która jest naszą Fasadą.

# HallLight
# MainDoor
# GarageDoor 

# #Fasada
# RemoteControl 
import time
import threading

class HallLight:
    def __init__(self):
        self.name = "Hall Light"
        print("Hall Light added to the system")

    def turn_on(self):
        print("Hall Light switched on")

    def turn_off(self):
        print("Hall Light switched off")

class SensorTemperature:
    def __init__(self):
        self.temperature = 23  
        self.name = "Sensor Temperature"
        print(f"Temperature: {self.temperature} °C ")

    def get_temperature(self):
        return self.temperature

class MainDoor:
    def __init__(self):
        self.name = "Main Door"
        print("Main Door added to the system ")

    def open(self):
        print("Main Door opened")

    def close(self):
        print("Main Door closed")


class GarageDoor:
    def __init__(self):
        self.name = "Garage Door"
        print("Garage Door added to the system")

    def open(self):
        print("Garage Door opened")

    def close(self):
        print("Garage Door closed")

class RemoteControler:
    def __init__ (self):
        self.doors = {"main_door" : MainDoor(), "garage_door" : GarageDoor()}
        self.hall_light = HallLight() 
        self.temperature_sensor = SensorTemperature() 

    def turn_on_light(self):
        self.hall_light.turn_on()

    def turn_off_light(self):
        self.hall_light.turn_off()

    def open_doors(self):
        for door in self.doors.values():
            door.open()

    def close_doors(self):
        for door in self.doors.values():
            door.close()

    def get_current_temperature(self):
        return self.temperature_sensor.get_temperature()

def main():
    remoteControler = RemoteControler()
    remoteControler.turn_on_light()
    remoteControler.turn_off_light()
    remoteControler.open_doors()
    remoteControler.close_doors()
    current_temp = remoteControler.get_current_temperature()
    print(f"Current temperature: {current_temp} °C") 

if __name__ == "__main__":
    main()


# Ćwiczenia
# Dodaj nowy komponent do systemu (np. czujnik temperatury).
# Dodaj funkcję, która otwiera tylko konkretne drzwi (np. open_main_door()).
# # Zmień Fasadę tak, aby użytkownik mógł ustawić czas automatycznego zamykania drzwi.
