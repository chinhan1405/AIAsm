class Piece:
    def __init__(self, color:str, i:int=-1, j:int=-1):
        '''Initializes the piece with a color. The color is a string that can be either "w" means white or "b" means black.'''
        self.color = color
        self.i = i
        self.j = j

    def get_pos(self):
        '''The position of the piece on the board.
        
        Returns:
            tuple: The first element of the tuple is the row number and the second element is the column number. The row and column numbers are 0-indexed.
        '''
        return (self.i, self.j)
    
    def available_moves(self, board):
        '''Available MOVES for the piece at position (i, j) on the board. Each tuple represents a position on the board.
        
        Args:
            board (Board): The board object on which the piece is placed.

        Returns:
            list[tuple[int, int]]: The first element of the tuple is the row number and the second element is the column number. The row and column numbers are 0-indexed.
        '''
        raise NotImplementedError("Subclass must implement abstract method")
    
    def available_captures(self, board):
        '''Available CAPTURING MOVES for the piece at position (i, j) on the board.
        
        Args:
            board (Board): The board object on which the piece is placed.

        Returns:
            list[tuple[int, int]]: The first element of the tuple is the row number and the second element is the column number. The row and column numbers are 0-indexed.
        '''
        return self.available_moves(board)

    def get_all_moves(self, board):
        '''Available MOVES after filtering out the moves that put the king in check.
        
        Args:
            board (Board): The board object on which the piece is placed.

        Returns:
            list[tuple[int, int]]: The first element of the tuple is the row number and the second element is the column number. The row and column numbers are 0-indexed.
        '''
        moves = self.available_moves(board)
        i, j = self.get_pos()
        filtered_moves = []
        for move in moves:
            new_board = board.create_board_copy()
            new_board.force_move(i, j, move[0], move[1], "Q")
            if new_board.is_check(self.color):
                continue
            filtered_moves.append(move)
        return filtered_moves

    def move(self, pos:tuple[int, int]) -> None:
        '''Updates the position of the piece on the board.
        
        Args:
            pos (tuple[int,int]): The first element of the tuple is the row number and the second element is the column number. The row and column numbers are 0-indexed.
        '''
        self.i, self.j = pos


class Pawn(Piece):
    def __init__(self, color:str, i:int=-1, j:int=-1):
        super().__init__(color, i, j)
        self.en_passant = False

    def __str__(self):
        if self.color == "w":
            return "♙"
        else:
            return "♟"

    def available_moves(self, board) -> list[tuple[int, int]]:
        board:list[list[Piece]] = board.board
        i, j = self.get_pos()
        moves = []
        if self.color == "w":
            if board[i+1][j] is None:
                moves.append((i+1, j))
                if i == 1 and board[i+2][j] is None:
                    moves.append((i+2, j))
        else:
            if board[i-1][j] is None:
                moves.append((i-1, j))
                if i == 6 and board[i-2][j] is None:
                    moves.append((i-2, j))
        return moves            
    
    def available_captures(self, board) -> list[tuple[int, int]]:
        board:list[list[Piece]] = board.board
        i, j = self.get_pos()
        captures = []
        if self.color == "w":
            if j > 0:
                if board[i+1][j-1] is not None and board[i+1][j-1].color == "b":
                    captures.append((i+1, j-1))
                elif board[i][j-1] is not None \
                    and type(board[i][j-1]) is Pawn \
                    and board[i][j-1].en_passant:
                    captures.append((i+1, j-1))
            if j < 7:
                if board[i+1][j+1] is not None and board[i+1][j+1].color == "b":
                    captures.append((i+1, j+1))
                elif board[i][j+1] is not None \
                    and type(board[i][j+1]) is Pawn \
                    and board[i][j+1].en_passant:
                    captures.append((i+1, j+1))
        else:
            if j > 0:
                if board[i-1][j-1] is not None and board[i-1][j-1].color == "w":
                    captures.append((i-1, j-1))
                elif board[i][j-1] is not None \
                    and type(board[i][j-1]) is Pawn \
                    and board[i][j-1].en_passant:
                    captures.append((i-1, j-1))
            if j < 7:
                if board[i-1][j+1] is not None and board[i-1][j+1].color == "w":
                    captures.append((i-1, j+1))
                elif board[i][j+1] is not None \
                    and type(board[i][j+1]) is Pawn \
                    and board[i][j+1].en_passant:
                    captures.append((i-1, j+1))
        return captures
        
    def get_all_moves(self, board) -> list[tuple[int, int]]:
        moves = self.available_moves(board) + self.available_captures(board)
        i, j = self.get_pos()
        filtered_moves = []
        for move in moves:
            new_board = board.create_board_copy()
            new_board.force_move(i, j, move[0], move[1], "Q")
            if not new_board.is_check(self.color):
                filtered_moves.append(move)
        return filtered_moves
            

