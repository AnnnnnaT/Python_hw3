# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

my_list = []
list_size = int(input('Количество чисел в списке: '))

for i in range(list_size):
    n = random.uniform(0, 100) 
    n = round(n, 2)
    my_list.append(n)    
print(my_list)

res_list = []

for num in my_list:
    num = round(num%1,2)
    res_list.append(num)
print(f"{res_list} -> {round((max(res_list) - min(res_list)),2)}")
