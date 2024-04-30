from board import Board
from pieces import *
from evaluator import ChessEvaluator
import math
import random

class ChessBot:
    def __init__(self, level:int, color:str):
        self.level = level
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
     
    def _evaluate_move(self, board:Board, move:tuple[int,int,int,int]) -> int:
            board_copy = board.create_board_copy()
            board_copy.move(*move, "Q")
            return self.evaluate(board_copy, self.turn_num)

    def sort_moves(self, board:Board, moves:list[tuple[int,int,int,int]], ascending) -> list[tuple[int,int,int,int]]:
        return sorted(moves, key=lambda move: self._evaluate_move(board, move), reverse=not ascending)
    
    def _move_translate(self, move:tuple[int,int,int,int]) -> str:
        return f"{chr(move[1]+97)}{move[0]+1}{chr(move[3]+97)}{move[2]+1}"

    # Minimax with alpha-beta pruning
    def minimax(self, board:Board, depth:int, alpha:int, beta:int, maximizing:bool) -> tuple[int,tuple[int,int,int,int]]:
        '''Minimax algorithm with alpha-beta pruning. 

        Args:
            board (Board): The board to evaluate.
            depth (int): The depth of the search (typically 1-5).
            alpha (int): The alpha value.
            beta (int): The beta value.
            maximizing (bool): Whether the current player is maximizing or not.

        Returns:
            tuple[int,tuple[int,int,int,int]]: The best score and the best move.
        '''
        if depth == 0 or board.match_result() != 0:
            return self.evaluate(board, self.turn_num), None
        all_moves = board.get_all_moves("w" if maximizing else "b")
        if len(all_moves) == 0:
            return self.evaluate(board, self.turn_num), None
        if depth != self.level:
            all_moves = self.sort_moves(board, all_moves, not maximizing)[:2]
        best_score = -10000 if maximizing else 10000
        best_move = None
        for move in all_moves:
            board_copy = board.create_board_copy()
            board_copy.move(*move, "Q")
            self.turn_num += 1
            eval, _ = self.minimax(board_copy, depth - 1, alpha, beta, not maximizing)
            self.turn_num -= 1
            if depth==self.level:
                print(eval, str(board.board[move[0]][move[1]]), self._move_translate(move))
            if maximizing:
                if eval >= best_score:
                    best_score = eval
                    best_move = move
                alpha = max(alpha, eval)
            else:
                if eval <= best_score:
                    best_score = eval
                    best_move = move
                beta = min(beta, eval)
            if beta <= alpha:
                break
        return best_score, best_move
        
    def best_move(self, board:Board, turn_num:int) -> tuple[int,int,int,int]:
        '''Find the best move for the bot. The bot uses minimax with alpha-beta pruning.
        
        Args:
            board (Board): The board to evaluate.
            turn_num (int): The turn number of the game.
        
        Returns:
            tuple[int,int,int,int]: The best move for the bot.
        '''
        print(self.evaluate(board, turn_num))
        self.turn_num = turn_num
        score, move = self.minimax(board, self.level, -10000, 10000, self.color=="w")
        return move

        
