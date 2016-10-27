Nm = input("NUMBER: ")
for n in range(1,Nm+1):
    if n%5==0 and n%3==0:
        print("FuzzBuzz")
    elif n%3==0:
        print("Fuzz")
    elif n%5==0:
        print("Buzz")
    else:
        print(n)
    