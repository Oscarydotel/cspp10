#Scramble Program
#first step. Have user input a sentenses inot variable called WORD
# Split each and every word in WORD
#Then put them into a list
#seperate each word into a list
# number_list.append(user_input)
import random

word = str(input("Enter A word "))
words = str(input("Enter a WORDS"))
slic = words.split(" ")
print(slic)
print(word)
def scramble_word(word):
    x1 = word[0]
    x2 = word[-1]
    inside = word[1:-1]
    lst = list(inside)
    random.shuffle(lst)
    lst.append(x2)
    lst.insert(0,x1)
    word = "".join(lst)
    print(word)
    
    
    
    
scramble_word(word)
