from oops_demo import Calculator


class Child(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 3, 4)

    def getcompletedata(self):
        return self.num + self.num2 + self.summation()


obj = Child()
print(obj.getcompletedata())
