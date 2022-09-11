def car_speed(time1,time2,camDistance):
    time1split = time1.split(":",1)
    time1hours = int(time1split[0]) * 60
    time1real = time1hours + int(time1split[1])

    time2split = time2.split(":",1)
    time2hours = int(time2split[0]) * 60
    time2real = time2hours + int(time2split[1])

    if time1real < time2real:
        timemins = time2real - time1real
    else:
        timemins = time2real + (1440 - time1real)

    timehours = timemins / 60

    speed_mph = int(camDistance) / timehours

    speed_mph_rounded = round(speed_mph, 2)

    return speed_mph_rounded

    '''
    mins = timemins % 60
    
    hours = int((timemins - mins) / 60)

    time = (f'{hours}h{mins}m')

    return time
    '''

time1 = input("what time did the car pass the first camera?\n")

if time1[2] != ":":
    print("Erorr: times must be given in a standard 24-hour format (XX:XX)")

time2 = input("what time did the car pass the second camera?\n")

if time2[2] != ":":
    print("Erorr: times must be given in a standard 24-hour format (XX:XX)")

camDistance = input("how far away are the cameras (mi)?\n")

speed = car_speed(time1,time2,camDistance)

print(f'{speed}mph')