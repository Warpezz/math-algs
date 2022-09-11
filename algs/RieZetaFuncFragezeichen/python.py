# uh i kinda forgor how this works :D

def rz_function(s,accuracy): # 'accuracy' as in the amount of inverse powers to add
    output = 0
    for i in range(1,accuracy):
        output += (1/(i ** s))
    return output

s = input("what power are we using\n")

accuracy = input("how accurate would you like it to be or whatever idfk\n")

print(rz_function(int(s),int(accuracy)))
