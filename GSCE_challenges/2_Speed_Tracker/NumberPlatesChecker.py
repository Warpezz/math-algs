#too many if statements i think but idk how else to do it; ill come back to this when im smorter

def plate_checker(numPlate):
    validPlate = True
    if len(numPlate) != 7:
        validPlate = False
    else:
        if numPlate[0:1].isalpha() == False:
            validPlate = False
        elif numPlate[2:3].isdigit() == False:
            validPlate = False
        elif numPlate[4:6].isalpha() == False:
            validPlate = False

    
    
    return validPlate

if __name__ == '__main__':
    numPlate = input("input a number plate of 7 alphanumeric characters\n")

    validPlate = plate_checker(numPlate)

    if validPlate:
        print("Plate follows the naming scheme")
    else:
        print("Plate is invalid")