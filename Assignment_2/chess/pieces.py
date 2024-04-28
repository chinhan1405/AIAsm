class Piece:
    def __init__(self, color:str):
        '''Initializes the piece with a color. The color is a string that can be either "w" means white or "b" means black.'''
        self.color = color
    
    def available_moves(self, board:list[list], i:int, j:int):
        '''Returns a list of tuples representing the available moves for the piece at position (i, j) on the board. Each tuple represents a position on the board. The first element of the tuple is the row number and the second element is the column number. The row and column numbers are 0-indexed.'''
        raise NotImplementedError("Subclass must implement abstract method")


class Pawn(Piece):
    def __init__(self, color:str):
        super().__init__(color)
        self.en_passant = False

    def __str__(self):
        if self.color == "w":
            return "♙"
        else:
            return "♟"

    def available_moves(self, board:list[list[Piece]], i:int, j:int) -> list[tuple[int, int]]:
        moves = []
        if self.color == "w":
            if board[i+1][j] is None:
                moves.append((i+1, j))
                if i == 1 and board[i+2][j] is None:
                    moves.append((i+2, j))
            if j > 0:
                if board[i+1][j-1] is not None and board[i+1][j-1].color == "b":
                    moves.append((i+1, j-1))
                elif board[i][j-1] is not None \
                    and type(board[i][j-1]) is Pawn \
                    and board[i][j-1].en_passant:
                    moves.append((i+1, j-1))
            if j < 7:
                if board[i+1][j+1] is not None and board[i+1][j+1].color == "b":
                    moves.append((i+1, j+1))
                elif board[i][j+1] is not None \
                    and type(board[i][j+1]) is Pawn \
                    and board[i][j+1].en_passant:
                    moves.append((i+1, j+1))
        else:
            if board[i-1][j] is None:
                moves.append((i-1, j))
                if i == 6 and board[i-2][j] is None:
                    moves.append((i-2, j))
            if j > 0:
                if board[i-1][j-1] is not None and board[i-1][j-1].color == "w":
                    moves.append((i-1, j-1))
                elif board[i][j-1] is not None \
                    and type(board[i][j-1]) is Pawn \
                    and board[i][j-1].en_passant:
                    moves.append((i-1, j-1))
            if j < 7:
                if board[i-1][j+1] is not None and board[i-1][j+1].color == "w":
                    moves.append((i-1, j+1))
                elif board[i][j+1] is not None \
                    and type(board[i][j+1]) is Pawn \
                    and board[i][j+1].en_passant:
                    moves.append((i-1, j+1))
        return moves
            

class Rook(Piece):
    def __init__(self, color:str):
        super().__init__(color)
        self.castling = True

    def __str__(self):
        if self.color == "w":
            return "♖"
        else:
            return "♜"

    def available_moves(self, board:list[list[Piece]], i:int, j:int) -> list[tuple[int, int]]:
        moves = []
        for k in range(i+1, 8):
            if board[k][j] is None:
                moves.append((k, j))
            else:
                if board[k][j].color != self.color:
                    moves.append((k, j))
                break
        for k in range(i-1, -1, -1):
            if board[k][j] is None:
                moves.append((k, j))
            else:
                if board[k][j].color != self.color:
                    moves.append((k, j))
                break
        for k in range(j+1, 8):
            if board[i][k] is None:
                moves.append((i, k))
            else:
                if board[i][k].color != self.color:
                    moves.append((i, k))
                break
        for k in range(j-1, -1, -1):
            if board[i][k] is None:
                moves.append((i, k))
            else:
                if board[i][k].color != self.color:
                    moves.append((i, k))
                break
        return moves


class Knight(Piece):
    def __init__(self, color:str):
        super().__init__(color)

    def __str__(self):
        if self.color == "w":
            return "♘"
        else:
            return "♞"

    def available_moves(self, board:list[list[Piece]], i:int, j:int) -> list[tuple[int, int]]:
        moves = []
        for k in range(-2, 3):
            for l in range(-2, 3):
                if abs(k) + abs(l) == 3:
                    if 0 <= i+k < 8 and 0 <= j+l < 8:
                        if board[i+k][j+l] is None or board[i+k][j+l].color != self.color:
                            moves.append((i+k, j+l))
        return moves


