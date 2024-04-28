from board import Board
import os

class ChessGame:
    def __init__(self):
        self.board = Board()
        self.turn = "w"
    
    def __str__(self):
        string = str(self.board) + "\n"
        if self.turn == "w":
            string += "White's turn"
        else:
            string += "Black's turn"
        return string
    
    def switch_turn(self):
        if self.turn == "w":
            self.turn = "b"
        else:
            self.turn = "w"
    
    def move(self, p1:tuple[int,int], p2:tuple[int,int], promote:str) -> bool:
        i1, j1 = p1
        i2, j2 = p2
        if self.board.board[i1][j1].color == self.turn:
            self.board.move(i1, j1, i2, j2, promote)
            self.switch_turn()
            return True
        else:
            return False
        
    def move_str(self, move:str) -> bool:
        i1 = int(move[1]) - 1
        j1 = ord(move[0]) - ord("a")
        if self.board.board[i1][j1] is not None and self.board.board[i1][j1].color==self.turn:
            self.board.make_move(move)
            self.switch_turn()
            return True
        else:
            return False
        
    def game_start(self):
        os.system("cls")
        print(self.board)
        while True:
            move = input("Enter move: ")
            if move == "exit":
                break
            elif move[0] == "i":
                print(self.board.get_info(move[1:]))
                continue
            if not self.move_str(move):
                continue
            os.system("cls")
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


if __name__ == "__main__":
    game = ChessGame()
    game.game_start()

        