def odd_num(n):
    for i in range(1, n + 1, 2):
        yield i


n = int(input('Введите число: '))
print(type(odd_num(n)))

odd_to_n = odd_num(n)

for i in odd_to_n:
    print(i)