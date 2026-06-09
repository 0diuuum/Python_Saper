import Board
import random


class Mine_Board(Board.Board):

    def __init__(self, x, y, mine):
        # Przeciazenie konstruktora
        super().__init__(x, y)
        self.__numMines = mine
        self.__set_Mine()
        self.__set_Num()

    def __set_Mine(self):
        placed_mines = set()
        while len(placed_mines) < self.get_numMines():
            x = random.randint(0, self.get_row()-1)
            y = random.randint(0, self.get_col()-1)
            
            if (x, y) not in placed_mines:
                self.set_cell(x, y, 9)
                placed_mines.add((x, y))



    def __set_Num(self):
        for i in range(self.get_row()):
            for j in range(self.get_col()):
                if self.get_cell(i, j) != 9:
                    n = 0
                    for i2 in range(max(i-1, 0),  min(i+1, self.get_row() - 1) + 1):
                        for j2 in range(max(j-1, 0),  min(j+1, self.get_col() - 1) + 1):
                            if (i2 == i and j2 == j):
                                continue
                            elif self.get_cell(i2, j2) == 9:
                                n += 1
                    self.set_cell(i, j, n)

    def __get_RandNum(self, r_min, r_max):
        return random.randint(r_min, r_max)

    def get_numMines(self):
        return self.__numMines



