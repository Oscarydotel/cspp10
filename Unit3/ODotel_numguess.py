import random

PcNum =  random.randint(1,101)
UserNum = int(input("Enter a Random Number:"))

while UserNum != PcNum:
    print("You Are " + str( PcNum - UserNum ) + " Away")
    UserNum = int(input("Enter a Number:"))
    
print("You got the Number Correct XD!!!!")