equation = input("Enter a equation")
n1 = float(equation[0])
operation = (equation[1])
n2 = float(equation[2])

if operation == "*":
    print("The Result " + str(n1*n2))
    
if operation == "/":
    print("The Result "+ str(n1/n2))

if operation == "+":
    print("The Result "+ str(n1+n2))

if operation == "-":
    print("The Result "+ str(n1-n2))

if operation == "%":
    print("The Result "+ str(n1%n2))