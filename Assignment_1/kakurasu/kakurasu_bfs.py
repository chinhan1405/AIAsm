from priority_queue import PriorityQueue
import time
from copy import deepcopy
from kakurasu import Kakurasu
INPUTFILE = "input5.txt"

def heuristic(kakurasu: Kakurasu) -> int:
    sum = 0
    for i in range(kakurasu.get_dim()):
        sum += kakurasu.get_rows_goal(i) - kakurasu.get_row_sum(i)
        sum += kakurasu.get_cols_goal(i) - kakurasu.get_col_sum(i)
    return sum

def past_cost(kakurasu: Kakurasu) -> int:
    count = 0
    for i in range(kakurasu.get_dim()):
        for j in range(kakurasu.get_dim()):
            if kakurasu.is_black(i, j):
                count += 1
    return count

def contain(l: list, k: Kakurasu) -> bool:
    for kakurasu in l:
        if kakurasu == k:
            return True
    return False

def kakurasu_best_first_search(kakurasu: Kakurasu):
    open = PriorityQueue()
    open.push((heuristic(kakurasu), kakurasu))
    close = []
    while not open.is_empty():
        current = open.pop()[1]
        if current.check():
            print(current)
            return True
        for i in range(current.get_dim()):
            for j in range(current.get_dim()):
                if not current.is_black(i, j):
                    new_kakurasu = deepcopy(current)
                    new_kakurasu.set_black(i, j)
                    if new_kakurasu.valid() and not contain(close, new_kakurasu):
                        open.push((heuristic(new_kakurasu) + past_cost(new_kakurasu), new_kakurasu))
        close.append(current)
    return False

def kakurasu_bfs_step_by_step(kakurasu: Kakurasu):
    open = PriorityQueue()
    open.push((heuristic(kakurasu), kakurasu))
    close = []
    while not open.is_empty():
        current = open.pop()[1]
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
                        open.push((heuristic(new_kakurasu) + past_cost(new_kakurasu), new_kakurasu))
        close.append(current)
    return False



if __name__ == "__main__":
    start_time = time.time() # Start timer
    kakurasu = Kakurasu(INPUTFILE)
    kakurasu_best_first_search(kakurasu)
    print("--- %s seconds ---" % (time.time() - start_time))