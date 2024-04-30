from pieces import *
from copy import deepcopy

class Board:
    def __init__(self):
        '''Initialize the board with the standard chess starting position.'''
        self.board:list[list[Piece]] = [[None for _ in range(8)] for _ in range(8)]
        self.white_pieces:list[Piece] = [
            Rook("w",0,0), Knight("w",0,1), Bishop("w",0,2), Queen("w",0,3), King("w",0,4), Bishop("w",0,5), Knight("w",0,6), Rook("w",0,7),
            Pawn("w",1,0), Pawn("w",1,1), Pawn("w",1,2), Pawn("w",1,3), Pawn("w",1,4), Pawn("w",1,5), Pawn("w",1,6), Pawn("w",1,7)
        ]
        self.black_pieces:list[Piece] = [
            Rook("b",7,0), Knight("b",7,1), Bishop("b",7,2), Queen("b",7,3), King("b",7,4), Bishop("b",7,5), Knight("b",7,6), Rook("b",7,7),
            Pawn("b",6,0), Pawn("b",6,1), Pawn("b",6,2), Pawn("b",6,3), Pawn("b",6,4), Pawn("b",6,5), Pawn("b",6,6), Pawn("b",6,7)
        ]
        for i in range(8):
            self.board[0][i] = self.white_pieces[i]
            self.board[1][i] = self.white_pieces[i+8]
            self.board[7][i] = self.black_pieces[i]
            self.board[6][i] = self.black_pieces[i+8]
        self.last_move:dict[str,Piece] = {
            "w": None,
            "b": None
        }
        
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
        '''Translate a position from string to tuple or vice versa.
        
        Args:
            pos (str | tuple[int,int]): The position to translate.

        Returns:
            tuple[int,int] | str: The translated position.
        '''
        if type(pos) is tuple:
            if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
                return ""
            return chr(pos[1] + ord("a")) + str(pos[0]+1) 
        else:
            if not pos[0] in "12345678" or not pos[1] in "abcdefgh":
                return ()
            return (int(pos[0]), ord(pos[1]) - ord("a"))
    
    def create_board_copy(self):
        '''Create a deep copy of the board.
        
        Returns:
            Board: A deep copy of the board.
        '''
        return deepcopy(self)
    
    def get_all_moves(self, color:str) -> list[tuple[int,int,int,int]]:
        '''Get all possible moves for a side (color).
        
        Args:
            color (str): The color of the side.
        
        Returns:
            list[tuple[int,int,int,int]]: A list of all possible moves for the side.
        '''
        if color == "w":
            moves = []
            for piece in self.white_pieces:
                for move in piece.get_all_moves(self):
                    moves.append((piece.i, piece.j, move[0], move[1]))
            return moves
        else:
            moves = []
            for piece in self.black_pieces:
                for move in piece.get_all_moves(self):
                    moves.append((piece.i, piece.j, move[0], move[1]))
            return moves
    
    def is_check(self, color:str) -> bool:
        '''Check if a side (color) is in check.
        
        Args:
            color (str): The color of the side.

        Returns:
            bool: True if the side is in check, False otherwise.
        '''
        if color == "w":
            for piece in self.white_pieces:
                if type(piece) is King:
                    king = piece
                    return self.aimed(king.i, king.j, "b")
        else:
            for piece in self.black_pieces:
                if type(piece) is King:
                    king = piece
                    return self.aimed(king.i, king.j, "w")
        return False
    
    def aimed(self, i:int, j:int, color:str) -> bool:
        '''Check if a square is aimed by a side.
        
        Args:
            i (int): The row of the square.
            j (int): The column of the square.
            color (str): The color of the side.

        Returns:
            bool: True if the square is aimed by the side, False otherwise.
        '''
        if color == "w":
            for piece in self.white_pieces:
                if (i, j) in piece.available_captures(self):
                    return True
        else:
            for piece in self.black_pieces:
                if (i, j) in piece.available_captures(self):
                    return True
        return False
    
    def aimed_by(self, i:int, j:int, color:str) -> list[Piece]:
        '''Get the pieces aiming at a square.
        
        Args:
            i (int): The row of the square.
            j (int): The column of the square.
            color (str): The color of the side.

        Returns:
            list[Piece]: A list of pieces aiming at the square.
        '''
        pieces = []
        if color == "w":
            for piece in self.white_pieces:
                if (i, j) in piece.available_captures(self):
                    pieces.append(piece)
        else:
            for piece in self.black_pieces:
                if (i, j) in piece.available_captures(self):
                    pieces.append(piece)
        return pieces

    def force_move(self, i1:int, j1:int, i2:int, j2:int, promote:str) -> None:
        '''Force a move on the board.
        
        Args:
            i1 (int): The row of the piece to move.
            j1 (int): The column of the piece to move.
            i2 (int): The row to move the piece to.
            j2 (int): The column to move the piece to.
            promote (str): The piece to promote to (N, B, R, Q).    
        '''
        piece:Piece = self.board[i1][j1]
        if type(self.last_move[piece.color]) is Pawn:
            self.last_move[piece.color].en_passant = False
        if type(piece) is Pawn:
            if abs(i1 - i2) == 2:
                piece.en_passant = True
            if j1 != j2 and self.board[i2][j2] is None:
                captured_piece = self.board[i1][j2]
                if captured_piece is not None:
                    if captured_piece.color == "w":
                        self.white_pieces.remove(captured_piece)
                    else:
                        self.black_pieces.remove(captured_piece)
                self.board[i1][j2] = None
            if i2 in (0, 7):
                if piece.color == "w":
                    self.white_pieces.remove(piece)
                else:
                    self.black_pieces.remove(piece)
                if promote == "N":
                    piece = Knight(piece.color)
                elif promote == "B":
                    piece = Bishop(piece.color)
                elif promote == "R":
                    piece = Rook(piece.color)
                elif promote == "Q":
                    piece = Queen(piece.color)
                if piece.color == "w":
                    self.white_pieces.append(piece)
                else:
                    self.black_pieces.append(piece)
        if type(piece) is King:
            if j1==4 and j2==6:
                rook = self.board[i1][7]
                rook.move((i1, 5))
                self.board[i1][5] = rook
                self.board[i1][7] = None
            elif j1==4 and j2==2:
                rook = self.board[i1][0]
                rook.move((i1, 3))
                self.board[i1][3] = rook
                self.board[i1][0] = None
        piece.move((i2, j2))
        self.board[i1][j1] = None
        captured_piece = self.board[i2][j2]
        if captured_piece is not None:
            if captured_piece.color == "w":
                self.white_pieces.remove(captured_piece)
            else:
                self.black_pieces.remove(captured_piece)
        self.board[i2][j2] = piece
        self.last_move[piece.color] = piece
    
    def move(self, i1:int, j1:int, i2:int, j2:int, promote:str) -> bool:
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
        if self.board[i1][j1] is None:
            return False
        piece:Piece = self.board[i1][j1]
        available_moves = piece.get_all_moves(self)
        if (i2, j2) in available_moves:
            self.force_move(i1, j1, i2, j2, promote)
            return True
        return False

    def move_by_string(self, move:str) -> bool:
        '''Translate a move in string format to a move on the board.
        
        Args:
            move (str): The move in string format ("e2e4" or "b7b8Q" for examples).

        Returns:
            bool: True if the move is valid and made, False otherwise.
        '''
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
    
    def get_info(self, target:str) -> str:
        '''Get string information about a piece on the board.
        
        Args:
            target (str): The position of the piece ("e2" for example).

        Returns:
            str: Information about the piece at the position ("♙ e3,e4" for example). The first character is the piece and the rest are the possible moves.
        '''
        if not target[0] in "abcdefgh" or not target[1] in "12345678":
            return ""
        i = int(target[1]) - 1
        j = ord(target[0]) - ord("a")
        if self.board[i][j] is None:
            return ""
        piece = self.board[i][j]
        return str(piece) + " " \
        + ",".join([self.translate_pos(pos) for pos in piece.get_all_moves(self)])
    
    def can_make_move(self, color:str) -> bool:
        '''Check if a side (color) can make any move.
        
        Args:
            color (str): The color of the side.
        
        Returns:
            bool: True if the side can make a move, False otherwise.
        '''
        if color == "w":
            for piece in self.white_pieces:
                if piece.get_all_moves(self) != []:
                    return True
        else:
            for piece in self.black_pieces:
                if piece.get_all_moves(self) != []:
                    return True
        return False
    
    def match_result(self) -> int:
        '''Get the result of the match.

        Returns:
            int: 0 if the match is ongoing, 1 if white wins, 2 if black wins, 3 if it's a draw (stalemate).
        '''
        if self.is_check("w") and not self.can_make_move("w"):
                return 2
        elif self.is_check("b") and not self.can_make_move("b"):
                return 1
        elif not self.can_make_move("w") and not self.can_make_move("b"):
                return 3
        return 0
