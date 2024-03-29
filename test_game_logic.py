from game_logic import minimax, alpha_beta

def test_minimax_terminal_state():
    # Terminal state where computer wins
    score = minimax(10, True, 5, 2)
    assert score == 3, f"Expected score 3, got {score}"
    
    # Terminal state where human wins
    score = minimax(10, False, 3, 6)
    assert score == -3, f"Expected score -3, got {score}"
    
    # Terminal state with a draw
    score = minimax(10, True, 4, 4)
    assert score == 0, f"Expected score 0, got {score}"

def test_alpha_beta_terminal_state():
    # Terminal state where computer wins
    score = alpha_beta(10, 0, float('-inf'), float('inf'), True, 5, 2)
    assert score == 3, f"Expected score 3, got {score}"
    
    # Terminal state where human wins
    score = alpha_beta(10, 0, float('-inf'), float('inf'), False, 3, 6)
    assert score == -3, f"Expected score -3, got {score}"
    
    # Terminal state with a draw
    score = alpha_beta(10, 0, float('-inf'), float('inf'), True, 4, 4)
    assert score == 0, f"Expected score 0, got {score}"

# Test for non-terminal states
def test_minimax_non_terminal_state():
    # Non-terminal state, maximizing player's turn
    score = minimax(24, True, 0, 0)
    # We can't predict the exact outcome without knowing the strategy,
    # but we can check if the function returns an integer which is required.
    assert isinstance(score, int), "Minimax should return an integer score."

def test_alpha_beta_non_terminal_state():
    # Non-terminal state, maximizing player's turn
    score = alpha_beta(24, 0, float('-inf'), float('inf'), True, 0, 0)
    # Similar to minimax, we expect an integer score.
    assert isinstance(score, int), "Alpha-beta should return an integer score."

def test_minimax_strategic_decision():
    # Simulate a scenario where the computer has to choose a strategic move
    score = minimax(24, True, 0, 0)
    assert isinstance(score, int), "Minimax should return an integer score."
    
    # Another scenario where the computer should avoid a loss
    score = minimax(27, True, -1, 2)
    # The computer should avoid moves that lead to immediate loss if possible
    assert score == -2, "Minimax should avoid losing moves."

def test_alpha_beta_strategic_decision():
    # Similar strategic scenario for alpha-beta
    score = alpha_beta(24, 5, float('-inf'), float('inf'), True, 0, 0)
    assert isinstance(score, int), "Alpha-beta should return an integer score."
    
    # Avoiding a loss
    score = alpha_beta(27, 5, float('-inf'), float('inf'), True, -1, 2)
    # The computer should avoid moves that lead to immediate loss if possible
    assert score == -2, "Alpha-beta should avoid losing moves."

# Run the test cases
try:
    test_minimax_terminal_state()
    print("Minimax terminal state tests passed.")
    test_alpha_beta_terminal_state()
    print("Alpha-beta terminal state tests passed.")
    test_minimax_non_terminal_state()
    print("Minimax non-terminal state test passed.")
    test_alpha_beta_non_terminal_state()
    print("Alpha-beta non-terminal state test passed.")
    test_minimax_strategic_decision()
    print("Minimax strategic decision test passed.")
    test_alpha_beta_strategic_decision()
    print("Alpha-beta strategic decision test passed.")
    print("All tests passed successfully.")
except AssertionError as e:
    print(f"A test failed with an error: {e}")

