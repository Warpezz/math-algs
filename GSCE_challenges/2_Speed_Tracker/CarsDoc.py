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

cars = [Car(random_speed(),make_plate(bool(random.randint(0,1)))) for i in range(amountWanted)]

i = 1
for _ in cars:
    print(f"car {i}: speed = {_.speed}mph, is speeding = {_.isSpeeding}, number plate = {_.plate}, plate is valid = {_.hasValidPlate}")
    i += 1
