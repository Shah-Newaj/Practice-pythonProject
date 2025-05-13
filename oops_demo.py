class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b
        print("I am called auto when object is called")
    def getData(self):
        print("method in class")

    def summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num


obj = Calculator(2, 3)
obj.getData()
print(obj.summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.summation())
