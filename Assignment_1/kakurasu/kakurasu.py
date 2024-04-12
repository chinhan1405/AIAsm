class Kakurasu:
    def __init__(self, input_file) -> None:
        '''Initialize the Kakurasu board from the input file'''
        f = open(input_file, "r")
        self.dim = int(f.readline())
        self.rows = [int(x) for x in f.readline().split(" ")]
        self.cols = [int(x) for x in f.readline().split(" ")]
        f.close()
        self.table = [[0 for i in range(self.dim)] for j in range(self.dim)]

    def get_dim(self) -> int:
        '''Return the dimension of the board'''
        return self.dim
    
    def get_row_goal(self, i:int=None) -> int | list[int]:
        '''Return the goal of the i-th row
        If i is None, return all the goals of the rows'''
        if i is None:
            return self.rows
        return self.rows[i]
    
    def get_col_goal(self, j:int=None) -> int | list[int]:
        '''Return the goal of the j-th column
        If j is None, return all the goals of the columns'''
        if j is None:
            return self.cols
        return self.cols[j]
    
    def get_rows(self, i:int) -> list[int]:
        '''Return the i-th row of the board'''
        return self.table[i]
    
    def get_cols(self, j:int) -> list[int]:
        '''Return the j-th column of the board'''
        return [row[j] for row in self.table]

    def set_black(self, i:int, j:int) -> None:
        '''Set the cell at position (i, j) to black (value 1)'''
        self.table[i][j] = 1

    def set_white(self, i:int, j:int) -> None:
        '''Set the cell at position (i, j) to white (value 0)'''
        self.table[i][j] = 0

    def is_black(self, i:int, j:int) -> bool:
        '''Check if the cell at position (i, j) is black (value 1)'''
        return self.table[i][j] == 1
    
    def get_row_sum(self, i:int) -> int:
        '''Return the sum of the i-th row'''
        return sum([cell*(j+1) for j, cell in enumerate(self.table[i])])
    
    def get_col_sum(self, j:int) -> int:
        '''Return the sum of the j-th column'''
        return sum([cell*(i+1) for i, cell in enumerate([row[j] for row in self.table])])

    def count_black(self) -> int:
        '''Return the number of black cells in the board'''
        count = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if self.is_black(i, j):
                    count += 1
        return count

    def count_white(self) -> int:
        '''Return the number of white cells in the board'''
        return self.dim*self.dim - self.count_black()

    def check(self) -> bool:
        '''Check if the board is a valid solution'''
        for i in range(self.dim):
            if self.get_row_sum(i) != self.get_row_goal(i):
                return False
            if self.get_col_sum(i) != self.get_col_goal(i):
                return False
        return True
    
    def valid(self) -> bool:
        '''Check if the board is valid (not violate the Kakurasu rules)'''
        for i in range(self.dim):
            if self.get_row_sum(i) > self.get_row_goal(i):
                return False
            if self.get_col_sum(i) > self.get_col_goal(i):
                return False
        return True
    
    def clear(self) -> None:
        '''Clear the board'''
        for i in range(self.dim):
            for j in range(self.dim):
                self.set_white(i, j)

    def __str__(self) -> str:
        out = ""
        for i in range(self.dim):
            for j in range(self.dim):
                out += '{:>2}'.format(str(self.table[i][j])) + " "
            out += '{:>2}'.format(self.rows[i]) + "\n"
        for i in range(self.dim):
            out += '{:>2}'.format(self.cols[i]) + " "
        return out

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Kakurasu):
            return False
        return self.table == __value.table
    
    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Kakurasu):
            return False
        return self.count_black() < __value.count_black()
    

if __name__ == "__main__":
    # Test the Kakurasu class
    k = Kakurasu("testcase/input1.txt")
    print(k)    