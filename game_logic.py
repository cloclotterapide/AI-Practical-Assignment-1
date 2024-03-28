import tkinter as tk
import numpy as np

# minimax algorithm
import random

#it generates a list of five random numbers between 20000 and 30000 that are divisible by 2, 3, and 4.
def generation_numbers():
    numlist=[]
    while len(numlist)<5:
        number=random.randint(20000, 30000)
        if number not in numlist and number % 2 == 0 and number % 3== 0 and number % 4 ==0:
            numlist.append(number) # Add the number to numlist if it meets the conditions
    return numlist

# function prints each number in the given list along with its index
def output_numbers(numlist):
    print("Generated numbers:")
    for i, number in enumerate(numlist):
        print(f"{i+1} - {number}") # and then print each number along with its index (starting from 1 for readability)

# function to choose a number from the given list and returns the selected number
def choose_Snumber(numbers):
    output_numbers(numbers)
    while True:
        try:
            index = int(input("Choose the number to start this Game : "))
            if 1 <= index <= len(numbers):  #check if the input is in valid range
                return numbers[index - 1]
            else:
                print("...Please choose a valid number from the list.")
        except ValueError:
            print("Please enter a valid number.")


'''

Your code (modify what you want)


def game():


example : 
if player1_points == player2_points:
    print("Draw Match !")
elif player1_points > player2_points:
    print("Player 1 Win !")
else:
    print("Player 2 Win !")

    

if __name__ == "__main__":
    numbers =generation_numbers()
    starting_number= choose_Snumber(generation_numbers)
    # game(starting_number)


'''



generation_numbers = generation_numbers() #list
output_numbers(generation_numbers) # generated numbers along with their indices

start_number = choose_Snumber(generation_numbers) #user choose a number from the generated list
print("Starting number chosen by the first person is :", start_number) #print the number chosen






# alpha-beta algorithm
def alpha_beta(number, depth, alpha, beta, is_maximizing_player, comp_score, human_score):
    if number <= 10:
        return comp_score - human_score

    if is_maximizing_player:
        max_eval = float('-inf')
        for factor in [2, 3, 4]:
            if number % factor == 0:
                next_number = number // factor
                if next_number % 2 == 0:
                    score_change = -1
                else:
                    score_change = 1
                eval = alpha_beta(next_number, depth - 1, alpha, beta, False, comp_score + score_change, human_score)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for factor in [2, 3, 4]:
            if number % factor == 0:
                next_number = number // factor
                if next_number % 2 == 0:
                    score_change = 1
                else:
                    score_change = -1
                eval = alpha_beta(next_number, depth - 1, alpha, beta, True, comp_score, human_score + score_change)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if alpha >= beta:
                    break
        return min_eval


def handle_click(number):
    global initial_number, comp_score, human_score
    initial_number = number
    for button in buttons:
        button.destroy()
    
    # Comp makes move based on the selected number
    depth = 10  # We can regulate the depth based on our needs !!!!!!
    ai_score = alpha_beta(initial_number, depth, float('-inf'), float('inf'), True, comp_score, human_score)
    print(f"AI Score Evaluation: {ai_score}")
    

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
    global comp_score, human_score, buttons, root
    comp_score = 0
    human_score = 0
    numbers = generate_numbers()
    
    #will continue
    root = tk.Tk()
    root.title("Number Game")
    
    buttons = []
    for i, num in enumerate(numbers):
        button = tk.Button(root, text=num, command=lambda num=num: handle_click(num))
        button.pack()
        buttons.append(button)
    
    root.mainloop()
    
    return comp_score, human_score, initial_number

if __name__ == "__main__":
    comp_score, human_score, initial_number = initialize()
    print("Initial number chosen:", initial_number)
