# Задача 22 Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 

# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите кол-во n элементов 1-го множества: '))
m = int(input('Введите кол-во m элементов 2-го множества: '))

list_1 = list()
list_2 = list()

for i in range(n):
    a = int(input(f'Значение {i+1} из {n+1} для множ 1: '))
    list_1.append(a)

for j in range(m):
    b = int(input(f'Значение {j+1} из {m+1} для множ 2: '))
    list_2.append(b)

# print(list_1)
# print(list_2)

list_1 = set(list_1)
list_2 = set(list_2)

print(list_1)
print(list_2)

x = list_1.intersection(list_2)

print(x)
