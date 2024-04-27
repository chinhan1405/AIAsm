from kakurasu import Kakurasu
from copy import deepcopy

def kakurasu_depth_first_search(kakurasu: Kakurasu) -> bool:
    visited:list[Kakurasu] = []
    stack:list[Kakurasu] = []
    stack.append(kakurasu)
    while stack:
        current:Kakurasu = stack.pop()
        if current.check():
            print(current)
            return True
        visited.append(current)
        for i in range(current.get_dim())[::-1]:
            for j in range(current.get_dim())[::-1]:
                if not current.is_black(i, j):
                    new_kakurasu:Kakurasu = deepcopy(current)
                    new_kakurasu.set_black(i, j)
                    if new_kakurasu.valid() \
                    and new_kakurasu not in visited:
                        stack.append(new_kakurasu)
    return False

def kakurasu_dfs_step_by_step(kakurasu: Kakurasu) -> bool:
    # This function will print the current state of the kakurasu board at each step
    visited:list[Kakurasu] = []
    stack:list[Kakurasu] = []
    stack.append(kakurasu)
    while stack:
        current:Kakurasu = stack.pop()
        print(current)
        print()
        if current.check():
            return True
        visited.append(current)
        for i in range(current.get_dim())[::-1]:
            for j in range(current.get_dim())[::-1]:
                if not current.is_black(i, j):
                    new_kakurasu:Kakurasu = deepcopy(current)
                    new_kakurasu.set_black(i, j)
                    if new_kakurasu.valid() \
                    and new_kakurasu not in visited:
                        stack.append(new_kakurasu)
                        
    return False

if __name__ == "__main__":
    import time
    import tracemalloc
    INPUTFILE = "testcase/input3.txt"
    tracemalloc.start()
    start_time = time.time()

    kakurasu = Kakurasu(INPUTFILE)
    if kakurasu_dfs_step_by_step(kakurasu):
        print("Solved!")
    else:
        print("No solution!")

    print("--- Time consumed: %s seconds ---" % (time.time() - start_time))
    print("--- Memory used: %s bytes ---" % (tracemalloc.get_traced_memory()[1]))

    tracemalloc.stop()