# # list_1 = []             # способ-1 создаем пустой список
# # list_1 = list()         # способ-2 функция list создаем пустой список
# # list_1 = [1, 2, 3, 8]
# # #print(list_1[3])       # вывести 4 элемент из списка
# # print(*list_1)          # вывести весь список, одной строкой

# # for i in list_1:        # перебор списка в цикле
# #     print(i)

# # print(len(list_1))      # определение длинны списка

# # list_1 = [1 , 5]
# # print(list_1)
# # list_1.append(8)
# # print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# print(list_1.pop()) # удалить послений элемент и печатаем его
# print(list_1)

# print(list_1.insert(2,1)) # вставить элемент на позицию 2 (0-1-2)
# print(list_1)

# u = set(list_1)             # подсчет уникальных элементов списка
# c = len(u)
# print(c)

# КОРТЕЖИ

# t = ()
# print(type(t))
# t = (1) # преобразуется в инт, это не кортеж <class 'int'>
# t = (1,) # знак , говорит что это КОРТЕЖ <class 'tuple'>
# print(type(t))


# #преобразование списка в кортеж
# v = [1,8,9]
# print(v)
# print(type(v))
# v = tuple(v)
# print(v)
# print(type(v))

# t = (1,3,2,4,5,)

# for i in t:  ПЕРЕБРАТЬ КОРЖЕЖ
#     print(i)        # i отобразит элементы кортежа построчно
#                     # t отобразит кортеж как есть, с повтором в число элементов

# for i in range(len(t)):
#     print(t[i])

# СЛОВАРИ

# d = {}      # вар 1 создать словарь
# d = dict()  # вар 2 создать словарь

# d['q'] = 'qwert'
# print(d)

# d['w'] = 'wert'
# print(d)

# list_1 = [exp for item in iterable]
# print(*list_1) 

# print(sum(
# 	1 for x in range(1000)
# 	if x % 2 == 0 and
# 	'9' in str(x)
# ))
def get_nearest_value(n_value, n_list):
    list_of_difs = [abs(n_value - x) for x in n_list]
    result_index = list_of_difs.index(min(list_of_difs))

    return n_list[result_index], result_index


if __name__ == '__main__':
    delimeter = 0.1           # различные тестовые условия
    max_range = 100000        # различные тестовые условия
    test_list = [delimeter * (x + 1) for x in range(max_range)]

    test_value = 100000 #7711.63  # любое число

    print()
    print('тестовое значение:', test_value)
    print('ближайшее значение:', get_nearest_value(test_value, test_list)[0])
    print('на позиции:', get_nearest_value(test_value, test_list)[1], 'считая от нуля')