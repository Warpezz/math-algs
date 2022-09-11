from SpeedCamera import car_speed
from NumberPlates import plate_checker
import random,string

class Car:
    def __init__(self, speed):
        self.speed = speed
        # self.plate = plate


x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))

time1mins = random.randint(0,1439)

time2mins = random.randint((time1mins - 60),(time1mins + 60))

distance = (random.randint(1,100)) / 10

car1 = Car(car_speed(time1mins,time2mins,distance))

print(car1.speed)

# TODO: speed and exceeding speed limit bool, randomised num plates and whether valid
