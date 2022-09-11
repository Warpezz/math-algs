# only for multiplication

def sigma(firstVal,lastVal,multiply):
    output = 0
    for i in range(firstVal,lastVal):
        output += (i * multiply)
    return output

firstVal = int(input("input start value of n\n"))

lastVal = int(input("input end value of n\n"))

multiply = int(input("input multiplying rule\n"))

print(sigma(firstVal,lastVal,multiply))