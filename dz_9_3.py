class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        gfn = f'{self.name} {self.surname}'
        return gfn

    def get_total_income(self):
        tot_inc = f'{sum(self._income.values())}'
        return tot_inc


gendir = Position('Duratan', 'Ork', 'Директор', 200000, 50000)
dr = Position('Hannibal', 'Lecter', 'Доктор', 100000, 30000)
print(gendir.get_full_name(), gendir.position, gendir.get_total_income())
print(dr.get_full_name(), dr.position, dr.get_total_income())