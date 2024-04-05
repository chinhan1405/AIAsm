import time
from kakurasu import Kakurasu
INPUTFILE = "input6.txt"

def kakurasu_depth_first_search(kakurasu: Kakurasu):
    if kakurasu.check():
        print(kakurasu)
        return True
    for i in range(kakurasu.get_dim()):
        for j in range(kakurasu.get_dim()):
            if not kakurasu.is_black(i, j):
                kakurasu.set_black(i, j)
                if (kakurasu.valid()):
                    if kakurasu_depth_first_search(kakurasu):
                        return True
                kakurasu.set_white(i, j)
    return False

def kakurasu_dfs_step_by_step(kakurasu: Kakurasu):
    if kakurasu.check():
        return True
    for i in range(kakurasu.get_dim()):
        for j in range(kakurasu.get_dim()):
            if not kakurasu.is_black(i, j):
                kakurasu.set_black(i, j)
                print(kakurasu)
                print()
                if (kakurasu.get_row_sum(i) <= kakurasu.get_rows(i)) and (kakurasu.get_col_sum(j) <= kakurasu.get_cols(j)):
                    if kakurasu_dfs_step_by_step(kakurasu):
                        return True
                kakurasu.set_white(i, j)
    return False

if __name__ == "__main__":
    start_time = time.time() # Start timer
    kakurasu = Kakurasu(INPUTFILE)
    kakurasu_depth_first_search(kakurasu)
    print("--- %s seconds ---" % (time.time() - start_time))