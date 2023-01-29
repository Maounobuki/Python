

# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите длину стороны n:"))
m = int(input("Введите длину стороны m:"))
k = int(input("Введите количество долек k:"))

if k % n != 0 or k % m != 0 or (n * m) <= k:
    print('Нет')
else: print('Да')