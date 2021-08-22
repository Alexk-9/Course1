class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        i = self.num - other.num
        if i <= 0:
            print('Во второй клетке больше ячеек чем в первой')
            return
        else:
            return i

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __floordiv__(self, other):
        return Cell(self.num // other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    @staticmethod
    def make_order(cell, y):
        x = ''
        i = 0
        while i < cell.num:
            x += '*'
            i += 1
            if i % y == 0:
                x += '\n'

        return x


i_1 = Cell(33)
i_2 = Cell(13)
rez = Cell.make_order(i_1, 5)
print(rez)
rez = i_1 - i_2
print(rez)
