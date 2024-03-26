import math
import numpy as np

# 5 initial numbers
def generate_numbers():
    numbers = []
    while len(numbers) < 5:
        number = np.random.randint(20000, 30001)
        if number % 12 == 0:
            numbers.append(number)
    return numbers

#Initialisation of the game
def initialize():
    comp_score = 0
    human_score = 0

    # will continue

#to be written 
def chosen_num():
    number = 0
    return number
    
#Modifying the score depending on the player
def Scoring(CurrentPlayerScore,OpponentPlayerScore,Number):
    while Number > 10:
        if (Number % 2 == 0):
            OpponentPlayerScore -= 1
        else:
            CurrentPlayerScore += 1
        return CurrentPlayerScore, OpponentPlayerScore

#Print the winner 
def Winner(ComputerScore,HumanScore):
    if (ComputerScore > HumanScore):
        print("Computer wins")
    elif (ComputerScore < HumanScore):
        print("You win")
    else:
        print("It's a draw")
