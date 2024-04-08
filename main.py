from tkinter import *
import random,time

#Game window parameters
root = Tk()
root.title("AI-ASSIGNEMENT GAME")
root.geometry('500x500')
root.configure(bg='lightblue')
root.tk.call('tk', 'scaling', 3.0)

currentnumber_label = Label(root, text="Current Number: ")
currentnumber_label.pack()
Turn_Count_label = Label(root, text="Turn Count: ",font=6)
Turn_Count_label.pack()

# Global variables to track data
minimax_nodes_visited = 0
alpha_beta_nodes_visited = 0
execution_times = []  # This will store execution times for both algorithms
victories = {'human': 0, 'computer': 0}  # To track victories

def generate_numbers():
    """
    Generate a list of 5 random numbers that are divisible by 2, 3, and 4 
    """
    numbers = []
    while len(numbers) < 5:
        number = random.randint(20000, 30000)
        if number % 12 == 0 and (number not in numbers):  # divisible by 2, 3, and 4
            numbers.append(number)
    return numbers

# Minimax algorithm
def minimax(number, is_maximizing_player, comp_score, human_score):
    """
    Calculate the minimax score for a given number in the number game.

    Parameters:
    - number (int): The current number in the game.
    - is_maximizing_player (bool): True if it's the maximizing player's turn, False otherwise.
    - comp_score (int): The current score of the computer player.
    - human_score (int): The current score of the human player.

    Returns:
    - int: The minimax score for the given number.

    Note: This implementation assumes that the number is always divisible by at least one of the factors [2, 3, 4].
    """
    global minimax_nodes_visited
    minimax_nodes_visited += 1
    
    if number <= 10:
        return comp_score - human_score

    if is_maximizing_player:
        max_eval = float('-inf')
        for factor in [2, 3, 4]:
            if number % factor == 0:
                next_number = number // factor
                score_change = 1 if next_number % 2 != 0 else -1
                eval = minimax(next_number, False, comp_score + score_change, human_score)
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for factor in [2, 3, 4]:
            if number % factor == 0:
                next_number = number // factor
                score_change = -1 if next_number % 2 != 0 else 1
                eval = minimax(next_number, True, comp_score, human_score + score_change)
                min_eval = min(min_eval, eval)
        return min_eval

# Alpha-beta algorithm
def alpha_beta(number, depth, alpha, beta, is_maximizing_player, comp_score, human_score):
    """
    Calculate the alpha-beta pruning algorithm for the number game.

    Parameters:
    - number (int): The current number in the game.
    - depth (int): The depth of the search tree.
    - alpha (float): The alpha value for alpha-beta pruning.
    - beta (float): The beta value for alpha-beta pruning.
    - is_maximizing_player (bool): True if it's the maximizing player's turn, False otherwise.
    - comp_score (int): The current score of the computer player.
    - human_score (int): The current score of the human player.

    Returns:
    - int: The evaluation score for the current state of the game.

    Note: The function assumes that the current number is greater than 10, as the game loop in the main code terminates when the current number becomes less than or equal to 10.
    """
    global alpha_beta_nodes_visited
    alpha_beta_nodes_visited += 1
    
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

#Only select the possible divisors of the current number
def Verified_Numbers(number):
    '''
    Take the current number as input and return the list of divisors of the number
    '''
    verified_numbers = []
    for factor in [2, 3, 4]:
        if number % factor == 0:
            verified_numbers.append(factor)
    return verified_numbers

#Main game loop function
def get_factor(Game_Parameters,factor_var):
    # Game_Parameters = (comp_score,human_score,Turn_Count,Number)
    Game_Parameters = list(Game_Parameters)

    comp_score = Game_Parameters[0]
    human_score = Game_Parameters[1]
    Turn_Count = Game_Parameters[2]
    current_number = Game_Parameters[3]
    
    Turn_Count += 1
    Turn_Count_label.config(text=f"Turn: {Turn_Count}")
    
    human_score,comp_score = Score_Modification(current_number,human_score,comp_score)
    
    factor = factor_var.get()
    current_number = Game_Parameters[3] // factor
    currentnumber_label.config(text=f"Current Number: {current_number}")
    
    Game_Parameters[0:4] = [comp_score, human_score, Turn_Count, current_number]
    Game_Parameters = tuple(Game_Parameters)

    if is_finished(current_number):
        end_game(Game_Parameters)
    else:
        AI_turn(Game_Parameters)
        
