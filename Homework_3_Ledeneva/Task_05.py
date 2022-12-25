# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# *Пример:*
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def findFib(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    return findFib(index-1) + findFib(index-2)


n = int(input("Введите число:\n"))
lst = [findFib(i) for i in range(1, n+2)]
print(lst)
lst = lst[::-1] + lst[1:]
print(lst, '\n')

# Еще вариант решения:
# num = input('Введите число: ')

# fib_list = []
# x, y = 0, 1
# for i in list(range(num)):
#     x, y = y, x + y
#     fib_list.append(x)
#     fib_list.insert(0, -x if i % 2 else x)
# print(fib_list)