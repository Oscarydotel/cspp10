e = input("Enter a equation")
n1 = float(e[0])
o = (e[1])
n2 = float(e[2])

if o == "*":
    print("The Result " + str(n1*n2))
    
if o == "/":
    print("The Result "+ str(n1/n2))

if o == "+":
    print("The Result "+ str(n1+n2))

if o == "-":
    print("The Result "+ str(n1-n2))

if o == "%":
    print("The Result "+ str(n1%n2))