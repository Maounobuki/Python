class Example4():
    def __call__(self, x, y):
        return x*y


obj5 = Example4()
print(obj5(2,9))
print(obj5.__call__(2,9))