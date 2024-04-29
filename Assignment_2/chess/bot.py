from board import Board
from pieces import *
from evaluator import ChessEvaluator

class ChessBot:
    def __init__(self, level:int, color:str):
        self.level = 1
        self.color = color
        self.opponent_color = "w" if color == "b" else "b"
        self.turn_num = 0
    
    def evaluate(self, board:Board, turn_num:int):
        '''Evaluate the board based on the position of the pieces on the board.
        
        Args:
            board (Board): The board to evaluate.
            turn_num (int): The turn number of the game.

        Returns:
            int: The evaluation of the board.
        '''
        return ChessEvaluator.evaluate(board, turn_num)
        
    def minimax(self, board:Board, depth:int, alpha:int, beta:int, maximizing:bool) -> int:
        if depth == 0 or board.match_result() != 0:
            return self.evaluate(board, self.turn_num)
        all_moves = board.get_all_moves("w" if maximizing else "b")
        if maximizing:
            max_eval = -10000
            for move in all_moves:
                board_copy = board.create_board_copy()
                board_copy.move(*move, "Q")
                eval = self.minimax(board_copy, depth - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = 10000
            for move in all_moves:
                board_copy = board.create_board_copy()
                board_copy.move(*move, "Q")
                eval = self.minimax(board_copy, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
        
    def best_move(self, board:Board, turn_num:int) -> tuple[int,int,int,int]:
        self.turn_num = turn_num
        all_moves = board.get_all_moves(self.color)
        if self.color == "w":
            best_move = all_moves[0]
            best_eval = -10000
            for move in all_moves:
                board_copy:Board = board.create_board_copy()
                board_copy.move(*move, "Q")
                eval = self.minimax(board_copy, self.level, -10000, 10000, False)
                if eval > best_eval:
                    best_eval = eval
                    best_move = move
            return best_move
        else:
            best_move = all_moves[0]
            best_eval = 10000
            for move in all_moves:
                board_copy:Board = board.create_board_copy()
                board_copy.move(*move, "Q")
                eval = self.minimax(board_copy, self.level, -10000, 10000, True)
                if eval < best_eval:
                    best_eval = eval
                    best_move = move
            return best_move


        