# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов 
# исходной последовательности.

my_list = input('Введите числа с повторяющими значениями через пробел: ')
my_list = my_list.split()
print(f'Список c повторяющимися элементами - {my_list}')
for i in range(len(my_list)):
    for j in range(len(my_list)):
        if i != j and my_list[i] == my_list[j]:
            break
    else:
        print(my_list[i], end=', ')
