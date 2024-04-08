from sudoku import Sudoku

counter = 0

def available(sudoku: Sudoku, i: int, j: int) -> list:
    available = []
    for value in range(1, sudoku.get_dim() + 1):
        sudoku.set(i, j, value)
        if sudoku.valid():
            available.append(value)
        sudoku.set(i, j, 0)
    return available

def get_best_square(sudoku: Sudoku) -> tuple:
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
                

def sudoku_minimum_remaining_values(sudoku: Sudoku):
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

def sudoku_mrv_step_by_step(sudoku: Sudoku):
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
    INPUT_FILE = "testcase/input2.txt"
    start_time = time.time() # Start timer
    sudoku = Sudoku(INPUT_FILE)
    sudoku_minimum_remaining_values(sudoku)
    print("--- %s seconds ---" % (time.time() - start_time))
