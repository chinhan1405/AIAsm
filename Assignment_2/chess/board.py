from pieces import *
from copy import deepcopy

class Board:
    def __init__(self):
        self.board:list[list[Piece]] = [[None for _ in range(8)] for _ in range(8)]
        self.last_move:Piece = None
        for i in range(8):
            self.board[1][i] = Pawn("w")
            self.board[6][i] = Pawn("b")
        self.board[0][0] = Rook("w")
        self.board[0][7] = Rook("w")
        self.board[7][0] = Rook("b")
        self.board[7][7] = Rook("b")
        self.board[0][1] = Knight("w")
        self.board[0][6] = Knight("w")
        self.board[7][1] = Knight("b")
        self.board[7][6] = Knight("b")
        self.board[0][2] = Bishop("w")
        self.board[0][5] = Bishop("w")
        self.board[7][2] = Bishop("b")
        self.board[7][5] = Bishop("b")
        self.board[0][3] = Queen("w")
        self.board[7][3] = Queen("b")
        self.board[0][4] = King("w")
        self.board[7][4] = King("b")
    
    def __str__(self):
        s = ""
        for i in range(7,-1,-1):
            s += str(i+1) + " "
            for j in range(8):
                if self.board[i][j] is None:
                    s += " "
                else:
                    s += str(self.board[i][j])
                s += "  "
            s += "\n"
        s += "  "
        for i in "abcdefgh":
            s += i + "  "
        return s
    
    def translate_pos(self, pos:str|tuple[int,int]) -> tuple[int,int]|str:
        if type(pos) is tuple:
            if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
                return ""
            return chr(pos[1] + ord("a")) + str(pos[0]+1) 
        else:
            if not pos[0] in "12345678" or not pos[1] in "abcdefgh":
                return ()
            return (int(pos[0]), ord(pos[1]) - ord("a"))
    
    def __create_board_copy(self):
        return deepcopy(self)
    
    def __is_check(self, color:str) -> bool:
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is not None and self.board[i][j].color == color:
                    if type(self.board[i][j]) is King:
                        return self.board[i][j].is_check(self.board, i, j)
        return False
    
    def get_available_moves(self, i:int, j:int) -> list[tuple[int, int]]:
        if self.board[i][j] is None:
            return []
        color = self.board[i][j].color
        available_moves = self.board[i][j].available_moves(self.board, i, j)
        filtered_moves = []
        for i2, j2 in available_moves:
            board_copy = self.__create_board_copy()
            board_copy.__force_move(i, j, i2, j2, "Q")
            if not board_copy.__is_check(color):
                filtered_moves.append((i2, j2))
        return filtered_moves
    
    def __force_move(self, i1:int, j1:int, i2:int, j2:int, promote:str) -> None:
        piece:Piece = self.board[i1][j1]
        if type(piece) is King:
            piece.castling = False
        if type(piece) is Rook:
            piece.castling = False
        if type(self.last_move) is Pawn:
            self.last_move.en_passant = False
        if type(piece) is Pawn:
            if abs(i1 - i2) == 2:
                piece.en_passant = True
            if j1 != j2 and self.board[i2][j2] is None:
                self.board[i1][j2] = None
            if i2 in (0, 7):
                if promote is None:
                    return False
                if promote == "N":
                    piece = Knight(piece.color)
                elif promote == "B":
                    piece = Bishop(piece.color)
                elif promote == "R":
                    piece = Rook(piece.color)
                elif promote == "Q":
                    piece = Queen(piece.color)
        if type(piece) is King:
            piece.castling = False
            if j1==4 and j2==6:
                self.board[i1][7].castling = False
                self.board[i1][5] = self.board[i1][7]
                self.board[i1][7] = None
            elif j1==4 and j2==2:
                self.board[i1][0].castling = False
                self.board[i1][3] = self.board[i1][0]
                self.board[i1][0] = None
        if type(piece) is Rook:
            piece.castling = False
        self.board[i1][j1] = None
        self.board[i2][j2] = piece
        self.last_move = piece
    
    def move(self, i1:int, j1:int, i2:int, j2:int, promote:str) -> bool:
        if self.board[i1][j1] is None:
            return False
        piece:Piece = self.board[i1][j1]
        available_moves = self.get_available_moves(i1, j1)
        if (i2, j2) in available_moves:
            self.__force_move(i1, j1, i2, j2, promote)
            return True
        return False

    def make_move(self, move:str) -> bool:
        '''Make a move on the board. The move should be in the format "a2a4" or "a7a8Q" (for promotion (N, B, R, Q)).'''
        if len(move) not in (4, 5):
            return False
        if not move[0] in "abcdefgh" or not move[2] in "abcdefgh":
            return False
        if not move[1] in "12345678" or not move[3] in "12345678":
            return False
        if len(move) == 5 and move[4] not in "NBRQ":
            return False
        i1 = int(move[1]) - 1
        j1 = ord(move[0]) - ord("a")
        i2 = int(move[3]) - 1
        j2 = ord(move[2]) - ord("a")
        return self.move(i1, j1, i2, j2, move[4] if len(move) == 5 else None)
    
    def get_info(self, target:str) -> bool:
        '''Get information about a piece on the board. The target should be in the format "a2".'''
        if not target[0] in "abcdefgh" or not target[1] in "12345678":
            return False
        i = int(target[1]) - 1
        j = ord(target[0]) - ord("a")
        if self.board[i][j] is None:
            return ""
        return str(self.board[i][j]) + " " \
        + ",".join([self.translate_pos(pos) for pos in self.get_available_moves(i, j)])
    
    def match_result(self) -> int:
        '''Get the result of the match. 0 for not finished, 1 for white wins, 2 for black wins, 3 for draw.'''
        if self.__is_check("w"):
            if all(self.get_available_moves(i, j) == [] for i in range(8) for j in range(8) if self.board[i][j] is not None and self.board[i][j].color == "w"):
                return 2
        elif self.__is_check("b"):
            if all(self.get_available_moves(i, j) == [] for i in range(8) for j in range(8) if self.board[i][j] is not None and self.board[i][j].color == "b"):
                return 1
        else:
            if all(self.get_available_moves(i, j) == [] for i in range(8) for j in range(8) if self.board[i][j] is not None):
                return 3
        return 0

    
if __name__ == "__main__":
    board = Board()
    import os
    os.system("cls")
    print(board)

    while True:
        move = input("Enter move: ")
        if move == "exit":
            break
        elif move[0] == "i":
            print(board.get_info(move[1:]))
            continue
        if not board.make_move(move):
            continue
        os.system("cls")
        print(board)
        result = board.match_result()
        if result == 1:
            print("White wins")
            break
        elif result == 2:
            print("Black wins")
            break
        elif result == 3:
            print("Draw")
            break