import random
 
# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():
    diceroll1 = random.randint(1,6)
    diceroll2 = random.randint(1,6)
    dices = diceroll1 + diceroll2
    return dices
    # generate a random number from 1 to 6
   
    # generate another random number from 1 to 6
   
    # get the sum of the two rolls
   
    # print the sum
   
    # return the sum
 
# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet(bank):
    bank = 100
    bet = int(input("What is the amount you want to bet?\n"))
    while bet < bank:
        bet = int(input("The amount you betted isn't an appropriate\nCan you please re-do you're bet again\n:"))
    return bet
    # ask the player how much they want to bet
   
    # if player's bet is more than they have
    #   available in bank, then get new bet
   
    # if player's bet is valid, then return
    #   the bet
 
# function that finds the range given a dice roll
# name: get_range
# arguments: sum of dice
# returns: the range:
#           "over7" if over 7
#           "under7" if under 7
#           "equal7" if equal to 7
def get_range(dice_sum):
    dice_sum = roll2dice()
    if dice_sum > 7 :
        dice_sum = "Greater than 7!"
    elif dice_sum < 7 :
        dice_sum = "Under than 7"
    else:
        dice_sum = "Is 7!!!\n"
    return dice_sum
    # if the sum is over 7, return "over7"
   
    # if the sum is under 7, return "under7"
   
    # if the sum is 7, return "equal7"
 
# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over7", "under7", or "equal7"
def choose_range():
    p1_move = input("Choose either Greater than 7|Under than 7|Is 7!!!\n ")
    return p1_move
    # present user with choices "over7", "under7",
    #   or "equal7"
   
    # return their choice
 
# function for the main game