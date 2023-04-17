class Example3():
    @staticmethod
    def hello():
        print("Hello world!")

    @classmethod
    def hello2(cls):
        print("Hello!",cls.__name__)


Example3.hello()
obj4 = Example3
obj4.hello()
Example3.hello2()
obj4.hello2()
