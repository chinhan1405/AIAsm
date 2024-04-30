import os
from board import Board
from bot import ChessBot

class ChessGame:
    def __init__(self):
        '''Initialize the game.'''
        self.board = Board()
        self.player_side = None
        self.turn = "w"
        self.turn_num = 0
        self.bot = None
        self.game_history = []
    
    def __str__(self):
        string = str(self.board) + "\n"
        if self.turn == "w":
            string += "White's turn"
        else:
            string += "Black's turn"
        return string
    
    def init_bot(self, level:int, color:str) -> None:
        '''Init chess bot.
        
        Args:
            level (int): How smart the bot will be.
            color (str): Side of the bot (w/b)
        '''
        self.bot = ChessBot(level, color)
    
    def switch_turn(self):
        '''Switch the current turn (from white to black and vice versa)'''
        if self.turn == "w":
            self.turn = "b"
        else:
            self.turn = "w"
    
    def add_to_history(self):
        '''Add current board to history.'''
        self.game_history.append(self.board)
        self.board = self.board.create_board_copy()

    def pop_from_history(self):
        return self.game_history.pop()

    def undo(self):
        '''Return the current board to the previous situation.'''
        if self.game_history:
            self.board = self.game_history.pop()

    def move(self, i1, j1, i2, j2, promote:str) -> bool:
        '''Check if a move is valid and make it on the board.
        
        Args:
            i1 (int): The row of the piece to move.
            j1 (int): The column of the piece to move.
            i2 (int): The row to move the piece to.
            j2 (int): The column to move the piece to.
            promote (str): The piece to promote to (N, B, R, Q).

        Returns:
            bool: True if the move is valid and made, False otherwise.
        '''
        if self.board.board[i1][j1].color == self.turn:
            if self.board.move(i1, j1, i2, j2, promote):
                self.switch_turn()
                return True
            else:
                return False
        else:
            return False
        
    def move_by_string(self, move:str) -> bool:
        '''Check if a move is valid and make it on the board.
        
        Args:
            move (str): The move to make in the format "a1a2" or "a1a2Q".

        Returns:
            bool: True if the move is valid and made, False otherwise.
        '''
        if move[0] not in "abcdefgh" or move[2] not in "abcdefgh":
            return False
        i1 = int(move[1]) - 1
        j1 = ord(move[0]) - ord("a")
        if self.board.board[i1][j1] is not None and self.board.board[i1][j1].color==self.turn:
            if self.board.move_by_string(move):
                self.switch_turn()
                return True
            else:
                return False
        else:
            return False
        
    def game_start(self):
        '''Start the game and keep it running until the game is over. The game is played in the console.'''
        # Choose side and bot level
        self.player_side = input("Choose side (w/b): ")
        while not self.player_side == "w" and not self.player_side == "b":
            self.player_side = input("Wrong format. Please choose again (w/b): ")
        bot_level = input("Choose bot level (1-5): ")
        while not len(bot_level) == 1  and bot_level not in "12345":
            bot_level = input("Wrong format. Please choose again (1-5): ")
        bot_level = int(bot_level)
        self.init_bot(bot_level, "w" if self.player_side == "b" else "b")
        # Game loop
        while True:
            # os.system("cls")
            print(len(self.game_history))
            print(self.board)
            result = self.board.match_result()
            if result == 1:
                print("White wins")
                break
            elif result == 2:
                print("Black wins")
                break
            elif result == 3:
                print("Draw")
                break
            if self.turn == self.player_side:
                move = input("Enter move: ")
                if move == "exit":
                    break
                elif move == "lose":
                    if self.turn == "w":
                        print("Black wins")
                    else:
                        print("White wins")
                    break
                elif move == "undo":
                    self.undo()
                    continue
                elif move[0] == "i" and len(move) == 3:
                    info = self.board.get_info(move[1:])
                    if info:
                        print(info)
                    continue
                self.add_to_history()
                if not self.move_by_string(move):
                    self.pop_from_history()
                    continue
            else:
                move = self.bot.best_move(self.board, self.turn_num)
                self.move(*move, "Q")
            if self.turn == "b":
                self.turn_num += 1
            


if __name__ == "__main__":
    game = ChessGame()
    game.game_start()

        