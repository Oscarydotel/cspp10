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
    Print("Dice Uno {} and Dice Dos {} \n".format(dice_uno,dice_dos))
    Print("total is {}".format(dice_add))
    return dice_add
    
def PHASE_UNO(player_Dinero):
     player_cash = player_Dinero
     Dinero_amount = int(input("Enter amount of bet!\n Bet can not be negative \n (2)Must not be more of what you bet \n(3)Must only be whole numbers "))
     if Dinero_amount > player_cash or Dinero_amount <= 0:
         Dinero_amount = int(("You betted wrong"))
     return Dinero_amount
     
def PHASE_DOS(dice_uno,dice_add,dice_add):
     print("Your Roll are:\nDice Uno {} !\nDice Dos {}!\nTotal is {} !" .format(dice_uno,dice_dos,dice_add))
    

DICEroll()
PHASE_DOS()