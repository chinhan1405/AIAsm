from math import sqrt

class Sudoku:
    def __init__(self, input_file) -> None:
        '''Initialize the Sudoku board from the input file'''
        f = open(input_file, "r")
        self.dim = int(f.readline())
        self.board = [[int(x) for x in line.split(" ")] for line in f.readlines()]
        f.close()

    def get_dim(self) -> int:
        '''Return the dimension of the board'''
        return self.dim

    def get(self, i:int, j:int) -> int:
        '''Return the value at position (i, j)'''
        return self.board[i][j]
    
    def set(self, i:int, j:int, value:int) -> None:
        '''Set the value at position (i, j)'''
        self.board[i][j] = value

    def get_row(self, i:int) -> list:
        '''Return the i-th row of the board'''
        return self.board[i]
    
    def get_col(self, j:int) -> list:
        '''Return the j-th column of the board'''
        return [row[j] for row in self.board]
    
    def get_box(self, i:int, j:int) -> list:
        '''Return the box that contains the position (i, j)'''
        box = []
        dim = int(sqrt(self.dim))
        i = i // dim * dim
        j = j // dim * dim
        for x in range(i, i + dim):
            for y in range(j, j + dim):
                box.append(self.get(x, y))
        return box
    
    def valid(self) -> bool:
        '''Check if the board is valid (not violate the Sudoku rules)'''
        for i in range(self.dim):
            for j in range(self.dim):
                if self.get(i, j) != 0:
                    if self.get_row(i).count(self.get(i, j)) > 1:
                        return False
                    if self.get_col(j).count(self.get(i, j)) > 1:
                        return False
                    if self.get_box(i, j).count(self.get(i, j)) > 1:
                        return False
        return True
    
    def check(self) -> bool:
        '''Check if the board is a valid solution'''
        sum_ = self.dim * (self.dim + 1) // 2
        for i in range(self.dim):
            if sum(self.get_row(i)) != sum_:
                return False
            if sum(self.get_col(i)) != sum_:
                return False
        for i in range(0, self.dim, int(sqrt(self.dim))):
            for j in range(0, self.dim, int(sqrt(self.dim))):
                if sum(self.get_box(i, j)) != sum_:
                    return False
        return True

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Sudoku):
            return False
        return self.board == __value.board

    def __str__(self) -> str:
        out = ""
        for i in self.board:
            for j in i:
                out += str(j) + " "
            out += "\n"
        return out
    

if __name__ == "__main__":
    # Test the Sudoku class
    sudoku = Sudoku("testcase/input1.txt")
    print(sudoku)