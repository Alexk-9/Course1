num = int(input('Введите число: '))

odd_nums = (n for n in range(1, num + 1, 2))

print(type(odd_nums))
print(*odd_nums)