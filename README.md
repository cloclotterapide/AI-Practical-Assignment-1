# AI-Practical-Assignment-1

## Additional software requirements

At the beginning of the game, the game software randomly generates 5 numbers in the range of
20000 to 30000, but those that are initially divisible by 3, 2 and 4. The human-player chooses which
of the generated numbers he wants to start the game with.

## Game description

At the beginning of the game, the number chosen by the human-player is given. Both players have 0
points. Players take turns, dividing the current number by 2, 3 or 4 in each turn. It is possible to
divide a number only if the result is a whole number. If the division results in an even number, then
1 point is deducted from the opponent's points, if it is an odd number, then the player's own points
are increased by 1 point. The game ends when a number less than or equal to 10 has just been
acquired. If the players have the same number of points, then the result is a draw. Otherwise, the
player with more points wins

## Tasks 
*Subject to modification*

**Person 1: Front-end Development and Minimax Algorithm**
Front-end: Lead the design and implementation of the initial GUI layout using Tkinter, focusing on the main game window, menus, and game setup options.
Minimax: Develop the Minimax algorithm for the game, ensuring it integrates seamlessly with the game logic.

**Person 2: Game Logic and Alpha-Beta Algorithm**
Game Logic: Develop the core mechanics of the game, including the rules for scoring, turns, and game termination conditions.
Alpha-Beta: Implement the Alpha-Beta pruning algorithm, optimizing it for performance and ensuring it works well with the game logic.

**Person 3: GUI Enhancements and Minimax Testing**
GUI Enhancements: Work on advanced GUI features, such as animations, game state updates, and end-game screens.
Minimax Testing: Assist Person 1 in testing and refining the Minimax algorithm, including conducting experiments to evaluate performance.

**Person 4: Data Management and Alpha-Beta Testing**
Data Management: Implement the functionality for generating the initial game numbers and managing game state changes. This includes integrating NumPy for efficient data handling.
Alpha-Beta Testing: Work with Person 2 to test and refine the Alpha-Beta algorithm, conducting performance evaluations similar to those for Minimax.
