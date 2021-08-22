from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def calc_cloth(self):
        pass


class Coat(Cloth):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 35:
            print('Слишком маленький размер, берём 35-ый')
            self._size = 35
        elif size > 60:
            print('Слишком большой размер, берём 60-ый')
            self._size = 60
        else:
            self._size = size

    @property
    def calc_cloth(self):
        return self._size / 6.5 + 0.5


class Suit(Cloth):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height < 135:
            print('Слишком маленький рост, берём 135 см')
            self._height = 135
        elif height > 260:
            print('Слишком большой рост, берём 260 см')
            self._height = 260
        else:
            self._height = height

    @property
    def calc_cloth(self):
        return 2 * self._height / 100 + 0.3


coat_1 = int(input('Введите размер пальто'))
d = Coat(coat_1)
print(f'Нв пальто вам потребуется {d.calc_cloth:.2f} метров ткани')
suit_1 = int(input('Введите рост в сантиметрах'))
f = Suit(suit_1)
print(f'Нв костюм вам потребуется {f.calc_cloth:.2f} метров ткани')
print(f'Общий расход ткани {d.calc_cloth + f.calc_cloth :.2f} метров')
