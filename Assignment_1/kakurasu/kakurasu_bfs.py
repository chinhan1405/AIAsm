from priority_queue import PriorityQueue
import os
from copy import deepcopy
from kakurasu import Kakurasu

# def available_combinations(max_value, target) -> list:
#     ret = []
#     for i in range(1 << max_value):
#         combination = []
#         for j in range(max_value):
#             if i & (1 << j):
#                 combination.append(j + 1)
#         if sum(combination) == target:
#             ret.append(combination)
#     return ret

def available_combinations(values: list, target: int) -> list:
    ret = []
    for i in range(1 << len(values)):
        combination = []
        for j in range(len(values)):
            if i & (1 << j):
                combination.append(values[j])
        if sum(combination) == target:
            ret.append(combination)
    return ret

def solve_kakurasu(kakurasu: Kakurasu) -> bool:
    if kakurasu.check():
        print(kakurasu)
        return True
    for i in range(kakurasu.get_dim()):
        for combine in available_combinations(range(kakurasu.get_dim()), kakurasu.get_row_goal(i)):
            new_kakurasu = deepcopy(kakurasu)
            for j in combine:
                new_kakurasu.set_black(i, j)
            if new_kakurasu.valid():
                if solve_kakurasu(new_kakurasu):
                    return True
    return False

def heuristic(kakurasu: Kakurasu) -> int:
    past_cost = kakurasu.count_black()
    sum = 0
    for i in range(kakurasu.get_dim()):
        row_remaining_target = kakurasu.get_row_goal(i) - kakurasu.get_row_sum(i)
        row_remaining_cells = [j for j in range(kakurasu.get_dim()) if not kakurasu.is_black(i, j)]
        sum += len(available_combinations(row_remaining_cells, row_remaining_target))
        col_remaining_target = kakurasu.get_col_goal(i) - kakurasu.get_col_sum(i)
        col_remaining_cells = [j for j in range(kakurasu.get_dim()) if not kakurasu.is_black(j, i)]
        sum += len(available_combinations(col_remaining_cells, col_remaining_target))
    return past_cost + sum

def contain(l: list, k: Kakurasu) -> bool:
    for kakurasu in l:
        if kakurasu == k:
            return True
    return False

def kakurasu_best_first_search(kakurasu: Kakurasu):
    open = PriorityQueue() # [(heuristic, kakurasu)]
    open.push((heuristic(kakurasu), kakurasu))
    close = []
    while not open.is_empty():
        current: Kakurasu = open.pop()[1]
        if current.check():
            print(current)
            return True
        for i in range(current.get_dim()):
            for j in range(current.get_dim()):
                if not current.is_black(i, j):
                    new_kakurasu = deepcopy(current)
                    new_kakurasu.set_black(i, j)
                    if new_kakurasu.valid() and not contain(close, new_kakurasu):
                        open.push((heuristic(new_kakurasu), new_kakurasu))
        close.append(current)
    return False

def kakurasu_bfs_step_by_step(kakurasu: Kakurasu):
    open = PriorityQueue()
    open.push((heuristic(kakurasu), kakurasu))
    close = []
    while not open.is_empty():
        current = open.pop()[1]
        os.system('cls')
        print(current)
        print()
        if current.check():
            return True
        for i in range(current.get_dim()):
            for j in range(current.get_dim()):
                if not current.is_black(i, j):
                    new_kakurasu = deepcopy(current)
                    new_kakurasu.set_black(i, j)
                    if new_kakurasu.valid() and not contain(close, new_kakurasu):
                        open.push((heuristic(new_kakurasu), new_kakurasu))
        close.append(current)
    return False



if __name__ == "__main__":
    import time
    INPUTFILE = "testcase/input5.txt"
    start_time = time.time() # Start timer
    kakurasu = Kakurasu(INPUTFILE)
    kakurasu_bfs_step_by_step(kakurasu)
    print("--- %s seconds ---" % (time.time() - start_time))

#  1  1  0  0  0  0  3
#  0  1  0  0  1  0  7
#  0  0  0  1  1  0  9
#  0  0  0  0  1  1 11
#  0  0  1  0  0  0  3
#  0  1  1  0  0  0  5
#  1  9 11  3  9  4