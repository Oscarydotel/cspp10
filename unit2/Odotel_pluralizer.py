nu= input("Enter a Number ")
n = input("Enter a noun ")
if nu=="1":
 print(nu+" "+ n)
elif n[-2:]=="ay":
    print(nu +" "+ n+ "s")
elif n[-2:]== "oy":
    print(nu +" "+ n+ "s")
elif n[-2:]=="ey":
    print(nu +" "+ n+ "s")
elif n[-2:]=="uy":
    print(nu +" "+ n+ "s")
elif n[-2:]=="fe":
    print(nu +" "+ n[0:-2]+"ves")
elif n[-1:]=="y":
    print(nu +" "+ n[0:-1]+ "ies")
elif n[-2:]=="sh":
    print(nu +" "+ n+ "es")
elif n[-2:]== "us":
    print(nu +" "+ n[0:-2]+ "i")
else: 
    print(nu +" "+n + "s")