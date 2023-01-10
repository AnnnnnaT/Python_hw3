# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

# def fin (n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fin(n-1) + fin(n-2)
        
a = int(input('Введите число: '))

fib_res = []
fib2_list = []
fib_list = [0,1]


for i in range(a-1):
    fib_list[i]= fib_list[i-2] + fib_list[i-1] 
    fib_list.append(fib_list[i])
    # fib2_list[i] = fib2_list[i+1]- fib2_list[i+2] 
    # fib2_list.append(fib2_list[i])

print(fib_list)  
# print(fib2_list)

# for item in range ()
# fib2_list = fib_list.reverse()
# print (fib2_list)



# fib_list1.reverse()
# res_list = fib_list1.copy()
# res_list.extend(fib_list)

# print(f'Для числа {a} последовательность Фибоначчи и Негафибоначчи: {res_list}')