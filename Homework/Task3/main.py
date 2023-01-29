# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет
# с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр
# равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# Пример:
# 385916 -> yes
# 123456 -> no


number = str(input("Введите шестизначное число:"))
int(number[0])+ int(number[1]) +int(number[2])

print(summ)
