# Задание 12
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.


basis =  int(input('Введите основание:'))
power = int(input('Введите показатель степени:'))


def PowerUp(base, degree):
    if degree == 0:
        return 1
    if degree == 1:
        return base
    else:
        return base * PowerUp(base,degree-1)

result = PowerUp(basis,power)

print(f'Число "{basis}" в степени "{power}" равняется "{result}"')