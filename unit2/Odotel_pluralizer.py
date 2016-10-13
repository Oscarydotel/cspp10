nu= input("Enter a Number ")
n = input("Enter a noun ")
if n[-2:]=="fe":
    print(nu +" "+ n[0:-2]+"ves")
if n[-1]=="y":
    print(nu +" "+ n[0:-1]+ "ies")
if n[-2]=="sh":
    print(nu +" "+ n[0:-2]+ "es")
if n[-2]== "us":
    print(nu +" "+ n[0:-2]+ "i")
if n[-2]=="ay":
    print(nu +" "+ n+ "s")
if n[-2]== "oy":
    print(nu +" "+ n+ "s")
if n[-2]=="ey":
    print(nu +" "+ n+ "s")
if n[-2]=="uy":
    print(nu +" "+ n+ "s")
else: print(nu +" "+n + "s")