class Bishop(Piece):
    def __init__(self, color:str):
        super().__init__(color)

    def __str__(self):
        if self.color == "w":
            return "♗"
        else:
            return "♝"

    def available_moves(self, board:list[list[Piece]], i:int, j:int) -> list[tuple[int, int]]:
        moves = []
        for k in range(1, 8):
            if i+k < 8 and j+k < 8:
                if board[i+k][j+k] is None:
                    moves.append((i+k, j+k))
                else:
                    if board[i+k][j+k].color != self.color:
                        moves.append((i+k, j+k))
                    break
            else:
                break
        for k in range(1, 8):
            if i+k < 8 and j-k >= 0:
                if board[i+k][j-k] is None:
                    moves.append((i+k, j-k))
                else:
                    if board[i+k][j-k].color != self.color:
                        moves.append((i+k, j-k))
                    break
            else:
                break
        for k in range(1, 8):
            if i-k >= 0 and j+k < 8:
                if board[i-k][j+k] is None:
                    moves.append((i-k, j+k))
                else:
                    if board[i-k][j+k].color != self.color:
                        moves.append((i-k, j+k))
                    break
            else:
                break
        for k in range(1, 8):
            if i-k >= 0 and j-k >= 0:
                if board[i-k][j-k] is None:
                    moves.append((i-k, j-k))
                else:
                    if board[i-k][j-k].color != self.color:
                        moves.append((i-k, j-k))
                    break
            else:
                break
        return moves


class Queen(Piece):
    def __init__(self, color:str):
        super().__init__(color)
        self.__rook = Rook(color)
        self.__bishop = Bishop(color)

    def __str__(self):
        if self.color == "w":
            return "♕"
        else:
            return "♛"

    def available_moves(self, board:list[list[Piece]], i:int, j:int) -> list[tuple[int, int]]:
        moves = []
        moves.extend(self.__rook.available_moves(board, i, j))
        moves.extend(self.__bishop.available_moves(board, i, j))
        return moves


class King(Piece):
    def __init__(self, color:str):
        super().__init__(color)
        self.castling = True

    def __str__(self):
        if self.color == "w":
            return "♔"
        else:
            return "♚"
        
    def __aimed_by_opponent(self, board:list[list[Piece]], i:int, j:int) -> bool:
        for k in range(8):
            for l in range(8):
                if board[k][l] is not None and board[k][l].color != self.color:
                    if (i, j) in board[k][l].available_moves(board, k, l):
                        return True
        return False
    
    def is_check(self, board:list[list[Piece]], i:int, j:int) -> bool:
        return self.__aimed_by_opponent(board, i, j)

    def available_moves(self, board:list[list[Piece]], i:int, j:int) -> list[tuple[int, int]]:
        moves = []
        for k in range(-1, 2):
            for l in range(-1, 2):
                if 0 <= i+k < 8 and 0 <= j+l < 8 and (k != 0 or l != 0):
                    if board[i+k][j+l] is None or board[i+k][j+l].color != self.color:
                        moves.append((i+k, j+l))
        if self.castling:
            if type(board[i][7]) is Rook and board[i][7].castling:
                if board[i][j+1] is None and board[i][j+2] is None:
                    if not (self.__aimed_by_opponent(board, i, j) \
                        or self.__aimed_by_opponent(board, i, j+1) \
                        or self.__aimed_by_opponent(board, i, j+2)):
                        moves.append((i, j+2))
            if type(board[i][0]) is Rook and board[i][0].castling:
                if board[i][j-1] is None and board[i][j-2] is None and board[i][j-3] is None:
                    if not (self.__aimed_by_opponent(board, i, j) \
                        or self.__aimed_by_opponent(board, i, j-1) \
                        or self.__aimed_by_opponent(board, i, j-2)):
                        moves.append((i, j-2))
        return moves
        
