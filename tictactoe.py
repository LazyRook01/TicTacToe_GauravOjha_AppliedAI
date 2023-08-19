"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
import numpy as np

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count = 0
    O_count = 0
    for row in board[:]:
        for unit in row:
            X_count = X_count + int(unit=="X")
            O_count = O_count + int(unit=="O")
 
    if X_count == O_count:
        return "X"
    elif X_count > O_count:
        return "O"

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for row_no, row in enumerate(board):
        for col_no, unit in enumerate(row):
            if unit==None:
                possible_actions.append((row_no, col_no))
                
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x,y) = action
    dummy = deepcopy(board)
    if dummy[x][y] == None:
        dummy[x][y] = player(board)
    else:
        raise Exception("Invalid Move")
        
    return dummy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:        #Checking row wins
        if sum(unit== "X" for unit in row) ==3:
            #print("row wise")
            return "X"
        elif sum(unit=="O" for unit in row) ==3:
            #print("row wise")
            return "O"
    
    for i in [0,1,2]:       #Checking column wins
        if sum(row[i]== "X" for row in board) ==3:
            #print("col wise")
            return "X"
        
        if sum(row[i]== "O" for row in board) ==3:
            #print("col wise")
            return "O"
        
    if sum([board[0][0]=="X", board[1][1]=="X", board[2][2]=="X"]) ==3:      #Checking Diagonal Wins
        #print("dia wise 1")
        return "X"
    
    if sum([board[0][2]=="X", board[1][1]=="X", board[2][0]=="X"]) ==3:      #Checking Diagonal Wins
        #print("dia wise 2")
        return "X"
    
    if sum([board[0][0]=="O", board[1][1]=="O", board[2][2]=="O"]) ==3:
        #print("dia wise 3")
        return "O"
    
    if sum([board[0][2]=="O", board[1][1]=="O", board[2][0]=="O"]) ==3:      #Checking Diagonal Wins
        #print("dia wise 4")
        return "O"
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    None_count=0
    for row in board:
        None_count = None_count + sum(unit==None for unit in row)
    
    if None_count == 0 or winner(board)!=None:
            return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    # Base case: Check if the game is over (terminal state)
    if terminal(board):
        # Return the utility value of the board and no move (game is over)
        return utility(board), None

    # Initialize the maximum utility value to negative infinity
    v = float('-inf')
    # Initialize the best move to None
    move = None

    # Loop through all possible actions (moves) on the board
    for action in actions(board):
        # Calculate the minimum value that the opponent (minimizer) can achieve
        aux, act = min_value(result(board, action))

        # If the opponent's value (aux) is greater than the current maximum (v)
        if aux > v:
            # Update the maximum value and the corresponding best move
            v = aux
            move = action

            # If the maximum value becomes 1 (indicating a certain win), return the value and move
            if v == 1:
                return v, move

    # Return the maximum value and the best move after evaluating all actions
    return v, move


def min_value(board):
    # Base case: Check if the game is over (terminal state)
    if terminal(board):
        # Return the utility value of the board and no move (game is over)
        return utility(board), None

    # Initialize the minimum utility value to positive infinity
    v = float('inf')
    # Initialize the best move to None
    move = None

    # Loop through all possible actions (moves) on the board
    for action in actions(board):
        # Calculate the maximum value that the player (maximizer) can achieve
        aux, act = max_value(result(board, action))

        # If the player's value (aux) is smaller than the current minimum (v)
        if aux < v:
            # Update the minimum value and the corresponding best move
            v = aux
            move = action

            # If the minimum value becomes -1 (indicating a certain win), return the value and move
            if v == -1:
                return v, move

    # Return the minimum value and the best move after evaluating all actions
    return v, move

