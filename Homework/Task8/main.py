
# Задание 8. Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random
list_lenght = int(input('Введите длину списка:'))
numbers = []
for i in range(list_lenght):
    numbers.append(random.randint(0, 101))

print(numbers)

desired_number = int(input('Введите искомое число:'))

counter = 0
for c in range(list_lenght):
    if numbers[c] == desired_number:
        counter += 1
else:
    if counter > 0:
        print(f'Искомое число встречается в списке {counter} раз')
    else:
     diff_list = []                            #Создаём новый список для сравнения значений
     for k in range(list_lenght):
      diff_list.append(abs(numbers[k] - desired_number))


     print(f'Такого  числа в списке нет, ближайшее похожее число: {numbers[diff_list.index(min(diff_list))]}')


