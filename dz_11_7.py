class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - (self.b * other.b), self.b * other.a + (self.a * other.b))

    def __str__(self):
        t = ''
        if self.b < 0:
            t = '-'
        else:
            t = '+'
        return f' {self.a} {t} {abs(self.b)}*j'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(f'z1 ={z_1}')
print(f'z2 ={z_2}')
print(f'z1 + z2 ={z_1 + z_2}')
print(f'z1 * z2 ={z_1 * z_2}')
