# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input('Введите значение N: '))
my_list = list(range(-num, num+1))
print(f'Список чисел из промежутка от -{num} до {num} равен {my_list}')

path = 'file.txt'
data = open(path, 'w')
data.write('2\n')
data.write('4\n')
data.close()

new_list = []
prod_nums = 1
path = 'file.txt'
data = open(path, 'r')
for line in data:
    prod_nums *= my_list[int(line)]
    print(line, end='')
print(f'Произведение чисел на позициях равно {prod_nums}')

exit()
