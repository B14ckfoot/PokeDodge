def countdown(intCounter):
    print(intCounter)
    if intCounter > 0:
        countdown(intCounter-1)

def countEasy(intCounter):
    for intX in range(intCounter,-1, -1):
        print(intX)


intStartCount = int(input("What number should I count down from? "))

countdown(intStartCount)

print("\n"*5)

countEasy(intStartCount)