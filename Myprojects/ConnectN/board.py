'''
Here is the Board Class of the game. In this class, the board is generated, and it checked whether someone win the game or not.
'''

class Board:
    def __init__(self, rows: int, cols: int):
        '''
        The init function here is to generate an empty board.
        :param rows: To make a board, we need the number of the row.
        :param cols: To make a board, we need the number of the column.
        '''
        self.rows = rows
        self.cols = cols
        self.grid = [["*" for _ in range(cols)] for _ in range(rows)]

    def display(self):
        '''
        The function here will generate the initial board with blank characters on it.
        :return: We will get a board with blank characters at each cell.
        '''
        for r in range(self.rows):
            print(f"{r} " + " ".join(self.grid[r]))
        print("  " + " ".join(str(c) for c in range(self.cols)))

    def place_piece(self, col: int, piece: str):
        '''
        The function here is to make sure the piece can be placed correctly.
        :param col: We need the column number to make sure the column is not full, so the piece can still be placed in.
        :param piece: We need to piece to be put into the board.
        :return: We will get the valid piece's row and col, or we will not let that piece get placed into the board.
        '''
        for row in range(self.rows -1, -1, -1):
            if self.grid[row][col] == "*":
                self.grid[row][col] = piece
                return True
        return False

    def is_full(self) -> bool:
        '''
        The function here is to check whether the board is full or not.
        :return: By checking the blank character, we can get whether the board is full or not.
        '''
        for row in self.grid:
            for cell in row:
                if cell == "*":
                    return False
        return True

    def check_winner(self, win_condition: int) -> bool:
        '''
        The function here is to check whether there is a horizontal win, or vertical win, or diagonal win.
        :param win_condition: For each different games, we need to use different win condition to
        make sure whether there is a winner.
        :return: We will get whether there is a winner or not.
        '''
        if self.check_horizontal(win_condition):
            return True
        if self.check_vertical(win_condition):
            return True
        if self.check_diagonal(win_condition):
            return True
        return False

    def check_horizontal(self, win_condition: int) -> bool:
        '''
        This function is to check whether the pieces in the board satisfy the win condition horizontally.
        :param win_condition: Since each new game have different win condition, so we need different numbers to check.
        :return: We will get whether someone win horizontally.
        '''
        for row in self.grid:
            for col in range(self.cols - win_condition + 1):
                is_winner = True
                for i in range(win_condition):
                    if row[col + i] != row[col] or row[col + i] == "*":
                        is_winner = False
                        break
                if is_winner:
                    return True

    def check_vertical(self, win_condition: int) -> bool:
        '''
        This function is to check whether the pieces in the board satisfy the win condition vertically.
        :param win_condition: Since each new game have different win condition, so we need different numbers to check.
        :return: We will get whether someone win vertically.
        '''
        for col in range(self.cols):
            for row in range(self.rows - win_condition + 1):
                is_winner = True
                for i in range(win_condition):
                    if self.grid[row + i][col] != self.grid[row][col] or self.grid[row][col] == "*":
                        is_winner = False
                        break
                if is_winner:
                    return True
        return False  

    def check_diagonal(self, win_condition: int) -> bool:
        '''
        This function is to check whether the pieces in the board satisfy the win condition diagonally.
        :param win_condition: Since each new game have different win condition, so we need different numbers to check.
        :return: We will get whether someone win diagonally.
        '''
        for row in range(self.rows - win_condition + 1):
            for col in range(self.cols - win_condition + 1):
                is_winner = True
                for i in range(win_condition):
                    if self.grid[row + i][col + i] != self.grid[row][col] or self.grid[row][col] == "*":
                        is_winner = False
                        break
                if is_winner:
                    return True

        for row in range(self.rows - win_condition + 1):
            for col in range(win_condition - 1, self.cols):
                is_winner = True
                for i in range(win_condition):
                    if self.grid[row + i][col - i] != self.grid[row][col] or self.grid[row][col] == "*":
                        is_winner = False
                        break
                if is_winner:
                    return True


