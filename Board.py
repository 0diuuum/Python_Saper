class Board:
    # Python domyślnie udostępnia wszystko jako publiczne; nie zapewnia kontroli dostępu.
    # Konwencja nazewnictwa określa dostęp: prywatne: __name, chronione: _name
    def __init__(self, x, y):
        self.__rows = x
        self.__cols = y
        self.__make_array(self.__rows, self.__cols)

    def get_cell(self, x, y):
        return self.__mine_Array[x][y]

    def get_row(self):
        return self.__rows

    def get_col(self):
        return self.__cols

    def set_cell(self, x, y, s):
        self.__mine_Array[x][y] = s

    def __make_array(self, x, y):
        # Tworzy dynamiczną tablicę 2D i inicjalizuje jej wartości zerami
        self.__mine_Array = [[0 for col in range(y)] for row in range(x)]

