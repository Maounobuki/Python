
import random

# Задание 5. На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# *Пример:
# 5 -> 1 0 1 1 0
# 2
# *



coins_quantity = int(input('Введите количество монет:'))

i =0
heads = 0
tails = 0
while i < coins_quantity:
      coin = random.randint(0, 1)
      print(coin)

      if coin == 0:
          tails += 1
      else: heads += 1
      i += 1
else:
    if tails < heads:
     print(tails)
    else: print(heads)