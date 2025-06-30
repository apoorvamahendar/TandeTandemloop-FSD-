class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "sub":
            return self.a - self.b
        elif self.operation == "mul":
            return self.a * self.b
        elif self.operation == "div":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, sub, mul, div): ").lower()

calc = Calculator(a, b, operation)
result = calc.calculate()

print("Result:", result)
