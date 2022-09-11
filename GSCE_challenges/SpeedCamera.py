def car_speed(time1,time2):
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

    mins = timemins % 60
    
    hours = int((timemins - mins) / 60)

    time = (f'{hours}h{mins}m')

    return time

time1 = input("what time did the car pass the first camera?\n")

if time1[2] != ":":
    print("Erorr: times must be given in a standard 24-hour format (XX:XX)")

time2 = input("what time did the car pass the second camera?\n")

if time2[2] != ":":
    print("Erorr: times must be given in a standard 24-hour format (XX:XX)")

time = car_speed(time1,time2)

print(time)