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

d = {}      # вар 1 создать словарь
d = dict()  # вар 2 создать словарь

d['q'] = 'qwert'
print(d)

d['w'] = 'wert'
print(d)
