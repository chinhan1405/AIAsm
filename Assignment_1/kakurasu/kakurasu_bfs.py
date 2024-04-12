'''Depricated Solution'''

from kakurasu import Kakurasu
from copy import deepcopy
from queue import PriorityQueue

def heuristic(kakurasu: Kakurasu) -> int:
    not_completed = 0
    for i in range(kakurasu.get_dim()):
        not_completed += 0 if kakurasu.get_row_goal(i) == kakurasu.get_row_sum(i) else 1
        not_completed += 0 if kakurasu.get_col_goal(i) == kakurasu.get_col_sum(i) else 1
    constraint = 0
    for i in range(kakurasu.get_dim()):
        for j in range(kakurasu.get_dim()):
            if not kakurasu.is_black(i, j):
                kakurasu.set_black(i, j)
                if not kakurasu.valid():
                    constraint += 1
                kakurasu.set_white(i, j)
    return constraint + not_completed * kakurasu.get_dim()**3

def kakurasu_best_first_search(kakurasu: Kakurasu):
    open = PriorityQueue() # [(heuristic, kakurasu)]
    open.put((heuristic(kakurasu), kakurasu))
    close:list[Kakurasu] = []
    while open:
        current:Kakurasu = open.get()[1]
        if current.check():
            print(current)
            return True
        for i in range(current.get_dim()):
            for j in range(current.get_dim()):
                if not current.is_black(i, j):
                    new_kakurasu:Kakurasu = deepcopy(current)
                    new_kakurasu.set_black(i, j)
                    if new_kakurasu.valid() and \
                    new_kakurasu not in close:
                        open.put((heuristic(new_kakurasu), new_kakurasu))
        close.append(current)
    return False


if __name__ == "__main__":
    import time
    INPUTFILE = "testcase/input7.txt"
    start_time = time.time() # Start timer

    kakurasu = Kakurasu(INPUTFILE)
    if kakurasu_best_first_search(kakurasu):
        print("Solved!")
    else:
        print("No solution!")

    print("--- %s seconds ---" % (time.time() - start_time))