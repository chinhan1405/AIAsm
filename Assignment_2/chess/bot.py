class ChessBot:
    def __init__(self, name):
        self.name = name

    def move(self, board):
        return board.get_random_move()