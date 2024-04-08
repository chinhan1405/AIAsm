from kakurasu import Kakurasu
import os

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

def copy_kakurasu(values: list, kakurasu: Kakurasu):
    for i in range(len(values)):
        for j in values[i]:
            kakurasu.set_black(i, j-1)
    print(kakurasu)

def get_best_row(kakurasu: Kakurasu):
    min_row_index = 0
    min_remaining = len(available_combinations(kakurasu.get_dim(), kakurasu.get_row_goal(0)))
    for i in range(kakurasu.get_dim()):
        remaining = len(available_combinations(kakurasu.get_dim(), kakurasu.get_row_goal(i)))
        if remaining < min_remaining:
            min_remaining = remaining
            min_row_index = i
    return min_row_index
            


def kakurasu_minimum_remaining_values(kakurasu: Kakurasu):
    combines = []
    for i in range(kakurasu.get_dim()):
        combines.append(available_combinations(range(kakurasu.get_dim()), kakurasu.get_row_goal(i)))
    curr = []
    for i in range(kakurasu.get_dim()):
        for j in range(len(combines[i])):
            curr.append(combines[i][j])
            if i == kakurasu.get_dim()-1:
                copy_kakurasu(curr, kakurasu)
                print(kakurasu)
                kakurasu.clear()
            curr.pop()

if __name__ == "__main__":
    import time
    INPUTFILE = "testcase/input5.txt"
    start_time = time.time() # Start timer
    kakurasu = Kakurasu(INPUTFILE)
    kakurasu_minimum_remaining_values(kakurasu)
    print("--- %s seconds ---" % (time.time() - start_time))