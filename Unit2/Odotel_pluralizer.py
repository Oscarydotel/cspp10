
number = input("Enter a Number ")
noun = input("Enter a noun ")
if nu=="1":
 print(number +" "+ noun)
elif n[-2:]=="ay":
    print(number +" "+ noun + "s")
elif n[-2:]== "oy":
    print(number +" "+ noun + "s")
elif n[-2:]=="ey":
    print(number +" "+ noun + "s")
elif n[-2:]=="uy":
    print(number +" "+ noun + "s")
elif n[-2:]=="fe":
    print(number +" "+ noun[0:-2] +"ves")
elif n[-1:]=="y":
    print(number +" "+ noun[0:-1] + "ies")
elif n[-2:]=="sh":
    print(number +" "+ noun + "es")
elif n[-2:]== "us":
    print(number+" "+ noun[0:-2] + "i")
else: 
    print(number +" " + noun + "s")