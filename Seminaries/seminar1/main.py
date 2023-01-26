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

 # n = 700
#m = 750
#s = (m + m - 1)//n
#print (s)


#year = int(input("Год:"))
#if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
 #   print("yes")
#else:
    #print("no")

   # number = float (input('Дробь:'))
   # print(round(number, int))

    number = float(input("Число:"))
    if number % 1 == 0:  # (digital == 0):
        print("no")
    else:
        digital = int(number * 10 % 10)
        print(digital)