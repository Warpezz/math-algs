def factorial_finder(n):
    n2 = n - 1
    while n2 > 1:
        n = n * n2
        n2 -= 1
    return n

nToFac = input("Whatnumber?\n")

print(factorial_finder(int(nToFac)))