def Score_Modification(current_number,player_score,other_player_score):
    if current_number % 2 == 0:
        player_score -= 1
    else:
        other_player_score += 1
    return player_score,other_player_score
    
def human_turn(Game_Parameters):
    print(Game_Parameters)
    #print(current_number)
    current_number = Game_Parameters[3]
    L = Verified_Numbers(current_number)
    
    if no_more_moves(L):
        end_game(Game_Parameters)
    else:   
        factor_var = IntVar()
        if 2 in L:
            radio_button2 = Radiobutton(root, text="2", variable=factor_var, value=2, font=6)
            radio_button2.pack()
        if 3 in L:
            radio_button3 = Radiobutton(root, text="3", variable=factor_var, value=3, font=6)
            radio_button3.pack()
        if 4 in L:
            radio_button4 = Radiobutton(root, text="4", variable=factor_var, value=4, font=6)
            radio_button4.pack()
        def lambda_handler():
            get_factor(Game_Parameters,factor_var)
            clear_button.pack_forget()
            if 2 in L:
                radio_button2.pack_forget()
            if 3 in L:
                radio_button3.pack_forget()
            if 4 in L:
                radio_button4.pack_forget()
            
        clear_button = Button(root, text="OK", command=lambda_handler , font=6)
        clear_button.pack()
    
    
def AI_turn(Game_Parameters):
    '''
    Take the game parameters as input and make the AI move
    Game_Parameters = (comp_score,human_score,Turn_Count,Number,Algorithm_Choice)
    '''
    global execution_times, minimax_nodes_visited, alpha_beta_nodes_visited
    
    # Resetting node counters before the move
    minimax_nodes_visited = 0
    alpha_beta_nodes_visited = 0
    start_time = time.time()
    
    print(Game_Parameters)
    comp_score = Game_Parameters[0]
    human_score = Game_Parameters[1]
    Turn_Count = Game_Parameters[2]
    current_number = Game_Parameters[3]
    Algorithm_choice = Game_Parameters[4]
    print(Game_Parameters)
    Turn_Count += 1
    Turn_Count_label.config(text=f"Turn: {Turn_Count}")
    
    ai_move_label = Label(root, text="AI Move: ",font=6)
    ai_move_label.pack(side=TOP,anchor=CENTER)
  
    L = Verified_Numbers(current_number)
    if no_more_moves(L):
        end_game(Game_Parameters)
    else:  
        best_score = float('-inf')
        best_move = L[0]
        for div in L:
            if current_number % div == 0:
                new_number = current_number // div
                if Algorithm_choice == 0: #minimax
                    score = minimax(new_number, False, comp_score, human_score)
                else:  # alpha-beta
                    score = alpha_beta(new_number, 10, float('-inf'), float('inf'), False, comp_score, human_score)
                                
                if score > best_score:
                    best_score = score
                    best_move = div
         
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)  # Log execution time
               
        current_number = current_number // best_move
        #print(f"AI chooses to divide by {best_move}")
        
        comp_score,human_score = Score_Modification(current_number,comp_score,human_score)
        
        ai_move_label.config(text=f"AI Move: Divide by {best_move}")
        ai_move_label.pack(side=TOP,anchor=CENTER)
        currentnumber_label.config(text=f"Current Number: {current_number}")
        
        Game_Parameters = (comp_score,human_score,Turn_Count,current_number,Algorithm_choice)
        
        if is_finished(current_number):
            end_game(Game_Parameters)
        else:
            human_turn(Game_Parameters)
 

               
def is_finished(number):
    return number <= 10

def no_more_moves(L):
    return len(L) == 0

# Determine the winner
def end_game(Game_Parameters):
    global victories, execution_times, minimax_nodes_visited, alpha_beta_nodes_visited

    comp_score, human_score = Game_Parameters[0:2]
    # Increment victory counters based on game outcome
    if comp_score > human_score:
        victories['computer'] += 1
    elif human_score > comp_score:
        victories['human'] += 1
        
    end_label = Label(root, text=f"Computer: {comp_score}, Human: {human_score}", font=6)
    end_label.pack()
    if comp_score == human_score:
        end_label.config(text="It's a tie: " + end_label.cget("text"))
    elif comp_score > human_score:
        end_label.config(text="Computer won: " + end_label.cget("text")) 
    else:
        end_label.config(text="Human won: "+ end_label.cget("text"))
        
    # Log the data
    print(f"Game Over. Computer: {comp_score}, Human: {human_score}")
    print(f"Minimax nodes visited: {minimax_nodes_visited}, Alpha-Beta nodes visited: {alpha_beta_nodes_visited}")
    print(f"Average move execution time: {sum(execution_times) / len(execution_times) if execution_times else 0} seconds")
    print(f"Computer victories: {victories['computer']}, Human victories: {victories['human']}")

    # Reset execution_times for the next game
    execution_times = []

