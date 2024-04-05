class Kakurasu:
    def __init__(self, input_file) -> None:
        f = open(input_file, "r")
        self.dim = int(f.readline())
        self.rows = [int(x) for x in f.readline().split(" ")]
        self.cols = [int(x) for x in f.readline().split(" ")]
        f.close()
        self.table = [[0 for i in range(self.dim)] for j in range(self.dim)]

    def get_dim(self):
        return self.dim
    
    def get_rows_goal(self, i=None):
        if i is None:
            return self.rows
        return self.rows[i]
    
    def get_cols_goal(self, j=None):
        if j is None:
            return self.cols
        return self.cols[j]
    
    def get_rows(self, i):
        return self.table[i]
    
    def get_cols(self, j):
        return [row[j] for row in self.table]

    def set_black(self, i, j):
        self.table[i][j] = 1

    def set_white(self, i, j):
        self.table[i][j] = 0

    def is_black(self, i, j):
        return self.table[i][j] == 1
    
    def get_row_sum(self, i):
        return sum([cell*(j+1) for j, cell in enumerate(self.table[i])])
    
    def get_col_sum(self, j):
        return sum([cell*(i+1) for i, cell in enumerate([row[j] for row in self.table])])

    def check(self):
        for i in range(self.dim):
            if self.get_row_sum(i) != self.get_rows_goal(i):
                return False
            if self.get_col_sum(i) != self.get_cols_goal(i):
                return False
        return True
    
    def valid(self):
        for i in range(self.dim):
            if self.get_row_sum(i) > self.get_rows_goal(i):
                return False
            if self.get_col_sum(i) > self.get_cols_goal(i):
                return False
        return True

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
    

if __name__ == "__main__":
    k = Kakurasu("input.txt")
    print(k)    