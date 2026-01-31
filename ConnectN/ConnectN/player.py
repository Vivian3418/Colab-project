'''
Here is the Player Class for this whole connect N game. In this class, we will make sure we get the valid player name and piece.
'''

class Player:
    def __init__(self, player_number: int, existing_piece:str, existing_name: str = None):
        '''
        The function here is to set up the player name, piece and their numbers.
        :param player_number: We will give players different numbers.
        :param existing_piece: This is the piece that the first player chose.
        :param existing_name: This is the name that the first player chose.
        '''
        self.name = self.get_valid_name(player_number, existing_name)
        self.piece = self.get_valid_piece(existing_piece=existing_piece, existing_name=existing_name)

    def get_valid_name(self, player_number: int, existing_name: str = None) -> str:
        '''
        The function here is to make sure inputs are valid.
        :param player_number: We need player's number to remind them some information if they gave the invalid input.
        :param existing_name: We need the name of player one to make sure the player 2 will not enter the same name as player 1.
        :return: We will get valid player name.
        '''
        while True:
            name = input(f"Player {player_number} enter your name: ").strip()
            if len(name) == 0:
                print(f"Player {player_number} your name must have at least one character in it: ")
            elif existing_name and name == existing_name:
                print(f"Player {player_number}, you cannot choose {name} as your name as another player has already chosen it.")
            else:
                return name

    def get_valid_piece(self, existing_piece: str = None, existing_name: str = None) -> str:
        '''
        The function here is to make sure the input pieces are valid.
        :param existing_piece: We need the piece for player 1 to make sure player 2 will not use the same piece.
        :param existing_name: We need the player 1 name to remind player 2 that the piece player 2 entered has been
        used by player 1, if player 2 entered the same piece as player 1.
        :return:
        '''
        while True:
            piece = input(f"{self.name} enter your piece: ").strip()

            if len(piece) != 1:
                print(f"{self.name}, the piece you choose can only be a single character long, but you entered {piece}.")
            elif existing_piece and piece == existing_piece:
                print(f"{self.name} you cannot use {piece} for your piece as {existing_name} is already using it.")
            else:
                return piece