# Function to start the game based on the user's selection  
def initialize_algo():
    
    comp_score = 0
    human_score = 0
    Turn_Count = 0
    Number = 0
    Algorithm_choice = -1
    
    Game_Parameters = [comp_score,human_score,Turn_Count,Number,Algorithm_choice]
    
    Algo_var = IntVar()
    Info_label = Label(root, text="Select an algorithm :", font=6)
    Info_label.pack(side=TOP,anchor=W)
    radio_button_MinMax = Radiobutton(root, text="minmax", variable=Algo_var, value=0, font=6)
    radio_button_AlphaBeta= Radiobutton(root, text="AlphaBeta", variable=Algo_var, value=1, font=6)
    radio_button_MinMax.pack(side=TOP,anchor=W)
    radio_button_AlphaBeta.pack(side=TOP,anchor=W)

    def lambda_handler_algo():
        Algorithm_choice = Algo_var.get()
        radio_button_MinMax.destroy()
        radio_button_AlphaBeta.destroy()
        clear_button.destroy()
        Info_label.pack_forget()
        Game_Parameters[4] = Algorithm_choice
        initialize_number(Game_Parameters)
        
    clear_button = Button(root, text="OK", command=lambda_handler_algo, font=6)
    clear_button.pack(side=TOP,anchor=W)
    
      
def initialize_number(Game_Parameters):
    numbers = generate_numbers()
    num_var=IntVar()
    radio_buttons = []
    Info_label = Label(root, text="Select a starting number :", font=6)
    Info_label.pack(side=TOP,anchor=W)
    for number in numbers:
        radio_button = Radiobutton(root, text=str(number), variable=num_var, value=number, font=6,pady=5,padx=5)
        radio_button.pack(side=TOP, anchor=W)
        radio_buttons.append(radio_button)
    
    def lambda_handler_init():
        clear_button.destroy()
        num = num_var.get()
        Game_Parameters[3] = num
        Starting_player(Game_Parameters)
        currentnumber_label.config(text=f"Current Number: {num}")
        clear_button.destroy()
        for radio_button in radio_buttons:
            radio_button.pack_forget()
        Info_label.pack_forget()
        
    clear_button = Button(root, text="OK", command=lambda_handler_init, font=6)
    clear_button.pack(side=TOP,anchor=W)
    
def Starting_player(Game_Parameters):
    start_var=IntVar()
    Info_label = Label(root, text="Who will start the game?", font=6)
    Info_label.pack(side=TOP,anchor=W)
    radio_button_human = Radiobutton(root, text="Human", variable=start_var, value=0, font=6)
    radio_button_comp = Radiobutton(root, text="Computer", variable=start_var, value=1, font=6)
    radio_button_human.pack(side=TOP,anchor=W)
    radio_button_comp.pack(side=TOP,anchor=W)
    
    def lambda_handler_start():
        clear_button.destroy()
        start = start_var.get()
        Info_label.pack_forget()
        if start == 0:
            human_turn(Game_Parameters)
        else:
            AI_turn(Game_Parameters)
        radio_button_human.pack_forget()
        radio_button_comp.pack_forget()
        
    clear_button = Button(root, text="OK", command=lambda_handler_start, font=6)
    clear_button.pack(side=TOP,anchor=W)
    #print(Game_Parameters)
    
def Restart_Handler():
    for widget in root.winfo_children():
        if widget != Restart_button and widget != currentnumber_label and widget != Turn_Count_label:
            widget.forget()
    Turn_Count_label.config(text= "Turn : 0")
    currentnumber_label.config(text="Current Number: ")
    initialize_algo()
  
Restart_button = Button(root, text="Restart", command=Restart_Handler, font=6)
Restart_button.pack(side=BOTTOM,anchor=CENTER)

# Entry point of the application
if __name__ == "__main__":
    initialize_algo()

root.mainloop()
