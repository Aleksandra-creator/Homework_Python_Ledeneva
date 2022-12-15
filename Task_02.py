# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Первый вариант решения:

# print('Введите значение x ')
# x = int(input())
# print('Введите значение y ')
# y = int(input())
# print('Введите значение z ')
# z = int(input())

# left_part = not (x or y or z)
# right_part = not x and not y and not z

# if left_part == right_part: print ('True')
# else: print ('False')

# Второй вариант решения:

# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a


# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result


# statement = inputNumbers(3)

# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")

# Третий вариант решения

print('Введите значение x ')
x = int(input())
print('Введите значение y ')
y = int(input())
print('Введите значение z ')
z = int(input())

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            print(x,'AND',y,'OR',z,'=',x and y or z)
