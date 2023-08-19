import random

# Initialize the tic-tac-toe board
board = ['-'] * 9

# Define the players
PLAYER_X = 'X'
PLAYER_O = 'O'

# Define the player symbols and their corresponding opponent symbols
PLAYER_SYMBOLS = {PLAYER_X: PLAYER_O, PLAYER_O: PLAYER_X}

# Function to display the tic-tac-toe board
def display_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)

# Function to check if the board is full
def is_board_full(board):
    return "-" not in board

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    
    for positions in winning_positions:
        if all(board[pos] == player for pos in positions):
            return True
    return False

# Function to get the available moves on the board
def get_available_moves(board):
    return [i for i, symbol in enumerate(board) if symbol == '-']

# Minimax algorithm
def minimax(board, depth, player):
    if check_winner(board, PLAYER_X):
        return 1
    if check_winner(board, PLAYER_O):
        return -1
    if is_board_full(board):
        return 0
    
    if player == PLAYER_X:
        best_score = -float('inf')
        for move in get_available_moves(board):
            new_board = board.copy()
            new_board[move] = player
            score = minimax(new_board, depth + 1, PLAYER_O)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            new_board = board.copy()
            new_board[move] = player
            score = minimax(new_board, depth + 1, PLAYER_X)
            best_score = min(best_score, score)
        return best_score

# Function to get the optimal move using the minimax algorithm
def get_optimal_move(board, player):
    available_moves = get_available_moves(board)
    best_move = None
    best_score = -float('inf') if player == PLAYER_X else float('inf')
    
    for move in available_moves:
        new_board = board.copy()
        new_board[move] = player
        score = minimax(new_board, 0, PLAYER_SYMBOLS[player])
        
        if player == PLAYER_X and score > best_score:
            best_score = score
            best_move = move
        elif player == PLAYER_O and score < best_score:
            best_score = score
            best_move = move
    
    return best_move

# Function to calculate the winning probabilities after each move
def calculate_winning_probabilities(board):
    total_moves = 9 - board.count('-')
    winning_probabilities = {PLAYER_X: 0, PLAYER_O: 0}
    
    for player in [PLAYER_X, PLAYER_O]:
        for move in get_available_moves(board):
            new_board = board.copy()
            new_board[move] = player
            if check_winner(new_board, player):
                winning_probabilities[player] += 1
    
    for player in [PLAYER_X, PLAYER_O]:
        winning_probabilities[player] /= total_moves
    
    return winning_probabilities

# Main game loop
current_player = PLAYER_X
display_board(board)

while True:
    if current_player == PLAYER_X:
        move = get_optimal_move(board, current_player)
    else:
        move = int(input(f"Player {current_player}, enter your move (0-8): "))
        
    board[move] = current_player
    display_board(board)
    
    winning_probabilities = calculate_winning_probabilities(board)
    print(f"Winning Probabilities - Player X: {winning_probabilities[PLAYER_X]:.2f}, Player O: {winning_probabilities[PLAYER_O]:.2f}")
    
    if check_winner(board, current_player):
        print(f"Player {current_player} wins!")
        break
    elif is_board_full(board):
        print("It's a draw!")
        break
    
    current_player = PLAYER_SYMBOLS[current_player]
