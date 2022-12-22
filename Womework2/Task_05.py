# Реализуйте алгоритм перемешивания списка.

import random
list1 = [1,2,3,4,5]
print (f'Изначальный список {list1}')
list2 = list1
random.shuffle(list2)
print (f'Итоговый список{list2}')
