"""
Here is the ConnectN class for the whole connectN game. In this class, the main thing is to play the game
and make sure players can place their pieces in the right place.
"""

class ConnectN:
    def __init__(self, board, players, win_condition: int):
        '''
        The function here is to set up the important information for playing this game.
        :param board: We need a board to place pieces.
        :param players: We need players to play the game.
        :param win_condition: We need the win condition to test whether the players win or not.
        '''
        self.board = board
        self.players = players
        self.win_condition = win_condition
        self.current_player = 0

    def play(self):
        '''
        The function here is to play the game, and announce the results.
        :return:It will return whether a player win the game or there is a tie.
        '''
        while True:
            self.board.display()
            player = self.players[self.current_player]
            col = self.get_valid_column(player)

            if not self.board.place_piece(col, player.piece):
                continue

            if self.board.check_winner(self.win_condition):
                self.board.display()
                print(f"{player.name} won the game!")
                return

            if self.board.is_full():
                self.board.display()
                print("Tie game.")
                return

            self.current_player = 1 - self.current_player

    def get_valid_column(self, player):
        '''
        The function here is to make sure the column input is valid.
        :param player: We need player information to ask them which column they want to place their pieces.
        :return:We will get valid column number that players can put their pieces into it.
        '''
        while True:
            col = input(f"{player.name} enter the column you want to play in: ")
            try:
                int_col = int(col)
            except ValueError:
                print(f'Column needs to be an integer but {col} was entered.')
                continue

            if not (0 <= int_col < self.board.cols):
                print(f"Column entered needs to be between 0 and {self.board.cols - 1} but {int_col} was entered.")
                continue

            if self.board.grid[0][int_col] != "*":
                print(f"You can't play in column {int_col} as it is already full")
                continue

            return int_col