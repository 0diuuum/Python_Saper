import random


class Dic_Board:
    # Wersja wykorzystujaca slownik (dictionary)
    def __init__(self, x, y, mine):
        self.__rows = x
        self.__cols = y
        self.__numMines = mine
        self.__make_array(self.__rows, self.__cols)
        self.__set_Mine()
        self.__set_Num()
        self.__numOpened = 0
        self.gameover = False
        self.pause = False

    def __make_array(self, x, y):
        # Tworzy tablice 2D w formacie slownika {'hide': (int), 'show': (int), 'checked': (bool)}
        self.__mine_Array = [[{'hide': 0, 'show': 10, 'checked': False} for col in range(y)] for row in range(x)]

    def get_cell(self, x, y, key):
        return self.__mine_Array[x][y].get(key)

    def get_row(self):
        return self.__rows

    def get_col(self):
        return self.__cols

    def set_cell(self, x, y, key, s):
        self.__mine_Array[x][y][key] = s

    def __get_RandNum(self, r_min, r_max):
        return random.randint(r_min, r_max)

    def get_numMines(self):
        return self.__numMines

    def __set_Mine(self):
        placed_mines = set()
        while len(placed_mines) < self.get_numMines():
            x = self.__get_RandNum(0, self.get_row()-1)
            y = self.__get_RandNum(0, self.get_col()-1)
            
            if (x, y) not in placed_mines:
                self.set_cell(x, y, 'hide', 9)
                placed_mines.add((x, y))

    def __set_Num(self):
        for i in range(self.get_row()):
            for j in range(self.get_col()):
                if self.get_cell(i, j, 'hide') != 9:
                    n = 0
                    for i2 in range(i-1, i+2):
                        for j2 in range(j-1, j+2):
                            if (i2 == i and j2 == j) or i2 < 0 or j2 < 0 or i2 >= self.get_row() or j2 >= self.get_col():
                                continue
                            elif self.get_cell(i2, j2, 'hide') == 9:
                                n += 1
                    self.set_cell(i, j, 'hide', n)

    def open(self, x, y):
        if 0 <= x < self.get_row() and 0 <= y < self.get_col() and not(self.get_cell(x, y, 'checked')):
            copy = self.get_cell(x, y, 'hide')
            if copy == 9:
                self.set_cell(x, y, 'show', copy)
                self.set_cell(x, y, 'checked', True)
                self.GameOver()
            elif copy == 0:
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        if (i == x and j == y) or i < 0 or j < 0 or i >= self.get_row() or j >= self.get_col():
                            continue
                        # Wywolanie rekurencyjne
                        self.set_cell(x, y, 'show', copy)
                        self.set_cell(x, y, 'checked', True)
                        self.open(i, j)
            else:
                self.set_cell(x, y, 'show', copy)
                self.set_cell(x, y, 'checked', True)
            # Zwieksza liczbe odkrytych pol
            self.__numOpened += 1
            # Warunek zwyciestwa
            if (self.get_row() * self.get_col() - self.__numOpened) == self.__numMines:
                self.GameClear()

    def GameOver(self):
        self.gameover = True
        self.pause = True
        print("Przegrana!")

    def GameClear(self):
        self.pause = True
        print("Zwyciestwo!")
        # Zwyciestwo

