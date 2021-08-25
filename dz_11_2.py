class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input("Введите делитель для числа 100: ")

try:
    inp_data = float(inp_data)
    if inp_data == 0:
        raise OwnError("Вы ввели 0! На 0 делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {100 / inp_data}")
