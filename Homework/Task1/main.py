

# Задание 1 Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)



number = str(input("Введите трёхзначное число:"))
if len(number) != 3:
    print('Неверное число')
    quit()
else: summ = int(number[0]) + int(number[1]) + int(number[2])
print(summ)

