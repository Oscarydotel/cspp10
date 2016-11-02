import random

PcNum =  random.randint(1,100)
UserNum = int(input("Enter a Random Number: "))
NumCount = 1

while UserNum != PcNum:
    NumCount = NumCount + 1
    if UserNum > PcNum:
        print("You're too high")
        UserNum = int(input("Enter a Number: "))
    elif UserNum < PcNum:
        print("You're too low")
        UserNum = int(input("Enter a Number: "))
    
print("You got the Number " +"\n You tried to guess the number " + str(NumCount) + " times")
