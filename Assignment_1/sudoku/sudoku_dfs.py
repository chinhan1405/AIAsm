from sudoku import Sudoku
from copy import deepcopy

def sudoku_depth_first_search(sudoku: Sudoku) -> bool:
    visited = []
    stack = []
    stack.append(sudoku)
    while stack:
        current = stack.pop()
        if current.check():
            print(current)
            return True
        visited.append(current)
        for i in range(current.get_dim()):
            for j in range(current.get_dim()):
                if current.get(i, j) == 0:
                    for value in range(current.get_dim()):
                        new_sudoku:Sudoku = deepcopy(current)
                        new_sudoku.set(i, j, value+1)
                        if new_sudoku.valid() \
                        and new_sudoku not in visited:
                            stack.append(new_sudoku)
    return False

def sudoku_dfs_step_by_step(sudoku: Sudoku) -> bool:
    # This function will print the current state of the sudoku board at each step
    visited = []
    stack = []
    stack.append(sudoku)
    while stack:
        current:Sudoku = stack.pop()
        if current.check():
            print(current)
            return True
        visited.append(current)
        for i in range(current.get_dim()):
            for j in range(current.get_dim()):
                if current.get(i, j) == 0:
                    for value in range(current.get_dim()):
                        new_sudoku: Sudoku = deepcopy(current)
                        new_sudoku.set(i, j, value+1)
                        if new_sudoku.valid() \
                        and new_sudoku not in visited:
                            stack.append(new_sudoku)
                            print(new_sudoku)
    return False


if __name__ == "__main__":
    import time
    INPUT_FILE = "testcase/input1.txt"
    import tracemalloc
    tracemalloc.start()
    start_time = time.time()

    sudoku = Sudoku(INPUT_FILE)
    sudoku_depth_first_search(sudoku)

    print("--- %s seconds ---" % (time.time() - start_time))
    print("Memory used: ", tracemalloc.get_traced_memory())
    
    tracemalloc.stop()