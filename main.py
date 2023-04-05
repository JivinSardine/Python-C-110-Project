import random

print("lets roll a dice")


a = True

while a == True:
    print("")
    number = random.randint(1,6)
    print("")

    if number == 1:
        print("-----")
        print("     ")
        print("  0  ")
        print("     ")
        print("-----")

    elif number == 2:
        print("-----")
        print("0    ")
        print("     ")
        print("    0")
        print("-----")

    elif number == 3:
        print("-----")
        print("0   0")
        print("     ")
        print("  0  ")
        print("-----")

    elif number == 4:
        print("-----")
        print("0   0")
        print("     ")
        print("0   0")
        print("-----")
    
    elif number == 5:
        print("-----")
        print("0   0")
        print("  0  ")
        print("0   0")
        print("-----")

    elif number == 6:
        print("-----")
        print("0   0")
        print(" 0 0 ")
        print("0   0")
        print("-----")

    b = input("press y to play again or e th exit: ")

    if b == "y":
        a = True
    
    elif b == "e":
        a = False
    
    else:
        print("please enter only y or e")
