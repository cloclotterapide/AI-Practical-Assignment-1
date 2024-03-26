import math
import numpy as np
#might have to add some imports here
#game logic functions

# 5 initial numbers
def generate_numbers():
    numbers = []
    while len(numbers) < 5:
        number = np.random.randint(20000, 30001)
        if number %12 == 0:
            numbers.append(number)
    return numbers

#to be written 
def HumanChoiceNumber():
    #would be the chosen number by the human using buttons on gui i suppose
    number = 0
    return number

#Initialisation of the game
def Initialisation():
    ComputerScore = 0
    HumanScore = 0
    Number = HumanChoiceNumber()
    return ComputerScore, HumanScore, Number
    
#Modifying the score depending of the player
def Scoring(CurrentPlayerScore,OpponentPlayerScore,Number):
    if (Number % 2 == 0):
        OpponentPlayerScore -= 1
    else:
        OpponentPlayerScore += 1
    return CurrentPlayerScore,OpponentPlayerScore

#True if the game is over, False if the game is not over
def EndGame(Number):
    return (Number <= 10)

#Print the winner 
def Winner(ComputerScore,HumanScore):
    if (ComputerScore > HumanScore):
        print("Computer wins")
    elif (ComputerScore < HumanScore):
        print("You win")
    else:
        print("It's a draw")
