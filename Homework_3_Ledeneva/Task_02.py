# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [5, 2, 7, 4, 3]

a = []
for i in range(int(len(my_list) // 2 + len(my_list) % 2)):
    a.append(my_list[i] * my_list[-(i + 1)])
print(a)

# math.ceil(len(my_list)/2)
# form math import ceil # метод округления
# for i in range(ceil(len(my_list) / 2)):