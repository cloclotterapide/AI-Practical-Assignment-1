import tkinter as tk
import numpy as np

def handle_click(number):
    global initial_number
    initial_number = number
    for button in buttons:
        button.destroy()
    
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
    numbers = generate_numbers()

    #will continue
    global root
    root = tk.Tk()
    root.title("Number Game")
    
    global buttons
    buttons = []
    for i, num in enumerate(numbers):
        button = tk.Button(root, text = num, command = lambda num = num: handle_click(num))
        button.pack()
        buttons.append(button)
    
    root.mainloop()
    
    return comp_score, human_score, initial_number

comp_score, human_score, initial_number = initialize()
print("Initial number chosen:", initial_number)
