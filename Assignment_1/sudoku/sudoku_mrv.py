from sudoku import Sudoku

def available(sudoku: Sudoku, i: int, j: int) -> list:
    '''Return the available values for the square (i, j) in the board'''
    available = []
    for value in range(1, sudoku.get_dim() + 1):
        sudoku.set(i, j, value)
        if sudoku.valid():
            available.append(value)
        sudoku.set(i, j, 0)
    return available

def get_best_square(sudoku: Sudoku) -> tuple:
    '''Return the square with the minimum number of available values'''
    min_len = sudoku.get_dim() * 3
    min_i = -1
    min_j = -1
    for i in range(sudoku.get_dim()):
        for j in range(sudoku.get_dim()):
            if sudoku.get(i, j) == 0:
                if len(available(sudoku, i, j)) < min_len:
                    min_len = len(available(sudoku, i, j))
                    min_i = i
                    min_j = j
    return (min_i, min_j)
                
def sudoku_minimum_remaining_values(sudoku: Sudoku) -> bool:
    if sudoku.check():
        print(sudoku)
        return True
    min_i, min_j = get_best_square(sudoku)
    if min_i == -1 and min_j == -1:
        return False
    for value in available(sudoku, min_i, min_j):
        sudoku.set(min_i, min_j, value)
        if sudoku_minimum_remaining_values(sudoku):
            return True
        sudoku.set(min_i, min_j, 0)
    return False

def sudoku_mrv_step_by_step(sudoku: Sudoku) -> bool:
    # This function will print the current state of the sudoku board at each step
    if sudoku.check():
        return True
    min_i, min_j = get_best_square(sudoku)
    if min_i == -1 and min_j == -1:
        return False
    for value in available(sudoku, min_i, min_j):
        sudoku.set(min_i, min_j, value)
        print(sudoku)
        if sudoku_mrv_step_by_step(sudoku):
            return True
        sudoku.set(min_i, min_j, 0)
    return False


if __name__ == "__main__":
    import time
    import tracemalloc
    INPUT_FILE = "testcase/input2.txt"
    tracemalloc.start()
    start_time = time.time() # Start timer

    sudoku = Sudoku(INPUT_FILE)
    if sudoku_minimum_remaining_values(sudoku):
        print("Solved!")
    else:
        print("No solution!")

    print("--- Time consumed: %s seconds ---" % (time.time() - start_time))
    print("--- Memory used: ", tracemalloc.get_traced_memory(), " ---")

    tracemalloc.stop()

