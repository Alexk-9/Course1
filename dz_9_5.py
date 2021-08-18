class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        return print(f'Отрисовка ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        return print(f'Отрисовка {self.title} карандашом')


class Handle(Stationery):
    def draw(self):
        return print(f'Отрисовка {self.title} фломастером')


draw = Stationery('начали:')
draw.draw()

draw_pen = Pen('Parker')
draw_pen.draw()

print()
draw_pencil = Pencil('простым')
draw_pencil.draw()

print()
draw_handle = Handle('чёрным')
draw_handle.draw()