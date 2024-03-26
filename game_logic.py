import tkinter as tk
import numpy as np

# Alpha-Beta Algorithm
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
    # If we want to update our GUI here to reflect the AI's move. 

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
