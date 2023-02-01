# Задание 7. Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8


limit_number = int(input('Введите число:'))
power_value = 0
power_2 = 1
while power_2 < limit_number:
    print(f'Значение степени 2: {power_value}  Число: {power_2}')
    power_value += 1
    power_2 = power_2 * 2

