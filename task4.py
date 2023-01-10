# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input('Введите число: '))

res = []
while n:
    a = n % 2
    res.append(a)
    n//= 2

res.reverse()
print(*res,  sep='')