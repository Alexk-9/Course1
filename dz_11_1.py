class Data:
    def __init__(self, str_data):
        self.str_data = str_data

    @classmethod
    def list_data(cls, str_data):
        t_data = [i for i in str_data.split('-')]
        return int(t_data[0]), int(t_data[1]), int(t_data[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= int(day) <= 31:
            if 1 <= int(month) <= 12:
                if 2021 >= int(year) >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


d = '09 - 02 - 1973'
d1 = Data(d)
print(Data.list_data(d))
print('09-02-1973', Data.valid('09', '02', '1973'))
print('0-12-1973', d1.valid('0', '12', '1973'))
print('09-13-1973', d1.valid(9, 13, 1973))
print('09-12-2973', d1.valid(9, 12, 2973))
print(d)
