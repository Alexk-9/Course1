class Store:
    store_full = []

    @staticmethod
    def actions_on_store():
        print("Программа учёта оргтехники на складе")
        try:
            while True:
                while True:
                    choice = input('Выберите действие:\n1 - просмотр содержимого склада\n2 - добавить на склад'
                                   '\n3 - удалить со склада\n4 - выйти из программы\n-->')
                    try:
                        choice = int(choice)
                        break
                    except ValueError:
                        print("Неверный ввод")

                if choice == 1:
                    Store.enum_list(Store.store_full)
                elif choice == 2:
                    try:
                        n_val = input('Введите название оборудования')
                        c_val = int(input('Введите количество'))
                        p_val = int(input('Введите цену за единицу'))
                        _val = int(input('Выберите тип добавляемого оборудования:\n 1 - Принтер\n 2 - Сканер\n'
                                         ' 3 - Ксерокс\n-->'))
                        if _val == 1:
                            t_val = 'Printer'
                            item = Printer(_type=t_val, name=n_val, col=c_val, price=p_val)
                        elif _val == 2:
                            t_val = 'Scanner'
                            item = Scanner(_type=t_val, name=n_val, col=c_val, price=p_val)
                        elif _val == 3:
                            t_val = 'Xerox'
                            item = Xerox(_type=t_val, name=n_val, col=c_val, price=p_val)
                        else:
                            print('Неверный выбор')
                            break
                        Store.add_base(item)
                    except ValueError as err:
                        print('Не корректные данные', err)
                elif choice == 3:
                    try:
                        print('Выберите номер записи для корректировки\n'
                              'При введении 0-го значения "Количество" объект будет удалён')
                        Store.enum_list(Store.store_full)
                        choice_cor = int(input('-->'))
                        choice_col = int(input('Введите новое значение количества -->'))
                        Store.store_full[choice_cor].col = choice_col
                    except ValueError as err:
                        print('Не корректный выбор', err)
                elif choice == 4:
                    Store.enum_list(Store.store_full)
                    break

                for i in range(len(Store.store_full)):
                    if Store.store_full[i].col == 0:
                        del Store.store_full[i]
                        break

        except ValueError:
            print('Incorrect input')

    @staticmethod
    def enum_list(_list):
        for i in range(len(_list)):
            print(f'{i} {_list[i]}')

    def add_base(self):
        Store.store_full.append(self)


class OrgTech(Store):
    def __init__(self, _type, name, col, price):
        self.name = name
        self.col = col
        self.price = price

    def __str__(self):
        _type = ""
        return f'Название: {self.name}, Количество: {int(self.col)}, Цена: {int(self.price)}'


class Printer(OrgTech):
    # def print_col(self):
    #    return f'Ёмкость картриджа - {self.prn} страниц'

    def __str__(self):
        _type = "Printer"
        return f'Тип: {_type}, Название: {self.name}, Количество: {int(self.col)}, Цена: {int(self.price)}'

    def prn_add(self):
        return Store.add_base(self)


class Scanner(OrgTech):
    # def scan_rez(self):
    #    return f'Разрешение сканирования - {self.scan}dpi'

    def __str__(self):
        _type = "Scanner"
        return f'Тип: {_type}, Название: {self.name}, Количество: {int(self.col)}, Цена: {int(self.price)}'

    def scan_add(self):
        return Store.add_base(self)


class Xerox(OrgTech):
    # def xerox_col(self):
    #   return f'Колличесво копий - {self.copy}'

    def __str__(self):
        _type = "Xerox"
        return f'Тип: {_type}, Название: {self.name}, Количество: {int(self.col)}, Цена: {int(self.price)}'

    def xerox_add(self):
        return Store.add_base(self)


d = Store()
s = Scanner(Scanner, 'Hp ScanJet 600', 88, 850)
p = Printer(Printer, 'Hp LaserJet 1100', 55, 1200)
x = Xerox(Xerox, 'Canon iR 1600', 34, 1500)
p.add_base()
s.add_base()
x.add_base()

d.actions_on_store()
