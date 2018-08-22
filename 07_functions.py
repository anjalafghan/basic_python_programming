def isOddOrEven(myNumber):
    if myNumber % 2 == 0:
        print("Your number is Even")
    else:
        print("Your number is Odd")

isOddOrEven(2)


#Return Value

def returnOddEven(myNumber):
    if myNumber % 2 == 0:
        return True
    else:
        return False

returnValue = returnOddEven(2)
print(returnValue)