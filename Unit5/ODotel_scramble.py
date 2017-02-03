#Scramble Program
#first step. Have user input a sentenses inot variable called WORD
# Split each and every word in WORD
#Then put them into a list
#seperate each word into a list
# 
import random

def scramble_word():
    WORD = str(input("Enter a Sent: "))
    a = WORD.split(" ")
    print(a)
scramble_word()
