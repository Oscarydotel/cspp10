import random
player = str(input("Hello, stranger what is your name?"))
cc = random.randint(1,3)
print("\nAhh nice to meet you {} on this fine day!".format(player))
if cc == 1:
    print("Where are you from {}?".format(player))
    where = str(input("I am from "))
    print("Ohh how interesting, I dont think I've ever been there.")
    print("I'm the village not so far from here called wethrer.")