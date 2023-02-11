# Задание. 10
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12



set_1_lenght = int(input('Введите введите количество элементов набора 1:'))

set_2_lenght = int(input('Введите введите количество элементов набора 2:'))


def FillSet (lenght):
 set_n = []
 for i in range(0, lenght):
          set_n.append(int(input(f'Введите элемент набора:')))
 print('Ввод набора окончен')
 print (f' Ваш набор: {set_n}')
 set_n = set(set_n)
 return set_n


set_1 = (FillSet(set_1_lenght))
set_2 = (FillSet(set_2_lenght))


set_union = set_1.intersection(set_2)
new_list = sorted(set_union)
if not new_list:
    print('В наборах нет идентичных чисел')
else:
  print(f'Повторяющиеся элементы 2х наборов по возрастанию: {new_list}')

