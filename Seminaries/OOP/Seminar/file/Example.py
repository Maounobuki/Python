class Example():
    a = 20
    b = "summ"

    def meth1(self, x):
        return 2*x

obj = Example()
print(obj.meth1(5))
print(obj.a)
print(Example.b)
