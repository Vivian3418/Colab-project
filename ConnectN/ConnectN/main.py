"""
The code here is to generate a connect n game. When one of the users achieve n same pieces line up horizontally, vertically,
or diagonally, the user wins. If the board is full, and no one wins, there is a tie.
"""

import random
from ConnectN.connectn import ConnectN
from ConnectN.player import Player
from ConnectN.board import Board

def main():
    '''
    Here is the main function for the game.
    :return: We will get inputs, player's sequence, and other things we will use here.
    '''
    seed = get_valid_integer("Enter the seed for the game: ", None)
    rows = get_valid_integer("Enter the number of rows: ", 1)
    cols = get_valid_integer("Enter the number of columns: ", 1)
    win_condition = get_valid_integer("Enter the number of pieces to win: ", 1)

    board = Board(rows, cols)

    player1 = Player(1,existing_name=None, existing_piece=None)
    player2 = Player(2, existing_name=player1.name, existing_piece=player1.piece)

    random.seed(seed)
    first_player = random.randint(0, 1)
    players = [player1, player2] if first_player == 0 else [player2, player1]

    game = ConnectN(board, players, win_condition)
    game.play()

def get_valid_integer(prompt: str, min_value: int = None) -> int:
    '''
    The function here is to make sure the user inputs are valid.
    :param prompt: We need the inputs from users, and what they enter are called prompt.
    :param min_value: The min value is the value that give users restrict and remind of what is the correct thing to enter.
    :return: We will get valid inputs.
    '''
    while True:
        value = input(prompt)
        try:
            int_value = int(value)
            if min_value is None or int_value >= min_value:
                return int_value
            print(f"The value entered needs to be at least {min_value}, but you entered {value}.")
        except ValueError:
            print(f"{value} is not a whole number.")

if __name__ == "__main__":
    main()
