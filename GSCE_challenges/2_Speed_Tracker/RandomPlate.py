import random,string

def make_plate(valid=True):
    if valid == True:
        plate = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        for _ in range(2):
            plate += random.choice(string.digits) 
        for _ in range(3):
            plate += random.choice(string.ascii_uppercase)
    else:
        plate = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
   
    return plate

if __name__ == '__main__':
    print(make_plate())