from sudoku import Sudoku

def sudoku_depth_first_search(sudoku: Sudoku):
    if sudoku.check():
        print(sudoku)
        return True
    for i in range(sudoku.get_dim()):
        for j in range(sudoku.get_dim()):
            if sudoku.get(i, j) == 0:
                for value in range(1, 10):
                    sudoku.set(i, j, value)
                    if sudoku.valid():
                        if sudoku_depth_first_search(sudoku):
                            return True
                sudoku.set(i, j, 0)
    return False

def sudoku_dfs_step_by_step(sudoku: Sudoku):
    # This function will print the current state of the sudoku board at each step
    if sudoku.check():
        return True
    for i in range(sudoku.get_dim()):
        for j in range(sudoku.get_dim()):
            if sudoku.get(i, j) == 0:
                for value in range(1, sudoku.get_dim() + 1):
                    sudoku.set(i, j, value)
                    print(sudoku)
                    print()
                    if sudoku.valid():
                        if sudoku_dfs_step_by_step(sudoku):
                            return True
                sudoku.set(i, j, 0)
    return False

if __name__ == "__main__":
    import time
    INPUT_FILE = "testcase/input1.txt"
    start_time = time.time() # Start timer
    sudoku = Sudoku(INPUT_FILE)
    sudoku_depth_first_search(sudoku)
    print("--- %s seconds ---" % (time.time() - start_time))