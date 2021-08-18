import random


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return print(f'{self.name} поехала со скоростью {self.speed} км/ч')

    def go(self):
        return print(f'{self.name} поехала')

    def stop(self):
        return print(f'{self.name} остановилась')

    def turn(self):
        turn = random.randint(0, 1)
        if turn == 0:
            turn = 'лево'
        else:
            turn = 'право'
        return print(f'{self.name} повернула на {turn}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} поехала со скоростью {self.speed} "км/ч". ' \
                   f'! WARNING ! скорость превышена на {self.speed - 60} км/ч'
        else:
            return f'{self.name}  поехала со скоростью {self.speed}'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} поехала со скоростью {self.speed} "км/ч". ' \
                   f'! WARNING ! скорость превышена на {self.speed - 40} км/ч'
        else:
            return f'{self.name} поехала со скоростью {self.speed} км/ч'

class PoliceCar(Car):
    def __init__(self, name, color='белый с синей полосой', speed=100, is_police=True):
        super().__init__(name, color, speed, is_police)

class SportCar(Car):
    pass

t_car = TownCar('Лада седан', 'баклажан', 80)
t_car.go()
t_car.turn()
print(t_car.show_speed())
t_car.stop()
print(f'{t_car.name} - {t_car.color}')

print()
w_car = WorkCar('Газель', 'синий', 50)
w_car.go()
w_car.turn()
print(w_car.show_speed())
w_car.stop()
print(f'{w_car.name} - {w_car.color}')

print()
p_car = PoliceCar('Полицейскмй УАЗик')
p_car.go()
p_car.turn()
p_car.show_speed()
p_car.stop()
print(f'{p_car.name} - {p_car.color}')

print()
s_car = SportCar('Бугатти', 'серебристый металлик', 250)
s_car.go()
s_car.turn()
s_car.turn()
s_car.show_speed()
s_car.stop()
print(f'{s_car.name} - {s_car.color}')