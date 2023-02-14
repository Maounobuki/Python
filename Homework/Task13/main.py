# Задание 13
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.




first_summand = int(input('Введите первое слагаемое:'))
second_summand = int(input('Введите второе слагаемое:'))

def Summary(number1, number2):
    if number1 == 0:
        return number2
    if number2 == 0:
        return number1
    if number1 > number2:                             #просто немного оптимизации, не сочтите за использование дополнительных арифметических знаков
                                                      #программа прекрасно работает и без этого дополнительного условия
        return Summary(number1 + 1, number2 - 1)
    else:
        return Summary(number1 - 1, number2 + 1)

result = (Summary(first_summand,second_summand))
print(f'Сумма двух введённых вами чисело составляет {result}')