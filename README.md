# AI-Practical-Assignment-1

## Additional software requirements

At the beginning of the game, the game software randomly generates 5 numbers in the range of
20000 to 30000, but those that are initially divisible by 3, 2 and 4. The human-player chooses which
of the generated numbers he wants to start the game with.

### Game description

At the beginning of the game, the number chosen by the human-player is given. Both players have 0
points. Players take turns, dividing the current number by 2, 3 or 4 in each turn. It is possible to
divide a number only if the result is a whole number. If the division results in an even number, then
1 point is deducted from the opponent's points, if it is an odd number, then the player's own points
are increased by 1 point. The game ends when a number less than or equal to 10 has just been
acquired. If the players have the same number of points, then the result is a draw. Otherwise, the
player with more points wins

## Tasks 
*Subject to modification*

Person 1: GUI Design and User Experience
Responsibilities:
Lead the design and implementation of the GUI in gui.py, focusing on the overall user experience, including the main menu, game setup options, and in-game interfaces.
Ensure the GUI is intuitive and responsive, with clear feedback for player actions.

Person 2: Game Logic and State Management
Responsibilities:
Develop the core game mechanics in game_logic.py, including turn management, scoring rules, and game termination conditions.
Manage the game state, ensuring accurate tracking of the current number, player scores, and turn sequence.

Person 3: Minimax Algorithm Development
Responsibilities:
Implement and optimize the Minimax algorithm in minimax.py, ensuring its integration with the game logic for AI decision-making.
Work with Persons 4 and 5 on integrating AI algorithms with the game and conducting performance analysis.

Person 4: Alpha-Beta Algorithm Development
Responsibilities:
Develop the Alpha-Beta pruning algorithm in alpha_beta.py, focusing on efficiency and integration with the game's decision-making processes.
Collaborate with Persons 3 and 5 to refine AI strategies and evaluate algorithm performance.

Person 5: Data Management and AI Integration
Responsibilities:
Oversee data management, including the generation of initial game numbers and the use of NumPy for efficient data operations.
Facilitate the integration of AI algorithms (Minimax and Alpha-Beta) with the game logic and GUI, serving as a bridge between the AI developers and the rest of the team.
Lead the design and execution of experiments to test AI algorithm effectiveness, collecting and analyzing performance data.
