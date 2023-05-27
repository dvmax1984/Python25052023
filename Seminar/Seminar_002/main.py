# list_1 = []             # способ-1 создаем пустой список
# list_1 = list()         # способ-2 функция list создаем пустой список
# list_1 = [1, 2, 3, 8]
# #print(list_1[3])       # вывести 4 элемент из списка
# print(*list_1)          # вывести весь список, одной строкой

# for i in list_1:        # перебор списка в цикле
#     print(i)

# print(len(list_1))      # определение длинны списка

# list_1 = [1 , 5]
# print(list_1)
# list_1.append(8)
# print(list_1)

list_1 = []
print(list_1)
for i in range(5):
    list_1.append(i)
    print(list_1)

print(list_1.pop()) # удалить послений элемент и печатаем его
print(list_1)

print(list_1.insert(2,1)) # вставить элемент на позицию 2 (0-1-2)
print(list_1)

u = set(list_1)             # подсчет уникальных элементов списка
c = len(u)
print(c)