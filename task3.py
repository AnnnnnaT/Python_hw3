# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

num_list = [round(uniform(1.0, 10.5), 2) for _ in range(randint(4, 10))]
fractional_part = []
for item in num_list:
    if isinstance(item, float):
        fractional_part.append(item % 1)
result = round(max(fractional_part) - min(fractional_part), 2)
print(f'Созданный список: {num_list}.\nРазница между максимальной и минимальной дробной частью: {result}')

dir(uniform)
dir(randint)