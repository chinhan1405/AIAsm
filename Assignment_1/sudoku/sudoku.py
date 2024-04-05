from math import sqrt

class Sudoku:
    def __init__(self, input_file) -> None:
        f = open(input_file, "r")
        self.dim = int(f.readline())
        self.board = [[int(x) for x in line.split(" ")] for line in f.readlines()]
        f.close()

    def get_dim(self):
        return self.dim

    def get(self, i, j) -> int:
        return self.board[i][j]
    
    def set(self, i, j, value):
        self.board[i][j] = value

    def get_row(self, i) -> list:
        return self.board[i]
    
    def get_col(self, j) -> list:
        return [row[j] for row in self.board]
    
    def get_box(self, i, j) -> list:
        box = []
        dim = int(sqrt(self.dim))
        i = i // dim * dim
        j = j // dim * dim
        for x in range(i, i + dim):
            for y in range(j, j + dim):
                box.append(self.get(x, y))
        return box
    
    def valid(self):
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
    
    def check(self):
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
    sudoku = Sudoku("input1.txt")
    print(sudoku)