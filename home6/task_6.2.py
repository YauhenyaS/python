# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [int(i) for i in input('Введите элементы списка через пробел: ').split()]
min_range = int(input(' Введите минимальную границу: '))
max_range = int(input(' Введите максимальную границу: '))
for i in range(len(list_1)):
     if min_range <= list_1[i] <= max_range:
         print(i, end=',')