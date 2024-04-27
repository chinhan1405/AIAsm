from kakurasu import Kakurasu
from copy import deepcopy
import math

def get_combinations(elems:list[int], sum:int) -> list[list[int]]:
    '''Get all possible combinations of elements in elems that sum up to sum'''
    def backtrack(start:int, path:list[int], target:int):
        if target == 0:
            res.append(path)
            return
        for i in range(start, len(elems)):
            if elems[i] > target:
                break
            backtrack(i + 1, path + [elems[i]], target - elems[i])
    res:list[list[int]] = []
    backtrack(0, [], sum)
    return res

def set_row_black_from_combination(kakurasu:Kakurasu, comb:list[int], row:int) -> Kakurasu:
    '''Set the cells in row to black based on the combination of numbers in comb'''
    for num in comb:
        kakurasu.set_black(row, num - 1)
    return kakurasu

def clear_row(kakurasu:Kakurasu, row:int) -> Kakurasu:
    '''Clear the row by setting all cells to white'''
    for i in range(kakurasu.get_dim()):
        kakurasu.set_white(row, i)
    return kakurasu

def get_promised_solutions(kakurasu:Kakurasu) -> bool:
    '''Get all possible combinations of numbers that sum up to the row goal for each row'''
    solutions:list[list[list[int]]] = []
    for i in range(kakurasu.get_dim()):
        solutions.append([])
        row_combinations = get_combinations(range(1, kakurasu.get_dim() + 1), kakurasu.get_row_goal(i))
        for comb in row_combinations:
            set_row_black_from_combination(kakurasu, comb, i)
            if kakurasu.valid():
                solutions[i].append(comb)
            clear_row(kakurasu, i)
    return solutions

def kakurasu_depth_first_search(kakurasu:Kakurasu) -> bool:
    solutions = get_promised_solutions(kakurasu)
    stack:list[Kakurasu] = []
    visited:list[Kakurasu] = []
    stack.append(kakurasu)
    while stack:
        current:Kakurasu = stack.pop()
        if current.check():
            print(current)
            return True
        visited.append(current)
        for i in range(current.get_dim())[::-1]:
            for comb in solutions[i]:
                new_kakurasu:Kakurasu = deepcopy(current)
                set_row_black_from_combination(new_kakurasu, comb, i)
                if new_kakurasu.valid() \
                and new_kakurasu not in visited:
                    stack.append(new_kakurasu)
    return False

def kakurasu_dfs_step_by_step(kakurasu:Kakurasu) -> bool:
    '''This function will print the current state of the kakurasu board at each step'''
    solutions = get_promised_solutions(kakurasu)
    stack:list[Kakurasu] = []
    visited:list[Kakurasu] = []
    stack.append(kakurasu)
    while stack:
        current:Kakurasu = stack.pop()
        print(current)
        print()
        if current.check():
            return True
        visited.append(current)
        for i in range(current.get_dim())[::-1]:
            for comb in solutions[i]:
                new_kakurasu:Kakurasu = deepcopy(current)
                set_row_black_from_combination(new_kakurasu, comb, i)
                if new_kakurasu.valid() \
                and new_kakurasu not in visited:
                    stack.append(new_kakurasu)
    return False


if __name__ == '__main__':
    import time
    import tracemalloc
    INPUT_FILE = "testcase/input3.txt"
    tracemalloc.start()
    start_time = time.time()
    
    kakurasu = Kakurasu(INPUT_FILE)
    print(get_promised_solutions(kakurasu))
    if kakurasu_dfs_step_by_step(kakurasu):
        print("Solved!")
    else:
        print("No solution!")

    print("--- Time consumed: %s seconds ---" % (time.time() - start_time))
    print("--- Memory used: %s bytes ---" % (tracemalloc.get_traced_memory()[1]))

    tracemalloc.stop()