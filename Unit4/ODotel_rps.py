import random

#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    #code here
    p1_move = input("Choose either r|p|s: ")
    return p1_move

#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move():
    #code here
    com_move = random.randint(1,3)
    if com_move == 1:
        return "r"
    elif com_move == 2:
        return "s"
    else:
        return "p"

#function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    #code here
    rounds_amount = int(input("How Much Rounds you want? From 1 to 9 rounds "))
    while rounds_amount <= 9:
        return rounds_amount
#function name: get_round_winner
#   arguments: player move, computer move
#   purpose: based on the player and computer's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player" if player won
#               "comp" if computer won
#               "tie" if it's a tie
def get_round_winner(p1_move, com_move):
    #code here
    if p1_move == "r" and com_move == "r":
        return("Tie")
    elif p1_move == "r" and com_move == "s":
        return("Player Won!")
    elif p1_move == "r" and com_move == "p":
        return("Computer Won!")
    elif p1_move == "s" and com_move == "s":
        return("Tie!")
    elif p1_move == "s" and com_move == "r":
        return("Computer Won!") 
    elif p1_move == "s" and com_move == "p":
        return("Player Won!")
    elif p1_move == "p" and com_move == "p":
        return("Tie!")
    elif p1_move == "p" and com_move == "s":
        return("Computer Won!")
    elif p1_move == "p" and com_move == "r":
        return("Player Won!")
        
#functionname: get_full_move
#   arguments: a single letter move 'r','p', or 's'
#   purpose: returns the "full" word of a given move
#   returns: returns a string based on the following:
#               "Rock" if given "r"
#               "Paper" if given "p"
#               "Scissors" if given "s"
def get_full_move(shortmove):
    #code here
    if shortmove == "r":
        print("Player Picked Rock!")
    elif shortmove == "s":
        print("Player Picked Scissors!")
    elif shortmove == "p":
        print("Player Picked Paper!")
        
#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score(pscore, cscore, ties):
    print ("PLayer 1 has {} points \nComputer has {} points \nYou both tied {} times".format(pscore, cscore, ties))

#function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
#   returns: none
def rps():
    score_player1 = 0
    score_comp = 0
    tie = 0
    rounds = get_rounds()
    for d in range(rounds):
        p1_move = get_p1_move()
        com_move = get_comp_move()
        winner = get_round_winner(p1_move,com_move)
        print(winner)
    
    

#function name: tests
#   arguments: none
#   purpose: a place for you to write your tests.  replace 'rps' below
#               with 'tests' to run this function instead of the game loop
#   returns: none

    #code here

rps()