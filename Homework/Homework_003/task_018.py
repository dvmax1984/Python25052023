# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

n = int(input('Введите число N кол-во элементов в массиве: '))
x = int(input('Искомое число X (самый близкий по величине элемент): '))
l = list()                      # создаем пустой список

l = [i for i in range(1, n, 4) ]

print('Список чисел: ', *l)
print('Искомое число Х: ', x)

for j in l:
    if x <= j:
        print('\nБлижайшее число к Х: ', j)
        break
    elif j == l[-1]:
        print('\nИскомое число Х вне диапазона массива N')
        print(f'Ближайшее число до Х это {l[-1]}')