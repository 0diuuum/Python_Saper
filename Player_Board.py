import Board


class Player_Board(Board.Board):

    def __init__(self, x, y, mine):
        # Przeciazenie konstruktora
        super(__class__, self).__init__(x, y)
        self.__init_Array(10)
        self.__numOpened = 0
        self.__numMines = mine
        self.gameover = False
        self.pause = False

    def __init_Array(self, k):
        for i in range(self.get_row()):
            for j in range(self.get_col()):
                self.set_cell(i, j, k)

    def open(self, x, y, b):
        if 0 <= x < self.get_row() and 0 <= y < self.get_col() and not(self.__is_checked(x, y)):
            copied = b.get_cell(x, y)
            if copied == 9:
                self.set_cell(x, y, copied)
                self.GameOver()
            elif copied == 0:
                for i in range(max(x-1, 0), min(x+1, self.get_col()-1) + 1):
                    for j in range(max(y-1, 0), min(y+1, self.get_row()-1) + 1):
                        if (i == x and j == y):
                            continue
                            # Wywolanie rekurencyjne
                        self.set_cell(x, y, copied)
                        self.open(i, j, b)
            else:
                self.set_cell(x, y, copied)
            # Zwieksza liczbe odkrytych pol
            self.__numOpened += 1
            # Warunek zwyciestwa
            if (self.get_row() * self.get_col() - self.__numOpened) == self.__numMines:
                self.GameClear()

    def __is_checked(self, x, y):
        checked = False
        if self.get_cell(x, y) != 10:
            checked = True
        return checked

    def GameOver(self):
        self.gameover = True
        self.pause = True
        print("Przegrana!")

    def GameClear(self):
        self.pause = True
        print("Zwyciestwo!")
        # Zwyciestwo

