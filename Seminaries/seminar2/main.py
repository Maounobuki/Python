

# По данному целому неотрицательному n вычислите значение n!. N!
# = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0!
# = 1 Решить задачу используя цикл while


# number = int(input('Введите целое число'))
# i = 1
# fact = 1
# for i in range(1, number + 1):
#while i <= number:
#     fact = fact * i
#     i += 1
# print(f'Факториал числа {number} = {fact}')






# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.


# number = int(input('Введите целое число: '))
#
# fibonachi_0 = 0
# fibonachi_1 = 1
# i = 3
# if number == 0:
#     print(f'Число А является числом фибоначчи по счету {1}')
# elif number ==1:
#
# print(fibonachi_0)
# print(fibonachi_1)
# while True:
#     fibonachi_n = fibonachi_1 + fibonachi_0
#     fibonachi_0 = fibonachi_1
#     fibonachi_1 = fibonachi_n
#     print(fibonachi_n)
#     if number == fibonachi_n:
#         print(f'Число А является числом фибоначчи по счету {i}')
#         break
#     elif number >fibonachi_n:
#         print(-1)
#         break
#     i += 1



# fib1 = 0
# fib2 = 1
#
# while True:
#     n = input("Число в Фибоначчи: ")
#     if n.isdigit():
#         n = int(n)
#         break
#     else:
#         print("Введите корректное число")
#
# i = 0
# while i < n:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
#     if fib_sum == n:
#         print("Значение этого элемента:", i+2)
#         break
# else:
#     print(-1)


# Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке
# каждое. Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 30000.

count_of_watermelon = int(input('Введите количество арбузов: '))
max_mass = 0
min_mass = 0
for i in range(count_of_watermelon):
    mass_new_watermelon = int(input('Масса нового : '))
    if max_mass < mass_new_watermelon:
        max_mass = mass_new_watermelon
        mass_new_watermelon > min_mass