class Rook(Piece):
    def __init__(self, color:str, i:int=-1, j:int=-1):
        super().__init__(color, i, j)
        self.castling = True

    def __str__(self):
        if self.color == "w":
            return "♖"
        else:
            return "♜"

    def available_moves(self, board) -> list[tuple[int, int]]:
        board:list[list[Piece]] = board.board
        i, j = self.get_pos()
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
    
    def move(self, pos:tuple[int, int]) -> None:
        self.i, self.j = pos
        self.castling = False


class Knight(Piece):
    def __init__(self, color:str, i:int=-1, j:int=-1):
        super().__init__(color, i, j)

    def __str__(self):
        if self.color == "w":
            return "♘"
        else:
            return "♞"

    def available_moves(self, board) -> list[tuple[int, int]]:
        board:list[list[Piece]] = board.board
        i, j = self.get_pos()
        moves = []
        for k in range(-2, 3):
            for l in range(-2, 3):
                if abs(k) + abs(l) == 3:
                    if 0 <= i+k < 8 and 0 <= j+l < 8:
                        if board[i+k][j+l] is None or board[i+k][j+l].color != self.color:
                            moves.append((i+k, j+l))
        return moves


class Bishop(Piece):
    def __init__(self, color:str, i:int=-1, j:int=-1):
        super().__init__(color, i, j)

    def __str__(self):
        if self.color == "w":
            return "♗"
        else:
            return "♝"

    def available_moves(self, board) -> list[tuple[int, int]]:
        board:list[list[Piece]] = board.board
        moves = []
        i, j = self.get_pos()
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
    def __init__(self, color:str, i:int=-1, j:int=-1):
        super().__init__(color, i, j)
        self.__rook = Rook(color, i, j)
        self.__bishop = Bishop(color, i, j)

    def __str__(self):
        if self.color == "w":
            return "♕"
        else:
            return "♛"

    def available_moves(self, board) -> list[tuple[int, int]]:
        moves = []
        i, j = self.get_pos()
        moves.extend(self.__rook.available_moves(board))
        moves.extend(self.__bishop.available_moves(board))
        return moves
    
    def move(self, pos:tuple[int, int]) -> None:
        self.i, self.j = pos
        self.__rook.move(pos)
        self.__bishop.move(pos)


class King(Piece):
    def __init__(self, color:str, i:int=-1, j:int=-1):
        super().__init__(color, i, j)
        self.castling = True

    def __str__(self):
        if self.color == "w":
            return "♔"
        else:
            return "♚"

    def _can_short_castle(self, board) -> bool:
        '''Checks if the king can perform short castling.
        
        Args:
            board (Board): The board object on which the piece is placed.

        Returns:
            bool: True if the king can perform short castling, False otherwise.
        '''
        if not self.castling:
            return False
        row = 0 if self.color == "w" else 7
        if board.board[row][5] is not None or board.board[row][6] is not None:
            return False
        if type(board.board[row][7]) is not Rook or not board.board[row][7].castling:
            return False
        op_color = "b" if self.color == "w" else "w"
        return not board.aimed(row, 5, op_color) \
            and not board.aimed(row, 6, op_color) \
            and not board.is_check(self.color)
    
    def _can_long_castle(self, board) -> bool:
        '''Checks if the king can perform long castling.

        Args:
            board (Board): The board object on which the piece is placed.

        Returns:
            bool: True if the king can perform long castling, False otherwise.
        '''
        if not self.castling:
            return False
        row = 0 if self.color == "w" else 7
        if board.board[row][1] is not None or board.board[row][2] is not None or board.board[row][3] is not None:
            return False
        if type(board.board[row][0]) is not Rook or not board.board[row][0].castling:
            return False
        op_color = "b" if self.color == "w" else "w"
        return not board.aimed(row, 2, op_color) \
            and not board.aimed(row, 3, op_color) \
            and not board.is_check(self.color)

    def available_moves(self, board) -> list[tuple[int, int]]:
        board_instance = board
        board:list[list[Piece]] = board.board
        moves = []
        i, j = self.get_pos()
        for k in range(-1, 2):
            for l in range(-1, 2):
                if 0 <= i+k < 8 and 0 <= j+l < 8 and (k != 0 or l != 0):
                    if board[i+k][j+l] is None or board[i+k][j+l].color != self.color:
                        moves.append((i+k, j+l))
        # castling
        if self._can_short_castle(board_instance):
            moves.append((i, j+2))
        if self._can_long_castle(board_instance):
            moves.append((i, j-2))
        return moves
    
    def available_captures(self, board):
        board:list[list[Piece]] = board.board
        moves = []
        i, j = self.get_pos()
        for k in range(-1, 2):
            for l in range(-1, 2):
                if 0 <= i+k < 8 and 0 <= j+l < 8 and (k != 0 or l != 0):
                    if board[i+k][j+l] is None or board[i+k][j+l].color != self.color:
                        moves.append((i+k, j+l))
        return moves
    
    
    def move(self, pos:tuple[int, int]) -> None:
        self.i, self.j = pos
        self.castling = False
