class OwnError(Exception):
    def __init__(self, *args):
        self.rez_list = []

    def val_input(self):
        while True:
            try:
                val = int(input('Введите значение и нажмите Enter: '))
                self.rez_list.append(val)
            except ValueError:
                print(f'Значение типа "строка" или "булево" не будет добавлено')
                next_try = input('Продолжим ввод? Y/N ')
                if next_try == 'Y' or next_try == 'y':
                    self.val_input()
                else:
                    print(f'Введённые значения - {self.rez_list}')
                break


d = OwnError()
d.val_input()
