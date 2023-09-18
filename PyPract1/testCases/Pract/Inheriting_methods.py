class SquareRoot:
    def __init__(self, number,value):
        self.number = number
        self.value=value

    def calculate(self):
        return self.number ** self.value

class Addition:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        return self.num1 + self.num2

class Subtraction:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        return self.num1 - self.num2

class Multiplication:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        return self.num1 * self.num2

class Division:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"

class MathNew(SquareRoot, Addition, Subtraction, Multiplication, Division):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# Creating an instance of MathNew and testing
math_instance = MathNew(25,0.5)
print("Square root:", math_instance.calculate())

math_instance = MathNew(10, 5)
print("Addition:", math_instance.calculate())

math_instance = MathNew(15, 7)
print("Subtraction:", math_instance.calculate())

math_instance = MathNew(8, 3)
print("Multiplication:", math_instance.calculate())

math_instance = MathNew(10, 2)
print("Division:", math_instance.calculate())