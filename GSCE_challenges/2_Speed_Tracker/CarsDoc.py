from SpeedCamera import car_speed,random_speed
from NumberPlatesChecker import plate_checker
from RandomPlate import make_plate
import random,string

class Car:
    def __init__(self, speed, plate):
        self.speed = speed
        self.plate = plate

amountWanted = int(input("How many random cars should be created?\n"))

cars = [Car(random_speed(),make_plate()) for i in range(amountWanted)]

# TODO: speed and exceeding speed limit bool, randomised num plates and whether valid
