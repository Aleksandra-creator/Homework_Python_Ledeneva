# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# Задача 1
# функция round 
# функция decimal

# 1. попросить пользователя ввести точность после запятой 10 в минус 1 <= d <= 10 в минус 10
# 2. И показать количество после запятой
# или пользователь вводи 0,001 и ему выдается что-то

# Решение "в лоб"
# n = float(input('Введите точность вычисления π: '))
# if n == 3:
#     print (f'Точность π равна 0.0')
# if n == 3.1:
#     print (f'Точность π равна 0.1')
# if n == 3.14:
#     print (f'Точность π равна 0.01')
# if n == 3.141:
#     print (f'Точность π равна 0.001')
# if n == 3.1415:
#     print (f'Точность π равна 0.001')
# if n == 3.1415:
#     print (f'Точность π равна 0.001')

   
# Решение через встроенные библиотеки
from math import pi

d = int(input("Введите точность вычисления π:\n"))
print(f'число π с заданной точностью {d} равно {round(pi, d)}')