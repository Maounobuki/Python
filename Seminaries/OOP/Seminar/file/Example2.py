class Example2():

    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z
        self.__param = 42


obj2 = Example2(2, 3, 2)
obj3 = Example2(4,8)
print(obj2.x, obj2.y, obj2.z)
print(obj3.x)
print(obj3._Example2__param)


