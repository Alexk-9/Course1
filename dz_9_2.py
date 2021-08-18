class Road:

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def count_asf(self, mass=25, depth=5):
        if self._length <=0 or self._width <= 0:
            raise ValueError('Значения не могут быть меньше или равны 0')
        rez = self._length * self._width * mass * depth / 1000
        return f'Масса асфальта {round(rez)} тонн'


while True:
    try:
        r = Road(int(input('Введите длину дороги: ')), int(input('Введите ширину дороги: ')))
        print(r.count_asf())
        break
    except ValueError as err:
        print(err, "Введите кооректные значения")
