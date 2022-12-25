# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]

length_list = 5
a = [round(my_list[i] - int(my_list[i]), 2) 
for i in range (length_list) if my_list[i] != 0]
print(a)

diff_num = max(a) - min(a)
print(diff_num)