import random

c1 = input("Whats your name ? ")
print("Hello! "+ c1 + " it's nice to meet you" )
Num_Question = 1
#I'm thinking about the computer having random questions being brought up to the player to answer.First think about series of Questions to ask and assighn them as questions
question = random.randint(1,2)
while question != 0 and Num_Question < 3:
    question = random.randint(1,2)
    Num_Question = Num_Question + 1 
    if question == 1:
        print("How are you " + c1 + input("?"))
    elif question == 2:
        print("Where are you from " + c1 + input("?"))
        

