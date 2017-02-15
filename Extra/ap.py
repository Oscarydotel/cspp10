import random
npc = random.randint(1,3)
if npc == 1:
    npc = "Charles Xavieer"
elif npc == 2:
    npc = "Peter the Beater"
elif npc == 3:
    npc = "Village Idiot"
def scramble_word(npc):
    x1 = npc[0]
    x2 = npc[-1]
    inside = npc[1:-1]
    lst = list(inside)
    random.shuffle(lst)
    lst.append(x2)
    lst.insert(0,x1)
    npc = "".join(lst)
    return npc
    
npc = scramble_word(npc) 

player = str(input("Hello stranger, my name is {}.\nWhat is your name? :".format(npc)))
cc = random.randint(1,3)
print("\nAhh nice to meet you {} on this fine day!".format(player))
if cc == 1:
    print("Where are you from {}?".format(player))
    where = str(input("I am from "))
    print("Ohh {} how interesting, I dont think I've ever been there. -{}".format(where,npc))
    print("I'm the town not so far from here called wethrer.")
elif cc == 2:
    print("What made you want to come out here so far out the city? -{}".format(npc))