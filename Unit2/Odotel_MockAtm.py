cash = 10000
Enter = input("Bank Account Balance: " + str(cash) + " \n<>Press 1, To WithDraw \n<>Press 2, Deposit \n<>Press 3, Exit\n---Press 3 To Exit Machine--- \n Enter Number: ")

while Enter != "3":
    if Enter == "1":
        cash = cash - int(input("Number"))
        print(str(cash) + " Is your account Balance")
    elif Enter == "2":
        cash = int(input("Amount: ")) + cash
        print("Balance: " + cash)
    elif Enter == "3":
        break
        
print('Bye, Bye!!! Have a Good Day!!')
    