# crazy skills learnt from fucking around in year 10 computing class

def prime_outputter(amountWanted):
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
    return primesList

amountWanted = input("How many p[rimes?\n")

print(prime_outputter(amountWanted))