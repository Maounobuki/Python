class Example5():
    def __init__(self, x):
          self.x = x


    def getx(self):
        return self.x


    def setx(self,x):
        self.x = x


ob = Example5(20)
print(ob.getx())
ob.setx(5)
print(ob.getx())