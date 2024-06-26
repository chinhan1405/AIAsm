from kakurasu import Kakurasu
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

def get_best_row(kakurasu:Kakurasu, solutions:list[list[list[int]]]) -> int:
    '''Get the row with the least number of possible solutions'''
    min_solutions = math.inf
    best_row = -1
    for i in range(kakurasu.get_dim()):
        if kakurasu.get_row_sum(i) == 0:
            if len(solutions[i]) < min_solutions:
                min_solutions = len(solutions[i])
                best_row = i
    return best_row

def kakurasu_minimum_remaining_values(kakurasu: Kakurasu):
    solutions = get_promised_solutions(kakurasu)
    def backtrack(kakurasu: Kakurasu):
        if kakurasu.check():
            print(kakurasu)
            return True
        row = get_best_row(kakurasu, solutions)
        if row == -1:
            return False
        for comb in solutions[row]:
            set_row_black_from_combination(kakurasu, comb, row)
            if kakurasu.valid():
                if backtrack(kakurasu):
                    return True
            clear_row(kakurasu, row)
        return False
    return backtrack(kakurasu)

def kakurasu_mrv_step_by_step(kakurasu: Kakurasu) -> bool:
    '''This function will print the current state of the kakurasu board at each step'''
    solutions = get_promised_solutions(kakurasu)
    def backtrack(kakurasu: Kakurasu):
        if kakurasu.check():
            return True
        row = get_best_row(kakurasu, solutions)
        if row == -1:
            return False
        for comb in solutions[row]:
            set_row_black_from_combination(kakurasu, comb, row)
            print(kakurasu)
            print()
            if kakurasu.valid():
                if backtrack(kakurasu):
                    return True
            clear_row(kakurasu, row)
    return backtrack(kakurasu)
    

if __name__ == '__main__':
    import time
    import tracemalloc
    INPUT_FILE = "testcase/input7.txt"
    tracemalloc.start()
    start_time = time.time()
    
    kakurasu = Kakurasu(INPUT_FILE)
    print(get_promised_solutions(kakurasu))
    if kakurasu_mrv_step_by_step(kakurasu):
        print("Solved!")
    else:
        print("No solution!")

    print("--- Time consumed: %s seconds ---" % (time.time() - start_time))
    print("--- Memory used: %s bytes ---" % (tracemalloc.get_traced_memory()[1]))

    tracemalloc.stop()
