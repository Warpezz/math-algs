from SpeedCamera import car_speed,random_speed
from NumberPlatesChecker import plate_checker
from RandomPlate import make_plate
import random,string

class Car:
    def __init__(self, speed, plate):
        self.speed = speed
        self.plate = plate
        self.isSpeeding = False
        self.hasValidPlate = True

        if self.speed > 70:
            self.isSpeeding = True

        if plate_checker(self.plate) == False:
            self.hasValidPlate = False
        

amountWanted = int(input("How many random cars should be created?\n"))

cars = [Car(random_speed(),make_plate()) for i in range(amountWanted)]

print(cars[0].speed)
print(cars[0].isSpeeding)
print(cars[0].plate)
print(cars[0].hasValidPlate)

# TODO: speed and exceeding speed limit bool, randomised num plates and whether valid
