from board import Board
from pieces import *

class ChessEvaluator:

    ENDGAME_PAWN_PSQT = [
        [  0,   0,   0,   0,   0,   0,   0,   0],
        [178, 173, 158, 134, 147, 132, 165, 187],
        [ 94, 100,  85,  67,  56,  53,  82,  84],
        [ 32,  24,  13,   5,  -2,   4,  17,  17],
        [ 13,   9,  -3,  -7,  -7,  -8,   3,  -1],
        [  4,   7,  -6,   1,   0,  -5,  -1,  -8],
        [ 13,   8,   8,  10,  13,   0,   2,  -7],
        [  0,   0,   0,   0,   0,   0,   0,   0]
    ]

    MIDGAME_PAWN_PSQT = [
        [  0,   0,   0,   0,   0,   0,   0,   0],
        [ 98, 134,  61,  95,  68, 126,  34, -11],
        [ -6,   7,  26,  31,  65,  56,  25, -20],
        [-14,  13,   6,  21,  23,  12,  17, -23],
        [-27,  -2,  -5,  12,  17,   6,  10, -25],
        [-26,  -4,  -4, -10,   3,   3,  33, -12],
        [-35,  -1, -20, -23, -15,  24,  38, -22],
        [  0,   0,   0,   0,   0,   0,   0,   0]
    ]

    ENDGAME_KNIGHT_PSQT = [
        [-58, -38, -13, -28, -31, -27, -63, -99],
        [-25,  -8, -25,  -2,  -9, -25, -24, -52],
        [-24, -20,  10,   9,  -1,  -9, -19, -41],
        [-17,   3,  22,  22,  22,  11,   8, -18],
        [-18,  -6,  16,  25,  16,  17,   4, -18],
        [-23,  -3,  -1,  15,  10,  -3, -20, -22],
        [-42, -20, -10,  -5,  -2, -20, -23, -44],
        [-29, -51, -23, -15, -22, -18, -50, -64]
    ]

    MIDGAME_KNIGHT_PSQT = [
       [-167, -89, -34, -49,  61, -97, -15, -107],
        [-73, -41,  72,  36,  23,  62,   7,  -17],
        [-47,  60,  37,  65,  84, 129,  73,   44],
        [ -9,  17,  19,  53,  37,  69,  18,   22],
        [-13,   4,  16,  13,  28,  19,  21,   -8],
        [-23,  -9,  12,  10,  19,  17,  25,  -16],
        [-29, -53, -12,  -3,  -1,  18, -14,  -19],
       [-105, -21, -58, -33, -17, -28, -19,  -23],
    ]

    ENDGAME_BISHOP_PSQT = [
        [-14, -21, -11,  -8,  -7,  -9, -17, -24],
        [ -8,  -4,   7, -12,  -3, -13,  -4, -14],
        [  2,  -8,   0,  -1,  -2,   6,   0,   4],
        [ -3,   9,  12,   9,  14,  10,   3,   2],
        [ -6,   3,  13,  19,   7,  10,  -3,  -9],
        [-12,  -3,   8,  10,  13,   3,  -7, -15],
        [-14, -18,  -7,  -1,   4,  -9, -15, -27],
        [-23,  -9, -23,  -5,  -9, -16,  -5, -17]
    ]

    MIDGAME_BISHOP_PSQT = [
        [-29,   4, -82, -37, -25, -42,   7,  -8],
        [-26,  16, -18, -13,  30,  59,  18, -47],
        [-16,  37,  43,  40,  35,  50,  37,  -2],
        [ -4,   5,  19,  50,  37,  37,   7,  -2],
        [ -6,  13,  13,  26,  34,  12,  10,   4],
        [  0,  15,  15,  15,  14,  27,  18,  10],
        [  4,  15,  16,   0,   7,  21,  33,   1],
        [-33,  -3, -14, -21, -13, -12, -39, -21]
    ]

    ENDGAME_ROOK_PSQT = [
        [ 13,  10,  18,  15,  12,  12,   8,   5],
        [ 11,  13,  13,  11,  -3,   3,   8,   3],
        [  7,   7,   7,   5,   4,  -3,  -5,  -3],
        [  4,   3,  13,   1,   2,   1,  -1,   2],
        [  3,   5,   8,   4,  -5,  -6,  -8, -11],
        [ -4,   0,  -5,  -1,  -7, -12,  -8, -16],
        [ -6,  -6,   0,   2,  -9,  -9, -11,  -3],
        [ -9,   2,   3,  -1,  -5, -13,   4, -20]
    ]

    MIDGAME_ROOK_PSQT = [
        [ 32,  42,  32,  51,  63,   9,  31,  43],
        [ 27,  32,  58,  62,  80,  67,  26,  44],
        [ -5,  19,  26,  36,  17,  45,  61,  16],
        [-24, -11,   7,  26,  24,  35,  -8, -20],
        [-36, -26, -12,  -1,   9,  -7,   6, -23],
        [-45, -25, -16, -17,   3,   0,  -5, -33],
        [-44, -16, -20,  -9,  -1,  11,  -6, -71],
        [-19, -13,   1,  17,  16,   7, -37, -26]
    ]

    ENDGAME_QUEEN_PSQT = [
        [ -9,  22,  22,  27,  27,  19,  10,  20],
        [-17,  20,  32,  41,  58,  25,  30,   0],
        [-20,   6,   9,  49,  47,  35,  19,   9],
        [  3,  22,  24,  45,  57,  40,  57,  36],
        [-18,  28,  19,  47,  31,  34,  39,  23],
        [-16, -27,  15,   6,   9,  17,  10,   5],
        [-22, -23, -30, -16, -16, -23, -36, -32],
        [-33, -28, -22, -43,  -5, -32, -20, -41]
    ]

    MIDGAME_QUEEN_PSQT = [
        [-28,   0,  29,  12,  59,  44,  43,  45],
        [-24, -39,  -5,   1, -16,  57,  28,  54],
        [-13, -17,   7,   8,  29,  56,  47,  57],
        [-27, -27, -16, -16,  -1,  17,  -2,   1],
        [ -9, -26,  -9, -10,  -2,  -4,   3,  -3],
        [-14,   2, -11,  -2,  -5,   2,  14,   5],
        [-35,  -8,  11,   2,   8,  15,  -3,   1],
        [ -1, -18,  -9,  10, -15, -25, -31, -50]
    ]

    ENDGAME_KING_PSQT = [
        [-74, -35, -18, -18, -11,  15,   4, -17],
        [-12,  17,  14,  17,  17,  38,  23,  11],
        [ 10,  17,  23,  15,  20,  45,  44,  13],
        [ -8,  22,  24,  27,  26,  33,  26,   3],
        [-18,  -4,  21,  24,  27,  23,   9, -11],
        [-19,  -3,  11,  21,  23,  16,   7,  -9],
        [-27, -11,   4,  13,  14,   4,  -5, -17],
        [-53, -34, -21, -11, -28, -14, -24, -43]
    ]

    MIDGAME_KING_PSQT = [
        [-65,  23,  16, -15, -56, -34,   2,  13],
        [ 29,  -1, -20,  -7,  -8,  -4, -38, -29],
        [ -9,  24,   2, -16, -20,   6,  22, -22],
        [-17, -20, -12, -27, -30, -25, -14, -36],
        [-49,  -1, -27, -39, -46, -44, -33, -51],
        [-14, -14, -22, -46, -44, -30, -15, -27],
        [  1,   7,  -8, -64, -43, -16,   9,   8],
        [-15,  36,  12, -54,   8, -28,  24,  14]
    ]

    ENDGAME_PSQT = {
        Pawn:ENDGAME_PAWN_PSQT,
        Knight:ENDGAME_KNIGHT_PSQT,
        Bishop:ENDGAME_BISHOP_PSQT,
        Rook:ENDGAME_ROOK_PSQT,
        Queen:ENDGAME_QUEEN_PSQT,
        King:ENDGAME_KING_PSQT
    }

    MIDGAME_PSQT = {
        Pawn:MIDGAME_PAWN_PSQT,
        Knight:MIDGAME_KNIGHT_PSQT,
        Bishop:MIDGAME_BISHOP_PSQT,
        Rook:MIDGAME_ROOK_PSQT,
        Queen:MIDGAME_QUEEN_PSQT,
        King:MIDGAME_KING_PSQT
    }

    PIECE_VALUES = {
        Pawn:100,
        Knight:300,
        Bishop:300,
        Rook:500,
        Queen:900,
        King:0
    }

    @staticmethod

    def check_bias(board:Board) -> int:
        '''Check if the board has a bias towards one side.
        
        Args:
            board (Board): The board to check.

        Returns:
            int: The bias of the board.
        '''
        if board.is_check("w"):
            return -30
        elif board.is_check("b"):
            return 30
        return 0
    
    def piece_value_bias(board:Board) -> int:
        '''Check if the board has a bias towards one side.
        
        Args:
            board (Board): The board to check.

        Returns:
            int: The bias of the board.
        '''
        value = 0
        for piece in board.white_pieces:
            value += ChessEvaluator.PIECE_VALUES[type(piece)]
        for piece in board.black_pieces:
            value -= ChessEvaluator.PIECE_VALUES[type(piece)]
        return value
    
    def piece_square_value_bias(board:Board, turn_num:int) -> int:
        '''Check if the board has a bias towards one side.
        
        Args:
            board (Board): The board to check.

        Returns:
            int: The bias of the board.
        '''
        value = 0
        psqt = ChessEvaluator.MIDGAME_PSQT
        if turn_num > 24:
            psqt = ChessEvaluator.ENDGAME_PSQT
        for piece in board.white_pieces:
            value += psqt[type(piece)][::-1][piece.i][piece.j]
        for piece in board.black_pieces:
            value -= psqt[type(piece)][piece.i][piece.j]
        return value
    
    def open_column_occupancy_bias(board:Board) -> int:
        '''Check if the board has a bias towards one side.
        
        Args:
            board (Board): The board to check.

        Returns:
            int: The bias of the board.
        '''
        value = 0
        for i in range(8):
            blank_count = 0
            column_bias = 0
            for j in range(8):
                cell = board.board[j][i]
                if cell == None:
                    blank_count += 1
                elif type(cell) in (Rook, Queen):
                    if cell.color == "w":
                        column_bias += 50
                    else:
                        column_bias -= 50
            if blank_count >= 7:
                value += column_bias
        return value
    
    def threat_bias(board:Board, turn_num:int) -> int:
        '''Check if the board has a bias towards one side.
        
        Args:
            board (Board): The board to check.
            turn_num (int): The turn number of the game.

        Returns:
            int: The bias of the board.
        '''
        if turn_num < 10:
            return 0
        def is_threatened(piece) -> bool:
            opponents = board.aimed_by(piece.i, piece.j, "w" if piece.color == "b" else "b")
            if len(opponents) == 0:
                return False
            opponent_point = sum([ChessEvaluator.PIECE_VALUES[type(piece)] for piece in opponents])
            allies = board.aimed_by(piece.i, piece.j, piece.color)
            ally_point = sum([ChessEvaluator.PIECE_VALUES[type(piece)] for piece in allies])
            return opponent_point > ally_point
        
        value = 0
        for piece in board.white_pieces:
            if is_threatened(piece):
                value -= 0.8 * ChessEvaluator.PIECE_VALUES[type(piece)]
        for piece in board.black_pieces:
            if is_threatened(piece):
                value += 0.8 * ChessEvaluator.PIECE_VALUES[type(piece)]
        return int(value)
    
    def evaluate(board:Board, turn_num:int) -> int:
        '''Evaluate the board based on the position of the pieces on the board.
        
        Args:
            board (Board): The board to evaluate.
            turn_num (int): The turn number of the game.

        Returns:
            int: The evaluation of the board.
        '''
        if board.match_result() == 1:
            return 10000
        elif board.match_result() == 2:
            return -10000
        elif board.match_result() == 3:
            return 0
        # Add bias
        value = 0
        value += ChessEvaluator.check_bias(board)
        value += ChessEvaluator.piece_value_bias(board)
        value += ChessEvaluator.piece_square_value_bias(board, turn_num)
        value += ChessEvaluator.threat_bias(board, turn_num)
        return value




