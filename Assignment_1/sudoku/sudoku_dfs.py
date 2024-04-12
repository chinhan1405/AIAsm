from sudoku import Sudoku
from copy import deepcopy

def sudoku_depth_first_search(sudoku: Sudoku) -> bool:
    visited:list[Sudoku] = []
    stack:list[Sudoku] = []
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
                        new_sudoku:Sudoku = deepcopy(current)
                        new_sudoku.set(i, j, value+1)
                        if new_sudoku.valid() \
                        and new_sudoku not in visited:
                            stack.append(new_sudoku)
    return False

def sudoku_dfs_step_by_step(sudoku: Sudoku) -> bool:
    # This function will print the current state of the sudoku board at each step
    visited:list[Sudoku] = []
    stack:list[Sudoku] = []
    stack.append(sudoku)
    while stack:
        current:Sudoku = stack.pop()
        print(current)
        if current.check():
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
    return False


if __name__ == "__main__":
    import time
    INPUT_FILE = "testcase/input1.txt"
    import tracemalloc
    tracemalloc.start()
    start_time = time.time()

    sudoku = Sudoku(INPUT_FILE)
    print(sudoku)
    if sudoku_depth_first_search(sudoku):
        print("Solved!")
    else:
        print("No solution!")

    print("--- Time consumed: %s seconds ---" % (time.time() - start_time))
    print("--- Memory used: %s bytes ---" % (tracemalloc.get_traced_memory()[1]))
    
    tracemalloc.stop()