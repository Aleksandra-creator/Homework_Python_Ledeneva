# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.

# *Пример:* 
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# k = 5 (коэффициентов будет больше на 1)
# x ** 5 + x ** 4 + x ** 3 + k ** 2 + K ** 1 + k ** 0 = 0
# значения x будут подбираться рандомно от 0 до 100
# нужно их записать в файл

# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line)

# Решение через словари:

# import random
# def CoeffList ():
#     from random import randint
#     my_list = [randint(0, 101) for i in range(k+1)]
#     while my_list[0] == 0:
#         my_list[0] = randint(0, 101)
#     return my_list

# k = int(input('Введите натуральную степерь k: '))

# my_dic = {}
# x = 0
# for i in range(0, k+1):
#     for j in CoeffList:
#         my_dic = dict([(j), (x^k)])
# print(my_dic)

k = int(input("Введите натуральную степень k = "))
import random

def CoeffList (k):
    from random import randint
    my_list = [randint(0, 101) for i in range(k+1)]
    while my_list[0] == 0:
        my_list[0] = randint(0, 101)
    return my_list

def CreatePolynomial (my_list):
    pol = len(my_list)
    result = ''
    for i in my_list:
        pol -= 1
        if i != 0:
            result += f'{i}'
            if pol > 0:
                result += f'*x^{pol} + '
    result += ' = 0'
    return result

def write_file(st):
    with open('file.txt', 'w') as data:
        data.write(st)

my_list = CoeffList(k)
print (my_list)
pol_string = CreatePolynomial(my_list)
print(pol_string)

write_file(pol_string)
