# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

a = int(input('Введите количество чисел в списке: '))
nums = []

for item in range(1, a+1):
    nums.append(int(input()))
print (nums)

sum = 0
for i in range(len(nums)):
    if i%2!=0:
       sum+=nums[i]
print(sum)


