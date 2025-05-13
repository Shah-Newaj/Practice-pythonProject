class BasicCalculator:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2


obj = BasicCalculator(10, 5)
print("Addition: 10 + 5 = ", obj.addition())
print("Subtraction: 10 - 5 = ", obj.subtraction())
print("Multiplication: 10 * 5 = ", obj.multiplication())
print("Division: 10 / 5 = ", obj.division())

