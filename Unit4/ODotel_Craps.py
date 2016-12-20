import random

#Function name: Player_Dinero
#purpose:this acts like a score board because the amount of money dettermines if the player can lose.. this keeps track of the money that is being used as a bet
#argument:none
#returns dinero
def Player_Dinero():
    player_Dinero = 100
    return player_Dinero
    
def DICEroll():
    dice_uno = random.randint(1,6)
    dice_dos = random.randint(1,6)
    dice_add = dice_uno + dice_dos
    print("Your Roll are:\nDice Uno {}!\nDice Dos {}!\nTotal is {}!" .format(dice_uno,dice_dos,dice_add))
    return dice_add
    
def PHASE_UNO():
     player_cash = Player_Dinero()
     Dinero_amount = int(input("Enter amount of bet!\n--RULES FOR A CORRECT BET--\n(1)Bet can not be negative \n(2)Must not be more of what you have \n(3)Must only be whole numbers\n(4)Must obviously ONLY NUMBERS\n\n\nENTER BET HERE:"))
     if Dinero_amount > player_cash or Dinero_amount <= 0:
         print("You bet a wrong number!\nTry again!")
         Dinero_amount = int(input("Enter a correct amount of money for a bet\nPlease READ what is allowed for a CORRECT BET ABOVE!!!\nPlease try again: "))
     return Dinero_amount
 
def PHASE_DOS():
     dice_add = DICEroll()
     if dice_add == 2:
        print("You lost")
     elif dice_add == 3 :
        print("You lost")
     elif dice_add == 12 :
        print("You lost")
     elif dice_add == 7 :
        print("You Won")
     elif dice_add == 11 :
        print("You Won")
     else:
        return dice_add
def PHASE_TRES():
     point_num = PHASE_DOS()
     dice_uno_Ph3 = random.randint(1,6)
     dice_dos_Ph3 = random.randint(1,6)
     dice_add_Ph3 = dice_uno_Ph3 + dice_dos_Ph3
     if point_num == 4 or point_num == 5 or point_num == 6 or point_num == 8 or point_num == 9 or point_num or 10:
         while dice_add_Ph3 != 7 or dice_add_Ph3 != point_num:
             dice_uno_Ph3 = random.randint(1,6)
             dice_dos_Ph3 = random.randint(1,6)
             dice_add_Ph3 = dice_uno_Ph3 + dice_dos_Ph3
         if dice_add_Ph3 == 7:
            print("Lost")
         elif dice_add_Ph3 == point_num:
            print("Won")

def game():
    print("Casino Royale")
    player_cash = Player_Dinero()
    
    while player_cash > 0:
        PHASE_UNO()
        DICEroll()
        PHASE_DOS()
        PHASE_TRES()
       
game()