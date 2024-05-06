import sys
from game import ChessGame

if sys.argv[1] == 'play':
    game = ChessGame()
    print(game.game_start())
elif sys.argv[1] == 'sim' and len(sys.argv) > 2:
    if len(sys.argv) == 3:
        game = ChessGame()
        print(game.simulate_game(int(sys.argv[2]), 0))
    elif len(sys.argv) == 4:
        if sys.argv[3] == 'white':
            game = ChessGame()
            print(game.simulate_game(int(sys.argv[2]), 2))
        elif sys.argv[3] == 'black':
            game = ChessGame()
            print(game.simulate_game(int(sys.argv[2]), 1))
else:
    print("Invalid arguments")
    print("Usage: python chess.py play")
    print("Usage: python chess.py sim <level>")
    print("Usage: python chess.py sim <level> white")
    print("Usage: python chess.py sim <level> black")
        