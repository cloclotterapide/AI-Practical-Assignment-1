import tkinter as tk
import random

# Global variables
comp_score = 0
human_score = 0
initial_number = 0
buttons = []

# Generate a list of five random numbers between 20000 and 30001 that are divisible by 2, 3, and 4
def generate_numbers():
    """
    Generate a list of 5 random numbers that are divisible by 2, 3, and 4.

    Returns:
        list: A list of 5 random numbers that are divisible by 2, 3, and 4.
    """
    numbers = []
    while len(numbers) < 5:
        number = random.randint(20000, 30000)
        if number % 12 == 0:  # divisible by 2, 3, and 4
            numbers.append(number)
    return numbers

# Print each number in the given list along with its index
def output_numbers(numbers):
    """
    Prints the generated numbers.

    Parameters:
    - numbers (list): A list of numbers to be printed.

    Returns:
    - None

    Example:
    output_numbers([1, 2, 3, 4, 5])
    Output:
    Generated numbers:
    1 - 1
    2 - 2
    3 - 3
    4 - 4
    5 - 5
    """
    print("Generated numbers:")
    for i, number in enumerate(numbers):
        print(f"{i+1} - {number}")

# Choose a number from the given list and return the selected number
def choose_Snumber(numbers):
    """
    Choose a starting number for the game.

    Parameters:
    - numbers (list): A list of numbers to choose from.

    Returns:
    - int: The chosen starting number.

    Example:
    choose_Snumber([1, 2, 3, 4, 5])
    Output:
    Generated numbers:
    1 - 1
    2 - 2
    3 - 3
    4 - 4
    5 - 5
    Choose the number to start this Game: 3
    3
    """
    output_numbers(numbers)
    while True:
        try:
            index = int(input("Choose the number to start this Game: "))
            if 1 <= index <= len(numbers):
                return numbers[index - 1]
            else:
                print("...Please choose a valid number from the list.")
        except ValueError:
            print("Please enter a valid number.")

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


# Function to start the game based on the user's selection
def handle_click(number):
    """
    Handle the click event on a button.

    This function is called when a button is clicked. It takes the clicked number as an argument and updates the global variable 'initial_number' with the clicked number. It then destroys all the buttons and calls the 'start_game_loop' function with the updated 'initial_number' as the argument.

    Parameters:
    - number (int): The number clicked on the button.

    Returns:
    None
    """
    global initial_number
    initial_number = number
    for button in buttons:
        button.destroy()
    start_game_loop(initial_number)

#Main game loop function
def start_game_loop(start_number):
    """
    Starts the game loop for the number game.

    Parameters:
    - start_number (int): The starting number for the game.

    Returns:
    - None

    The function allows the user to play against the computer in a number game. 
    The user can choose between two algorithms, 'minimax' and 'alpha-beta', to play against. 
    The game loop continues until the current number becomes less than or equal to 10. 
    In each iteration of the loop, the user and the computer take turns dividing the current number by 2, 3, or 4. 
    The user's score and the computer's score are updated based on the division. 
    At the end of the game, the function determines the winner based on the scores and prints the final scores.

    Note: The function assumes that the global variables 'comp_score' and 'human_score' are defined and accessible.
    """
    global comp_score, human_score
    current_number = start_number
    is_human_turn = True

    # User chooses algorithm
    algorithm_choice = input("Choose which algorithm to play against ('minimax' or 'alpha-beta'): ").strip().lower()
    while algorithm_choice not in ["minimax", "alpha-beta"]:
        print("Invalid choice. Please type 'minimax' or 'alpha-beta'.")
        algorithm_choice = input("Choose which algorithm to play against ('minimax' or 'alpha-beta'): ").strip().lower()

    while current_number > 10:
        if is_human_turn:
            # Actual human turn
            print(f"Current number: {current_number}. Your turn to play.")
            factor = int(input("Choose to divide by 2, 3, or 4: "))
            while factor not in [2, 3, 4] or current_number % factor != 0:
                print("Invalid move. You must choose 2, 3, or 4 and the current number must be divisible by your choice.")
                factor = int(input("Choose to divide by 2, 3, or 4: "))
            
            current_number //= factor
            if current_number % 2 == 0:
                comp_score -= 1
            else:
                human_score += 1
        else:
            # AI turn
            best_score = float('-inf')
            best_move = None
            for factor in [2, 3, 4]:
                if current_number % factor == 0:
                    new_number = current_number // factor
                    if algorithm_choice == "minimax":
                        score = minimax(new_number, False, comp_score, human_score)
                    else:  # alpha-beta
                        score = alpha_beta(new_number, 10, float('-inf'), float('inf'), False, comp_score, human_score)
                    
                    if score > best_score:
                        best_score = score
                        best_move = factor
            
            print(f"AI chooses to divide by {best_move}")
            current_number //= best_move
            if current_number % 2 == 0:
                human_score -= 1
            else:
                comp_score += 1

        is_human_turn = not is_human_turn
        print(f"Current number: {current_number}, Human score: {human_score}, Computer score: {comp_score}")

    # Determine the winner
    if comp_score == human_score:
        print("It's a draw!")
    elif comp_score > human_score:
        print("Computer wins!")
    else:
        print("Human wins!")
    print(f"Final scores - Human: {human_score}, Computer: {comp_score}")



# Initialize the game
def initialize():
    """
    Initialize the number game.

    Returns:
        None
    """
    global buttons
    numbers = generate_numbers()

    root = tk.Tk()
    root.title("Number Game")

    for i, num in enumerate(numbers):
        button = tk.Button(root, text=num, command=lambda num=num: handle_click(num))
        button.pack()
        buttons.append(button)

    root.mainloop()

# Entry point of the application
if __name__ == "__main__":
    initialize()
