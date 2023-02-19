# Задание 15
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
from typing import List

index_list = list()
numbers_list = list()

for i in range(int(input('Введите количество элементов списка:'))):
    numbers_list.append(random.randint(0,30))
else: print(f'Ваш список:{", ".join(map(str,numbers_list))}')

treshold_min =int(input('Введите минимальное значение для элементов списка:'))
treshold_max =int(input('Введите максимальное значение для элементов списка:'))

for i in range(len(numbers_list)):
         if treshold_max >= numbers_list[i] >= treshold_min:
             index_list.append(i)
if not index_list: print(f'В списке нет элементов, значения которых, попадают в обозначенный диапазон')
else: print(f'Индексы элементов, значения которых, попадают в указанный дапазон: {", ".join(map(str,index_list))}')


