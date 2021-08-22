class Matrix:
    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.obj])

    @staticmethod
    def check_matrix_compatibility(m1, m2):
        if len(m1.obj) == 0 or len(m1.obj[0]) == 0 or len(m1.obj) != len(m2.obj):
            return False

        try:
            col = len(m1.obj[0])
            for i in range(len(m1.obj)):
                if len(m1.obj[i]) != col or len(m2.obj[i]) != col:
                    return False
        except IndexError:
            return False

        return True

    def __add__(self, other):
        if not Matrix.check_matrix_compatibility(self, other):
            return print("Invalid matrix size")

        rez_matr = [[int(self.obj[row][i]) + int(other.obj[row][i]) for i in range(len(self.obj[row]))]
                    for row in range(len(self.obj))]
        return Matrix(rez_matr)


matr_1 = [[1, 4, 7], [3, 45, 6], [13, 21, 1]]
matr_2 = [[6, 12, -7], [83, 2, 13], [-13, 11, 9]]

print(Matrix(matr_1) + Matrix(matr_2))
