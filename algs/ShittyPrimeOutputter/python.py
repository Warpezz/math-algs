# crazy skills learnt from fucking around in year 10 computing class

def prime_outputter(amountWanted):
    global primesList
    primesList = []
    numToTest = 2
    while len(primesList) < amountWanted:
        isPrime = True
        # producing primes
        divisor = numToTest - 1
        while divisor > 1:
            if (numToTest % divisor == 0):
                isPrime = False
            divisor -= 1
        if isPrime == True:
            primesList.append(numToTest)
        numToTest += 1

amountWanted = input("How many p[rimes?\n")

prime_outputter(int(amountWanted))

print(primesList)