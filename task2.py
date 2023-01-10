# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

a = int(input('Введите количество чисел в списке: '))

nums = []
for item in range (1,a+1):
    nums.append(int(input()))
print(nums)

res = []
for i in range (len(nums)//2):
    res.append(nums[i]*nums[(len(nums)-1)-i])
if len(nums)%2!=0:
    res.append(nums[len(nums)//2]*nums[len(nums)//2])
print(res)



# count = 1
# for i in range (len(nums)//2):
#     res.append(nums[i]*nums[len(nums)-count])
#     count+=1
# if len(nums)%2!=0:
#     res.append(nums[len(nums)//2]*nums[len(nums)//2])
# print(res)

