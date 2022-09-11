import random

def get_time_from_24hour(time):
    timeSplit = time.split(":",1) # splitting it up into hours and minutes
    hoursPartInMinutes = int(timeSplit[0]) * 60
    timeReal = hoursPartInMinutes + int(timeSplit[1]) # total time in minutes

    return timeReal

def random_speed():
    time1mins = random.randint(0,1439)

    time2mins = random.randint((time1mins + 1),(time1mins + 60))

    distance = (random.randint(1,100))

    speed = car_speed(time1mins,time2mins,distance)

    return speed

def car_speed(time1Real,time2Real,camDistance):
    # gets difference
    if time1Real < time2Real:
        timemins = time2Real - time1Real
    else:
        timemins = time2Real + (1440 - time1Real)

    timehours = timemins / 60

    speed_mph = int(camDistance) / timehours

    speed_mph_rounded = round(speed_mph, 2)

    return speed_mph_rounded

def get_difference_hoursmins(difference):
    mins = difference % 60
    
    hours = int((difference - mins) / 60)

    time = (f'{hours}h{mins}m')

    return time

def make_speed():
    time1 = input("what time did the car pass the first camera?\n")

    if time1[2] != ":":
        print("Erorr: times must be given in a standard 24-hour format (XX:XX)")

    time2 = input("what time did the car pass the second camera?\n")

    if time2[2] != ":":
        print("Erorr: times must be given in a standard 24-hour format (XX:XX)")

    camDistance = input("how far away are the cameras (mi)?\n")

    time1Real = get_time_from_24hour(time1)
    time2Real = get_time_from_24hour(time2)

    speed = car_speed(time1Real,time2Real,camDistance)

    print(f'{speed}mph')

if __name__ == '__main__':
    make_speed()